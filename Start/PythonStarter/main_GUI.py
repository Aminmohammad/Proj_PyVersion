import ast

import sys

from termcolor import cprint

from GeneralTools.RootProjectFolderAddressExtractor.root_project_folder_address_extractor import \
    root_project_folder_address_extractor
from GeneralTools.RawDataAddressExtractor.raw_data_address_extractor import raw_data_folder_address_extractor
from ProjectManager.project_manager import project_manager


def main_GUI(parameters):
    # TODO: here is the place of Graphic Resources Address
    """
    Start of program
    """
    project_name = parameters["project_name"]

    zero_conversion_threshold = float(parameters["zero_conversion_threshold"]),
    number_of_subRegions = int(parameters["number_of_subRegions"]),
    number_of_symbols_per_preamble = int(parameters["number_of_symbols_per_subRegion"]),
    number_of_chips_per_subRegion = int(parameters["number_of_chips_per_subRegion"]),
    time_length_of_a_single_chip_in_second = float(parameters["time_length_of_chip"]),
    sampling_frequency = int(float(parameters["sampling_frequency"])),
    communication_frequency = int(float(parameters["communication_frequency"])),
    data_set_address = parameters["data_set_address"]

    # the extensions
    selected_initial_data_set_saving_format = parameters["data_set_saving_format"]  # "txt"
    selected_initial_data_set_loading_format = parameters["data_set_loading_format"]  # "txt"
    selected_preProcessed_data_set_saving_format = parameters["preProcessed_data_set_saving_format"]  # "txt"
    selected_data_bank_saving_format = parameters["data_bank_saving_format"]  # "csv" or "mat"

    # output data_bank structure
    dimension_must_be_in_rows_or_columns = parameters["data_bank_dimensions_in_columns"]  # rows or columns

    # permissions
    make_new_data_set = parameters["make_new_data_set"]  # if 'make_new_data_set=False' >> it will load an existing "data-set.selected_loading_format"
    # if 'make_new_data_set=False' and 'exist(InitialDataSet) == 0' >> # automatically changes: 'make_new_data_set=True'

    run_preProcess = parameters["run_preProcess"]
    run_finger_print_production = parameters["run_data_bank"]
    run_postProcess = parameters["run_postProcess"] # if 'run_preProcess=False' or  'run_finger_print_production==False' >>> automatically: 'run_postProcess=False'

    save_initial_data_set = parameters["save_data_set"]
    save_preProcessed_data_set = parameters["save_preProcessed_data_set"]  # if 'run_preProcess=False' >> automatically: 'save_preProcessed_data_set=False'
    save_data_bank = parameters["save_data_bank"]  # if 'run_finger_print_production=False' >> automatically: 'save_data_bank=False'

    add_labels_to_saved_data_bank = parameters["add_dim_headers"]   # if 'run_finger_print_production=False'
    # or 'selected_data_bank_saving_format!=csv'
    # >> automatically:  'add_labels_to_saved_data_bank=False'

    if make_new_data_set:
        try:
            selected_characteristics_extraction_methods_for_data_set_making = ast.literal_eval(parameters["data_set_extractor_methods"])
        except (ValueError, SyntaxError):
            cprint("Error happened in conversion of data-set methods to dict. Maybe it is not a valid string. Program stops here!", "red")
            sys.exit(0)

    else:
        selected_characteristics_extraction_methods_for_data_set_making = []

    if run_preProcess:
        try:
            selected_conversion_methods_for_preProcessing = ast.literal_eval(parameters["preProcessing_methods"])

        except (ValueError, SyntaxError):
            cprint("Error happened in conversion of preProcessing methods to dict. Maybe it is not a valid string. Program stops here!", "red")
            sys.exit(0)
    else:
        selected_conversion_methods_for_preProcessing = []

    if run_finger_print_production:
        try:
            selected_feature_extraction_methods_for_finger_printing = ast.literal_eval(parameters["data_bank_methods"])

        except (ValueError, SyntaxError):
            cprint("Error happened in conversion of data-bank methods to dict. Maybe it is not a valid string. Program stops here!", "red")
            sys.exit(0)

    else:
        selected_feature_extraction_methods_for_finger_printing = []

    if run_postProcess:
        try:
            selected_conversion_methods_for_postProcessing = ast.literal_eval(parameters["postProcessing_methods"])

        except (ValueError, SyntaxError):
            cprint("Error happened in conversion of data-bank methods to dict. Maybe it is not a valid string. Program stops here!", "red")
            sys.exit(0)

    else:
        selected_conversion_methods_for_postProcessing = []

    output = project_manager(data_set_address=data_set_address,
                             zero_conversion_threshold=zero_conversion_threshold,
                             number_of_subRegions=number_of_subRegions,
                             number_of_symbols_per_preamble=number_of_symbols_per_preamble,
                             number_of_chips_per_subRegion=number_of_chips_per_subRegion,
                             time_length_of_a_single_chip_in_second=time_length_of_a_single_chip_in_second,
                             sampling_frequency=sampling_frequency,
                             communication_frequency=communication_frequency,
                             characteristics_extractor_methods=
                             selected_characteristics_extraction_methods_for_data_set_making,
                             selected_preProcessing_conversion_methods=selected_conversion_methods_for_preProcessing,
                             selected_postProcessing_conversion_methods=selected_conversion_methods_for_postProcessing,
                             selected_feature_extraction_methods=selected_feature_extraction_methods_for_finger_printing,
                             selected_initial_data_set_saving_format=selected_initial_data_set_saving_format,
                             selected_initial_data_set_loading_format=selected_initial_data_set_loading_format,
                             selected_preProcessed_data_set_saving_format=selected_preProcessed_data_set_saving_format,
                             selected_data_bank_saving_format=selected_data_bank_saving_format,
                             make_new_data_set=make_new_data_set,
                             run_preProcess=run_preProcess,
                             run_postProcess=run_postProcess,
                             run_finger_print_production=run_finger_print_production,
                             save_initial_data_set=save_initial_data_set,
                             save_preProcessed_data_set=save_preProcessed_data_set,
                             save_data_bank=save_data_bank,
                             project_name=project_name,
                             add_labels_to_saved_data_bank=add_labels_to_saved_data_bank,
                             dimension_must_be_in_rows_or_columns=dimension_must_be_in_rows_or_columns
                             )

    return output

