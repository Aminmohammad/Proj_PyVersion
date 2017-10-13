import csv


def csv_file_saver(**kwarg):

    data = kwarg["data"]
    saving_address = kwarg["saving_address"]
    file_address = saving_address + "/data_bank.csv"
    with open(file_address, 'w') as temp0:
        temp1 = csv.writer(temp0)
        temp1.writerows(data)
