from GeneralTools.DataSetDecomposerAndRecombiner.generated_data_set_decomposer_and_recombiner import \
    generated_data_set_decomposer_and_recombiner


def preProcessor_manager(extracted_data_set, selected_conversion_methods, project_name):
    name_of_caller_manager = "preProcessor_manager",
    data_set, _ = generated_data_set_decomposer_and_recombiner(extracted_data_set, name_of_caller_manager,
                                                            selected_conversion_methods, project_name)

    return data_set
