from numpy import angle, unwrap, arange, polyfit, exp, size

from preFeatureGenerationProcessor.preProcessingTools.phase_compensator.reference_phase_generator import \
    reference_phase_generator


def phase_compensator(**kwargs):
    reference_phase = reference_phase_generator(sampling_frequency=kwargs["sampling_frequency"],
                                                communication_frequency=kwargs["communication_frequency"])
    signal_phase = unwrap(angle(kwargs["preamble"]))

    error = reference_phase - signal_phase

    polynomial = polyfit(arange(len(error)), error, 1)

    compensation = polynomial[0] * arange(len(kwargs["preamble"])) + polynomial[1]

    compensated_signal = kwargs["preamble"] * exp(1j * compensation)

    return compensated_signal
