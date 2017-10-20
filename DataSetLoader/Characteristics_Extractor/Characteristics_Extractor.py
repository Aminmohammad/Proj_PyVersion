from DataSetLoader.Characteristics_Extractor.AmpPhaseFreq_Chars import AmpPhaseFreq_Chars


def Characteristics_Extractor(a_single_subRegion,
                              characteristics_extractor_methods):
    amplitude, phase, ifrequency = AmpPhaseFreq_Chars(a_single_subRegion)

    characteristics_extractor_methods = dict(characteristics_extractor_methods)
    for key in sorted(characteristics_extractor_methods.keys()):

        if characteristics_extractor_methods[key] == "AmpPhaseFreq_Chars":
            amplitude, phase, ifrequency = AmpPhaseFreq_Chars(a_single_subRegion)

    # TODO: make characteristic Selection automatic

    return amplitude, phase, ifrequency


