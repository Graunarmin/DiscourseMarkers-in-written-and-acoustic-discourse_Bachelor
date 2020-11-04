import statistics
import math
import pandas as pd
from scipy import stats


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
    # harmonic_mean_dem_per_sentence = statistics.harmonic_mean(values)
    # median_dm_per_sentence = statistics.median(values)
    mode_dm_per_sentence = statistics.mode(values)

    return [min_dm_per_sentence,
            arith_mean_dm_per_sentence,
            # harmonic_mean_dem_per_sentence,
            # median_dm_per_sentence,
            mode_dm_per_sentence,
            max_dm_per_sentence]


def percentage(part, whole):
    return (float(part) * 100) / (float(whole))


def add_value_to_dataframe(names, frame_dict, columns, label, data):
    names.append(label)
    for column, value in zip(columns, data):
        frame_dict[column].append(value)

    return names, frame_dict


def show_dataframe(title, columns, data1, data2=None, data3=None, data4=None, data5=None,
                   label1=None, label2=None, label3=None, label4=None, label5=None):
    """
    Prints a pandas dataframe
    :param columns:
    :param data1:
    :param data2:
    :param data3:
    :param data4:
    :param data5:
    :param label1:
    :param label2:
    :param label3:
    :param label4:
    :param label5:
    :return:
    """
    frame_dict = {}
    names = []
    for column in columns:
        frame_dict[column] = []

    names, frame_dict = add_value_to_dataframe(names, frame_dict, columns, label1, data1)

    if data2:
        names, frame_dict = add_value_to_dataframe(names, frame_dict, columns, label2, data2)

    if data3:
        names, frame_dict = add_value_to_dataframe(names, frame_dict, columns, label3, data3)

    if data4:
        names, frame_dict = add_value_to_dataframe(names, frame_dict, columns, label4, data4)

    if data5:
        names, frame_dict = add_value_to_dataframe(names, frame_dict, columns, label5, data5)

    frame_dict['names'] = names

    values_dataframe = pd.DataFrame(frame_dict)
    values_dataframe.set_index('names', inplace=True)
    print(title)
    print(values_dataframe)


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


def compile_most_common_marker_list(title, datalist, names):
    markers = []

    for i in range(len(datalist)):
        for j in range(2):
            if j % 2 == 0:
                markers = markers + [m for m in datalist[i][j] if m not in markers]

    marker_frame = {}
    for marker in markers:
        marker_frame[marker] = []

        for i in range(len(datalist)):
            for j in range(2):
                if j % 2 == 1:
                    if marker in datalist[i][0]:
                        marker_index = datalist[i][0].index(marker)
                        marker_frame[marker].append(datalist[i][j][marker_index])
                    else:
                        marker_frame[marker].append(0)

    marker_frame['Data'] = names
    values_dataframe = pd.DataFrame(marker_frame)
    values_dataframe.set_index('Data', inplace=True)
    pd.set_option('display.max_columns', 25)
    print(title)
    print(values_dataframe)

    values1 = []
    values2 = None
    values3 = None
    values4 = None
    values5 = None

    for marker in markers:
        values1.append(marker_frame[marker][0])
    if len(datalist) > 1:
        values2 = []
        for marker in markers:
            values2.append(marker_frame[marker][1])
    if len(datalist) > 2:
        values3 = []
        for marker in markers:
            values3.append(marker_frame[marker][2])
    if len(datalist) > 3:
        values4 = []
        for marker in markers:
            values4.append(marker_frame[marker][3])
    if len(datalist) > 4:
        values5 = []
        for marker in markers:
            values5.append(marker_frame[marker][4])

    return markers, [values1, values2, values3, values4, values5]


def compute_cohens_d(x1, x2):
    """
    Computes the Effektsize Cohen's d for two equal-sized sets of data
    :param x1:
    :param x2:
    :return:
    """
    return (statistics.mean(x1) - statistics.mean(x2)) / (math.sqrt((
        statistics.stdev(x1) ** 2 + statistics.stdev(x2) ** 2) / 2
    ))


def compute_t_test(x1, x2):
    """
    Calculate the T-test for the means of two independent samples of scores.
    This is a two-sided test for the null hypothesis that 2 independent samples
    have identical average (expected) values.
    (Assume different variances)
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
    :param x1:
    :param x2:
    :return:
    """
    return stats.ttest_ind(x1, x2, equal_var=False)


def effectsize_and_significance(title, data, labels):

    effectsize = []
    t_statistics = []
    p_values = []
    names = []

    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            effectsize.append(compute_cohens_d(data[i], data[j]))
            t_statistic, p_value = compute_t_test(data[i], data[j])
            t_statistics.append(t_statistic)
            p_values.append(p_value)
            names.append(labels[i] + ", " + labels[j])

    values_dataframe = pd.DataFrame({"Effectsize": effectsize,
                                     "T-Statistic": t_statistics,
                                     "P-Value": p_values,
                                     "Data": names})
    values_dataframe.set_index('Data', inplace=True)
    pd.set_option('display.max_columns', 25)
    print(title)
    print(values_dataframe)


def compute_marker_deltas(title, data, labels):
    print("TODO: Write Function to compute deltas between marker averages")
