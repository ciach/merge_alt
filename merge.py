def merge(*iterables):
    rtn_list = []
    for item in iterables:
        for i in item:
            rtn_list.append(i)
    return sorted(rtn_list)


if __name__ == "__main__":
    print(merge([1, 5, 9], [2, 5], [1, 6, 10, 11]))
    # print(concat_generators([1, 2, 3], [2, 3, 4], [3, 4, 5]))
    # 1, 1, 2, 5, 5, 6, 9, 10, 11
