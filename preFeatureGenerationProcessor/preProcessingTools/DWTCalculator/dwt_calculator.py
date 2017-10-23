from  pywt import dwt


def dwt_calculator(signal, special_parameters):
    approximation_coefficients, detail_coefficients = dwt(signal, 'haar')
    if special_parameters["important_element"] == "details":
        converted_signal = detail_coefficients

    elif special_parameters["important_element"] == "approximations":
        converted_signal = approximation_coefficients

    return converted_signal
