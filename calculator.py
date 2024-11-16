

def sums(x, y):
    """sum

    Args:
        x (float): Number
        y (float): Number

    Returns:
        _type_: Number


    >>> sums(10, 20)
    30

    >>> sums(-10, 20)
    10

    >>> sums('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: 10 needs to be int or float

    """
    assert isinstance(x, (int, float)), f'{x} needs to be int or float'
    assert isinstance(y, (int, float)), f'{x} needs to be int or float'
    return x + y


def sub(x, y):
    """
    >>> sub(2, 5)
    -3
    """
    assert isinstance(x, (int, float)), f'{x} needs to be int or float'
    assert isinstance(y, (int, float)), f'{x} needs to be int or float'
    return x - y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
