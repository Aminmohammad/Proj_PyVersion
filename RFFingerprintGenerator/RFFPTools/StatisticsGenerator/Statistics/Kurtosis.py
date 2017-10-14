from scipy.stats import kurtosis


def kurt(**kwarg):
    signal = kwarg["signal"]
    statistic = kurtosis(signal)
    return statistic
