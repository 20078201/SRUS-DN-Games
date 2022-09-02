def find_max_square_dimension(length, width):
    """
    Return the ideal length and width for a given plot of land
    :param length:
    :param width:
    :return:
    """
    # Base case
    if length % width == 0:
        return f"length = {length} \n width = {width}"
    else:
        return find_max_square_dimension(length % width, width) if length > width else find_max_square_dimension(length,
                                                                                                                 width % length)
