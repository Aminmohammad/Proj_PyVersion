from numpy import angle, unwrap, arange, polyfit, exp

from Tools.PhaseCompensator.reference_phase_generator import reference_phase_generator


def phase_compensator(preamble, sampling_frequency):

    reference_phase = reference_phase_generator(sampling_frequency)
    preamble_phase = unwrap(angle(preamble))
    error = reference_phase - preamble_phase

    polynomial = polyfit(arange(len(error)), error, 1)

    compensation = polynomial[0] * arange(len(polynomial))+polynomial[1]

    compensated_signal = preamble * exp(1j*compensation)

    return compensated_signal

