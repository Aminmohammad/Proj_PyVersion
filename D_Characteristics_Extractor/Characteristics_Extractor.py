import inspect
import os

import sys

from matplotlib.pyplot import figure, plot, show
from numpy import shape, size, transpose, array

from D_Characteristics_Extractor.AmpPhaseFreq_Chars import AmpPhaseFreq_Chars


def Characteristics_Extractor(a_single_subRegion,
                              characteristics_Extractor_Method):
    amplitude, phase, ifrequency = AmpPhaseFreq_Chars(a_single_subRegion)

    return amplitude, phase, ifrequency


