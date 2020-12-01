import statistics
import math
import pandas as pd
from scipy import stats

from helpers.DataFrames import save_dataframe


def percentage(part, whole):
    return (float(part) * 100) / (float(whole))


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


def compute_cohens_d(x1, x2):
    """
    Computes the Effektsize Cohen's d for two equal-sized sets of data
    :param x1:
    :param x2:
    :return:
    """
    return (statistics.mean(x1) - statistics.mean(x2)) / (
        math.sqrt((statistics.stdev(x1) ** 2 + statistics.stdev(x2) ** 2) / 2))


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


def gaussian_sum(stop):
    g_sum = 0
    for i in range(1, stop):
        g_sum += i
    return g_sum


def effectsize_and_significance(title, data, labels):
    effectsize = []
    t_statistics = []
    p_values = []
    alpha_small = 0.05
    significant_for_alpha_small = []
    alpha_medium = 0.1
    significant_for_alpha_medium = []
    names = []

    number_of_tests = gaussian_sum(len(data))
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            effectsize.append(compute_cohens_d(data[i], data[j]))
            t_statistic, p_value = compute_t_test(data[i], data[j])
            t_statistics.append(t_statistic)
            p_values.append(p_value)

            '''Bonferroni correction'''
            significant_for_alpha_small.append("yes" if p_value < (alpha_small / number_of_tests) else "no")
            significant_for_alpha_medium.append("yes" if p_value < (alpha_medium / number_of_tests) else "no")

            names.append(labels[i] + ", " + labels[j])

    values_dataframe = pd.DataFrame({"Effectsize": effectsize,
                                     "T-Statistic": t_statistics,
                                     "P-Value": p_values,
                                     "0.05 significant": significant_for_alpha_small,
                                     "0.1 significant": significant_for_alpha_medium,
                                     "Data": names})

    values_dataframe.set_index('Data', inplace=True)
    values_dataframe.to_csv("../../data/listenability-tools/tables/statistics" + title + ".csv")


def compute_marker_deltas(title, data):
    """
    :param title:
    :param data:
    :return:
    """
    names = []
    data = data.transpose()
    for i in range(data.shape[0] - 1):
        for j in range(i + 1, data.shape[0]):
            names.append(data.index[i] + " → " + data.index[j])

    deltas = {'Data': names}

    for marker in data:
        deltas[marker] = []
        for i in range(len(data[marker]) - 1):
            for j in range(i + 1, len(data[marker])):
                # delta = abs(data[marker][i] - data[marker][j])
                delta = round(((data[marker][j] / data[marker][i]) - 1) * 100, 2)
                deltas[marker].append(delta)

    deltas_dataframe = pd.DataFrame(deltas)
    deltas_dataframe.set_index('Data', inplace=True)
    deltas_dataframe = deltas_dataframe
    save_dataframe(title + "_deltas", deltas_dataframe.transpose())




