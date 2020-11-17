import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics
import ast
import json



# ----------- Plot the Data ------------
def draw_barchart(title, x, y_1, y_1_label,
                  y_2=None, y_2_label=None, y_3=None, y_3_label=None, y_4=None, y_4_label=None,
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

    plt.style.use('fivethirtyeight')
    width = 0.15

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
        plt.yticks(ticks=y_ticks[0], labels=y_ticks[1])

    if y_2:
        '''Add a legend for more than one dataset to distinguish which color stands for which dataset'''
        plt.legend()

    plt.tight_layout()

    plt.show()


def draw_piechart(title, slices, labels, colors, angle):
    """
    Draws a Piechart of the given data with a title and labels for the slices
    """
    plt.pie(slices, labels=labels, colors=colors,
            startangle=angle, autopct='%1.1f%%')

    plt.title(title)
    plt.tight_layout()
    plt.show()


def draw_horizontal_barchart(title, y_data, x_1, label_1, x_label, y_ticks, x_2=None, label_2=None,
                             x_3=None, label_3=None, x_4=None, label_4=None,
                             color_1='k', color_2='k', color_3='k', color_4='k'):
    """
    analysis a horizontal barchart
    :param title: Titel of the barchart
    :param y_data: The Data to be shown (e.g. a list of all the markers]
    :param x_1: The Numbers for the first dataset (e.g. a list of occurrence-numbers of the markers)
    :param label_1: Name of the first dataset
    :param x_label: Label for the x values (e.g. "Number of occurrences")
    :param x_2: The Numbers for the first dataset (e.g. a list of occurrence-numbers of the markers)
    :param label_2: Name of the first dataset
    :param x_3: The Numbers for the first dataset (e.g. a list of occurrence-numbers of the markers)
    :param label_3: Name of the first dataset
    :param x_4: The Numbers for the first dataset (e.g. a list of occurrence-numbers of the markers)
    :param label_4: Name of the first dataset
    :param color_1: the color for the bars
    :param color_2: the color for the bars
    :param color_3: the color for the bars
    :param color_4: the color for the bars
    :return:
    """

    plt.style.use('fivethirtyeight')
    width = 0.15

    y_indexes = y_ticks[0]

    if not x_2 and not x_3 and not x_4:
        plt.barh(y_data, x_1, height=width, color=color_1, label=label_1)

    elif not x_3 and not x_4:
        plt.barh(y_indexes - (width / 4) * 3, x_1, height=width, color=color_1, label=label_1)
        plt.barh(y_indexes + (width / 4) * 3, x_2, height=width, color=color_2, label=label_2)

    elif not x_4:
        plt.barh(y_indexes - (width / 4) * 6, x_1, height=width, color=color_1, label=label_1)
        plt.barh(y_indexes, x_2, height=width, color=color_2, label=label_2)
        plt.barh(y_indexes + (width / 4) * 6, x_3, height=width, color=color_3, label=label_3)

    else:
        plt.barh(y_indexes - (width / 4) * 9, x_1, height=width, color=color_1, label=label_1)
        plt.barh(y_indexes - (width / 4) * 3, x_2, height=width, color=color_2, label=label_2)
        plt.barh(y_indexes + (width / 4) * 3, x_3, height=width, color=color_3, label=label_3)
        plt.barh(y_indexes + (width / 4) * 9, x_4, height=width, color=color_4, label=label_4)

    plt.title(title)

    plt.xlabel(x_label)
    plt.yticks(ticks=y_ticks[0], labels=y_ticks[1])

    plt.legend()

    plt.tight_layout()
    plt.show()


def draw_horizontal_subplots(title, y_data, x_1, label_1, x_label, x_2=None, label_2=None,
                             x_3=None, label_3=None, x_4=None, label_4=None,
                             color_1='k', color_2='k', color_3='k', color_4='k'):
    plt.style.use('fivethirtyeight')
    width = 0.15

    if not x_2 and not x_3 and not x_4:
        fig, ax = plt.subplots()
        ax.barh(y_data, x_1, height=width, color=color_1, label=label_1)

        ax.legend()
        ax.set_title(title)
        ax.set_xlabel(x_label)

    elif not x_3 and not x_4:
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True)
        ax1.barh(y_data, x_1, height=width, color=color_1, label=label_1)
        ax2.barh(y_data, x_2, height=width, color=color_2, label=label_2)

        ax1.legend()
        ax1.set_title(title)
        ax1.set_xlabel(x_label)

        ax2.legend()
        ax2.set_xlabel(x_label)

    elif not x_4:
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharey=True)
        ax1.barh(y_data, x_1, height=width, color=color_1, label=label_1)
        ax2.barh(y_data, x_2, height=width, color=color_2, label=label_2)
        ax3.barh(y_data, x_3, height=width, color=color_3, label=label_3)

        ax1.legend()
        ax1.set_title(title)

        ax2.legend()
        ax2.set_xlabel(x_label)

        ax3.legend()
        ax3.set_xlabel(x_label)

    else:
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharey=True, sharex=True)
        ax1.barh(y_data, x_1, height=width, color=color_1, label=label_1)
        ax2.barh(y_data, x_2, height=width, color=color_2, label=label_2)
        ax3.barh(y_data, x_3, height=width, color=color_3, label=label_3)
        ax4.barh(y_data, x_4, height=width, color=color_4, label=label_4)

        ax1.set_title(title)
        ax1.legend()

        ax2.legend()

        ax3.legend()
        ax3.set_xlabel(x_label)

        ax4.legend()
        ax4.set_xlabel(x_label)

    plt.tight_layout()
    plt.show()


