import sys

from preFeatureGenerationProcessor.preProcessingTools.dwt_calculator.dwt_calculator import dwt_calculator

signal_statistics = {}



def conversion_manager(signal, conversions):

    conversions = dict(conversions)
    for key in sorted(conversions.keys()):

        if conversions[key] == "dwt_calculator":
            signal = dwt_calculator(signal)

    return signal

