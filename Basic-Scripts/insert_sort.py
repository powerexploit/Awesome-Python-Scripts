def insert_sort(_list):
    for i in range(1, len(_list)):
        elm = _list[i]
        k = i
        while not k <= 0 and _list[k - 1] > elm :
            _list[k] = _list[k - 1]
            k -= 1
            _list[k] = elm
    l = _list
    return l
