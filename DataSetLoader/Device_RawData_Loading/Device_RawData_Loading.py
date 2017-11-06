import os

import sys
from numpy import array, zeros, arange, hstack
from pylab import size, amax
from scipy.io import loadmat
from scipy.sparse import csc_matrix

from DataSetLoader.CharTools.Manager.Characteristics_Extractor import characteristics_extractor
from DataSetLoader.Device_RawData_Loading.Burst_Index_Extractor import Burst_Index_Extractor
from DataSetLoader.PhaseCompensator.phase_compensator import phase_compensator
from GeneralTools.ModuleOrClassImporterSection.ImporterMethodsManager.ImporterMethedsManager import \
    importer_methods_manager


def device_raw_data_loading(**kwarg):

    # Extraction of inputs
    device_data_set_address = kwarg["device_data_set_address"]
    zero_conversion_threshold = array(kwarg["zero_conversion_threshold"])
    number_of_subregions = int(array(kwarg["number_of_subregions"]))
    number_of_symbols_per_preamble = array(kwarg["number_of_symbols_per_preamble"])
    number_of_chips_per_subregion = array(kwarg["number_of_chips_per_subregion"])
    time_length_of_a_single_chip_in_second = array(kwarg["time_length_of_a_single_chip_in_second"])
    sampling_frequency = array(kwarg["sampling_frequency"])
    communication_frequency = array(kwarg["communication_frequency"])
    characteristics_extractor_methods = kwarg["characteristics_extractor_methods"]
    project_name = kwarg["project_name"]

    # Extracting the Address of all Records in the 'DataSet Folder' for a Single Device
    list_of_records = os.listdir(device_data_set_address)

    # Extracting of Essential Parameters
    number_of_subregions_per_preamble = int(number_of_subregions / number_of_symbols_per_preamble)

    # extraction of modules
    selected_methods = importer_methods_manager(project_name, characteristics_extractor_methods)

    # Extracting all Records of Current Device
    overall_burst_index = 0
    vertical_hashmap_of_all_bursts = {}
    for records_Index in range(len(list_of_records)):
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
                temp1 = zeros(length_of_a_single_preamble - size(current_burst, 0), 1)
                temp0 = temp0.append(current_burst)
                temp0 = temp0.append(temp1)
                current_burst = array(temp0)
            else:
                current_burst = array(current_burst[0: length_of_a_single_preamble])
            current_burst = array(current_burst)

            # burst phase compensation
            current_burst = phase_compensator(preamble=current_burst,
                                              sampling_frequency=sampling_frequency,
                                              communication_frequency=communication_frequency)
            # TODO: Omit these lines

            # subRegions of 'current_burst'
            length_of_a_single_subregion = int(size(current_burst) / number_of_subregions)

            pure_all_subregions = []
            vertical_hash_map_of_a_single_burst = {}
            fields = {}
            for subRegion_Index in arange(number_of_subregions + 1):
                if subRegion_Index < number_of_subregions:
                    starting_index = subRegion_Index * length_of_a_single_subregion
                    ending_index = (subRegion_Index + 1) * length_of_a_single_subregion
                    a_single_subregion = current_burst[starting_index:ending_index]

                    # Selected Character Extraction Methods
                    subRegion_characteristics = characteristics_extractor(a_single_subregion,
                                                                          selected_methods)

                    pure_all_subregions = hstack((pure_all_subregions, a_single_subregion))
                    # TODO: this assignmentation is still in vein

                    # getting all characteristics of a single subRegion
                    for key in subRegion_characteristics.keys():
                        vertical_hash_map_of_a_single_burst[
                            key + "_single_subRegion_" + str(subRegion_Index)] = array(subRegion_characteristics[key])

                        fields[key] = key

                        # saving the current subRegion in the Dictionary of Burst
                        if not (("%s_all_subregions" % key) in locals()):
                            vars()[("%s_all_subregions" % key)] = array(subRegion_characteristics[key])

                        else:
                            vars()[("%s_all_subregions" % key)] = hstack((vars()[("%s_all_subregions" % key)],
                                                                          array(subRegion_characteristics[key])))

                else:
                    # saving and deleting all subRegions together in the Nr+1 subRegion
                    for key in fields.keys():
                        vertical_hash_map_of_a_single_burst[
                            key + "_single_subRegion_" + str(subRegion_Index)] = array(
                            vars()[("%s_all_subregions" % key)])
                        del (vars()[("%s_all_subregions" % key)])

                    # saving the Single Burst in the Dictionary of all Bursts
                    vertical_hashmap_of_all_bursts[str(overall_burst_index)] = vertical_hash_map_of_a_single_burst
                    overall_burst_index += 1

    return vertical_hashmap_of_all_bursts
