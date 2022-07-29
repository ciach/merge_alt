def merge(*iterables, key=None, reverse=False) -> list:
    """_summary_

    Args:
        key (_type_, optional): _description_. Defaults to None.
        reverse (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    rtn_list = []
    for item in iterables:
        for i in item:
            rtn_list.append(i)
    return sorted(rtn_list, key=key, reverse=reverse)


if __name__ == "__main__":
    print(type(merge([1], [2], [3])))
