import os
import timeit

from numpy import array

from DataSetLoader.Data_Loading_Manager.Data_Set_Loading_Manager import data_set_loading_manager
from GeneralTools.MATSaver.mat_file_saver import mat_file_saver
from GeneralTools.PickleSaver.pickle_file_saver import pickle_file_saver
from GeneralTools.TimeCalculator.time_caculator import time_calculator
from RFFingerprintGenerator.RFFP_Production_Manager.FingerPrint_Manager import \
    finger_print_manager
from GeneralTools.CSVSaver.csv_file_saver import csv_file_saver
from postFeatureGenerationProcessor.postProcessorManager.postProcessor_manager import postProcessor_manager
from preFeatureGenerationProcessor.preProcessorManager.preProcessor_manager import preProcessor_manager


def project_manager(**kwargs):
    # TODO: manage kwargs
    """this is good"""

    # output
    output = {}
    simulation_times = {}

    # extract the DataSet
    data_set_making_time_start = timeit.default_timer()
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

    data_set_making_time_end = timeit.default_timer()
    temp = {"value": time_calculator(data_set_making_time_end - data_set_making_time_start)[0],
            "label": time_calculator(data_set_making_time_end - data_set_making_time_start)[1]}
    simulation_times["data_set_making/loading_time"] = temp

    output["Initial_data_set"] = extracted_data_set
    if kwargs["save_initial_data_set"]:
        kwargs["selected_saving_format"] = kwargs["selected_initial_data_set_saving_format"]
        file_saver(extracted_data_set, "InitialDataSet", "initial_data_set", kwargs)

    # Running the pre-Processing
    if kwargs["run_preProcess"]:
        preProcess_time_start = timeit.default_timer()
        extracted_data_set = preProcessor_manager(extracted_data_set,
                                                  kwargs["selected_preProcessing_conversion_methods"],
                                                  kwargs["project_name"])

        preProcess_time_end = timeit.default_timer()
        temp = {"value": time_calculator(preProcess_time_end - preProcess_time_start)[0],
                "label": time_calculator(preProcess_time_end - preProcess_time_start)[1]}

        simulation_times["preProcess_time"] = temp
        print(simulation_times["preProcess_time"])

        output["preProcessed_data_set"] = extracted_data_set

        if kwargs["save_preProcessed_data_set"]:
            kwargs["selected_saving_format"] = kwargs["selected_preProcessed_data_set_saving_format"]
            file_saver(extracted_data_set, "preProcessedDataSet", "preProcessed_data_set", kwargs)

    # producing the Finger-Print from `extracted_data_set
    if kwargs["run_finger_print_production"]:
        data_bank_time_start = timeit.default_timer()
        data_bank, collected_labels = finger_print_manager(extracted_data_set,
                                                           kwargs["selected_feature_extraction_methods"],
                                                           kwargs["project_name"])

        data_bank_time_end = timeit.default_timer()
        temp = {"value": time_calculator(data_bank_time_end - data_bank_time_start)[0],
                "label": time_calculator(data_bank_time_end - data_bank_time_start)[1]}

        simulation_times["data_bank_time"] = temp
        data_bank = array(data_bank)  # Here, dimensions are in 'Rows'

        kwargs["collected_labels"] = collected_labels

        if kwargs["dimension_must_be_in_rows_or_columns"] == "columns":
            output["data_bank"] = data_bank.transpose()  # Here, dimensions are in 'Columns'

        elif kwargs["dimension_must_be_in_rows_or_columns"] == "rows":
            output["data_bank"] = data_bank  # Here, dimensions are in 'Rows'

        if kwargs["save_data_bank"]:
            kwargs["selected_saving_format"] = kwargs["selected_data_bank_saving_format"]
            file_saver(output["data_bank"], "DataBank", "data_bank", kwargs)

    # Running the post-Processing
    if kwargs["run_finger_print_production"] and kwargs["run_postProcess"]:
        postProcess_time_start = timeit.default_timer()
        new_data_bank, new_collected_labels = postProcessor_manager(data_bank,  # Here, dimensions are in 'Rows'
                                                                    kwargs["project_name"],
                                                                    kwargs[
                                                                        "selected_postProcessing_conversion_methods"],
                                                                    kwargs["dimension_must_be_in_rows_or_columns"])
        #   new_data_bank: Dimensions are in 'Rows'

        postProcess_time_end = timeit.default_timer()
        temp = {"value": time_calculator(postProcess_time_end - postProcess_time_start)[0],
                "label": time_calculator(postProcess_time_end - postProcess_time_start)[1]}

        simulation_times["postProcess_time"] = temp

        if new_collected_labels:
            kwargs["collected_labels"] = new_collected_labels

        if kwargs["dimension_must_be_in_rows_or_columns"] == "columns":
            output["postProcessed_data_bank"] = new_data_bank.transpose()  # Here, dimensions are in 'Columns'

        elif kwargs["dimension_must_be_in_rows_or_columns"] == "rows":
            output["postProcessed_data_bank"] = new_data_bank  # here, dimensions are in 'Rows'

        if kwargs["save_data_bank"]:
            kwargs["selected_saving_format"] = kwargs["selected_data_bank_saving_format"]
            file_saver(output["postProcessed_data_bank"], "postProcessedDataBank", "postProcessed_data_set", kwargs)

    output["simulation_times"] = simulation_times

    return output


def file_saver(data, folder_name, file_name, kwargs):
    data_saving_address = kwargs["data_set_address"].replace("RawData", folder_name)
    if not (os.path.exists(data_saving_address)):
        os.makedirs(data_saving_address)

    if kwargs["selected_saving_format"] == "csv":
        csv_file_saver(data, data_saving_address, file_name, kwargs)

    elif kwargs["selected_saving_format"] == "txt":
        special_input = []
        pickle_file_saver(data, data_saving_address, file_name, special_input)

    elif kwargs["selected_saving_format"] == "mat":
        special_input = []
        mat_file_saver(data, data_saving_address, file_name, special_input)
