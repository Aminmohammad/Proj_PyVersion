import pickle


def pickle_file_saver(data, data_saving_address, file_name, special_input):
    file_address = data_saving_address + "/" + file_name + ".txt"
    with open(file_address, "wb") as myFile:
        pickle.dump(data, myFile)
