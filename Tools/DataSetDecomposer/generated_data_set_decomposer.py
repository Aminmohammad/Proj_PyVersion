import sys
from numpy import vstack, size, reshape, column_stack, row_stack, shape, array

from RFFingerprintGenerator.subRegion_FingePrintGenerator.subRegion_finger_print_generator import SRFingerPrintGenerator
from Tools.StatisticsGenerator.StatisticsGenaerator_Manager import statistics_generator_manager

reference = SRFingerPrintGenerator()


def generated_data_set_decomposer(**kwargs):
    extracted_data_set = dict(kwargs["extracted_data_set"])
    data_bank = [0]
    first_burst = True

    device_label = 0
    for device_data_set_key in extracted_data_set.keys():
        bursts_of_a_single_device = dict(extracted_data_set[device_data_set_key])
        device_label += 1

        burst_key_list = array(list(bursts_of_a_single_device.keys()))
        number_of_bursts_covered_for_current_device = 0
        all_characteristics_of_current_burst_covered = False
        for burst_key in bursts_of_a_single_device.keys():
            burst = bursts_of_a_single_device[burst_key]
            number_of_bursts_covered_for_current_device += 1
            if number_of_bursts_covered_for_current_device == size(burst_key_list):
                all_characteristics_of_current_burst_covered = True

            for characteristic_key in burst.keys():  # since we have 3 chars for each subRegion

                output = reference.subRegion_finger_print_generator(device_label=device_label,
                                                                    subregion_calculated_characteristic=
                                                                    burst[characteristic_key],
                                                                    all_characteristics_of_current_burst_covered=
                                                                    all_characteristics_of_current_burst_covered)
                print(shape(output))

    # calculated_statistics_for_subregion = dict(statistics_generator_manager
    #                                                        (subregion_calculated_characteristic))
    #
    #             for stat_key in calculated_statistics_for_subregion.keys():
    #                 burst_finger_print = vstack((burst_finger_print, calculated_statistics_for_subregion[stat_key]))
    #
    #         burst_finger_print = burst_finger_print[1:]
    #         burst_finger_print = reshape(burst_finger_print, size(burst_finger_print), 1)
    #         if first_burst:
    #             data_bank = burst_finger_print
    #             first_burst = False
    #
    #         else:
    #             data_bank = column_stack((data_bank, burst_finger_print))
    #
    #         label_horz_vector = column_stack((label_horz_vector, [device_label]))
    #
    # label_horz_vector = array(label_horz_vector)
    # data_bank = array(data_bank)
    # label_horz_vector = label_horz_vector[0, 1:]
    # data_bank = row_stack((data_bank, label_horz_vector))

    return data_bank
