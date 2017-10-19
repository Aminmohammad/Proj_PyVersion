from ProjectManager.project_manager import project_manager
from GeneralTools.FolderAddressExtractor.folder_address_extractor import folder_address_extractor
from tkinter import Tk, filedialog
import os, sys


def main():
    # TODO: here is the place of Graphic Resources Address


    """
    Start of program
    """
    # Input Parameters
    selected_data_set_name = "2016_07_11_IQ_20Msps_RZUSBSTICK"
    zero_conversion_threshold = 0.7,
    number_of_subRegions = 32,
    number_of_symbols_per_preamble = 8,
    number_of_chips_per_subRegion = 4,
    time_length_of_a_single_chip_in_second = 1e-6,
    sampling_frequency = 20e6,
    communication_frequency = 2e6,
    characteristics_extractor_method = "AmpPhaseFreq_Chars"
    selected_conversion_methods = "dwt_calculator"  # TODO: make it plural
    selected_saving_format = "csv"  # "csv" or "mat"
    selected_loading_format = "csv"  # "csv" or "mat"

    # permissions
    make_new_data_set = True  # if 'make_new_data_set=False' >> it will load an existing
    # "data-set.selected_loading_format"
    run_preProcess = True
    run_finger_print_production = True
    save_initial_data_set = True
    save_preProcessed_data_set = True  # if 'run_preProcess=False' >> automatically: 'save_preProcessed_data_set=False'
    save_data_bank = True  # if 'run_finger_print_production=False' >> automatically: 'save_data_bank=False'

    # Address Extraction of Selected Data-Set
    root_folder_address = folder_address_extractor(target_folder_name="PythonVersion")
    data_set_address = root_folder_address + "\\Resources\\" + selected_data_set_name + "\\RawData"
    data_set_address = data_set_address.replace("\\", "/")

    output = project_manager(data_set_address=data_set_address,
                             zero_conversion_threshold=zero_conversion_threshold,
                             number_of_subRegions=number_of_subRegions,
                             number_of_symbols_per_preamble=number_of_symbols_per_preamble,
                             number_of_chips_per_subRegion=number_of_chips_per_subRegion,
                             time_length_of_a_single_chip_in_second=time_length_of_a_single_chip_in_second,
                             sampling_frequency=sampling_frequency,
                             communication_frequency=communication_frequency,
                             characteristics_extractor_method=characteristics_extractor_method,
                             selected_conversion_methods=selected_conversion_methods,
                             selected_saving_format=selected_saving_format,
                             selected_loading_format=selected_loading_format,
                             make_new_data_set=make_new_data_set,
                             run_preProcess=run_preProcess,
                             run_finger_print_production=run_finger_print_production,
                             save_initial_data_set=save_initial_data_set,
                             save_preProcessed_data_set=save_preProcessed_data_set,
                             save_data_bank=save_data_bank
                             )

    return output


if __name__ == '__main__':
    # print(main.__doc__)
    # help(main)
    a = main()
    print(a.keys())
