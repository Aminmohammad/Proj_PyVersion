import os

import pywt
from numpy.matlib import repmat
from pylab import size, amax, figure, plot, show
from scipy.io import loadmat
from scipy.sparse import csc_matrix

from C_Device_RawData_Loading.Burst_Index_Extractor import Burst_Index_Extractor
from D_Characteristics_Extractor.Characteristics_Extractor import Characteristics_Extractor


def Device_RawData_Loading(device_dataset_address,
                           zero_conversion_threshold,
                           number_of_subregions,
                           number_of_symbols_per_preamble,
                           number_of_chips_per_subregion,
                           time_length_of_a_single_chip_with_respect_to_seconds,
                           sampling_frequency,
                           allow,
                           characteristics_Extractor_Method):

    # Extracting the Address of all Records in the 'DataSet Folder' for a Single Device
    list_of_records = os.listdir(device_dataset_address)

    # Extracting of Essential Parameters

    number_of_subregions_per_preamble = int(number_of_subregions / number_of_symbols_per_preamble)

    # Extracting all Records of Current Device
    for records_Index in range(len(list_of_records)):
        name_of_current_record = list_of_records[records_Index]
        print("Record:" + str(records_Index))
        address_of_current_record = device_dataset_address + "/" + name_of_current_record

        # Loading a Single Record
        record = loadmat(address_of_current_record)
        record = record['sparse_matrix']

        record = csc_matrix(record, dtype=float)
        record = record.todense()

        # Extracting the 'Bursts' and 'subRegions' of a Single Record
        #  indices_of_Bursts = find (content_of_Current_Record > .1 * max ( content_of_Current_Record ) )
        threshold = zero_conversion_threshold * amax(record)
        bursts_indices_matrix = Burst_Index_Extractor(record, threshold)

        key_values = bursts_indices_matrix.keys()

        vertical_hashmap_of_all_bursts = {}
        for burst_Index in range(len(key_values)):
            print("    burst_Index:" + str(burst_Index))
            temp = bursts_indices_matrix[str(burst_Index)]

            starting_point = temp[0]
            ending_point = temp[1]

            current_burst = record[starting_point: ending_point, 0]

            # Extraction of Preamble
            length_of_a_single_preamble = int(number_of_symbols_per_preamble *
                                              number_of_subregions_per_preamble *
                                              number_of_chips_per_subregion *
                                              time_length_of_a_single_chip_with_respect_to_seconds *
                                              sampling_frequency)

            if size(current_burst, 0) < number_of_subregions:
                current_burst = repmat(current_burst, number_of_subregions, 1)
            else:
                current_burst = current_burst[0: length_of_a_single_preamble, 0]

            # subRegions of 'current_burst'
            length_of_a_single_subregion = int(size(current_burst, 0) / number_of_subregions)
            vertical_hashMap_of_a_single_burst = {}

            for subRegion_Index in range(number_of_subregions):
                print("        subRegion_Index:" + str(subRegion_Index))
                if subRegion_Index <= number_of_subregions:
                    starting_index = subRegion_Index * length_of_a_single_subregion
                    ending_index = (subRegion_Index + 1) * length_of_a_single_subregion - 1

                    a_single_subRegion = current_burst[starting_index:ending_index, 0]

                    Characteristics_Extractor ( a_single_subRegion,
                                                characteristics_Extractor_Method )

                    # if allow == 1:
                    #     tree = pywt.wavedec(a_single_subRegion, 'haar')
                    #     tree = tree[0][0:79]
                    #     figure()
                    #     plot(tree)
                    #     show(block=False)
                    #     allow = 0

                    vertical_hashMap_of_a_single_burst[
                        "a_Single_subRegion_" + str(subRegion_Index)] = a_single_subRegion

                else:

                    vertical_hashMap_of_a_single_burst["a_Single_subRegion_" + str(subRegion_Index)] = current_burst

                    # saving the Single Burst
                    vertical_hashmap_of_all_bursts[
                        "a_Single_Burst_" + str(burst_Index)] = vertical_hashMap_of_a_single_burst

    input("promt: ")

# a = array ([1+1j, 1+1j, 1+1j, 2+1j, 2+1j, 2+1j, 3+1j, 1+1j, 1+1j, 1+1j, 1+4j, 1+4j, 1+1j, 1+1j, 3+4j, 3+4j])
# Burst_Index_Extractor( a, 2 )


# def scalogram(data):
#     bottom = 0
#
#     vmin = min(map(lambda x: min(abs(x)), data))
#     vmax = max(map(lambda x: max(abs(x)), data))
#
#     gca().set_autoscale_on(False)
#
#     for row in range(0, len(data)):
#         scale = 2.0 ** (row - len(data))
#
#         imshow(
#             array([abs(data[row])]),
#             interpolation='nearest',
#             vmin=vmin,
#             vmax=vmax,
#             extent=[0, 1, bottom, bottom + scale])
#
#         bottom += scale
