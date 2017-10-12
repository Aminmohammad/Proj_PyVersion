from numpy import vstack, size, reshape, column_stack

from Tools.StatisticsGenerator.StatisticsGenaerator_Manager import statistics_generator_manager
from Tools.generated_data_set_decomposer import generated_data_set_reader


def finger_print_production_manager(**kwargs):
    data_bank = generated_data_set_reader(extracted_data_set=kwargs["extracted_data_set"])

    return data_bank
