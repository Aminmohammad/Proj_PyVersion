from numpy import angle, unwrap, arange, polyfit, exp

from Tools.PhaseCompensator.reference_phase_generator import reference_phase_generator


def phase_compensator(**kwarg):

    reference_phase = reference_phase_generator(sampling_frequency=kwarg["sampling_frequency"],
                                                communication_frequency=kwarg["communication_frequency"])
    preamble_phase = unwrap(angle(kwarg["preamble"]))
    error = reference_phase - preamble_phase
    polynomial = polyfit(arange(len(error)), error, 1)

    compensation = polynomial[0] * arange(len(kwarg["preamble"]))+polynomial[1]

    compensated_signal = kwarg["preamble"] * exp(1j*compensation)

    return compensated_signal