# ------------ PROCESS DATA ----------
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


def plot_horizontal_barchart(title, y_values, x_values, x_label,
                             label_1, label_2=None, label_3=None, label_4=None,
                             color_1='k', color_2='k', color_3='k', color_4='k',
                             subplot=False):
    """
    :param title: Title of the Barchart
    :param y_values: list of y_values (e.g. all the markers),
    :param x_values: the values for the x-achsis (e.g. the different numbers of occurrences)
    :param x_label: the label for the x-Achsis
    :param label_1: label for the first dataset
    :param label_2: label for the second dataset
    :param label_3: label for the third dataset
    :param label_4: label for the fourth dataset
    :param color_1: color for the first dataset
    :param color_2: color for the second dataset
    :param color_3: color for the third dataset
    :param color_4: color for the fourth dataset
    :param subplot: indicates whether the data is to be displayed in a single plot (False, default),
                    or in different subplots(True)
    :return:
    """

    y_values = y_values
    x_values_1 = x_values[0]
    x_values_2 = None
    if len(x_values) > 1:
        x_values_2 = x_values[1]
    x_values_3 = None
    if len(x_values) > 2:
        x_values_3 = x_values[2]
    x_values_4 = None
    if len(x_values) == 4:
        x_values_4 = x_values[3]

    y_ticks = [np.arange(len(x_values_1)), y_values]

    if subplot:
        draw_horizontal_subplots(title, y_values, x_values_1, label_1,
                                 x_label=x_label,
                                 x_2=x_values_2, label_2=label_2,
                                 x_3=x_values_3, label_3=label_3,
                                 x_4=x_values_4, label_4=label_4,
                                 color_1=color_1, color_2=color_2, color_3=color_3, color_4=color_4)
    else:
        draw_horizontal_barchart(title, y_values, x_values_1, label_1,
                                 x_label=x_label, y_ticks=y_ticks,
                                 x_2=x_values_2, label_2=label_2,
                                 x_3=x_values_3, label_3=label_3,
                                 x_4=x_values_4, label_4=label_4,
                                 color_1=color_1, color_2=color_2, color_3=color_3, color_4=color_4)


