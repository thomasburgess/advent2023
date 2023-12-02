from pathlib import Path
import math


def read_data(path: Path) -> list:
    """Read line data."""
    with path.open("r") as f:
        return [i.strip() for i in f.readlines()]


def parse(data: list[str]) -> list[list[tuple[int, ...]]]:
    """Turn input rows into list of rgb tuples."""
    result = []
    for game in data:
        subsets = []
        for sub in game.split(":")[1].split(";"):
            cubes = {s.split()[-1]: int(s.split()[0]) for s in sub.split(",")}
            subsets.append(tuple(cubes.get(col, 0) for col in ("red", "green", "blue")))
        result.append(subsets)
    return result


def max_rgb(game: list[tuple[int, ...]]) -> tuple[int, ...]:
    """Find max of rgb tuples."""
    return tuple(max(game, key=lambda t: t[i])[i] for i in range(len(game[0])))


def part1(data: list[str], limit: tuple[int, ...] = (12, 13, 14)):
    return sum(
        igame * all((i <= c) for i, c in zip(max_rgb(game), limit))
        for igame, game in enumerate(parse(data), 1)
    )


def part2(data: list[str]):
    return sum(math.prod(max_rgb(game)) for igame, game in enumerate(parse(data), 1))


if __name__ == "__main__":
    DAY = "02"
    exdata = read_data(Path(f"day{DAY}_example.txt"))
    indata = read_data(Path(f"day{DAY}_input.txt"))

    print("PART 1")
    print(f"\texample: {part1(exdata)}")
    print(f"\tinput: {part1(indata)}")

    print("PART 2")
    print(f"\texample: {part2(exdata)}")
    print(f"\tinput: {part2(indata)}")
