import sys

from DataSetLoader.DataSet_Maker.DataSet_Maker import DataSetMakerOrLoader


def data_set_loading_manager(**kwargs):
    input_hash_map = {"data_set_address": kwargs["data_set_address"],
                      "zero_conversion_threshold": kwargs["zero_conversion_threshold"],
                      "number_of_subRegions": kwargs["number_of_subRegions"],
                      "number_of_symbols_per_preamble": kwargs["number_of_symbols_per_preamble"],
                      "number_of_chips_per_subRegion": kwargs["number_of_chips_per_subRegion"],
                      "time_length_of_a_single_chip_in_second": kwargs["time_length_of_a_single_chip_in_second"],
                      "sampling_frequency": kwargs["sampling_frequency"],
                      "communication_frequency": kwargs["communication_frequency"],
                      "characteristics_extractor_methods": kwargs["characteristics_extractor_methods"],
                      "make_new_data_set": kwargs["make_new_data_set"],
                      "selected_loading_format": kwargs["selected_loading_format"],
                      "project_name": kwargs["project_name"]}

    dsmol_instance = DataSetMakerOrLoader(input_hash_map)
    extracted_data_set = dsmol_instance.method_caller()
    return extracted_data_set