# ---------- General statistical distribution of DM -----------------
def add_values(values_dict, columns, values, dataset):
    """
    adds values to a given dict and returns the extended dict
    :param values_dict: the dict with key:[list] entries to add values to
    :param columns: the keys for the dict
    :param values: the values that are to add to the respective keys
    :param dataset: the name of the dataset, functions as the row-index
    :return:
    """
    for key, value in zip(columns, values):
        values_dict[key].append(value)
    values_dict['Data'].append(dataset)
    return values_dict


def print_dataframe(values_dict, rows):
    """
    prints the values as a pandas dataframe, which is a more beautiful dict with rows (index)
    and columns
    :param values_dict: the dictionary to be printed as dataframe
    :param rows: the name of the row that should function als index (row-names)
    :return:
    """
    values_dataframe = pd.DataFrame(values_dict)
    values_dataframe.set_index(rows, inplace=True)
    print(values_dataframe)


def get_sentence_values_for_dataset(data):
    """
    Interprets the given data, which is a string formatted like a python dictionary like
    {dmCount1:sentenceCountA, dmCount2:sentenceCountB,...}
    and retrieves a list of all the dm counts.
    E.g.: If there are three sentences that contain 2 DM, then 2 is added to the list 3 times.
    :param data: the string to be interpreted
    :return: list of values of dm occurrences per sentence
    """
    values = []

    '''
    read the string and evaluate it like a pyton dict
    '''
    for doc in data:
        doc_counts = ast.literal_eval(doc)

        for dm_counter in doc_counts:
            sentence_counter = int(doc_counts[dm_counter])
            for i in range(sentence_counter):
                values.append(dm_counter)

    return values


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


def compute_y_values_statics(data_1, label_1=None, data_2=None, label_2=None, data_3=None, label_3=None, data_4=None,
                             label_4=None):
    """
    Computes the y-values for the given data when just the respective min/mean/max is needed
    :param data_1: the first set of data, either a list of values or a list of value-lists
    :param label_1: Name of the first dataset
    :param data_2: the second set of data, either a list of values or a list of value-lists
    :param label_2: Name of the second dataset
    :param data_3: the third set of data, either a list of values or a list of value-lists
    :param label_3: Name of the third dataset
    :param data_4: the fourth set of data, either a list of values or a list of value-lists
    :param label_4: Name of the fourth dataset
    :return: an array of the computed data-values in the order they where given
    """

    y_values_1 = compute_statistics(data_1)
    y_values_2 = None
    y_values_3 = None
    y_values_4 = None

    '''Prepare the Pandas Dataframe'''
    values = {}
    columns = ['Min', 'A_Mean', 'H_Mean', 'Median', 'Mode', 'Max']
    for key, value in zip(columns, y_values_1):
        values[key] = [value]
    values['Data'] = [label_1]

    if data_2 is not None:
        y_values_2 = compute_statistics(data_2)
        values = add_values(values, columns, y_values_2, label_2)

    if data_3 is not None:
        y_values_3 = compute_statistics(data_3)
        values = add_values(values, columns, y_values_3, label_3)

    if data_4 is not None:
        y_values_4 = compute_statistics(data_4)
        values = add_values(values, columns, y_values_4, label_4)

    print_dataframe(values, 'Data')

    return [y_values_1, y_values_2, y_values_3, y_values_4]


# ------------- DM per Sentence (Histogram) ----------------
def compute_dm_per_sentence(data, title, color):
    """
    Computes the number of DM per sentence and plotting a histogram with a bar for each number of DM
    :param data: dictionary with that contains the numbers of DMs as key and the number of sentences that contain the
    respective number of DM as value
    :param title: the title of the dataset
    :param color: the color of the dataset (Spotify: '#1DB954', NYTimes: '#cecece', Gigaword: '#7CACED')
    :return:
    """
    values = {}

    '''
    Scores are stored in one cell as a String, formated like a python dict
    read the string and evaluate it like a pyton dict
    '''
    for doc in data:
        doc_counts = ast.literal_eval(doc)

        for dm_counter in doc_counts:
            if dm_counter not in values:
                values[dm_counter] = int(doc_counts[dm_counter])
            else:
                values[dm_counter] += int(doc_counts[dm_counter])

    # x values are the number of dms per sentence
    x_values = []
    # y values are the number of sentences that contain as many dms.
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


