from numpy import angle, unwrap, arange, polyfit, exp, size

from pre_FeatureGeneration_Processor.preProcTools.PhaseCompensator.Reference_Pahse.reference_phase_generator import \
    reference_phase_generator


def phase_compensator(**kwargs):

    reference_phase = reference_phase_generator(sampling_frequency=kwargs["sampling_frequency"],
                                                communication_frequency=kwargs["communication_frequency"])
    signal_phase = unwrap(angle(kwargs["signal"]))
    signal_index = unwrap(angle(kwargs["subregion_index"]))

    if size(signal_index) < size(signal_phase):
        starting_index = signal_index * size (signal_phase)
        ending_index = ( signal_index + 1 ) * size (signal_phase) - 1
        error = reference_phase (starting_index-ending_index)- signal_phase

    else:
        error = reference_phase - signal_phase

    polynomial = polyfit(arange(len(error)), error, 1)

    compensation = polynomial[0] * arange(len(kwargs["preamble"])) + polynomial[1]

    compensated_signal = kwargs["signal"] * exp(1j * compensation)

    return compensated_signal
