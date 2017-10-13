from GeneralTools.DataSetDecomposer.generated_data_set_decomposer import generated_data_set_decomposer


def preProc_manager(**kwargs):
    data_bank = generated_data_set_decomposer(extracted_data_set=kwargs["extracted_data_set"])

    return data_bank
