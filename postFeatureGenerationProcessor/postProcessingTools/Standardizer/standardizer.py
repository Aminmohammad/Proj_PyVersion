from numpy.ma import array, transpose, size, mean, amax, amin


def standardizer(data_bank, special_input, data_bank_structure):
    # TODO: do sth with special_input
    if data_bank_structure == "columns":
        data_bank = transpose(array(data_bank))

    for row_index in range(size(data_bank, 0)):
        current_dimension = data_bank[row_index, :]
        current_dimension = (current_dimension - mean(current_dimension)) / \
                                                                         (amax(current_dimension) - amin(current_dimension))

        data_bank [row_index, :] = current_dimension

    if data_bank_structure == "columns":
        data_bank = transpose(array(data_bank))

    return data_bank