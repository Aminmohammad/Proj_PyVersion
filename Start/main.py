from ProjectManager.project_manager import project_manager
from GeneralTools.FolderAddressExtractor.folder_address_extractor import folder_address_extractor


def main():
    """
    Start of program
    """
    # Input Parameters
    selected_data_set_name = "2016_07_11_IQ_20Msps_RZUSBSTICK"
    do_you_want_to_make_new_data_set = True,
    zero_conversion_threshold = 0.7,
    number_of_subRegions = 32,
    number_of_symbols_per_preamble = 8,
    number_of_chips_per_subRegion = 4,
    time_length_of_a_single_chip_in_second = 1e-6,
    sampling_frequency = 20e6,
    communication_frequency = 2e6,
    characteristics_extractor_method = "AmpPhaseFreq_Chars"

    # Address Extraction of Selected Data-Set
    root_folder_address = folder_address_extractor(target_folder_name="PythonVersion")
    data_set_address = root_folder_address + "\\resources\\" + selected_data_set_name + "\\RawData"
    data_set_address = data_set_address.replace("\\", "/")

    project_manager(do_you_want_to_make_new_data_set=do_you_want_to_make_new_data_set,
                    data_set_address=data_set_address,
                    zero_conversion_threshold=zero_conversion_threshold,
                    number_of_subRegions=number_of_subRegions,
                    number_of_symbols_per_preamble=number_of_symbols_per_preamble,
                    number_of_chips_per_subRegion=number_of_chips_per_subRegion,
                    time_length_of_a_single_chip_in_second=time_length_of_a_single_chip_in_second,
                    sampling_frequency=sampling_frequency,
                    communication_frequency=communication_frequency,
                    characteristics_extractor_method=characteristics_extractor_method,
                    )


if __name__ == '__main__':
    # print(main.__doc__)
    # help(main)
    main()
