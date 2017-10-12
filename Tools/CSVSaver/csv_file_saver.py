import csv


def csv_file_saver(**kwarg):

    data = kwarg["data"]
    saving_address = kwarg["saving_address"]
    file_address = saving_address + "/data_bank.csv"

    try:
        temp0 = open(file_address, 'w')

    except IOError:
        # Todo: Complete this section
        file_address.close()
        temp0 = open(file_address, 'w')

    temp1 = csv.writer(temp0)
    temp1.writerows(data)
    temp0.close()
