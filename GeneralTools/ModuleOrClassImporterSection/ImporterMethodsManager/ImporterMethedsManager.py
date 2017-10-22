from GeneralTools.ModuleOrClassImporterSection.AutoImporter.module_and_class_importer import module_and_class_importer


def importer_methods_manager(project_name, methods):
    module_or_class_handle_dictionary = {}
    for key in sorted(methods.keys()):

        if methods[key]:
            current_function_information = methods[key]

            module_name = current_function_information["module_name"]
            class_name = current_function_information["class_name"]

            module_or_class_handle = module_and_class_importer(project_name, module_name, class_name)
            module_or_class_handle_dictionary[key] = {'module_or_class': module_or_class_handle,
                                                      'method_name': current_function_information["method_name"],
                                                      "special_parameters":
                                                          current_function_information["special_parameters"],
                                                      }

    return module_or_class_handle_dictionary
