from Tools.generated_data_set_reader import generated_data_set_reader


class preProc_Manager:
    def __init__(self, **input_set):
        self.input_data_set = input_set ["selected_"]
        self.selected_method = input_set ["selected_"]

    def data_set_reader (self):
        input_data_set = self.input_data_set
        self.input_data_set = generated_data_set_reader (input_data_set)

    def pre_processor_Caller (self):
        self.selected_method (self.input_data_set)
