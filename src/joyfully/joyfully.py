def hello_world(s: str = "Hello World!") -> str:
    """
    Returns the string "Hello World!"

    >>> hello_world()
    'Hello World!'

    >>> hello_world("Hello World!")
    'Hello World!'

    >>> hello_world("Hello World")
    'Hello World'

    """
    return s


if __name__ == "__main__":
    import doctest

    doctest.testmod()
