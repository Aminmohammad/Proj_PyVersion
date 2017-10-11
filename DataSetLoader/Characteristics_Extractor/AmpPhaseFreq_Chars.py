from math import sqrt
from timeit import timeit

import sys
from numpy.ma import power, absolute, angle, array, diff, shape, size


def AmpPhaseFreq_Chars(a_single_subRegion):

    # Amplitude
    # print("3333333333333333333333333333333333333333333333333333333333333333333")
    # print(a_single_subRegion)
    # print(size(a_single_subRegion))
    amplitude = array(absolute(a_single_subRegion))
    # print(amplitude)
    # print(shape(amplitude))
    # Phase
    phase = array(angle(a_single_subRegion))
    # print(phase)
    # print(shape(phase))

    # Instantaneous Frequency
    ifreq = array(diff(phase))
    # print(ifreq)
    # print(shape(ifreq))
    return amplitude, phase, ifreq


