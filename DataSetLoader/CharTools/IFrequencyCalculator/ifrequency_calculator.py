from numpy.ma import angle, array, diff


def ifreq(a_single_subRegion, special_parameters):
    # TODO: this 'special_parameters' maybe be useful

    phase = array(angle(a_single_subRegion))
    ifreq = array(diff(phase))

    return ifreq


