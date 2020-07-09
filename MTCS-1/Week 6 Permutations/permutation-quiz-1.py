
def swap_string(string, x, y):
    print(x, y)
    str_list = list(string)
    str_list[x], str_list[y] = str_list[y], str_list[x]
    return ''.join(str_list)


def seq_util(start, final):
    ans = []
    length = len(start)

    for i in range(length-1):
        print(final)
        find = final[i]
        print(find)
        loc = start.index(find)
        print(loc)
        if i == loc:
            continue
        ans.append((i, loc))
        print(f'Before swapping\t-> { start }')
        start = swap_string(start, i, loc)
        print(f'After swapping\t-> { start }')
        print()

    return ans


def sequence():
    # return [( , ), ( , ),...,( , )]
    # return [(0, 1), (1, 3), (4, 5)]
    return seq_util('MARINE', 'AIRMEN')


print(sequence())
