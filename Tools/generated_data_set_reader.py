def generated_data_set_reader (extracted_data_set, conversion_methods, **kwargs):
    input_data_set = kwargs("extracted_data_set")
    conversion_methods = conversion_methods

    data_bank = []
    for device_data_set in input_data_set:
        bursts_of_a_single_device = device_data_set["a_Single_Device"]

        burst_finger_print = []
        burst_index = 0
        for burst in bursts_of_a_single_device:
            for subregion_index in range(len(burst)):
                current_subregion = burst[subregion_index]

                for key in current_subregion.items():

                    if len(conversion_methods) > 0:
                        for methods in conversion_methods:
                            current_subregion[key] = methods (current_subregion[key])

            burst_finger_print [burst_index]
            burst_index += 1

    return data_bank

