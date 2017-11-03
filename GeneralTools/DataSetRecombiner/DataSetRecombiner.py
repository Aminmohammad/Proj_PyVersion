import sys
from numpy.ma import vstack, reshape, size, column_stack, row_stack, array, shape, ndim

from RFFingerprintGenerator.RFFPTools.Manager.finger_print_producer import finger_print_producer
from preFeatureGenerationProcessor.preProcessingTools.Manager.conversion_manager import conversion_manager


class DataSetRecombiner(object):
    def __init__(self):
        # general inputs
        self.single_characteristic = []

        # pre-process inputs
        self.device_key = []
        self.burst_key = []
        self.characteristic_key = []
        self.selected_methods = []

        # finger-print inputs
        self.label_vector = 0
        self.device_label = 0
        self.output_label_index = 0

        # general outputs
        self.converted_characteristic = []
        self.collected_burst = 0
        self.data_collection = array([])
        self.output_labels = {}
        self.collected_labels = []

        # pre-process outputs
        self.device_collection = {}

        # finger-print outputs
        self.subregion_calculated_statistics = []

    def data_set_recombiner(self, **kwargs):
        self.device_label = kwargs["device_label"]
        self.single_characteristic = kwargs["subregion_calculated_characteristic"]

        # Extraction of the name of "manager" which calls this function
        name_of_caller_manager = ("%s" % kwargs["name_of_caller_manager"])
        name_of_caller_manager = name_of_caller_manager.replace("manager", "")

        # characteristic converter function name
        characteristic_converter_function_name = ("%s%s" % (name_of_caller_manager, "characteristic_converter"))
        characteristic_converter_function = getattr(DataSetRecombiner, characteristic_converter_function_name)

        # converted characteristic collector function name
        converted_characteristic_collector_function_name = ("%s%s" % (name_of_caller_manager,
                                                                      "characteristic_collector"))
        converted_characteristic_collector_function = getattr(DataSetRecombiner,
                                                              converted_characteristic_collector_function_name)

        # burst collector function name
        burst_collector_function_name = ("%s%s" % (name_of_caller_manager, "burst_collector"))
        burst_collector_function = getattr(DataSetRecombiner, burst_collector_function_name)

        # device collector function name
        device_collector_function_name = ("%s%s" % (name_of_caller_manager, "device_collector"))
        device_collector_function = getattr(DataSetRecombiner, device_collector_function_name)

        # output collector function name
        output_collector_function_name = ("%s%s" % (name_of_caller_manager, "output_collector"))
        output_collector_function = getattr(DataSetRecombiner, output_collector_function_name)

        # if we cover all characteristics of all subregions of a burst
        all_characteristics_of_current_burst_covered = kwargs["all_characteristics_of_current_burst_covered"]

        # if we cover all bursts of current device
        all_bursts_of_current_device_covered = kwargs["all_bursts_of_current_device_covered"]

        # if we cover all devices
        all_devices_covered = kwargs["all_devices_covered"]

        # if we cover all devices
        self.selected_methods = kwargs["selected_methods"]

        # device_key
        self.device_key = kwargs["device_key"]

        # burst_key
        self.burst_key = kwargs["burst_key"]

        # key characteristic
        self.characteristic_key = ("%s" % kwargs["characteristic_key"])

        # convert characteristic
        self.converted_characteristic, self.output_labels = characteristic_converter_function(self)

        # collect converted characteristic in burst
        self.collected_burst, self.collected_labels = converted_characteristic_collector_function(self)

        if all_characteristics_of_current_burst_covered:
            burst_collector_function(self)

        if all_characteristics_of_current_burst_covered:
            device_collector_function(self)
            self.output_label_index = 0

        if all_devices_covered and all_bursts_of_current_device_covered and \
                all_characteristics_of_current_burst_covered:
            output_collector_function(self)

        return self.data_collection, self.collected_labels

    # preProcessing Functions
    def preProcessor_characteristic_converter(self):
        converted_characteristic = conversion_manager(self.single_characteristic, self.selected_methods)

        output_labels = ""
        return converted_characteristic, output_labels

    def preProcessor_characteristic_collector(self):
        if self.collected_burst == 0:
            self.collected_burst = {}

        collected_characteristics_dict = self.collected_burst
        collected_characteristics_dict[self.characteristic_key] = self.converted_characteristic
        collected_labels = ""
        return collected_characteristics_dict, collected_labels

    def preProcessor_burst_collector(self):
        self.device_collection[self.burst_key] = self.collected_burst
        self.collected_burst = 0

    def preProcessor_device_collector(self):
        if size(self.data_collection) == 0:
            self.data_collection = {}

        self.data_collection[self.device_key] = self.device_collection

    def preProcessor_output_collector(self):
        self.data_collection = dict(self.data_collection)

    # FingerPrinting Functions
    def finger_print_characteristic_converter(self):
        characteristic_statistics, output_labels = finger_print_producer(self.single_characteristic,
                                                                         self.selected_methods,
                                                                         self.characteristic_key)
        characteristic_statistics = dict(characteristic_statistics)
        output_labels = dict(output_labels)

        return characteristic_statistics, output_labels

    #
    def finger_print_characteristic_collector(self):
        collected_characteristics_vector = self.collected_burst
        collected_labels = self.collected_labels

        for key in self.converted_characteristic.keys():

            self.converted_characteristic[key] = array(self.converted_characteristic[key])
            if size(self.converted_characteristic[key]) > 1:
                self.converted_characteristic[key] = reshape(self.converted_characteristic[key],
                                                             [size(self.converted_characteristic[key], 0), 1])

            collected_characteristics_vector = row_stack(
                (collected_characteristics_vector, self.converted_characteristic[key]))

            if size(collected_labels) == 0:
                collected_labels = {self.output_label_index: self.output_labels[key]}
                self.output_label_index += 1

            else:
                collected_labels[self.output_label_index] = self.output_labels[key]
                self.output_label_index += 1

        return collected_characteristics_vector, collected_labels

    def finger_print_burst_collector(self):
        # saving the whole burst in the data-bank
        self.collected_burst = self.collected_burst[1:]
        self.collected_burst = reshape(self.collected_burst, [size(self.collected_burst, 0), 1])
        if size(self.data_collection) == 0:
            self.data_collection = self.collected_burst
        else:
            self.data_collection = column_stack((self.data_collection, self.collected_burst))

        self.label_vector = column_stack((self.label_vector, self.device_label))
        self.collected_burst = 0

    def finger_print_device_collector(self):
        pass

    def finger_print_output_collector(self):
        self.label_vector = self.label_vector[0, 1:]

        self.data_collection = row_stack((self.data_collection, self.label_vector))

        return self.data_collection

    # postProcessing Functions
    def postProcessor_characteristic_converter(self):
        characteristic_statistics = dict(self.single_characteristic)
        return characteristic_statistics

    def postProcessor_characteristic_collector(self):
        collected_characteristics_vector = self.collected_burst
        for key in self.converted_characteristic.keys():
            collected_characteristics_vector = vstack(
                (collected_characteristics_vector, self.converted_characteristic[key]))

        return collected_characteristics_vector

    def postProcessor_burst_collector(self):
        # saving the whole burst in the data-bank
        self.collected_burst = self.collected_burst[1:]
        self.collected_burst = reshape(self.collected_burst, size(self.collected_burst), 1)
        if size(self.data_collection) == 0:
            self.data_collection = self.collected_burst
        else:
            self.data_collection = column_stack((self.data_collection, self.collected_burst))

        self.label_vector = column_stack((self.label_vector, self.device_label))
        self.collected_burst = 0

    def postProcessor_device_collector(self):
        pass

    def postProcessor_output_collector(self):
        self.label_vector = self.label_vector[0, 1:]
        self.data_collection = row_stack((self.data_collection, self.label_vector))
        self.data_collection = array(self.data_collection)

        return self.data_collection
