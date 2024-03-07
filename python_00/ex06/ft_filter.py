def ft_basic_filter(item):
    """
    ft_basic_filter(item) --> boolean
    Return True if item is True, False else
    """
    return bool(item)


def ft_filter(func, iterable):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    """

    try:
        if func is None:
            func = ft_basic_filter
        filtered = []
        for item in iterable:
            if func(item):
                filtered.append(item)
    except Exception as e:
        print(e)
    return iter(filtered)
