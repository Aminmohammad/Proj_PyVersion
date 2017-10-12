from Tools.DataSetDecomposer.generated_data_set_decomposer import generated_data_set_decomposer


class preProc_manager:
    def __init__(self, **input_set):
        self.input_data_set = input_set["selected_"]
        self.selected_method = input_set["selected_"]

    def data_set_reader(self):
        input_data_set = self.input_data_set
        self.input_data_set = generated_data_set_decomposer(input_data_set)

    def pre_processor_caller(self):
        self.selected_method(self.input_data_set)
