from scipy.stats import skew


def skewness(signal, special_parameters):
    # TODO: this 'special_parameters' maybe be useful
    statistic = skew(signal)

    added_label = "skew"

    return statistic, added_label
