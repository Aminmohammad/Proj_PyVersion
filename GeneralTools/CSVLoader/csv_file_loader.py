import csv


def csv_file_loader(data, saving_address, file_name):

    file_address = saving_address + "/"+file_name+".csv"
    with open(file_address, 'w') as temp0:
        with open('eggs.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

            # TODO: This code is wrong. Correct it. Because how can we save and load 'extracted_dataset' as csv file