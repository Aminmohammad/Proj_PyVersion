import csv

from DataSetLoader.B_DataSet_Maker.DataSet_Maker import DatasetMakerOrLoader


def initialization(test):
    data_set_address = "U:\\MAHAB\Ph.D._Files\\PHD_Project_Folder\Resources\\2016_07_11_IQ_20Msps_RZUSBSTICK\\RawData"
    data_set_address = data_set_address.replace("\\", "/")

    input_hash_map = {"do_You_Want_to_Make_new_DataSet": True,
                      "data_Set_Address": data_set_address,
                      "zero_Conversion_Threshold": 0.7,
                      "number_of_subRegions": 32,
                      "number_of_Symbols_per_Preamble": 8,
                      "number_of_Chips_per_subRegion": 4,
                      "time_Length_of_a_Single_Chip_with_Respect_to_Seconds": 1e-6,
                      "sampling_Frequency": 20e6,
                      "allow": 1,
                      "characteristics_Extractor_Method": "AmpPhaseFreq_Chars",
                      }

    dg = DatasetMakerOrLoader(input_hash_map)
    dataSet = dg.method_Caller()
    print(dataSet)
    w = csv.writer(open("output.csv", "w"))
    for key, val in dataSet.items():
        w.writerow([key, val])


if __name__ == '__main__':
    initialization('Test')
