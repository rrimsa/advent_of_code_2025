def get_sum(limit: int):
    banks = []
    with open('input.txt', mode='r') as input:
        banks = input.read().splitlines()
        banks = [[{'i': i, 'v': int(v)} for i, v in enumerate(list(b))] for b in banks]

    int_list = []
    for bank in banks:
        nums = []
        for b in bank:
            while (
                nums
                and nums[-1] < b['v']
                and len(nums) - 1 + len(bank[b['i']:]) >= limit
            ):
                nums.pop()
            if len(nums) < limit:
                nums.append(b['v'])
        int_list.append(int(''.join([str(i) for i in nums])))
    print(sum(int_list))


if __name__ == "__main__":
    get_sum(limit=2)
    get_sum(limit=12)
