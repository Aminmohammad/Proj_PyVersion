import csv


def csv_file_loader(loading_address):
    print(loading_address)
    with open(loading_address, "w") as file_obj:

        reader = csv.DictReader(file_obj, delimiter=',')
        print(reader)
        for line in reader:
            print(line["first_name"]),
            print(line["last_name"])

        print(reader)
        print(line)

    return reader