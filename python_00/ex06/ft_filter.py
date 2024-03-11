def default_fun(item):
    """
    default_fun(item) -> boolean
    return the boolean value of the item given as argument
    """
    return bool(item)


def ft_filter(func, iterable):
    """
    ft_filter(function or None, iterable) --> list iterator object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    """

    if func is None:
        func = default_fun
    filtered = [item for item in iterable if func(item)]
    return iter(filtered)
