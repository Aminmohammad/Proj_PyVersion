import ast

import sys

from GeneralTools.RootProjectFolderAddressExtractor.root_project_folder_address_extractor import \
    root_project_folder_address_extractor
from GeneralTools.RawDataAddressExtractor.raw_data_address_extractor import raw_data_folder_address_extractor
from ProjectManager.project_manager import project_manager


def main(parameters):
    # TODO: here is the place of Graphic Resources Address
    """
    Start of program
    """













    project_name = parameters["project_name"]
    selected_data_set_name = parameters[
        "data_set_name"]  # if it is empty, a pop-up window will give you the opportunity to select it graphically   2016_07_11_IQ_20Msps_RZUSBSTICK
    zero_conversion_threshold = float(parameters["zero_conversion_threshold"]),
    number_of_subRegions = int(parameters["number_of_subRegions"]),
    number_of_symbols_per_preamble = int(parameters["number_of_symbols_per_subRegion"]),
    number_of_chips_per_subRegion = int(parameters["number_of_chips_per_subRegion"]),
    time_length_of_a_single_chip_in_second = float(parameters["time_length_of_chip"]),
    sampling_frequency = int(float(parameters["sampling_frequency"])),
    communication_frequency = int(float(parameters["communication_frequency"])),

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

    selected_characteristics_extraction_methods_for_data_set_making = ast.literal_eval(parameters["data_set_extractor_methods"])
    selected_conversion_methods_for_preProcessing = ast.literal_eval(parameters["preProcessing_methods"])
    selected_feature_extraction_methods_for_finger_printing = ast.literal_eval(parameters["data_bank_methods"])
    selected_conversion_methods_for_postProcessing = ast.literal_eval(parameters["postProcessing_methods"])
















    # # Input Parameters
    # print(project_name)
    # print(selected_data_set_name)  # if it is empty, a pop-up window will give you the opportunity to select it graphically   2016_07_11_IQ_20Msps_RZUSBSTICK
    # print(zero_conversion_threshold)
    # print(number_of_subRegions)
    # print(number_of_symbols_per_preamble)
    # print(number_of_chips_per_subRegion)
    # print(time_length_of_a_single_chip_in_second)
    # print(sampling_frequency)
    # print(communication_frequency)
    #
    # # the extensions
    # print(selected_initial_data_set_saving_format)  # "txt"
    # print(selected_initial_data_set_loading_format) # "txt"
    # print(selected_preProcessed_data_set_saving_format)  # "txt"
    # print(selected_data_bank_saving_format)  # "csv" or "mat"
    #
    # # permissions
    # print(make_new_data_set) # if 'make_new_data_set=False' >> it will load an existing "data-set.selected_loading_format"
    #                                     # if 'make_new_data_set=False' and 'exist(InitialDataSet) == 0' >> # automatically changes: 'make_new_data_set=True'
    #
    # print(run_preProcess)
    # print(run_finger_print_production)
    # print(run_postProcess)
    # print(save_initial_data_set)
    # print(save_preProcessed_data_set)  # if 'run_preProcess=False' >> automatically: 'save_preProcessed_data_set=False'
    # print(save_data_bank)              # if 'run_finger_print_production=False' >> automatically: 'save_data_bank=False'
    #
    # print(add_labels_to_saved_data_bank)      # if 'run_finger_print_production=False'
    #                                                     # or 'selected_data_bank_saving_format!=csv'
    #                                                     # >> automatically:  'add_labels_to_saved_data_bank=False'
    #
    # print(selected_characteristics_extraction_methods_for_data_set_making)
    # print(selected_conversion_methods_for_preProcessing)
    # print(selected_feature_extraction_methods_for_finger_printing)
    # print(selected_conversion_methods_for_postProcessing)
    # print(dimension_must_be_in_rows_or_columns)




























    # # Input Parameters
    # project_name = "PythonVersion"
    # selected_data_set_name = "2016_07_11_IQ_20Msps_RZUSBSTICK"  # if it is empty, a pop-up window will give you the opportunity to select it graphically   2016_07_11_IQ_20Msps_RZUSBSTICK
    # zero_conversion_threshold = 0.7,
    # number_of_subRegions = 32,
    # number_of_symbols_per_preamble = 8,
    # number_of_chips_per_subRegion = 4,
    # time_length_of_a_single_chip_in_second = 1e-6,
    # sampling_frequency = 20e6,
    # communication_frequency = 2e6,
    #
    # # the extensions
    # selected_initial_data_set_saving_format = "txt"  # "txt"
    # selected_initial_data_set_loading_format = "txt"  # "txt"
    # selected_preProcessed_data_set_saving_format = "txt"  # "txt"
    # selected_data_bank_saving_format = "csv"  # "csv" or "mat"
    #
    # # output data_bank structure
    # dimension_must_be_in_rows_or_columns = "columns"  # rows or columns
    #
    # # permissions
    # make_new_data_set = True  # if 'make_new_data_set=False' >> it will load an existing "data-set.selected_loading_format"
    # # if 'make_new_data_set=False' and 'exist(InitialDataSet) == 0' >> # automatically changes: 'make_new_data_set=True'
    #
    # run_preProcess = True
    # run_finger_print_production = True
    # run_postProcess = True  # if 'run_finger_print_production=False' >> automatically: 'run_postProcess=False'
    # save_initial_data_set = True
    # save_preProcessed_data_set = True  # if 'run_preProcess=False' >> automatically: 'save_preProcessed_data_set=False'
    # save_data_bank = True  # if 'run_finger_print_production=False' >> automatically: 'save_data_bank=False'
    #
    # add_labels_to_saved_data_bank = True  # if 'run_finger_print_production=False'
    # # or 'selected_data_bank_saving_format!=csv'
    # # >> automatically:  'add_labels_to_saved_data_bank=False'
    #
    # selected_characteristics_extraction_methods_for_data_set_making = {1: {
    #                                                                         "module_name":
    #                                                                             "amplitude_calculator",
    #                                                                         "class_name": "",
    #                                                                         "method_name":
    #                                                                             "amp",
    #                                                                         "special_parameters":
    #                                                                             {""}
    #                                                                        },
    #                                                                     2: {
    #                                                                         "module_name":
    #                                                                             "phase_calculator",
    #                                                                         "class_name": "",
    #                                                                         "method_name":
    #                                                                             "phase",
    #                                                                         "special_parameters":
    #                                                                             {""}
    #                                                                     },
    #                                                                     3: {
    #                                                                         "module_name":
    #                                                                             "ifrequency_calculator",
    #                                                                         "class_name": "",
    #                                                                         "method_name":
    #                                                                             "ifreq",
    #                                                                         "special_parameters":
    #                                                                             {""}
    #                                                                     },
    #                                                                    4: ""}  # these functions are executed in the order of keys
    #
    # selected_characteristics_extraction_methods_for_data_set_making = {1: {
    #     "module_name":
    #         "no_change_char",
    #     "class_name": "",
    #     "method_name":
    #         "no_change_char",
    #     "special_parameters":
    #         {""}
    # }
    # }  # these functions are executed in the order of keys
    #
    # selected_conversion_methods_for_preProcessing = {1:
    #     {
    #         "module_name": "dwt_calculator",
    #         "class_name": "",
    #         "method_name": "dwt_calculator",
    #         "special_parameters": {"important_element": "details"}  # 'approximations' or 'details'
    #     },
    #     2: ""}  # these functions are executed in order of the keys
    #
    # selected_feature_extraction_methods_for_finger_printing = {1:
    #                                                                {"module_name": "variance",
    #                                                                 "class_name": "",
    #                                                                 "method_name": "variance",
    #                                                                 "special_parameters": {}
    #                                                                 },
    #                                                            2:
    #                                                                {"module_name": "skewness",
    #                                                                 "class_name": "",
    #                                                                 "method_name": "skewness",
    #                                                                 "special_parameters": {}
    #                                                                 },
    #                                                            3:
    #                                                                {"module_name": "kurtosis",
    #                                                                 "class_name": "",
    #                                                                 "method_name": "kurt",
    #                                                                 "special_parameters": {}
    #                                                                 },
    #                                                            4: ""}  # these functions are executed in order of
    #
    # # selected_feature_extraction_methods_for_finger_printing = {1:
    # #                                                                {"module_name": "no_change_FP",
    # #                                                                 "class_name": "",
    # #                                                                 "method_name": "no_change_FP",
    # #                                                                 "special_parameters": {}
    # #                                                                 }
    # #                                                            }  # these functions are executed in order of
    #
    # selected_conversion_methods_for_postProcessing = {1:
    #     {
    #         "module_name": "normalizer",
    #         "class_name": "",
    #         "method_name": "normalizer",
    #         "special_parameters": {}
    #     },
    #     2:
    #         {
    #             "module_name": "standardizer",
    #             "class_name": "",
    #             "method_name": "standardizer",
    #             "special_parameters": {}
    #         },
    # }  # these functions are executed in order of the keys




















    # Address Extraction of Selected Data-Set
    root_folder_address = root_project_folder_address_extractor(target_folder_name=project_name)

    data_set_address = raw_data_folder_address_extractor(root_folder_address, selected_data_set_name)

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


if __name__ == '__main__':
    # print(main.__doc__)
    # help(main)
    a = main()
    print(a.keys())
