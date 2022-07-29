def merge(*iterables, key=None):
    rtn_list = []
    for item in iterables:
        for i in item:
            rtn_list.append(i)
    return sorted(rtn_list, key=key)


if __name__ == "__main__":
    print(merge([1, 5, 9], [2, 5], [1, 6, 10, 11]))
