import sys


def ft_tqdm(lst: range) -> None:
    """print a progress bar"""
    total = len(lst)
    for i, val in enumerate(lst):
        percent = (i + 1) / total
        bar_lenght = 80
        filled = int(bar_lenght * percent)
        bar = '█' * filled + ' ' * (bar_lenght - filled)
        sys.stdout.write(f'\r{int(percent * 100)}%|{bar}| {i + 1}/{total}')
        sys.stdout.flush()
        yield val