# --------------- DM Positions in Sentence -----------------
def percentage(part, whole):
    return (float(part) * 100) / (float(whole))


def compute_percentages(values, data):
    """
    Computes the percentages for an array of 3 values
    :param values: the values to compute the percentage of
    :param data:
    :return: list of the three computed values
    """
    whole = sum(values)
    return [percentage(sum(data[0]), whole), percentage(sum(data[1]), whole),
            percentage(sum(data[2]), whole)]


def compute_yvalues_positions(data_1, label_1=None, data_2=None, label_2=None, data_3=None, label_3=None, data_4=None,
                              label_4=None, perc=False):
    """
    Computes the total number or percentage of DM at the beginning, middle or end of a sentence
    data_x = [dm_pos_sent_begin, dm_pos_sent_middle, dm_pos_sent_end]
    :return:
    """

    y_values_1 = [sum(data_1[0]), sum(data_1[1]), sum(data_1[2])]
    if perc:
        y_values_1 = compute_percentages(y_values_1, data_1)

    y_values_2 = None
    y_values_3 = None
    y_values_4 = None

    values = {}
    columns = ['Begin', 'Middle', 'End']
    for key, value in zip(columns, y_values_1):
        values[key] = [value]
    values['Data'] = [label_1]

    if data_2 is not None:
        y_values_2 = [sum(data_2[0]), sum(data_2[1]), sum(data_2[2])]
        if perc:
            y_values_2 = compute_percentages(y_values_2, data_2)
        values = add_values(values, columns, y_values_2, label_2)

    if data_3 is not None:
        y_values_3 = [sum(data_3[0]), sum(data_3[1]), sum(data_3[2])]
        if perc:
            y_values_3 = compute_percentages(y_values_3, data_3)
        values = add_values(values, columns, y_values_3, label_3)

    if data_4 is not None:
        y_values_4 = [sum(data_4[0]), sum(data_4[1]), sum(data_4[2])]
        if perc:
            y_values_4 = compute_percentages(y_values_4, data_4)
        values = add_values(values, columns, y_values_4, label_4)

    print_dataframe(values, 'Data')

    return [y_values_1, y_values_2, y_values_3, y_values_4]


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
    # TODO: Change so it can accept 4 datasets!
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


# ------------ Marker Häufigkeiten -------------

def get_position_values(data, flag):
    """
    Extracts the values from the dict for positions in 'flag'
    Returns a dictionary with the marker as key and the counts as value-list
    {markerA:[begin, middle, end], markerB:[...],...}
    :param data: the dictionary to extract the values from
    :param flag: 'S' for Sentence or 'D' for Document
    :return: a dictionary with the markers as key and the list of their position-values as value-list
    """
    if flag == 'S':
        begin = 'sent_begin'
        middle = 'sent_middle'
        end = 'sent_end'
    else:
        begin = 'doc_begin'
        middle = 'doc_middle'
        end = 'doc_end'

    markers = {}

    for marker in data:
        markers[marker] = [data[marker][begin], data[marker][middle], data[marker][end]]

    return markers


def list_all_markers(data1, data2=None, data3=None, data4=None):
    markers_1 = mp.DatasetMarkers(data1)
    markers = markers_1.get_markers()

    if data2 is not None:
        markers_2 = mp.DatasetMarkers(data2)
        for marker in markers_2.get_markers():
            if marker not in markers:
                markers.append(marker)

    if data3 is not None:
        markers_3 = mp.DatasetMarkers(data3)
        for marker in markers_3.get_markers():
            if marker not in markers:
                markers.append(marker)

    if data4 is not None:
        markers_4 = mp.DatasetMarkers(data4)
        for marker in markers_4.get_markers():
            if marker not in markers:
                markers.append(marker)

    return markers


