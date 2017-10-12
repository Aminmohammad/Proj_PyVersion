from numpy import vstack, size, reshape, column_stack, row_stack, shape, array

from Tools.StatisticsGenerator.StatisticsGenaerator_Manager import statistics_generator_manager


def generated_data_set_reader(**kwargs):
    extracted_data_set = dict(kwargs["extracted_data_set"])
    data_bank = [0]
    first_burst = True

    device_label = 0
    label_horz_vector = [0]
    for device_data_set_key in extracted_data_set.keys():
        bursts_of_a_single_device = dict(extracted_data_set[device_data_set_key])
        device_label += 1

        for burst_key in bursts_of_a_single_device.keys():
            burst = dict(bursts_of_a_single_device[burst_key])
            burst_finger_print = [0]
            for subregion_key in burst.keys():
                subregion_calculated_characteristic = burst[subregion_key]
                calculated_statistics_for_subregion = dict(statistics_generator_manager
                                                           (subregion_calculated_characteristic))

                for stat_key in calculated_statistics_for_subregion.keys():
                    burst_finger_print = vstack((burst_finger_print, calculated_statistics_for_subregion[stat_key]))

            burst_finger_print = burst_finger_print[1:]
            burst_finger_print = reshape(burst_finger_print, size(burst_finger_print), 1)
            if first_burst:
                data_bank = burst_finger_print
                first_burst = False

            else:
                data_bank = column_stack((data_bank, burst_finger_print))

            label_horz_vector = column_stack((label_horz_vector, [device_label]))

    label_horz_vector = array(label_horz_vector)
    data_bank = array(data_bank)
    label_horz_vector = label_horz_vector[0, 1:]
    data_bank = row_stack((data_bank, label_horz_vector))

    return data_bank

