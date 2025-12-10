def main():
    check_freshness()


def check_freshness():
    data = []
    with open("input.txt", "r") as input:
        data = input.read().splitlines()

    split_index = data.index("")
    ranges = data[:split_index]
    ranges = [
        sorted([int(id) for id in r.split("-")])
        for r in ranges
    ]
    ranges = [[r[0], r[1] + 1] for r in ranges]
    ranges = [range(*r) for r in ranges]

    ids = data[split_index + 1:]
    ids = [{"id": int(id), "fresh": False} for id in ids]
    for id in ids:
        for r in ranges:
            if id["id"] in r:
                id["fresh"] = True
                break

    result = len([id for id in ids if id["fresh"]])
    print(f"Fresh items: {result}")


if __name__ == "__main__":
    main()
