from  pywt import dwt


def dwt_calculator (signal):
    approximation_coefficients, detail_coefficients = dwt(signal, 'haar')
    return detail_coefficients
