import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics


# ----------- Plot the Data ------------
def draw_barchart(title, x, y_1, y_1_label,
                  y_2=None, y_2_label=None, y_3=None, y_3_label=None, y_4=None, y_4_label=None,
                  width=0.25, style='fivethirtyeight',
                  color_1='k', color_2='k', color_3='k', color_4='k',
                  x_label=None, y_label=None, x_ticks=None, y_ticks=None):
    """
    Draws a Barchart of the given Data
    :param title: the title of the plot
    :param x: the array of x values
    :param y_1: the array of the first set of y values
    :param y_1_label: the label of the first dataset
    :param y_2: the array of the second set of y values
    :param y_2_label: the label of the second dataset
    :param y_3: the array of the third set of y values
    :param y_3_label: the label of the third dataset
    :param y_4: the array of the fourth set of y values
    :param y_4_label: the label of the fourth dataset
    :param width: the width of the bars
    :param style: the style that should be used in the plot
    :param color_1: color for the first set of data
    :param color_2: color for the second set of data
    :param color_3: color for the third set of data
    :param color_4: color for the fourth set of data
    :param x_label: the label for the x-axis
    :param y_label: the label for the y-axis
    :param x_ticks: array of [[x-ticks], [labels for those ticks]]
    :param y_ticks: array of [[y-ticks], [labels for those ticks]]
    :return: nothing
    """

    plt.style.use(style)

    '''For two sets of data we need to set the bars a bit appart, otherwise they would overlap'''
    x_indexes = x_ticks[0]

    if not y_2 and not y_3 and not y_4:
        plt.bar(x, y_1, color=color_1)

    elif y_2 and not y_3 and not y_4:
        plt.bar(x_indexes - (width / 4) * 3, y_1, width=width, color=color_1, label=y_1_label)
        plt.bar(x_indexes + (width / 4) * 3, y_2, width=width, color=color_2, label=y_2_label)

    elif not y_4:
        plt.bar(x_indexes - (width / 4) * 3, y_1, width=width, color=color_1, label=y_1_label)
        plt.bar(x_indexes, y_2, width=width, color=color_2, label=y_2_label)
        plt.bar(x_indexes + (width / 4) * 3, y_3, width=width, color=color_3, label=y_3_label)

    elif y_4:
        plt.bar(x_indexes - (width / 4) * 9, y_1, width=width, color=color_1, label=y_1_label)
        plt.bar(x_indexes - (width / 4) * 3, y_2, width=width, color=color_2, label=y_2_label)
        plt.bar(x_indexes + (width / 4) * 3, y_3, width=width, color=color_3, label=y_3_label)
        plt.bar(x_indexes + (width / 4) * 9, y_4, width=width, color=color_4, label=y_4_label)

    plt.title(title)

    '''Set the labels for the x- and the y-axis'''
    if x_label:
        plt.xlabel(x_label)
    if y_label:
        plt.ylabel(y_label)

    '''Set the ticks and their labels for x and y'''
    if x_ticks:
        plt.xticks(ticks=x_ticks[0], labels=x_ticks[1])
    if y_ticks:
        plt.xticks(ticks=y_ticks[0], labels=y_ticks[1])

    if y_2:
        '''Add a legend for more than one dataset to distinguish which color stands for which dataset'''
        plt.legend()

    plt.tight_layout()

    plt.show()


# ------------ READ & PROCESS DATA ----------
def read_data(spotify_file, ted_file):
    spotify_data = pd.read_csv(spotify_file)
    ted_data = pd.read_csv(ted_file)

    process_data(spotify_data, ted_data)


