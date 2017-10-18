import os

from DataSetLoader.Device_RawData_Loading.Device_RawData_Loading import device_raw_data_loading
from GeneralTools.CSVLoader.csv_file_loader import csv_file_loader
from GeneralTools.MATLoader.mat_file_loader import mat_file_loader


class DataSetMakerOrLoader:
    def __init__(self, input_set):
        self.vertical_structure_of_all_devices = {}
        self.data_set_address = input_set["data_set_address"]
        self.make_new_data_set = input_set["make_new_data_set"]
        self.zero_conversion_threshold = input_set["zero_conversion_threshold"]
        self.number_of_subregions = input_set["number_of_subRegions"]

        self.number_of_symbols_per_preamble = input_set["number_of_symbols_per_preamble"]
        self.number_of_chips_per_subregion = input_set["number_of_chips_per_subRegion"]
        self.time_length_of_a_single_chip_in_second = input_set[
            "time_length_of_a_single_chip_in_second"]
        self.sampling_frequency = input_set["sampling_frequency"]
        self.communication_frequency = input_set["communication_frequency"]
        self.characteristics_extractor_method = input_set["characteristics_extractor_method"]
        self.selected_loading_format = input_set["selected_loading_format"]
        self.file_address = []
        self.loading_data_set_address = []

    def method_caller(self):
        self.loading_data_set_address = self.data_set_address.replace("RawData", "InitialDataSet")
        self.file_address = self.loading_data_set_address + "//data_set." + self.selected_loading_format
        if (not self.make_new_data_set) and (
                os.path.isfile(self.file_address)):
            data_set = self.data_set_loader()
        else:
            data_set = self.data_set_maker()

        return data_set

    def data_set_loader(self):
        # if self.selected_loading_format == "csv":
        #     data_set = csv_file_loader(self.file_address)
        #
        # elif self.selected_loading_format == "mat":
        #     data_set = mat_file_loader(self.file_address)
        data_set = self.data_set_maker()

        # TODO: Un-comment previous files and delete: 'data_set = self.data_set_maker()'

        return data_set

    def data_set_maker(self):
        list_of_folders_in_the_data_set_folder = os.listdir(self.data_set_address)
        for device_index in [0, 1]:  # range(len(list_of_folders_in_the_data_set_folder)):
            print("device:%d" % device_index)
            current_data_location = self.data_set_address + "/" + list_of_folders_in_the_data_set_folder[device_index]
            vertical_structure_of_all_bursts = device_raw_data_loading(device_data_set_address=current_data_location,
                                                                       zero_conversion_threshold=
                                                                       self.zero_conversion_threshold,
                                                                       number_of_subregions=self.number_of_subregions,
                                                                       number_of_symbols_per_preamble=
                                                                       self.number_of_symbols_per_preamble,
                                                                       number_of_chips_per_subregion=
                                                                       self.number_of_chips_per_subregion,
                                                                       time_length_of_a_single_chip_in_second=
                                                                       self.time_length_of_a_single_chip_in_second,
                                                                       sampling_frequency=
                                                                       self.sampling_frequency,
                                                                       communication_frequency=
                                                                       self.communication_frequency,
                                                                       characteristics_extractor_method=
                                                                       self.characteristics_extractor_method)

            self.vertical_structure_of_all_devices["single_device_"
                                                   + str(device_index)] = vertical_structure_of_all_bursts

        return self.vertical_structure_of_all_devices
