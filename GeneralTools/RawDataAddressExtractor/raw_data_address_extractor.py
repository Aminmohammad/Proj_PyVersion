import os
from tkinter import Tk, filedialog


def raw_data_folder_address_extractor(root_folder_address, selected_data_set_name):
    if not selected_data_set_name:
        root = Tk()
        root.withdraw()  # use to hide tkinter window

        parent_folder_address = filedialog.askdirectory(parent=root, initialdir=root_folder_address,
                                                        title='Please select a Recorded Data Collection')

    else:
        parent_folder_address = root_folder_address + "\\Resources\\" + selected_data_set_name

    data_set_address = parent_folder_address + "\\RawData"
    data_set_address = data_set_address.replace("\\", "/")

    if not os.path.exists(data_set_address):
        raise ValueError('There is no folder named RawData in: %s' % parent_folder_address)

    return data_set_address
