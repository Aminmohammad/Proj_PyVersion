import os

import sys
from numpy.matlib import repmat
from pylab import size, amax
from scipy.io import loadmat
from scipy.sparse import csc_matrix
from numpy import array, zeros, arange, shape, hstack

from DataSetLoader.Characteristics_Extractor.Characteristics_Extractor import Characteristics_Extractor
from DataSetLoader.Device_RawData_Loading.Burst_Index_Extractor import Burst_Index_Extractor


def device_raw_data_loading(**kwarg):
    # Extraction of inputs
    device_data_set_address = kwarg["device_data_set_address"]
    zero_conversion_threshold = array(kwarg["zero_conversion_threshold"])
    number_of_subregions = int(array(kwarg["number_of_subregions"]))
    number_of_symbols_per_preamble = array(kwarg["number_of_symbols_per_preamble"])
    number_of_chips_per_subregion = array(kwarg["number_of_chips_per_subregion"])
    time_length_of_a_single_chip_in_second = array(kwarg["time_length_of_a_single_chip_in_second"])
    sampling_frequency = array(kwarg["sampling_frequency"])
    characteristics_extractor_method = kwarg["characteristics_extractor_method"]

    # Extracting the Address of all Records in the 'DataSet Folder' for a Single Device
    list_of_records = os.listdir(device_data_set_address)

    # Extracting of Essential Parameters
    number_of_subregions_per_preamble = int(number_of_subregions / number_of_symbols_per_preamble)

    # Extracting all Records of Current Device
    overall_burst_index = 0
    vertical_hashmap_of_all_bursts = {}
    for records_Index in [0]:#range(len(list_of_records)):
        name_of_current_record = list_of_records[records_Index]
        print("    Record:" + str(records_Index))
        address_of_current_record = device_data_set_address + "/" + name_of_current_record

        # Loading a Single Record
        record = loadmat(address_of_current_record)
        record = csc_matrix(record['sparse_matrix'])
        record = record.toarray()
        # Extracting the 'Bursts' and 'subRegions' of a Single Record
        threshold = zero_conversion_threshold * amax(record)
        bursts_indices_matrix = Burst_Index_Extractor(record, threshold)  # indices_of_Bursts = find (
        # content_of_Current_Record > .1 * max ( content_of_Current_Record ) )

        key_values = bursts_indices_matrix.keys()

        for burst_Index in range(len(key_values)):
            print("        burst_Index:" + str(burst_Index))
            temp = bursts_indices_matrix[str(burst_Index)]

            starting_point = temp[0]
            ending_point = temp[1]

            current_burst = record[starting_point: ending_point, 0]

            # Extraction of Preamble
            length_of_a_single_preamble = int(number_of_symbols_per_preamble *
                                              number_of_subregions_per_preamble *
                                              number_of_chips_per_subregion *
                                              time_length_of_a_single_chip_in_second *
                                              sampling_frequency)

            if size(current_burst, 0) < length_of_a_single_preamble:
                temp0 = []
                # current_burst = repmat(current_burst, number_of_subregions, 1)
                temp1 = zeros(length_of_a_single_preamble - size(current_burst, 0), 1)
                temp0 = temp0.append(current_burst)
                temp0 = temp0.append(temp1)
                current_burst = array(temp0)
            else:
                current_burst = array(current_burst[0: length_of_a_single_preamble])
            current_burst = array(current_burst)
            # subRegions of 'current_burst'
            length_of_a_single_subregion = int(size(current_burst) / number_of_subregions)

            pure_all_subregions = []
            amplitude_all_subregions = []
            phase_all_subregions = []
            ifrequency_all_subregions = []
            vertical_hash_map_of_a_single_burst = {}
            for subRegion_Index in arange(number_of_subregions + 1):
                # print("            subRegion_Index:" + str(subRegion_Index))
                if subRegion_Index < number_of_subregions:
                    starting_index = subRegion_Index * length_of_a_single_subregion
                    ending_index = (subRegion_Index + 1) * length_of_a_single_subregion
                    a_single_subregion = current_burst[starting_index:ending_index]

                    amplitude, phase, ifrequency = Characteristics_Extractor(a_single_subregion,
                                                                             characteristics_extractor_method)

                    # if allow == 1:
                    #     tree = pywt.wavedec(a_single_subregion, 'haar')
                    #     tree = tree[0][0:79]
                    #     figure()
                    #     plot(tree)
                    #     show(block=False)
                    #     allow = 0

                    # vertical_hash_map_of_a_single_burst[
                    #     "pure_single_subRegion_" + str(subRegion_Index)] = a_single_subregion
                    vertical_hash_map_of_a_single_burst[
                        "amp_single_subRegion_" + str(subRegion_Index)] = amplitude
                    vertical_hash_map_of_a_single_burst[
                        "phase_single_subRegion_" + str(subRegion_Index)] = phase

                    vertical_hash_map_of_a_single_burst[
                        "ifreq_single_subRegion_" + str(subRegion_Index)] = ifrequency

                    pure_all_subregions = hstack((pure_all_subregions, a_single_subregion))
                    amplitude_all_subregions = hstack((amplitude_all_subregions, amplitude))
                    phase_all_subregions = hstack((phase_all_subregions, phase))
                    ifrequency_all_subregions = hstack((ifrequency_all_subregions, ifrequency))
                else:

                    # vertical_hash_map_of_a_single_burst[
                    #     "pure_single_subRegion_" + str(subRegion_Index)] = array(pure_all_subregions)

                    vertical_hash_map_of_a_single_burst[
                        "amp_single_subRegion_" + str(subRegion_Index)] = amplitude_all_subregions

                    vertical_hash_map_of_a_single_burst[
                        "phase_single_subRegion_" + str(subRegion_Index)] = phase_all_subregions

                    vertical_hash_map_of_a_single_burst[
                        "ifreq_single_subRegion_" + str(subRegion_Index)] = ifrequency_all_subregions

                    # saving the Single Burst
                    vertical_hashmap_of_all_bursts[str(overall_burst_index)] = vertical_hash_map_of_a_single_burst
                    overall_burst_index += 1

    return vertical_hashmap_of_all_bursts
