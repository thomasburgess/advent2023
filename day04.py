from pathlib import Path
import re


def read_data(path: Path) -> list:
    """Read line data."""
    with path.open("r") as f:
        return [i.strip() for i in f.readlines()]


def parse(data: list[str]) -> list[tuple[int, set[int], set[int]]]:
    pattern = r"Card\s+(\d+):\s*(.+?)\s*\|\s*(.+)"
    result = []
    for line in data:
        match = re.findall(pattern, line)
        card, a, b = match[0]
        result.append((int(card), set(map(int, a.split())), set(map(int, b.split()))))
    return result


def wins(parsed: list[tuple[int, set[int], set[int]]]) -> list[tuple[int, int]]:
    return [(i, len(w.intersection(n))) for i, w, n in parsed]


def part1(data: list[str]):
    return sum(int(2 ** (w - 1)) for i, w in wins(parse(data)))


def part2(data: list[str]):
    cards = {k: {"wins": v, "count": 1} for k, v in wins(parse(data))}
    for i, c in cards.items():
        for j in range(i + 1, i + 1 + c["wins"]):
            cards[j]["count"] += c["count"]
    return sum(c["count"] for i, c in cards.items())


if __name__ == "__main__":
    DAY = "04"
    exdata = read_data(Path(f"day{DAY}_example.txt"))
    indata = read_data(Path(f"day{DAY}_input.txt"))

    print("PART 1")
    print(f"\texample: {part1(exdata)}")
    print(f"\tinput: {part1(indata)}")

    print("PART 2")
    print(f"\texample: {part2(exdata)}")
    print(f"\tinput: {part2(indata)}")
