import os

from GeneralTools.RootProjectFolderAddressExtractor.root_project_folder_address_extractor import \
    root_project_folder_address_extractor


def module_address_extractor(project_folder_name, module_name):

    # output
    address_of_package_for_module = []

    # add file extension, if not exist
    if not ('.' in module_name):
        module_name = module_name + '.py'

    # Extract the address of 'Root Folder Address'
    root_folder_address = root_project_folder_address_extractor(target_folder_name=project_folder_name) # TODO: Make this roo name , automatic

    # extract the contents all folders and sub-folders in 'Root Folder Address'
    contents_of_root_project_folder = [contents[0] for contents in os.walk(root_folder_address)]

    # extract the contents all folders and sub-folders in 'Root Folder Address'
    for folder_pass in contents_of_root_project_folder:

        if folder_pass and (any(module_name in temp for temp in os.listdir(folder_pass))):
            address_of_package_for_module = folder_pass

    return address_of_package_for_module

