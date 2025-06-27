from typing import Callable, Iterable, TypeVar, Iterator, Optional

T = TypeVar('T')


def ft_filter(
    function: Optional[Callable[[T], bool]],
    iterable: Iterable[T]
) -> Iterator[T]:
    """
    Function using function filter.
    If function is None, return the items that are true.
    Otherwise, return the items for which function(item) is true.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))


def count_in_list(lst: list, s: str) -> int:
    """
    Return how many times `s` in lst
    Uses ft_filter to count `s`
    """
    return len(list(ft_filter(lambda x: x == s, lst)))
