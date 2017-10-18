from pre_FeatureGeneration_Processor.preProcessingTools.dwt_calculator.dwt_calculator import dwt_calculator
from pre_FeatureGeneration_Processor.preProcessingTools.phase_compensator.phase_compensator import phase_compensator

signal_statistics = {}


# def module_adder(conversion_method):
#     root_folder_address = folder_address_extractor(target_folder_name="PythonVersion")
#     preProcessor_folder_address = root_folder_address + "pre_FeatureGeneration_Processor" + "\\preProcessingTools\\"
#     os.chdir(preProcessor_folder_address)
#     print(os.getcwd())
#     module_address = preProcessor_folder_address + conversion_method + "." + conversion_method
#     test = conversion_method + "." + conversion_method
#     print(test)
#     imported_module = import_module(test, ".")
#
#     return imported_module


def conversion_manager(signal, conversions):
    # all conversions
    for conversion_method in conversions:
        if conversion_method == "dwt_calculator":
            signal = dwt_calculator(signal)

    return signal
