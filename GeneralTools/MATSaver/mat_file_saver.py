import scipy


def mat_file_saver(data, saving_address, file_name):
    file_address = saving_address + "/"+file_name+".mat"
    scipy.io.savemat(file_address, mdict={file_name: data})
