def merge(*iterables, key=None):
    rtn_list = []
    for item in iterables:
        for i in item:
            rtn_list.append(i)
    return sorted(rtn_list, key=key)
