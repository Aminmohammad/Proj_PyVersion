class DataSetMakerOrLoader:
    def __init__(self, input_set):
        x = DataSetMakerOrLoader
        self.vertical_structure_of_all_devices = {}
        self.data_set_address = input_set["data_set_address"]
        self.do_you_want_to_make_new_data_set = input_set["do_you_want_to_make_new_data_set"]
        self.zero_conversion_threshold = input_set["zero_conversion_threshold"]
        self.number_of_subregions = input_set["number_of_subRegions"]

        self.number_of_symbols_per_preamble = input_set["number_of_symbols_per_preamble"]
        self.number_of_chips_per_subregion = input_set["number_of_chips_per_subRegion"]
        self.time_length_of_a_single_chip_in_second = input_set[
            "time_length_of_a_single_chip_in_second"]
        self.sampling_frequency = input_set["sampling_frequency"]
        self.communication_frequency = input_set["communication_frequency"]
        # self.allow = input_set["allow"]
        self.characteristics_extractor_method = input_set["characteristics_extractor_method"]

    def method_caller(self):
        if (not self.do_you_want_to_make_new_data_set) and (
                os.path.isfile(self.data_set_address + "//DataSet//DataSet.mat")):
            self.data_set_loader()
        else:
            data_set = self.data_set_maker()

            return data_set

    def data_set_loader(self):
        pass
        # TODO: Complete the code

    def data_set_maker(self):
        list_of_folders_in_the_data_set_folder = os.listdir(self.data_set_address)
        # sys.exit(0)
        # scipy.io.savemat('arrdata.mat', mdict={'arr': self.vertical_Structure_of_all_Devices})
        for device_index in range(len(list_of_folders_in_the_data_set_folder)):
            current_data_location = self.data_set_address + "/" + list_of_folders_in_the_data_set_folder[device_index]
            vertical_structure_of_all_bursts = device_raw_data_loading(device_data_set_address=current_data_location,
                                                                       zero_conversion_threshold=self.zero_conversion_threshold,
                                                                       number_of_subregions=self.number_of_subregions,
                                                                       number_of_symbols_per_preamble=self.number_of_symbols_per_preamble,
                                                                       number_of_chips_per_subregion=self.number_of_chips_per_subregion,
                                                                       time_length_of_a_single_chip_in_second=self.time_length_of_a_single_chip_in_second,
                                                                       sampling_frequency=self.sampling_frequency,
                                                                       communication_frequency=self.communication_frequency,
                                                                       characteristics_extractor_method=self.characteristics_extractor_method)

            self.vertical_structure_of_all_devices["single_device_"
                                                   + str(device_index)] = vertical_structure_of_all_bursts

        return self.vertical_structure_of_all_devices
