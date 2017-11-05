import csv


def csv_file_saver(data, saving_address, file_name, special_input):
    file_address = saving_address + "/" + file_name + ".csv"

    # TODO: Do sth with 'special_input=collected_labels'

    if special_input:
        header_dictionary = dict(special_input["collected_labels"])
        column_headers_list = header_dictionary.values()

    with open(file_address, 'w') as temp0:
        temp1 = csv.writer(temp0)

        if special_input and special_input["add_labels_to_saved_data_bank"]:
            temp1.writerow(column_headers_list)

        temp1.writerows(data)
