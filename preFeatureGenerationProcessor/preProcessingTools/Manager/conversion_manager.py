def conversion_manager(signal, conversions):
    conversions = dict(conversions)
    for key in sorted(conversions.keys()):

        if conversions[key]:
            current_method_information = conversions[key]

            current_method_module_or_class = current_method_information ['module_or_class']
            method_name = current_method_information['method_name']
            special_parameters = current_method_information['special_parameters']

            signal = getattr(current_method_module_or_class, method_name)(signal, special_parameters)

    return signal
