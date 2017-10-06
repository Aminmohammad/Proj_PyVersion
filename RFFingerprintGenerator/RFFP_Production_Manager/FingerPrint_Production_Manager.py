from numpy import var, array
from scipy.stats import skew, kurtosis


def finger_print_production_manager(**kwargs):
    extracted_data_set = kwargs["extracted_data_set"]

    data_bank = []
    for device_data_set in extracted_data_set:
        bursts_of_a_single_device = device_data_set["a_Single_Device"]

        burst_finger_print = []
        for burst in bursts_of_a_single_device:
            for subregion_index in range(len(burst)):
                current_subregion = burst[subregion_index]

                # Characteristics of the single sub-Region
                amp_single_subregion = current_subregion["amp_single_subRegion"]
                phase_single_subregion = current_subregion["amp_single_subRegion"]
                ifreq_single_subregion = current_subregion["amp_single_subRegion"]

                # Variance
                amp_variance = var(amp_single_subregion)
                phase_variance = skew(phase_single_subregion)
                ifreq_variance = skew(ifreq_single_subregion)

                # Skewness
                amp_skewness = skew(amp_single_subregion)
                phase_skewness = skew(phase_single_subregion)
                ifreq_skewness = skew(ifreq_single_subregion)

                # Kurtosis
                amp_kurtosis = kurtosis(amp_single_subregion)
                phase_kurtosis = skew(phase_single_subregion)
                ifreq_kurtosis = skew(ifreq_single_subregion)

                burst_finger_print = burst_finger_print.append(array(
                    [amp_variance, phase_variance, ifreq_variance, amp_skewness, phase_skewness, ifreq_skewness,
                     amp_kurtosis, phase_kurtosis, ifreq_kurtosis]))

        data_bank = data_bank.append(burst_finger_print)

    return data_bank
