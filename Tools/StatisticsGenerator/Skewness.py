from scipy.stats import skew


def skewness(**kwarg):
    signal = kwarg["signal"]
    statistic = skew(signal)
    return statistic
