from math import sqrt
from timeit import timeit

from numpy.ma import power, absolute, angle, array, diff


def AmpPhaseFreq_Chars(a_single_subRegion):

    # Amplitude
    amplitude = array(absolute(a_single_subRegion))

    # Phase
    phase = array(angle(a_single_subRegion))

    # Instantaneours Frequency
    ifreq = array(diff(a_single_subRegion))

    return amplitude, phase, ifreq


