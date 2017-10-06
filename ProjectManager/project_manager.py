from DataSetLoader.Data_Loading_Manager.Data_Set_Loading_Manager import data_set_loading_manager
from RFFingerprintGenerator.RFFP_Production_Manager.FingerPrint_Production_Manager import finger_print_production_manager


def project_manager():
    # extract the DataSet
    data_set_address = ".\\2016_07_11_IQ_20Msps_RZUSBSTICK\\RawData"
    # Todo: make the address dynamic

    data_set_address = data_set_address.replace("\\", "/")

    extracted_data_set = data_set_loading_manager(do_You_Want_to_Make_new_DataSet=True,
                                                  data_Set_Address=data_set_address,
                                                  zero_Conversion_Threshold=0.7,
                                                  number_of_subRegions=32,
                                                  number_of_Symbols_per_Preamble=8,
                                                  number_of_Chips_per_subRegion=4,
                                                  time_length_of_a_single_chip_in_second=1e-6,
                                                  sampling_Frequency=20e6,
                                                  characteristics_Extractor_Method="AmpPhaseFreq_Chars"
                                                  )

    data_bank = finger_print_production_manager(extracted_data_set=extracted_data_set)
    data_bank.to_csv(data_set_address+"\\data_bank.csv")
    # Todo: make the address dynamic

    # pre-processing of extracted data-set



if __name__ == '__main__':
    project_manager()
