from  pywt import dwt


def dwt_calculator(signal, special_parameters):
    # TODO: this 'special_parameters' maybe be useful
    approximation_coefficients, detail_coefficients = dwt(signal, 'haar')
    return detail_coefficients
