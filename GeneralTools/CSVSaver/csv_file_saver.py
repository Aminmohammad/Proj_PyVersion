import csv


def csv_file_saver(data, saving_address, file_name):

    file_address = saving_address + "/"+file_name+".csv"
    with open(file_address, 'w') as temp0:
        temp1 = csv.writer(temp0)
        temp1.writerows(data)
