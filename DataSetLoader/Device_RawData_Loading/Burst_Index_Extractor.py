from numpy import *
from scipy.sparse import csc_matrix


def Burst_Index_Extractor(record, threshold):
    # conversion of sparse to Dense
    record = csc_matrix(record, dtype=float)
    record = record.todense()

    record = abs(record)
    record = vstack([[0], record, [0]])
    indices = argwhere(record <= threshold)

    record[indices] = 0
    indices_of_nonzero_elements = argwhere(record != 0)
    indices_of_nonzero_elements = indices_of_nonzero_elements.transpose()
    index_vector = array(range(len(indices_of_nonzero_elements.transpose()) - 1)) + 1
    hashmap_bursts_indices_matrix = {}

    hashmap_bursts_indices_matrix_index = 0
    previous_index = 0
    for index in index_vector:
        if (indices_of_nonzero_elements[0][index] - indices_of_nonzero_elements[0][index - 1]) > 100:
            hashmap_bursts_indices_matrix[str(hashmap_bursts_indices_matrix_index)] = [
                indices_of_nonzero_elements[0][previous_index], indices_of_nonzero_elements[0][index - 1]]
            previous_index = index
            hashmap_bursts_indices_matrix_index += 1

    hashmap_bursts_indices_matrix[str(hashmap_bursts_indices_matrix_index)] = [indices_of_nonzero_elements[0]
                                                            [previous_index], indices_of_nonzero_elements[0][index]]

    return hashmap_bursts_indices_matrix

