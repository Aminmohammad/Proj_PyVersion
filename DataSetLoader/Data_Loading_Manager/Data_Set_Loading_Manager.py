import sys

from DataSetLoader.DataSet_Maker.DataSet_Maker import DatasetMakerOrLoader


def data_set_loading_manager(**kwargs):
    input_hash_map = {"do_You_Want_to_Make_new_DataSet": kwargs["do_You_Want_to_Make_new_DataSet"],
                      "data_Set_Address": kwargs["data_Set_Address"],
                      "zero_Conversion_Threshold": kwargs["zero_Conversion_Threshold"],
                      "number_of_subRegions": kwargs["number_of_subRegions"],
                      "number_of_Symbols_per_Preamble": kwargs["number_of_Symbols_per_Preamble"],
                      "number_of_Chips_per_subRegion": kwargs["number_of_Chips_per_subRegion"],
                      "time_length_of_a_single_chip_in_second": kwargs[
                      "time_length_of_a_single_chip_in_second"],
                      "sampling_Frequency": kwargs["sampling_Frequency"],
                      "characteristics_Extractor_Method": kwargs["characteristics_Extractor_Method"]}

    dsmol_instance = DatasetMakerOrLoader(input_hash_map)
    extracted_data_set = dsmol_instance.method_caller()

    print(extracted_data_set)

    return extracted_data_set
