from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate and print statistical measures based on provided arguments.

    Args:
        *args: Variable length argument list containing numerical data.
        **kwargs: Keyword arguments specifying which statistics to calculate.
            Valid keys include "mean", "median", "quartile", "std", and "var".
    Returns:
        None
    """
    if len(args) == 0:
        for _ in kwargs:
            print("ERROR")
        return

    def ft_len(lst):
        count = 0
        for _ in lst:
            count += 1
        return count

    def ft_sum(lst):
        total = 0
        for x in lst:
            total += x
        return total

    def ft_sorted(lst):
        lst = list(lst)
        for i in range(1, ft_len(lst)):
            key = lst[i]
            j = i - 1
            while j >= 0 and lst[j] > key:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
        return lst

    def ft_mean(lst):
        return ft_sum(lst) / ft_len(lst)

    def ft_variance(lst, m):
        total = 0
        for x in lst:
            total += (x - m) * (x - m)
        return total / ft_len(lst)

    def ft_median(lst):
        n = ft_len(lst)
        if n % 2 == 0:
            return (lst[n // 2 - 1] + lst[n // 2]) / 2
        else:
            return lst[n // 2]

    def ft_quartiles(lst):
        n = ft_len(lst)
        q1 = lst[n // 4]
        q3 = lst[(3 * n) // 4]
        return q1, q3

    def ft_contains(container, value):
        for item in container:
            if item == value:
                return True
        return False

    values = []
    for x in args:
        values.append(x)

    sorted_values = ft_sorted(values)

    mean = None
    if (
        ft_contains(kwargs.values(), "mean")
        or ft_contains(kwargs.values(), "std")
        or ft_contains(kwargs.values(), "var")
    ):
        mean = ft_mean(values)

    variance = None
    if (
        ft_contains(kwargs.values(), "std")
        or ft_contains(kwargs.values(), "var")
    ):
        variance = ft_variance(values, mean)

    for _, val in kwargs.items():
        if val == "mean":
            print(f"mean: {mean:.1f}")
        elif val == "median":
            print(f"median: {ft_median(sorted_values)}")
        elif val == "quartile":
            q1, q3 = ft_quartiles(sorted_values)
            print(f"quartile: [{q1:.1f}, {q3:.1f}]")
        elif val == "std":
            print(f"std: {(variance ** 0.5):.12f}")
        elif val == "var":
            print(f"var: {variance:.10f}")
