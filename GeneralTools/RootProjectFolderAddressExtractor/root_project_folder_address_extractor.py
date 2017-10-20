import os


def root_project_folder_address_extractor(**kwarg):
    target_folder_name = kwarg["target_folder_name"]
    current_folder_address = os.getcwd()
    starting_index = current_folder_address.find(target_folder_name)
    target_folder_address = current_folder_address[0:starting_index+len(target_folder_name)+1]
    return target_folder_address
