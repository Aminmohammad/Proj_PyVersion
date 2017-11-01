from numpy.ma import array, transpose, size, mean, amax, amin, shape


def normalizer(data_bank, special_input, data_bank_structure):
    # TODO: do sth with special_input

    # data_bank: dimensions are in 'Rows'

    for row_index in range(size(data_bank, 0) - 1):
        current_dimension = data_bank[row_index, :]
        current_dimension = (current_dimension - mean(current_dimension)) / \
                                                                         (amax(current_dimension) - amin(current_dimension))

        data_bank[row_index, :] = current_dimension

    return data_bank