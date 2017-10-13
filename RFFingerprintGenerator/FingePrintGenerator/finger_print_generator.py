from numpy.ma import vstack, reshape, size, column_stack, row_stack, array

from RFFingerprintGenerator.RFFPTools.StatisticsGenerator.Manager.StatisticsGenaerator_Manager import \
    statistics_generator_manager


class FingerPrintGenerator(object):
    def __init__(self):
        self.burst_finger_print = 0
        self.subregion_calculated_characteristic = [0]
        self.label_vector = 0
        self.data_bank = array([])

    def finger_print_generator(self, **kwargs):
        device_label = kwargs["device_label"]
        subregion_calculated_characteristic = kwargs["subregion_calculated_characteristic"]
        subregion_calculated_statistics = self.subRegion_finger_print_generator(subregion_calculated_characteristic)

        # if we cover all characteristics of all subregions of a burst
        all_characteristics_of_current_burst_covered = kwargs["all_characteristics_of_current_burst_covered"]

        # if we cover all bursts of current device
        all_bursts_of_current_device_covered = kwargs["all_bursts_of_current_device_covered"]

        # if we cover all devices
        all_devices_covered = kwargs["all_devices_covered"]

        for stat_key in subregion_calculated_statistics.keys():
            self.burst_finger_print = vstack((self.burst_finger_print, subregion_calculated_statistics[stat_key]))

        if all_characteristics_of_current_burst_covered:
            self.burst_finger_print = self.burst_finger_print[1:]
            self.burst_finger_print = reshape(self.burst_finger_print, size(self.burst_finger_print), 1)
            if size(self.data_bank) == 0:
                self.data_bank = self.burst_finger_print

            else:
                self.data_bank = column_stack((self.data_bank, self.burst_finger_print))

            self.label_vector = column_stack((self.label_vector, device_label))
            self.burst_finger_print = 0

        if all_devices_covered and all_bursts_of_current_device_covered and all_characteristics_of_current_burst_covered:
            self.label_vector = self.label_vector[0, 1:]
            self.data_bank = row_stack((self.data_bank, self.label_vector))

        return array(self.data_bank)

    @staticmethod
    def subRegion_finger_print_generator(subregion_calculated_characteristic):
        subregion_calculated_statistics = dict(statistics_generator_manager(subregion_calculated_characteristic))
        return subregion_calculated_statistics
