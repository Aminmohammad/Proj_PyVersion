from DataSetLoader.Characteristics_Extractor.AmpPhaseFreq_Chars import AmpPhaseFreq_Chars


def Characteristics_Extractor(a_single_subRegion,
                              characteristics_Extractor_Method):
    amplitude, phase, ifrequency = AmpPhaseFreq_Chars(a_single_subRegion)
    # TODO: maker here automatic

    return amplitude, phase, ifrequency


