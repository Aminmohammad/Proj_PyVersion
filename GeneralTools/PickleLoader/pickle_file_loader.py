import pickle


def pickle_file_loader(file_address):
    with open(file_address, "rb") as myFile:
        loaded_file = pickle.load(myFile)

    return loaded_file
