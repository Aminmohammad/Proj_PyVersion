import csv
import os

import sys
from numpy import array
import pickle

from DataSetLoader.Data_Loading_Manager.Data_Set_Loading_Manager import data_set_loading_manager
from GeneralTools.MATSaver.mat_file_saver import mat_file_saver
from GeneralTools.PickleSaver.pickle_file_saver import pickle_file_saver
from RFFingerprintGenerator.RFFP_Production_Manager.FingerPrint_Manager import \
    finger_print_manager
from GeneralTools.CSVSaver.csv_file_saver import csv_file_saver
from preFeatureGenerationProcessor.preProcessorManager.preProcessor_manager import preProcessor_manager


def project_manager(**kwargs):
    # TODO: manage kwargs
    """this is good"""

    # output
    output = {}
    # extract the DataSet
    extracted_data_set = data_set_loading_manager(
        data_set_address=kwargs["data_set_address"],
        zero_conversion_threshold=kwargs["zero_conversion_threshold"],
        number_of_subRegions=kwargs["number_of_subRegions"],
        number_of_symbols_per_preamble=kwargs["number_of_symbols_per_preamble"],
        number_of_chips_per_subRegion=kwargs["number_of_chips_per_subRegion"],
        time_length_of_a_single_chip_in_second=kwargs["time_length_of_a_single_chip_in_second"],
        sampling_frequency=kwargs["sampling_frequency"],
        communication_frequency=kwargs["communication_frequency"],
        characteristics_extractor_methods=kwargs["characteristics_extractor_methods"],
        make_new_data_set=kwargs["make_new_data_set"],
        selected_loading_format=kwargs["selected_initial_data_set_loading_format"],
        project_name=kwargs["project_name"]
    )

    output["Initial_data_set"] = extracted_data_set

    if kwargs["save_initial_data_set"]:
        kwargs["selected_saving_format"] = kwargs ["selected_initial_data_set_saving_format"]
        file_saver(extracted_data_set, "InitialDataSet", "initial_data_set", kwargs)

    # Running the pre-Processing
    if kwargs["run_preProcess"]:

        extracted_data_set = preProcessor_manager(extracted_data_set,
                                                  kwargs["selected_conversion_methods"],
                                                  kwargs["project_name"])
        output["preProcessed_data_set"] = extracted_data_set

        if kwargs["save_preProcessed_data_set"]:
            kwargs["selected_saving_format"] = kwargs["selected_preProcessed_data_set_saving_format"]
            file_saver(extracted_data_set, "preProcessedDataSet", "preProcessed_data_set", kwargs)

    # producing the Finger-Print from `extracted_data_set`
    if kwargs["run_finger_print_production"]:
        data_bank = array(finger_print_manager(extracted_data_set,
                                               kwargs["selected_feature_extraction_methods"],
                                               kwargs["project_name"]))
        output["data_bank"] = data_bank.transpose()

        if kwargs["save_preProcessed_data_set"]:
            kwargs["selected_saving_format"] = kwargs["selected_data_bank_saving_format"]
            file_saver(data_bank.transpose(), "DataBank", "data_bank", kwargs)

    return output


def file_saver(data, folder_name, file_name, kwargs):
    data_saving_address = kwargs["data_set_address"].replace("RawData", folder_name)
    if not (os.path.exists(data_saving_address)):
        os.makedirs(data_saving_address)

    if kwargs["selected_saving_format"] == "csv":
        csv_file_saver(data, data_saving_address, file_name)

    elif kwargs["selected_saving_format"] == "txt":
        pickle_file_saver(data, data_saving_address, file_name)

    elif kwargs["selected_saving_format"] == "mat":
        mat_file_saver(data, data_saving_address, file_name)
