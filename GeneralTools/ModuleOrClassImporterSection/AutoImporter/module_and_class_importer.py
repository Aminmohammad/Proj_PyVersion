import inspect
from importlib import import_module

from GeneralTools.ModuleOrClassImporterSection.ModuleAddressExtractor.module_address_extractor import \
    module_address_extractor
from GeneralTools.ModuleOrClassImporterSection.PackageSeriesExtractor.package_series_extractor import \
    package_series_extractor


def module_and_class_importer(project_folder_name, module_name, class_name):
    module_address = module_address_extractor(project_folder_name, module_name)
    package_series = package_series_extractor(module_address, project_folder_name)

    imported_module = import_module(package_series + "." + module_name, ".")

    output = []
    if class_name:
        for name, obj in inspect.getmembers(imported_module):
            if inspect.isclass(obj):
                temp_obj = str(obj).replace('\'>', '')
                temp_obj = temp_obj.replace('<class \'', '')
                starting_index = temp_obj.rfind('.') + 1
                temp_class_name = temp_obj[starting_index:]
                if temp_class_name == class_name:
                    output = obj

    else:
        output = imported_module

    return output

