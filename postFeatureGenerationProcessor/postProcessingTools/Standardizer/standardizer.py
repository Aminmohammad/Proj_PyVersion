from numpy.ma import array, transpose, size


def standardizer (data_bank, special_input):

    if (special_input["dimension_are_in_rows_or_columns"] == "columns" ):
        data_bank = transpose(array(data_bank))

    for row_index in range(size(data_bank, 0)):
        curernt_dimension = data_bank