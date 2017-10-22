from numpy.ma import absolute, array


def amp(a_single_subRegion, special_parameters):
    # TODO: this 'special_parameters' maybe be useful

    amplitude = array(absolute(a_single_subRegion))

    return amplitude


