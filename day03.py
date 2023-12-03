from pathlib import Path
import itertools
import math


def read_data(path: Path) -> list:
    """Read line data."""
    with path.open("r") as f:
        return [i.strip() for i in f.readlines()]


def checks(data: list[str], x: int, y: int, chr=None) -> tuple[int, int] | None:
    for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
        try:
            c = data[y + dy][x + dx]
        except IndexError:
            continue
        if c == chr if chr else not (c.isnumeric() or c == "."):
            return (x + dx, y + dy)
    return None


def find_connections(data: list[str], chr=None) -> dict[tuple[int, int], list[int]]:
    connections = {}
    conn = None
    for y, row in enumerate(data):
        number = ""
        for x, c in enumerate(row):
            if c.isnumeric():
                number += c
                conn = checks(data, x, y, chr) or conn
            if (x == len(row) - 1) or not c.isnumeric():
                if number and conn:
                    connections[conn] = connections.get(conn, []) + [int(number)]
                conn = None
                number = ""
    return connections


def part1(data: list[str]) -> int:
    return sum(sum(find_connections(data).values(), []))


def part2(data: list[str]) -> int:
    connections = {
        k: v for k, v in find_connections(data, chr="*").items() if len(v) == 2
    }
    return sum(math.prod(v) for v in connections.values())


if __name__ == "__main__":
    DAY = "03"
    exdata = read_data(Path(f"day{DAY}_example.txt"))
    indata = read_data(Path(f"day{DAY}_input.txt"))

    print("PART 1")
    print(f"\texample: {part1(exdata)}")
    print(f"\tinput: {part1(indata)}")

    print("PART 2")
    print(f"\texample: {part2(exdata)}")
    print(f"\tinput: {part2(indata)}")
