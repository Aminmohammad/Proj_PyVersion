import csv

import scipy


def mat_file_loader(data, saving_address, file_name):
    file_address = saving_address + "/"+file_name+".mat"
    scipy.io.savemat(file_address, mdict={file_name: data})

    # TODO: This code is wrong. Correct it. Because how can we save and load 'extracted_dataset' as mat file