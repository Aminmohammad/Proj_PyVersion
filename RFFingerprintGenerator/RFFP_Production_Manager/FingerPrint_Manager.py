from GeneralTools.DataSetDecomposerAndRecombiner.generated_data_set_decomposer_and_recombiner import \
    generated_data_set_decomposer_and_recombiner


def finger_print_manager(extracted_data_set, selected_feature_extraction_methods, project_name):
    name_of_caller_manager = "finger_print_manager",

    data_bank = generated_data_set_decomposer_and_recombiner(extracted_data_set, name_of_caller_manager,
                                                             selected_feature_extraction_methods, project_name)

    return data_bank
