import statistics


def compute_statistics(values):
    """
    computes the min, max, arithmetic mean, harmonic mean, median and mode
    of an iterable set of values
    :param values: the iterable set of values to compute the statistics of.
    :return: returns a list with [min, a_mean, h_mean, median, mode, max] values
    """

    min_dm_per_sentence = min(values)
    max_dm_per_sentence = max(values)
    arith_mean_dm_per_sentence = statistics.mean(values)
    harmonic_mean_dem_per_sentence = statistics.harmonic_mean(values)
    median_dm_per_sentence = statistics.median(values)
    mode_dm_per_sentence = statistics.mode(values)

    return [min_dm_per_sentence,
            arith_mean_dm_per_sentence, harmonic_mean_dem_per_sentence,
            median_dm_per_sentence, mode_dm_per_sentence,
            max_dm_per_sentence]


def percentage(part, whole):
    return (float(part) * 100) / (float(whole))


def show_dataframe(data1, data2, data3, data4):
    """
    Prints a pandas dataframe
    :param data1:
    :param data2:
    :param data3:
    :param data4:
    :return:
    """
    pass


def list_all_markers(data1, data2=None, data3=None, data4=None):
    markers = data1.get_markers()

    if data2 is not None:
        for marker in data2.get_markers():
            if marker not in markers:
                markers.append(marker)

    if data3 is not None:
        for marker in data3.get_markers():
            if marker not in markers:
                markers.append(marker)

    if data4 is not None:
        for marker in data4.get_markers():
            if marker not in markers:
                markers.append(marker)

    return markers


def