def main():
    moves = []
    with open("./1/input.txt", "r") as input:
        moves = input.read().splitlines()
    moves = [m.lower().strip() for m in moves]

    position = 50
    move_positions = []
    passes = 0
    for m in moves:
        move_int = int(m.replace("r", "").replace("l", "-"))
        position = (100 + position + move_int) % 100
        move_positions.append({
            "move": m,
            "pos": position
        })

    print(len([m for m in move_positions if m["pos"] == 0]))


if __name__ == "__main__":
    main()
