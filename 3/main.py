def part1():
    banks = []
    with open('input.txt', mode='r') as input:
        banks = input.read().splitlines()
        banks = [[{'i': i, 'v': int(v)} for i, v in enumerate(list(b))] for b in banks]

    int_list = []

    for bank in banks:
        v_max_1 = max(bank, key=lambda b: b['v'])
        if v_max_1['i'] + 1 == len(bank):
            v_max_2 = max(bank[:v_max_1['i']], key=lambda b: b['v'])
        else:
            v_max_2 = max(bank[v_max_1['i'] + 1:], key=lambda b: b['v'])
        maxes = [v_max_1, v_max_2]
        i_sort = sorted(maxes, key=lambda b: b['i'])
        int_list.append(int(''.join([str(i['v']) for i in i_sort])))

    print(sum(int_list))


if __name__ == "__main__":
    part1()
