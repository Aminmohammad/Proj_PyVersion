# from numpy.ma import vstack, reshape, size, column_stack, row_stack, array
#
# from RFFingerprintGenerator.RFFPTools.StatisticsGenerator.Manager.StatisticsGenaerator_Manager import \
#     statistics_generator_manager
#
#
# class preProcessor(object):
#     def __init__(self):
#         self.burst_finger_print = 0
#         self.subregion_calculated_characteristic = [0]
#         self.label_vector = 0
#         self.data_bank = array([])
#         self.device_label = 0
#
#     def finger_print_generator(self, **kwargs):
#         self.device_label = kwargs["device_label"]
#         self.subregion_calculated_characteristic = kwargs["subregion_calculated_characteristic"]
#
#         # Extraction of the name of "manager" which calls this function
#         name_of_caller_manager = ("%s" % kwargs["name_of_caller_manager"])
#         name_of_caller_manager = name_of_caller_manager.replace("manager", "")
#
#         # subRegion signal Generator function name
#         subRegions_signal_generator_function_name = ("%s%s" % name_of_caller_manager, "_subRegion_signal_generator")
#
#         # if we cover all characteristics of all subregions of a burst
#         all_characteristics_of_current_burst_covered = kwargs["all_characteristics_of_current_burst_covered"]
#
#         # if we cover all bursts of current device
#         all_bursts_of_current_device_covered = kwargs["all_bursts_of_current_device_covered"]
#
#         # if we cover all devices
#         all_devices_covered = kwargs["all_devices_covered"]
#
#         # burst collector function name
#         burst_collector_function_name = ("%s%s" % name_of_caller_manager, "_burst_collector")
#
#         # output collector function name
#         output_collector_function_name = ("%s%s" % name_of_caller_manager, "_burst_collector")
#
#         # generate new subregion
#         self.subRegion_generated_output = subRegions_signal_generator_function_name(self.subregion_calculated_characteristic)
#
#
#         # TODO: Make these functions selectable
#         return array(self.output)
#
#     @staticmethod
#     def FingerPrint_subRegion_signal_generator(self):
#         self.subregion_calculated_statistics = dict(statistics_generator_manager(self.subregion_calculated_characteristic))
#     def preProcessor_subRegion_signal_generator(self):
#         pass
#
#     def FingerPrint_burst_collector(self, generated_output):
#         # Saving the result of conversion of each "subRegion"
#         for key in generated_output.keys():
#             self.burst_finger_print = vstack((self.burst_finger_print, generated_output[key]))
#
#     def preProcessor_burst_collector(self):
#
#         pass
#     def FingerPrint_burst_collector(self):
#         # Saving the result of conversion of each "subRegion"
#         if self.all_characteristics_of_current_burst_covered:
#             self.burst_finger_print = self.burst_finger_print[1:]
#             self.burst_finger_print = reshape(self.burst_finger_print, size(self.burst_finger_print), 1)
#             if size(self.data_bank) == 0:
#                 self.data_bank = self.burst_finger_print
#             else:
#                 self.data_bank = column_stack((self.data_bank, self.burst_finger_print))
#
#             self.label_vector = column_stack((self.label_vector, self.device_label))
#             self.burst_finger_print = 0
#
#     def preProcessor_output_collector(self):
#     def FingerPrint_output_collector(self):
#         if self.all_devices_covered and self.all_bursts_of_current_device_covered and self.all_characteristics_of_current_burst_covered:
#         self.label_vector = self.label_vector[0, 1:]
#         self.data_bank = row_stack((self.data_bank, self.label_vector))
#
#
#
#
#
