def divide_and_plot(width, height):
    """Determines the maximum size of a square plot given a larger plot of width x height  proportions"""
    if width == height or height == 0:  # no further remainder or already a square
        return width
    smaller, larger = (width, height) if width < height else (height, width)
    # largest possible square is the shorter of the two lengths
    return divide_and_plot(smaller, larger % smaller)  # if there is any remainder we have to keep looking


def main():
    """Tests the divide_and_plot recursive function
    :examples:
    >>> divide_and_plot(1680, 640)
    80
    >>> divide_and_plot(640, 1680)
    80
    >>> divide_and_plot(640, 640)
    640
    """


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
