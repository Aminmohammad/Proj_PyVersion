import sys

from GeneralTools.ModuleOrClassImporterSection.ImporterMethodsManager.ImporterMethedsManager import \
    importer_methods_manager


def postProcessor_manager(signal, project_name, selected_methods, data_bank_structure):
    # extraction of modules
    conversions = importer_methods_manager(project_name, selected_methods)

    conversions = dict(conversions)
    for key in sorted(conversions.keys()):

        if conversions[key]:
            current_method_information = conversions[key]

            current_method_module_or_class = current_method_information['module_or_class']
            method_name = current_method_information['method_name']
            special_parameters = current_method_information['special_parameters']

            signal = getattr(current_method_module_or_class, method_name)(signal, special_parameters,
                                                                          data_bank_structure)

    return signal, []
