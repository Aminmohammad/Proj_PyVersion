def generated_data_set_reader (**kwargs):
    input_data_set = kwargs["extracted_data_set"]
    conversion_methods = kwargs["conversion_methods"]

    data_bank = []
    for device_data_set in input_data_set:
        bursts_of_a_single_device = device_data_set["a_Single_Device"]

        burst_finger_print = []
        for burst in bursts_of_a_single_device:
            for subregion_index in range(len(burst)):
                current_subregion = burst[subregion_index]

                for key in current_subregion.items():

                    if len(conversion_methods) > 0:
                        for methods in conversion_methods:
                            current_subregion[key] = methods (current_subregion[key])

    return

