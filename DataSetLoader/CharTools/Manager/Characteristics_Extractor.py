def characteristics_extractor(a_single_subRegion,
                              characteristics_extractor_methods):
    signal_characteristics = {}
    for key in sorted(characteristics_extractor_methods.keys()):

        if characteristics_extractor_methods[key]:
            current_method_information = characteristics_extractor_methods[key]

            current_method_module_or_class = current_method_information['module_or_class']
            method_name = current_method_information['method_name']
            special_parameters = current_method_information['special_parameters']

            signal_characteristic = getattr(current_method_module_or_class, method_name)(a_single_subRegion,
                                                                                         special_parameters)

            # output
            signal_characteristics[method_name] = signal_characteristic

    return signal_characteristics
