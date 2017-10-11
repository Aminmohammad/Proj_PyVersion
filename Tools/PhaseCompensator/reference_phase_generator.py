import math

from numpy.ma import arange, reshape, zeros, hstack, angle
from numpy.matlib import repmat, unwrap


def reference_phase_generator(**kwarg):
    sampling_frequency = kwarg["sampling_frequency"]
    communication_frequency = kwarg["communication_frequency"]

    sampling_time = 1 / sampling_frequency
    communication_time = 1 / communication_frequency

    ratio = communication_time / sampling_time
    preamble = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]

    inPhase_elements = preamble[::2]
    quadrature_elements = preamble[1::2]

    inPhase_elements = inPhase_elements * 2 - 1
    quadrature_elements = quadrature_elements * 2 - 1

    # creation of pulse shaping in sin
    k = arange(0, 2 * communication_time - sampling_time, communication_time)
    pulse_shape = math.sin((math.pi * k) / (2 * communication_time))
    pulse_shape = repmat(pulse_shape, 16, 1)

    # Oversample of I & Q and blocker order 0
    Iup = repmat(inPhase_elements, 2 * ratio, 1)
    Qup = repmat(quadrature_elements, 2 * ratio, 1)

    # signal pulse shaping
    Iup = Iup * pulse_shape
    Qup = Iup * pulse_shape

    # wave shaping
    Iup = reshape(Iup, 1, 16 * 2 * ratio)
    Iup = reshape(Qup, 1, 16 * 2 * ratio)

    # repeat the matrix for 8 symbols
    I8up = repmat(Iup, 1, 8)
    Q8up = repmat(Qup, 1, 8)

    # application of 90 degrees offset on Q for reference only
    Iup = hstack((Iup, zeros(1, 10)))
    Qup = hstack((zeros(1, 10), Qup))

    # construction of a phase cycle
    signal = Iup + 1j * Qup
    phase_cycle = unwrap(angle(signal))

    phase_cycle[1:10] = []
    phase_cycle[320:330] = []

    # applying the 90 degrees offset on Q
    I8up = hstack((I8up, zeros(1, 10)))
    Q8up = hstack((zeros(1, 10), Q8up))

    # complex signal shaping
    signal = I8up + 1j * Q8up

    # creation of the theoretical phase
    phase_ref = unwrap(angle(signal))
    phase_ref[1:10] = []

    return phase_ref
