def ft_filter(function, iterable):
    """
    Construct an iterator from those elements of iterable,
    for which function returns true.

    ft_filter(function or None, iterable) --> filter object

    If function is None, return the items that are true.
    Otherwise, return the items for which function(item) is true.
    """
    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))