def process_data(spotify_data, ted_data):
    """
    Calls all the computations and plots for all the datasets
    :param spotify_data:
    :param ted_data:
    :return:
    """

    '''
    Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''
    plot_data("Percent Discourse Markers per Text",
              compute_y_values_basic(spotify_data['dm_words_perc'], ted_data['dm_words_perc']),
              ["Min % DM", "Mean % DM", "Max % DM"],
              "Percent Markers",
              label_1="Spotify", label_2="TED",
              color_1='#1DB954', color_2='#e62b1e')

    '''
    Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_count_doc)
    '''
    plot_data("Number of Discourse Markers per Text",
              compute_y_values_basic(spotify_data['dm_count_doc'], ted_data['dm_count_doc']),
              ["Min # DM", "Mean # DM", "Max # DM"],
              "Number Markers",
              label_1="Spotify", label_2="TED",
              color_1='#1DB954', color_2='#e62b1e')

    '''
    Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    min/mean/max(dm_sentences_perc)
    '''
    plot_data("Percent of Sentences with DM per Text",
              compute_y_values_basic(spotify_data['dm_sentences_perc']),
              ["Min % Sent w/DM", "Mean % Sent w/DM", "Max % Sent w/DM"],
              "Percent Sentences containing DM",
              label_1="Spotify", color_1='#1DB954')

    '''
    Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_sentences)
    '''
    plot_data("Number of Sentences with DM per Text",
              compute_y_values_basic(spotify_data['dm_sentences']),
              ["Min # Sent w/DM", "Mean # Sent w/DM", "Max # Sent w/DM"],
              "Number Sentences containing DM",
              label_1="Spotify", color_1='#1DB954')

    '''Number of DM per sentence'''
    plot_data("Number of Discourse Markers per Sentence",
              compute_dm_per_sentence_count(
                      [spotify_data['dm_count_min'], spotify_data['dm_count_mean'],
                       spotify_data['dm_count_max']]),
              ["Min # DM", "Mean # DM", "Max # DM"],
              "Number Markers per Sentence",
              label_1="Spotify", color_1='#1DB954')

    '''Number of DM at certain positions in a sentence'''
    plot_data("Number of DM at a certain Position in a Sentence",
              compute_dm_position_sentence_count(
                      [spotify_data['dm_pos_sent_begin'], spotify_data['dm_pos_sent_middle'], spotify_data['dm_pos_sent_end']]),
              ["Sent. Begin", "Sent. Middle", "Sent. End"],
              "Number DM at Postion",
              label_1="Spotify", color_1='#1DB954')


def plot_data(title, y_values, x_labels, y_label,
              label_1, label_2=None, label_3=None, label_4=None,
              color_1='k', color_2='k', color_3='k', color_4='k'):
    """
    Prepare the Data for plotting

    :param title: Title of the plot
    :param y_values: Array of the y-value sets that are to be plottet: [data_1,data_2,etc]
    :param x_labels: Array of Labels for the x-ticks
    :param y_label: Label for the y-axis
    :param label_1: Label for the first set of y-values
    :param label_2: Label for the second set of y-values
    :param label_3: Label for the third set of y-values
    :param label_4: Label for the fourth set of y-values
    :param color_1: Color for the first set of y-values
    :param color_2: Color for the second set of y-values
    :param color_3: Color for the third set of y-values
    :param color_4: Color for the fourth set of y-values
    :return:
    """

    y_values_1 = y_values[0]
    y_values_2 = y_values[1]
    y_values_3 = y_values[2]
    y_values_4 = y_values[3]

    x_values = np.arange(len(y_values_1))
    print(x_values)
    print(x_labels)

    draw_barchart(title, x_values,
                  y_values_1, label_1, y_values_2, y_2_label=label_2,
                  y_label=y_label, x_ticks=[x_values, x_labels],
                  y_3=y_values_3, y_3_label=label_3, y_4=y_values_4, y_4_label=label_4,
                  color_1=color_1, color_2=color_2, color_3=color_3, color_4=color_4)


# ----------- Computing the Distributions ------------
def compute_y_values_basic(data_1, data_2=None, data_3=None, data_4=None):
    """
    Computes the y-values for the given data when just the respective min/mean/max is needed
    :param data_1: the first set of data
    :param data_2: the second set of data
    :param data_3: the third set of data
    :param data_4: the fourth set of data
    :return: an array of the computed data-values in the order they where given
    """
    y_values_1 = [min(data_1), statistics.mean(data_1), max(data_1)]
    y_values_2 = None
    y_values_3 = None
    y_values_4 = None

    if data_2 is not None:
        y_values_2 = [min(data_2), statistics.mean(data_2), max(data_2)]

    if data_3 is not None:
        y_values_3 = [min(data_3), statistics.mean(data_3), max(data_3)]

    if data_4 is not None:
        y_values_4 = [min(data_4), statistics.mean(data_4), max(data_4)]

    print([y_values_1, y_values_2, y_values_3, y_values_4])
    return [y_values_1, y_values_2, y_values_3, y_values_4]


def compute_dm_per_sentence_count(data_1, data_2=None, data_3=None, data_4=None):
    """
    The minimum number of discourse markers per sentence over all texts
    min(dm_count_min)
    Takes the mean of the mean number of discourse markers per sentence per text
    mean(dm_count_mean)
    the maximum number of discourse markers per sentence over all texts
    max(dm_count_max)
    :return:
    """
    y_values_1 = [min(data_1[0]), statistics.mean(data_1[1]), max(data_1[2])]
    y_values_2 = None
    y_values_3 = None
    y_values_4 = None

    if data_2 is not None:
        y_values_2 = [min(data_2[0]), statistics.mean(data_2[1]), max(data_2[2])]

    if data_3 is not None:
        y_values_3 = [min(data_3[0]), statistics.mean(data_3[1]), max(data_3[2])]

    if data_4 is not None:
        y_values_4 = [min(data_4[0]), statistics.mean(data_4[1]), max(data_4[2])]

    print([y_values_1, y_values_2, y_values_3, y_values_4])
    return [y_values_1, y_values_2, y_values_3, y_values_4]


def compute_dm_position_sentence_count(data_1, data_2=None, data_3=None, data_4=None):
    """
    Anzahl der DM, die im Satz vorne, in der Mitte und am Ende stehen
    sum(dm_pos_sent_begin)
    sum(dm_pos_sent_middle)
    sum(dm_pos_sent_end)
    :return:
    """

    y_values_1 = [sum(data_1[0]), sum(data_1[1]), sum(data_1[2])]
    y_values_2 = None
    y_values_3 = None
    y_values_4 = None

    if data_2 is not None:
        y_values_2 = [sum(data_2[0]), sum(data_2[1]), sum(data_2[2])]

    if data_3 is not None:
        y_values_3 = [sum(data_3[0]), sum(data_3[1]), sum(data_3[2])]

    if data_4 is not None:
        y_values_4 = [sum(data_4[0]), sum(data_4[1]), sum(data_4[2])]

    print([y_values_1, y_values_2, y_values_3, y_values_4])
    return [y_values_1, y_values_2, y_values_3, y_values_4]


def compute_dm_position_sentence_perc(title, data_1, label_1, data_2, label_2, x_labels, y_label):
    """
    Prozentualer Anteil der DM, die im Satz vorne stehen oder in der Mitte oder hinten
    whole = sum(sum(dm_pos_sent_begin) + sum(dm_pos_sent_middle) + sum(dm_pos_sent_end))
    part = respective
    :return:
    """
    whole_1 = sum([sum(data_1[0]), sum(data_1[1]), sum(data_1[2])])
    whole_2 = sum([sum(data_2[0]), sum(data_2[1]), sum(data_2[2])])

    y_values_1 = [percentage(sum(data_1[0]), whole_1), percentage(sum(data_1[1]), whole_1),
                  percentage(sum(data_1[2]), whole_1)]

    y_values_2 = [percentage(sum(data_2[0]), whole_2), percentage(sum(data_2[1]), whole_2),
                  percentage(sum(data_2[2]), whole_2)]

    x_values = np.arange(len(y_values_2))

    '''Draw PieChart of this!'''


# ----------- HELPER -----------
def percentage(part, whole):
    return (float(part) * 100) / (float(whole))


# ------------ MAIN -------------
def main():
    # distribution.read_data("../../data/listenability-tools/pipeline-output/SpotifyData/spotify-scores.csv")
    read_data("../../data/listenability-tools/pipeline-output/SpotifyData/spotify-scores.csv",
              "../../data/listenability-tools/pipeline-output/TedData/ted-scores.csv")


if __name__ == '__main__':
    main()
