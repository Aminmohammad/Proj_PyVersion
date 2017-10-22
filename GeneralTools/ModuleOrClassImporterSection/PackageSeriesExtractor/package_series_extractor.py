def package_series_extractor(address_of_package_for_module, root_project_folder_name):
    package_series = ""
    if address_of_package_for_module:
        starting_index = str(address_of_package_for_module).find(root_project_folder_name) + len \
            (root_project_folder_name) + 1
        package_series = str.replace(address_of_package_for_module[starting_index:], "\\", ".")

    return package_series
