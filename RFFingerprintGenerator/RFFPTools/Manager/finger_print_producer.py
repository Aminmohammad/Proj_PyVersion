def finger_print_producer(signal, methods):
    methods = dict(methods)
    method_index = 0
    signal_finger_print = {}
    for key in sorted(methods.keys()):

        if methods[key]:
            current_method_information = methods[key]

            current_method_module_or_class = current_method_information['module_or_class']
            method_name = current_method_information['method_name']
            special_parameters = current_method_information['special_parameters']

            signal_RFFP = getattr(current_method_module_or_class, method_name)(signal, special_parameters)

            # output
            new_key = ("RFFP_%s" % method_index)
            signal_finger_print[new_key] = signal_RFFP
            method_index += 1

    return signal_finger_print
