import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics
import ast


# ----------- Plot the Data ------------
def draw_barchart(title, x, y_1, y_1_label,
                  y_2=None, y_2_label=None, y_3=None, y_3_label=None, y_4=None, y_4_label=None,
                  width=0.15, style='fivethirtyeight',
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
        plt.bar(x_indexes - (width / 4) * 6, y_1, width=width, color=color_1, label=y_1_label)
        plt.bar(x_indexes, y_2, width=width, color=color_2, label=y_2_label)
        plt.bar(x_indexes + (width / 4) * 6, y_3, width=width, color=color_3, label=y_3_label)

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
        plt.xticks(ticks=x_indexes, labels=x_ticks[1])
    if y_ticks:
        plt.xticks(ticks=y_ticks[0], labels=y_ticks[1])

    if y_2:
        '''Add a legend for more than one dataset to distinguish which color stands for which dataset'''
        plt.legend()

    plt.tight_layout()

    plt.show()


def draw_piechart(title, slices, labels, colors, angle):
    plt.pie(slices, labels=labels, colors=colors,
            startangle=angle, autopct='%1.1f%%')

    plt.title(title)
    plt.tight_layout()
    plt.show()


# ------------ READ & PROCESS DATA ----------
def read_data(spotify_file, ted_file, ny_file, gig_file):
    spotify_data = pd.read_csv(spotify_file)
    ted_data = pd.read_csv(ted_file)
    ny_data = pd.read_csv(ny_file)
    gig_data = pd.read_csv(gig_file)

    process_data(spotify_data, ted_data, ny_data, gig_data)


def process_data(spotify_data, ted_data, ny_data, gig_data):
    """
    Calls all the computations and plots for all the datasets
    :param spotify_data: scores from the Spotify Podcast Data
    :param ted_data: scores from the TED-LIUM 3 Data
    :param ny_data: scores from the New York Times Data
    :param gig_data: scores from the Gigaword Data
    :return:
    """

    '''
    01: Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''
    # plot_data_barchart("Percent Discourse Markers per Text",
    #                    compute_y_values_basic(spotify_data['dm_words_perc'].dropna(),
    #                                           ted_data['dm_words_perc'].dropna(),
    #                                           ny_data['dm_words_perc'].dropna(),
    #                                           gig_data['dm_words_perc'].dropna()),
    #                    ["Min % DM", "Mean % DM", "Max % DM"],
    #                    "Percent Markers",
    #                    label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                    color_1='#1DB954', color_2='#e62b1e', color_3='#cecece', color_4='#7CACED')
    #
    # '''
    # 02: Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    # min/mean/max(dm_count_doc)
    # '''
    # plot_data_barchart("Number of Discourse Markers per Text",
    #                    compute_y_values_basic(spotify_data['dm_count_doc'].dropna(), ted_data['dm_count_doc'].dropna(),
    #                                           ny_data['dm_count_doc'].dropna(), gig_data['dm_count_doc'].dropna()),
    #                    ["Min # DM", "Mean # DM", "Max # DM"],
    #                    "Number Markers",
    #                    label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                    color_1='#1DB954', color_2='#e62b1e', color_3='#cecece', color_4='#7CACED')
    #
    # '''
    # 03: Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    # min/mean/max(dm_sentences_perc)
    # '''
    # plot_data_barchart("Percent of Sentences with DM per Text",
    #                    compute_y_values_basic(spotify_data['dm_sentences_perc'].dropna(),
    #                                           ny_data['dm_sentences_perc'].dropna(),
    #                                           gig_data['dm_sentences_perc'].dropna()),
    #                    ["Min % Sent w/DM", "Mean % Sent w/DM", "Max % Sent w/DM"],
    #                    "Percent Sentences containing DM",
    #                    label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                    color_1='#1DB954', color_2='#cecece', color_3='#7CACED')
    #
    # '''
    # 04: Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    # min/mean/max(dm_sentences)
    # '''
    # plot_data_barchart("Number of Sentences with DM per Text",
    #                    compute_y_values_basic(spotify_data['dm_sentences'].dropna(), ny_data['dm_sentences'].dropna(),
    #                                           gig_data['dm_sentences'].dropna()),
    #                    ["Min # Sent w/DM", "Mean # Sent w/DM", "Max # Sent w/DM"],
    #                    "Number Sentences containing DM",
    #                    label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                    color_1='#1DB954', color_2='#cecece', color_3='#7CACED')
    #
    # '''05:
    # Number of DM per sentence'''
    # plot_data_barchart("Number of Discourse Markers per Sentence",
    #                    compute_dm_per_sentence_count(
    #                        [spotify_data['dm_count_min'].dropna(), spotify_data['dm_count_mean'].dropna(),
    #                         spotify_data['dm_count_max'].dropna()],
    #                        [ny_data['dm_count_min'].dropna(), ny_data['dm_count_mean'].dropna(),
    #                         ny_data['dm_count_max'].dropna()],
    #                        [gig_data['dm_count_min'].dropna(), gig_data['dm_count_mean'].dropna(),
    #                         gig_data['dm_count_max'].dropna()]),
    #                    ["Min # DM", "Mean # DM", "Max # DM"],
    #                    "Number Markers per Sentence",
    #                    label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                    color_1='#1DB954', color_2='#cecece', color_3='#7CACED')
    #
    # '''06:
    # Number of DM at certain positions in a sentence'''
    # plot_data_barchart("Number of DM at a certain Position in a Sentence",
    #                    compute_dm_position_sentence_count(
    #                        [spotify_data['dm_pos_sent_begin'].dropna(), spotify_data['dm_pos_sent_middle'].dropna(),
    #                         spotify_data['dm_pos_sent_end'].dropna()],
    #                        [ny_data['dm_pos_sent_begin'].dropna(), ny_data['dm_pos_sent_middle'].dropna(),
    #                         ny_data['dm_pos_sent_end'].dropna()],
    #                        [gig_data['dm_pos_sent_begin'].dropna(), gig_data['dm_pos_sent_middle'].dropna(),
    #                         gig_data['dm_pos_sent_end'].dropna()]
    #                    ),
    #                    ["Sent. Begin", "Sent. Middle", "Sent. End"],
    #                    "Number DM at Postion",
    #                    label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                    color_1='#1DB954', color_2='#cecece', color_3='#7CACED')
    #
    # '''07:
    #     Percentage of DM at certain positions in a sentence'''
    # plot_data_barchart("% of DM in certain Positions in a Sentence",
    #                    compute_dm_position_sentence_perc(
    #                        [spotify_data['dm_pos_sent_begin'].dropna(), spotify_data['dm_pos_sent_middle'].dropna(),
    #                         spotify_data['dm_pos_sent_end'].dropna()],
    #                        [ny_data['dm_pos_sent_begin'].dropna(), ny_data['dm_pos_sent_middle'].dropna(),
    #                         ny_data['dm_pos_sent_end'].dropna()],
    #                        [gig_data['dm_pos_sent_begin'].dropna(), gig_data['dm_pos_sent_middle'].dropna(),
    #                         gig_data['dm_pos_sent_end'].dropna()]
    #                    ),
    #                    ["Sent. Begin", "Sent. Middle", "Sent. End"],
    #                    "% DM at Postion",
    #                    label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                    color_1='#1DB954', color_2='#cecece', color_3='#7CACED')
    #
    # '''Number of DM at certain positions in a sentence per Dataset'''
    # plot_dm_positions_sent_piechart("Number of DM in a Sentence at Position:",
    #                                 [[spotify_data['dm_pos_sent_begin'].dropna(),
    #                                   spotify_data['dm_pos_sent_middle'].dropna(),
    #                                   spotify_data['dm_pos_sent_end'].dropna()],
    #                                  [ny_data['dm_pos_sent_begin'].dropna(), ny_data['dm_pos_sent_middle'].dropna(),
    #                                   ny_data['dm_pos_sent_end'].dropna()],
    #                                  [gig_data['dm_pos_sent_begin'].dropna(), gig_data['dm_pos_sent_middle'].dropna(),
    #                                   gig_data['dm_pos_sent_end'].dropna()]
    #                                  ],
    #                                 ["Spotify Data", "NYTimes Data", "Gigaword Data"],
    #                                 ['#1DB954', '#cecece', '#7CACED'])

    '''Histogram with Number of DM per Sentence per Dataset'''
    compute_dm_per_sentence(spotify_data['dm_count_dict'].dropna(), "Spotify", '#1DB954')
    compute_dm_per_sentence(ny_data['dm_count_dict'].dropna(), "New York Times", '#cecece')
    compute_dm_per_sentence(gig_data['dm_count_dict'].dropna(), "Gigaword", '#7CACED')


def plot_data_barchart(title, y_values, x_labels, y_label,
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

    draw_barchart(title, x_values,
                  y_values_1, label_1, y_values_2, y_2_label=label_2,
                  y_label=y_label, x_ticks=[x_values, x_labels],
                  y_3=y_values_3, y_3_label=label_3, y_4=y_values_4, y_4_label=label_4,
                  color_1=color_1, color_2=color_2, color_3=color_3, color_4=color_4)


def plot_dm_positions_sent_piechart(title, data, labels, colors):
    """
    Prepares the Data for Piecharts:
    One for each Dataset with slices=[counter_begin, counter_middle, counder_end]
    and one for each Position (Begin, Middle, End) with slices for each dataset
    :param: data array that contains the datasets
    :param: array of labels for the datasets
    :param: array of colors for the datasets
    :return:
    """
    set_labels = ["Sentence Begin", "Sentence Middle", "Sentence End"]
    # greens, greys, blues
    set_colors = [['#61D836', '#007B76', '#1DB100'], ['#f2f2f2', '#cecece', '#aba7a7'],
                  ['#7CACED', '#2657AF', '#6291E7']]
    begin_slices = []
    middle_slices = []
    end_slices = []
    for dataset, label, color in zip(data, labels, set_colors):
        begin_slices.append(sum(dataset[0]))
        middle_slices.append(sum(dataset[1]))
        end_slices.append(sum(dataset[2]))
        set_slices = [sum(dataset[0]), sum(dataset[1]), sum(dataset[2])]
        set_title = label
        draw_piechart(set_title, set_slices, set_labels, color, 0)

    # draw_piechart(title + " Begin", begin_slices, labels, colors, 0)
    # draw_piechart(title + " Middle", middle_slices, labels, colors, 0)
    # draw_piechart(title + " End", end_slices, labels, colors, 0)


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
    data_x = [dm_pos_sent_begin, dm_pos_sent_middle, dm_pos_sent_end]
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


def compute_dm_per_sentence(data, title, color):

    values = {}

    # Scores are stored in one cell as a String, formated like a python dict
    # read the string and evaluate it like a pyton dict
    for doc in data:
        doc_count = ast.literal_eval(doc)

        for count in doc_count:
            if count not in values:
                values[count] = int(doc_count[count])
            else:
                values[count] += int(doc_count[count])

    x_values = []
    y_values = []
    for element in sorted(values.items()):
        x_values.append(element[0])
        y_values.append(element[1])

    plt.style.use('fivethirtyeight')

    plt.bar(x_values, y_values, color=color)
    plt.xlabel("Number Marker per Sentence")
    plt.ylabel("Number Sentences")

    plt.title("Number of DM per Sentence - " + title)

    plt.tight_layout()
    plt.show()


def compute_dm_position_sentence_perc(data_1, data_2=None, data_3=None, data_4=None):
    """
    Anzahl der DM, die im Satz vorne, in der Mitte und am Ende stehen
    sum(dm_pos_sent_begin)
    sum(dm_pos_sent_middle)
    sum(dm_pos_sent_end)
    data_x = [dm_pos_sent_begin, dm_pos_sent_middle, dm_pos_sent_end]
    :return:
    """

    whole_1 = sum([sum(data_1[0]), sum(data_1[1]), sum(data_1[2])])
    y_values_1 = [percentage(sum(data_1[0]), whole_1), percentage(sum(data_1[1]), whole_1),
                  percentage(sum(data_1[2]), whole_1)]

    y_values_2 = None
    y_values_3 = None
    y_values_4 = None

    if data_2 is not None:
        whole_2 = sum([sum(data_2[0]), sum(data_2[1]), sum(data_2[2])])
        y_values_2 = [percentage(sum(data_2[0]), whole_2), percentage(sum(data_2[1]), whole_2),
                      percentage(sum(data_2[2]), whole_2)]

    if data_3 is not None:
        whole_3 = sum([sum(data_3[0]), sum(data_3[1]), sum(data_3[2])])
        y_values_3 = [percentage(sum(data_3[0]), whole_3), percentage(sum(data_3[1]), whole_3),
                      percentage(sum(data_3[2]), whole_3)]

    if data_4 is not None:
        whole_4 = sum([sum(data_4[0]), sum(data_4[1]), sum(data_4[2])])
        y_values_4 = [percentage(sum(data_4[0]), whole_4), percentage(sum(data_4[1]), whole_4),
                      percentage(sum(data_4[2]), whole_4)]

    print([y_values_1, y_values_2, y_values_3, y_values_4])
    return [y_values_1, y_values_2, y_values_3, y_values_4]


# ----------- HELPER -----------
def percentage(part, whole):
    return (float(part) * 100) / (float(whole))


# ------------ MAIN -------------
def main():
    """
    To add more data: change "read_data(), give more parameters here, change function calls in "process_data"
    :return:
    """
    read_data("../../bigData/listenability-tools/pipeline-output/spotify-scores.csv",
              "../../bigData/listenability-tools/pipeline-output/ted-scores.csv",
              "../../bigData/listenability-tools/pipeline-output/nytimes-scores.csv",
              "../../bigData/listenability-tools/pipeline-output/gigaword-scores.csv")


if __name__ == '__main__':
    main()
