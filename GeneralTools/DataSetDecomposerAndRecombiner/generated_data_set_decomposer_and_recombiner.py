from numpy import size, array

from GeneralTools.DataSetRecombiner.DataSetRecombiner import DataSetRecombiner
from GeneralTools.ModuleOrClassImporterSection.ImporterMethodsManager.ImporterMethedsManager import \
    importer_methods_manager

reference = DataSetRecombiner()


def generated_data_set_decomposer_and_recombiner(extracted_data_set, name_of_caller_manager, selected_methods,
                                                 project_name):
    # extraction of modules
    selected_methods = importer_methods_manager(project_name, selected_methods)

    # running the codes
    device_key_list = array(list(extracted_data_set.keys()))
    device_label = 0
    all_devices_covered = False
    for device_data_set_key in extracted_data_set.keys():
        bursts_of_a_single_device = dict(extracted_data_set[device_data_set_key])
        device_label += 1

        if device_label == size(device_key_list):
            all_devices_covered = True

        bursts_key_list = array(list(bursts_of_a_single_device.keys()))
        number_of_bursts_covered_for_current_device = 0
        all_bursts_of_current_device_covered = False

        for burst_key in bursts_of_a_single_device.keys():
            burst = bursts_of_a_single_device[burst_key]

            number_of_bursts_covered_for_current_device += 1
            if number_of_bursts_covered_for_current_device == size(bursts_key_list):
                all_bursts_of_current_device_covered = True

            characteristics_key_list = array(list(burst.keys()))
            number_of_characteristics_covered_for_current_burst = 0
            all_characteristics_of_current_burst_covered = False
            for characteristic_key in burst.keys():  # since we have 3 chars for each subRegion
                number_of_characteristics_covered_for_current_burst += 1
                if number_of_characteristics_covered_for_current_burst == size(characteristics_key_list):
                    all_characteristics_of_current_burst_covered = True

                output = reference.data_set_recombiner(device_label=device_label,
                                                       subregion_calculated_characteristic=
                                                       burst[characteristic_key],
                                                       all_characteristics_of_current_burst_covered=
                                                       all_characteristics_of_current_burst_covered,
                                                       all_devices_covered=all_devices_covered,
                                                       all_bursts_of_current_device_covered=
                                                       all_bursts_of_current_device_covered,
                                                       name_of_caller_manager=name_of_caller_manager,
                                                       device_key=device_data_set_key,
                                                       burst_key=burst_key,
                                                       characteristic_key=characteristic_key,
                                                       selected_methods=selected_methods)
    reference.__init__()
    return output
