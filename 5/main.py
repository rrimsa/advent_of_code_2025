def main():
    data = []
    with open("./5/input.txt", "r") as input:
        data = input.read().splitlines()

    ranges = get_ranges(data)

    check_freshness(data, ranges)
    check_all_fresh(ranges)


def check_all_fresh(ranges: list[range]):
    ranges = sorted(ranges, key=lambda r: r.start)
    ranges_ss = [[r.start, r.stop] for r in ranges]
    unique = []
    for r in ranges_ss:
        if not unique:
            unique.append(r)
        elif r[0] <= unique[-1][1]:
            unique[-1][1] = max(r[1], unique[-1][1])
        else:
            unique.append(r)
    total_fresh = sum(stop - start for start, stop in unique)
    print(f"Fresh in ranges: {total_fresh}")


def check_freshness(data: list[str], ranges: list[range]):
    split_index = data.index("")
    ids = data[split_index + 1:]
    ids = [{"id": int(id), "fresh": False} for id in ids]
    for id in ids:
        for r in ranges:
            if id["id"] in r:
                id["fresh"] = True
                break

    result = len([id for id in ids if id["fresh"]])
    print(f"Fresh items: {result}")


def get_ranges(data: list[str]) -> list[range]:
    split_index = data.index("")
    ranges = data[:split_index]
    ranges = [
        sorted([int(id) for id in r.split("-")])
        for r in ranges
    ]
    ranges = [[r[0], r[1] + 1] for r in ranges]
    ranges = [range(*r) for r in ranges]
    return ranges


if __name__ == "__main__":
    main()
