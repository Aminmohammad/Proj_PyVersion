from math import sqrt
from timeit import timeit

import sys
from numpy.ma import power, absolute, angle, array, diff, shape, size


def phase(a_single_subRegion, special_parameters):
    # TODO: this 'special_parameters' maybe be useful

    phase = array(angle(a_single_subRegion))

    return phase


