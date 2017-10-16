from scipy.stats import skew


def skewness(signal, **kwarg):
    signal = signal
    statistic = skew(signal)
    return statistic
