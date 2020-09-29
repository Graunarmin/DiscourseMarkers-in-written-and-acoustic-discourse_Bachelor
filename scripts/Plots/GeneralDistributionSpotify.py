import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics


# ----------- Plot the Data ------------
def draw_barchart(title,
                  x, y,
                  style='fivethirtyeight',
                  x_label=None, y_label=None, x_ticks=None, y_ticks=None):
    """
    Draws a vertical barchart with the given parameters
    :param x: the array of x values
    :param y: the array of y values
    :param title: the title of the plot
    :param style: the style that should be used in the plot. Default is 'fivethirtyeight'.
    :param x_label: the label for the x-axis
    :param y_label: the label for the y-axis
    :param x_ticks: array of [[x-ticks], [labels for those ticks]]
    :param y_ticks: array of [[y-ticks], [labels for those ticks]]
    :return: nothing
    """

    plt.style.use(style)
    plt.bar(x, y)

    plt.title(title)

    if x_label:
        plt.xlabel(x_label)
    if y_label:
        plt.ylabel(y_label)

    if x_ticks:
        plt.xticks(ticks=x_ticks[0], labels=x_ticks[1])
    if y_ticks:
        plt.xticks(ticks=y_ticks[0], labels=y_ticks[1])

    plt.tight_layout()
    
    plt.show()


def draw_barchart_two_sets(title,
                           x,
                           y_1, y_1_label,
                           y_2, y_2_label,
                           width,
                           style='fivethirtyeight',
                           x_label=None, y_label=None,
                           x_ticks=None, y_ticks=None):
    """
    Draws a vertical barchart for two y-value sets on the same x-basis


    :param title: the title of the plot
    :param x: the array of x values
    :param y_1: the array of the first set of y values
    :param y_1_label: The Label of the first dataset
    :param y_2: the array of the second set of y values
    :param y_2_label: The Label of the second dataset
    :param width: the width of the bars
    :param style: the style that should be used in the plot. Default is 'fivethirtyeight'.
    :param x_label: the label for the x-axis
    :param y_label: the label for the y-axis
    :param x_ticks:
    :param y_ticks:
    :return: nothing
    """

    plt.style.use(style)

    x_indexes = x_ticks[0]
    plt.bar(x_indexes - (width / 4) * 3, y_1, width=width, color='#1DB954', label=y_1_label)
    plt.bar(x_indexes + (width / 4) * 3, y_2, width=width, color='#e62b1e', label=y_2_label)

    plt.title(title)

    if x_label:
        plt.xlabel(x_label)
    if y_label:
        plt.ylabel(y_label)

    if x_ticks:
        plt.xticks(ticks=x_ticks[0], labels=x_ticks[1])
    if y_ticks:
        plt.xticks(ticks=y_ticks[0], labels=y_ticks[1])

    plt.legend()

    plt.xticks(ticks=x_ticks[0], labels=x_ticks[1])

    plt.tight_layout()

    plt.show()


def percentage(part, whole):
    return (float(part) * 100) / (float(whole))


# ------------ READ DATA ----------
def read_data(spotify_file, ted_file):
    spotify_data = pd.read_csv(spotify_file)
    ted_data = pd.read_csv(ted_file)
    '''
    Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''
    plot_two_datasets(spotify_data['dm_words_perc'], "Spotify", ted_data['dm_words_perc'], "TED",
                      "Percent Discourse Markers per Text",
                      ["Min % DM", "Mean % DM", "Max % DM"],
                      "Percent Markers")

    '''
    Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_count_doc)
    '''
    plot_two_datasets(spotify_data['dm_count_doc'], "Spotify",
                      ted_data['dm_count_doc'], "TED",
                      "Number of Discourse Markers per Text",
                      ["Min # DM", "Mean # DM", "Max # DM"],
                      "Number Markers")

    '''
    Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    min/mean/max(dm_sentences_perc)
    '''
    plot_two_datasets(spotify_data['dm_sentences_perc'], "Spotify",
                      ted_data['dm_sentences_perc'], "TED",
                      "Percent of Sentences with DM per Text",
                      ["Min % Sent w/DM", "Mean % Sent w/DM", "Max % Sent w/DM"],
                      "Percent Sentences containing DM")

    # plot_one_dataset(ted_data['dm_count_doc'], "DM per Text (TED)", ["Min # DM", ""])


# ----------- Distribution ------------
def plot_one_dataset(data, title, x_labels, y_label):
    """
    Plot a barchart of one Dataset for min, mean, max values
    :param data: The data to compute the min, mean, max from
    :param title: The Title of the Plot
    :param x_labels: Array of the Labels for the x-ticks
    :param y_label: The Label for the y-Achsis
    :return:
    """
    y_values = [min(data), statistics.mean(data), max(data)]
    x_values = np.arange(len(y_values))
    x_labels = x_labels

    draw_barchart(title, x_values, y_values,
                  y_label=y_label,
                  x_ticks=[x_values, x_labels])


def plot_two_datasets(data_1, label1, data_2, label2, title, x_labels, y_label):
    """
    Plots two given sets of y-values over set of x-values.

    :param data_1: First set of y-values
    :param label1: Label for the first set of y-values
    :param data_2: Second set of y-values
    :param label2: Label for the second set of y-values
    :param title: Title of the plot
    :param x_labels: Array of Labels for the x-ticks
    :param y_label: Label for the y-axis
    :return: nothing
    """
    y_values_1 = [min(data_1), statistics.mean(data_1), max(data_1)]
    y_values_2 = [min(data_2), statistics.mean(data_2), max(data_2)]

    x_values = np.arange(len(y_values_1))

    draw_barchart_two_sets(title,
                           x_values,
                           y_values_1, label1,
                           y_values_2, label2,
                           0.25,
                           y_label=y_label,
                           x_ticks=[x_values, x_labels])


def dm_sentences_per_text_perc():
    """
    Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    min/mean/max(dm_sentences_perc)
    :return:
    """
    pass


def dm_sentences_per_text_count():
    """
    Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_sentences)
    :return:
    """
    pass


def dm_per_sentence_count():
    """
    The minimum number of discourse markers per sentence over all texts
    min(dm_count_min)
    Takes the mean of the mean number of discourse markers per sentence per text
    mean(dm_count_mean)
    the maximum number of discourse markers per sentence over all texts
    max(dm_count_max)
    :return:
    """
    pass


def dm_position_sentence_count():
    """
    Anzahl der DM, die im Satz vorne, in der Mitte und am Ende stehen
    sum(dm_pos_sent_begin)
    sum(dm_pos_sent_middle)
    sum(dm_pos_sent_end)
    :return:
    """
    pass


def dm_position_sentence_perc():
    """
    Prozentualer Anteil der DM, die im Satz vorne stehen oder in der Mitte oder hinten
    whole = sum(sum(dm_pos_sent_begin) + sum(dm_pos_sent_middle) + sum(dm_pos_sent_end))
    part = respective
    :return:
    """
    pass


# ------------ MAIN -------------
def main():
    # distribution.read_data("../../data/listenability-tools/pipeline-output/SpotifyData/spotify-scores.csv")
    read_data("../../data/listenability-tools/pipeline-output/SpotifyData/spotify-scores.csv",
              "../../data/listenability-tools/pipeline-output/TedData/ted-scores.csv")


if __name__ == '__main__':
    main()