def compute_marker_occurences(data1, data2=None, data3=None, data4=None):
    markers = list_all_markers(data1, data2, data3, data4)
    markers_1 = mp.DatasetMarkers(data1).get_total_values()
    y_values_1 = []

    markers_2 = []
    y_values_2 = None
    markers_3 = []
    y_values_3 = None
    markers_4 = []
    y_values_4 = None

    if data2 is not None:
        markers_2 = mp.DatasetMarkers(data2).get_total_values()
        y_values_2 = []

    if data3 is not None:
        markers_3 = DatasetMarkers(data3).get_total_values()
        y_values_3 = []

    if data4 is not None:
        markers_4 = mp.DatasetMarkers(data4).get_total_values()
        y_values_4 = []

    for marker in markers:
        if marker in markers_1:
            y_values_1.append(markers_1[marker])
        else:
            y_values_1.append(0)
        if data2 is not None:
            if marker in markers_2:
                y_values_2.append(markers_2[marker])
            else:
                y_values_2.append(0)
        if data3 is not None:
            if marker in markers_3:
                y_values_3.append(markers_3[marker])
            else:
                y_values_3.append(0)
        if data4 is not None:
            if marker in markers_4:
                y_values_4.append(markers_4[marker])
            else:
                y_values_4.append(0)

    return [markers, y_values_1, y_values_2, y_values_3, y_values_4]


def compute_marker_percentages(data1, data2=None, data3=None, data4=None):
    markers = list_all_markers(data1, data2, data3, data4)
    markers_1 = mp.DatasetMarkers(data1).get_total_percents()
    y_values_1 = []

    markers_2 = []
    y_values_2 = None
    markers_3 = []
    y_values_3 = None
    markers_4 = []
    y_values_4 = None

    if data2 is not None:
        markers_2 = mp.DatasetMarkers(data2).get_total_percents()
        y_values_2 = []

    if data3 is not None:
        markers_3 = mp.DatasetMarkers(data3).get_total_percents()
        y_values_3 = []

    if data4 is not None:
        markers_4 = mp.DatasetMarkers(data4).get_total_percents()
        y_values_4 = []

    for marker in markers:
        if marker in markers_1:
            y_values_1.append(markers_1[marker])
        else:
            y_values_1.append(0)
        if marker in markers_2:
            y_values_2.append(markers_2[marker])
        else:
            y_values_2.append(0)
        if marker in markers_3:
            y_values_3.append(markers_3[marker])
        else:
            y_values_3.append(0)
        if marker in markers_4:
            y_values_4.append(markers_4[marker])
        else:
            y_values_4.append(0)

    return [markers, y_values_1, y_values_2, y_values_3, y_values_4]


def compute_marker_statistics(data_1, data_2=None, data_3=None, data_4=None):
    pass



'''10:
Number of Occurences per Discourse Marker per Dataset
'''
marker_occurences = compute_marker_occurences(data.spotify_marker, data.ted_marker,
                                              data.ny_marker, data.gig_marker)
plot_horizontal_barchart("Discourse Marker Occurrences",
                         marker_occurences[0],
                         [marker_occurences[1], marker_occurences[2],
                             marker_occurences[3], marker_occurences[4]],
                         "Number of Occurrences",
                         label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                         color_1='#1DB954', color_2='#e62b1e', color_3='#FFA700', color_4='#227DFB')

plot_horizontal_barchart("Discourse Marker Occurrences",
                         marker_occurences[0],
                         [marker_occurences[1], marker_occurences[2],
                         marker_occurences[3], marker_occurences[4]],
                         "Number of Occurrences",
                         label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                         color_1='#1DB954', color_2='#e62b1e', color_3='#FFA700', color_4='#227DFB',
                         sub=True)