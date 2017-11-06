def time_calculator (time_in_second):
    if time_in_second < 60:
        label = "S."

    elif (time_in_second > 60) and (time_in_second < 3600):
        time_in_second = time_in_second / 60
        label = "M."

    elif time_in_second > 3600:
        time_in_second = time_in_second / 3600
        label = "H."

    return time_in_second, label


