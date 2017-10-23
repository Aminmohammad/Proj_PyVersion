from scipy.stats import kurtosis


def kurt(signal, special_parameters):
    # TODO: this 'special_parameters' maybe be useful
    statistic = kurtosis(signal)

    return statistic
