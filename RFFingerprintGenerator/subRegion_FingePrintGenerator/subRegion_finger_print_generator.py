from numpy.ma import vstack, reshape, size, column_stack, array, row_stack
import sys

from Tools.StatisticsGenerator.StatisticsGenaerator_Manager import statistics_generator_manager


class SRFingerPrintGenerator(object):
    def __init__(self):
        self.device_label = 0
        self.burst_finger_print = 0
        self.subregion_calculated_characteristic = [0]
        self.all_characteristics_of_current_burst_covered = False
        self.label_vector = 0
        self.data_bank = 0

    def subRegion_finger_print_generator(self, **kwargs):
        self.device_label = kwargs["device_label"]
        subregion_calculated_characteristic = dict(statistics_generator_manager
                                                   (kwargs["subregion_calculated_characteristic"]))

        all_characteristics_of_current_burst_covered = kwargs["all_characteristics_of_current_burst_covered"]

        all_devices_of_current_burst_covered = kwargs["all_devices_of_current_burst_covered"]

        for stat_key in subregion_calculated_characteristic.keys():
            self.burst_finger_print = vstack((self.burst_finger_print, subregion_calculated_characteristic[stat_key]))
        # burst_finger_print = burst_finger_print[1:]
        # burst_finger_print = reshape(burst_finger_print, size(burst_finger_print), 1)

        if all_characteristics_of_current_burst_covered:
            self.data_bank = column_stack((self.data_bank, self.burst_finger_print))
            self.label_vector = column_stack((self.label_vector, self.device_label))
            self.burst_finger_print = 0

        if all_devices_of_current_burst_covered:
            self.data_bank = column_stack((self.data_bank, self.label_vector))

        # if self.first_burst:
        return self.burst_finger_print
