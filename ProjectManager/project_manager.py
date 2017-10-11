import sys

from numpy import savetxt, shape
import os

from DataSetLoader.Data_Loading_Manager.Data_Set_Loading_Manager import data_set_loading_manager
from RFFingerprintGenerator.RFFP_Production_Manager.FingerPrint_Production_Manager import \
    finger_print_production_manager
from Tools.CSVSaver.csv_file_saver import csv_file_saver


def project_manager(**kwarg):
    """this is good"""
    # extract the DataSet
    extracted_data_set = data_set_loading_manager(
        do_you_want_to_make_new_data_set=kwarg["do_you_want_to_make_new_data_set"],
        data_set_address=kwarg["data_set_address"],
        zero_conversion_threshold=kwarg["zero_conversion_threshold"],
        number_of_subRegions=kwarg["number_of_subRegions"],
        number_of_symbols_per_preamble=kwarg["number_of_symbols_per_preamble"],
        number_of_chips_per_subRegion=kwarg["number_of_chips_per_subRegion"],
        time_length_of_a_single_chip_in_second=kwarg["time_length_of_a_single_chip_in_second"],
        sampling_frequency=kwarg["sampling_frequency"],
        characteristics_extractor_method=kwarg["characteristics_extractor_method"]
    )
    # producing the Finger-Print from `extracted_data_set`
    data_bank = finger_print_production_manager(extracted_data_set=extracted_data_set)
    print(data_bank)
    print(type(data_bank))

    # saving the generated from data-bank
    data_bank_saving_address = kwarg["data_set_address"].replace("RawData", "DataBank")
    if not (os.path.exists(data_bank_saving_address)):
        os.makedirs(data_bank_saving_address)

    csv_file_saver(saving_address=data_bank_saving_address,
                   data=data_bank)

    # Todo: make the address dynamic

    # pre-processing of extracted data-set
