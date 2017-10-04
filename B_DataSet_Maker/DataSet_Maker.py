import os

import pickle

import scipy
import sys

from C_Device_RawData_Loading.Device_RawData_Loading import Device_RawData_Loading


class DatasetMakerOrLoader:
    def __init__(self, varargin):
        self.vertical_Structure_of_all_Devices = {}
        self.dataSet_Address = varargin["data_Set_Address"]
        self.do_You_Want_to_Make_new_DataSet = varargin["do_You_Want_to_Make_new_DataSet"]
        self.zero_Conversion_Threshold = varargin["zero_Conversion_Threshold"]
        self.number_of_subRegions = varargin["number_of_subRegions"]

        self.number_of_Symbols_per_Preamble = varargin["number_of_Symbols_per_Preamble"]
        self.number_of_Chips_per_subRegion = varargin["number_of_Chips_per_subRegion"]
        self.time_Length_of_a_Single_Chip_with_Respect_to_Seconds = varargin[
            "time_Length_of_a_Single_Chip_with_Respect_to_Seconds"]
        self.sampling_Frequency = varargin["sampling_Frequency"]
        self.allow = varargin["allow"]
        self.characteristics_Extractor_Method = varargin["characteristics_Extractor_Method"]

    def method_Caller(self):
        if (not self.do_You_Want_to_Make_new_DataSet) and (os.path.isfile(self.dataSet_Address + "//DataSet//DataSet.mat")):
            dataSet = self.Data_Set_Loader()
        else:
            dataSet = self.Data_Set_Maker()

            return dataSet

    def Data_Set_Loader(self):
        pass
        # TODO: Complete the code

    def Data_Set_Maker(self):
        list_of_folders_in_the_dataset_folder = os.listdir(self.dataSet_Address)
        # sys.exit(0)
        # scipy.io.savemat('arrdata.mat', mdict={'arr': self.vertical_Structure_of_all_Devices})
        for device_Index in [0]:
            #range(len(list_of_folders_in_the_dataset_folder))
            current_data_location = self.dataSet_Address + "/" + list_of_folders_in_the_dataset_folder[device_Index]
            vertical_structure_of_all_bursts = Device_RawData_Loading(current_data_location,
                                                                      self.zero_Conversion_Threshold,
                                                                      self.number_of_subRegions,
                                                                      self.number_of_Symbols_per_Preamble,
                                                                      self.number_of_Chips_per_subRegion,
                                                                      self.time_Length_of_a_Single_Chip_with_Respect_to_Seconds,
                                                                      self.sampling_Frequency,
                                                                      self.allow,
                                                                      self.characteristics_Extractor_Method)

            self.vertical_Structure_of_all_Devices[device_Index] = {"a_Single_Device": vertical_structure_of_all_bursts,
                                                                    }

        return self.vertical_Structure_of_all_Devices


# data_Set_Address = "D:\\PHD_Project_Folder\\Resources\\2016_07_11_IQ_20Msps_RZUSBSTICK\\RawData"
# data_Set_Address = data_Set_Address.replace("\\", "/")
#
# input_Hash_Map = {"do_You_Want_to_Make_new_DataSet": True,
#                   "data_Set_Address": data_Set_Address,
#                   "zero_Conversion_Threshold": 0.7,
#                   "number_of_subRegions": 32,
#                   "number_of_Symbols_per_Preamble": 8,
#                   "number_of_Chips_per_subRegion": 4,
#                   "time_Length_of_a_Single_Chip_with_Respect_to_Seconds": 1e-6,
#                   "sampling_Frequency": 20e6,
#                   "allow": 1,
#                   }
# dg = DatasetMakerOrLoader(input_Hash_Map)
# dg.method_Caller()
