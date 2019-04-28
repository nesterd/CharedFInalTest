def linear(some_list):
    if not some_list:
        return [], 0, 0

    main_list_len = len(some_list)
    inner_list_len = len(some_list[0])

    new_list = []

    for j in range(inner_list_len):
        for i in range(main_list_len):
            new_list.append(some_list[i][j])

    return new_list, main_list_len, inner_list_len


def de_linear(some_list, main_list_len, inner_list_len):
    if not some_list:
        return []

    new_list = [[0] * inner_list_len for _ in range(main_list_len)]
    index = 0
    for j in range(inner_list_len):
        for i in range(main_list_len):
            new_list[i][j] = some_list[index]
            index += 1

    return new_list


def sorted2(data, key=lambda x: -x):
    lineared, main_list_len, inner_list_len = linear(data)

    sorted_data = sorted(lineared, key=key)
    de_lineared = de_linear(sorted_data, main_list_len, inner_list_len)
    return de_lineared



