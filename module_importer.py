from importlib import import_module

from GeneralTools.ModuleAddressExtractor.module_address_extractor import module_address_extractor
from GeneralTools.PackageSeriesExtractor.package_series_extractor import package_series_extractor


def module_importer(project_folder_name, module_name, method_name):
    module_address = module_address_extractor(project_folder_name, module_name)
    package_series = package_series_extractor(module_address, project_folder_name)

    imported_module = import_module(package_series, ".")
    print(imported_module)

    print(method_name)
    # method = getattr('preFeatureGenerationProcessor.preProcessingTools.dwt_calculator', method_name)
    getattr(imported_module, method_name)([1, 2, 3, 4, 5, 6, 7, 8, 9])
    #a = method([1, 2, 3, 4, 5, 6, 7, 8, 9])
    #print (a)

    print("error Found")


module_importer("PythonVersion", "dwt_calculator", "dwt_calculator")