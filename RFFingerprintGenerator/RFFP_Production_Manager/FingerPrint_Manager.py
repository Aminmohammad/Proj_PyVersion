from GeneralTools.DataSetDecomposerAndRecombiner.generated_data_set_decomposer_and_recombiner import \
    generated_data_set_decomposer_and_recombiner


def finger_print_manager(**kwargs):
    data_bank = generated_data_set_decomposer_and_recombiner(extracted_data_set=kwargs["extracted_data_set"],
                                                             name_of_caller_manager="finger_print_manager")

    return data_bank
