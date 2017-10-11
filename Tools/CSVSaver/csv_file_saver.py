import csv


def csv_file_saver(**kwarg):

    data = kwarg["data"]
    saving_address = kwarg["saving_address"]

    temp0 = open(saving_address + "/data_bank.csv", 'w')
    temp1 = csv.writer(temp0)
    # data = [np.array([1, 2, 3]), np.array([3., 4., 5., 6., 7.]), np.array([7, 8])]
    temp1.writerows(data)
    temp0.close()
