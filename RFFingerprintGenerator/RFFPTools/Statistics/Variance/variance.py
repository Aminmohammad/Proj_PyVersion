from numpy.ma import power, mean, size


def variance(signal, special_parameters):
    # TODO: this 'special_parameters' maybe be useful
    signal = signal - mean(signal)
    squared_signal = power(signal, 2)
    summation = sum(squared_signal)
    statistic = (1 / size(signal)) * summation

    return statistic
