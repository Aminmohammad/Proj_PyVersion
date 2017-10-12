from Tools.StatisticsGenerator.Kurtosis import kurt
from Tools.StatisticsGenerator.Skewness import skewness
from Tools.StatisticsGenerator.Variance import variance

signal_statistics = {}


def statistics_generator_manager(signal):

    # Variance
    signal_variance = variance(signal=signal)

    # # Skewness
    signal_skewness = skewness(signal=signal)
    #
    # # Kurtosis
    signal_kurtosis = kurt(signal=signal)

    # output
    signal_statistics["stat_0"] = signal_variance
    signal_statistics["stat_1"] = signal_skewness
    signal_statistics["stat_2"] = signal_kurtosis

    return signal_statistics
