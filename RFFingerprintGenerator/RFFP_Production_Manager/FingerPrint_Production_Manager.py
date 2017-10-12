from Tools.DataSetDecomposer.generated_data_set_decomposer import generated_data_set_decomposer


def finger_print_production_manager(**kwargs):
    data_bank = generated_data_set_decomposer(extracted_data_set=kwargs["extracted_data_set"],
                                              function_name="subRegion_finger_print_generator")

    return data_bank
