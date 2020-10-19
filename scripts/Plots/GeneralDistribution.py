import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics
import ast


# -------- Read in data ----------
class CorpusData:
    def __init__(self, spotify_file, ted_file, ny_file, gig_file):
        self.spotify_data = pd.read_csv(spotify_file)
        self.ted_data = pd.read_csv(ted_file)
        self.ny_data = pd.read_csv(ny_file)
        self.gig_data = pd.read_csv(gig_file)


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
    """
    Draws a Piechart of the given data with a title and labels for the slices
    """
    plt.pie(slices, labels=labels, colors=colors,
            startangle=angle, autopct='%1.1f%%')

    plt.title(title)
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
    prints the values as a pandas dataframe, which is a more beautiful dict with rows (index) and columns
    :param values_dict: the dictionary to be printed as dataframe
    :param rows: the name of the row that should function als index (row-names)
    :return:
    """
    values_dataframe = pd.DataFrame(values_dict)
    values_dataframe.set_index(rows, inplace=True)
    print(values_dataframe)


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

    if isinstance(data_1, pd.core.series.Series):
        y_values_1 = [min(data_1), statistics.mean(data_1), max(data_1)]
    else:
        y_values_1 = [min(data_1[0]), statistics.mean(data_1[1]), max(data_1[2])]
    y_values_2 = None
    y_values_3 = None
    y_values_4 = None

    values = {}
    columns = ['Min', 'Mean', 'Max']
    for key, value in zip(columns, y_values_1):
        values[key] = [value]
    values['Data'] = [label_1]

    if data_2 is not None:
        if isinstance(data_2, pd.core.series.Series):
            y_values_2 = [min(data_2), statistics.mean(data_2), max(data_2)]
        else:
            y_values_2 = [min(data_2[0]), statistics.mean(data_2[1]), max(data_2[2])]
        values = add_values(values, columns, y_values_2, label_2)

    if data_3 is not None:
        if isinstance(data_3, pd.core.series.Series):
            y_values_3 = [min(data_3), statistics.mean(data_3), max(data_3)]
        else:
            y_values_3 = [min(data_3[0]), statistics.mean(data_3[1]), max(data_3[2])]
        values = add_values(values, columns, y_values_3, label_3)

    if data_4 is not None:
        if isinstance(data_4, pd.core.series.Series):
            y_values_4 = [min(data_4), statistics.mean(data_4), max(data_4)]
        else:
            y_values_4 = [min(data_4[0]), statistics.mean(data_4[1]), max(data_4[2])]
        values = add_values(values, columns, y_values_4, label_4)

    print_dataframe(values, 'Data')

    return [y_values_1, y_values_2, y_values_3, y_values_4]


# ------------- DM per Sentence (Histogram) ----------------
def compute_dm_per_sentence(data, title, color):
    """
    Computes the number of DM per sentence and plots a histogram with a bar for each number of DM
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


# ------------ MAIN -------------
def main():

    data = CorpusData("../bigData/listenability-tools/pipeline-output/spotify-scores.csv",
                      "../bigData/listenability-tools/pipeline-output/ted-scores.csv",
                      "../bigData/listenability-tools/pipeline-output/nytimes-scores.csv",
                      "../bigData/listenability-tools/pipeline-output/gigaword-scores.csv")

    '''01: 
    Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''
    plot_data_barchart("Percent Discourse Markers per Text",
                       compute_y_values_statics(data.spotify_data['dm_words_perc'].dropna(), label_1="Spotify",
                                                data_2=data.ted_data['dm_words_perc'].dropna(), label_2="TED",
                                                data_3=data.ny_data['dm_words_perc'].dropna(), label_3="NYTimes",
                                                data_4=data.gig_data['dm_words_perc'].dropna(), label_4="Gigaword"),
                       ["Min % DM", "Mean % DM", "Max % DM"],
                       "Percent Markers",
                       label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                       color_1='#1DB954', color_2='#e62b1e', color_3='#cecece', color_4='#7CACED')

    '''02:
    Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_count_doc)
    '''
    plot_data_barchart("Number of Discourse Markers per Text",
                       compute_y_values_statics(data.spotify_data['dm_count_doc'].dropna(), label_1="Spotify",
                                                data_2=data.ted_data['dm_count_doc'].dropna(), label_2="TED",
                                                data_3=data.ny_data['dm_count_doc'].dropna(), label_3="NYTimes",
                                                data_4=data.gig_data['dm_count_doc'].dropna(), label_4="Gigaword"),
                       ["Min # DM", "Mean # DM", "Max # DM"],
                       "Number Markers",
                       label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                       color_1='#1DB954', color_2='#e62b1e', color_3='#cecece', color_4='#7CACED')

    '''03: 
    Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    min/mean/max(dm_sentences_perc)
    '''
    plot_data_barchart("Percent of Sentences with DM per Text",
                       compute_y_values_statics(data.spotify_data['dm_sentences_perc'].dropna(), label_1="Spotify",
                                                data_2=data.ny_data['dm_sentences_perc'].dropna(), label_2="NYTimes",
                                                data_3=data.gig_data['dm_sentences_perc'].dropna(), label_3="Gigaword"),
                       ["Min %", "Mean %", "Max %"],
                       "% Sentences containing DM",
                       label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                       color_1='#1DB954', color_2='#cecece', color_3='#7CACED')

    '''04: 
    Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_sentences)
    '''
    plot_data_barchart("Number of Sentences with DM per Text",
                       compute_y_values_statics(data.spotify_data['dm_sentences'].dropna(), label_1="Spotify",
                                                data_2=data.ny_data['dm_sentences'].dropna(), label_2="NYTimes",
                                                data_3=data.gig_data['dm_sentences'].dropna(), label_3="Gigaword"),
                       ["Min #", "Mean #", "Max #"],
                       "# Sentences containing DM",
                       label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                       color_1='#1DB954', color_2='#cecece', color_3='#7CACED')

    '''05:
    Number of DM per sentence
    '''
    plot_data_barchart("Number of Discourse Markers per Sentence",
                       compute_y_values_statics(
                           [data.spotify_data['dm_count_min'].dropna(), data.spotify_data['dm_count_mean'].dropna(),
                            data.spotify_data['dm_count_max'].dropna()], label_1="Spotify",
                           data_2=[data.ny_data['dm_count_min'].dropna(), data.ny_data['dm_count_mean'].dropna(),
                                   data.ny_data['dm_count_max'].dropna()], label_2="NYTimes",
                           data_3=[data.gig_data['dm_count_min'].dropna(), data.gig_data['dm_count_mean'].dropna(),
                                   data.gig_data['dm_count_max'].dropna()], label_3="Gigaword"),
                       ["Min # DM", "Mean # DM", "Max # DM"],
                       "# Markers per Sentence",
                       label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                       color_1='#1DB954', color_2='#cecece', color_3='#7CACED')

    '''06:
    Histogram with Number of DM per Sentence per Dataset
    '''
    compute_dm_per_sentence(data.spotify_data['dm_count_dict'].dropna(), "Spotify", '#1DB954')
    compute_dm_per_sentence(data.ny_data['dm_count_dict'].dropna(), "New York Times", '#cecece')
    compute_dm_per_sentence(data.gig_data['dm_count_dict'].dropna(), "Gigaword", '#7CACED')

    '''07:
    Percentage of DM at certain positions in a sentence
    '''
    plot_data_barchart("% of DM in a Position in a Sentence",
                       compute_yvalues_positions(
                           [data.spotify_data['dm_pos_sent_begin'].dropna(),
                            data.spotify_data['dm_pos_sent_middle'].dropna(),
                            data.spotify_data['dm_pos_sent_end'].dropna()], label_1="Spotify",
                           data_2=[data.ny_data['dm_pos_sent_begin'].dropna(),
                                   data.ny_data['dm_pos_sent_middle'].dropna(),
                                   data.ny_data['dm_pos_sent_end'].dropna()], label_2="NYTimes",
                           data_3=[data.gig_data['dm_pos_sent_begin'].dropna(),
                                   data.gig_data['dm_pos_sent_middle'].dropna(),
                                   data.gig_data['dm_pos_sent_end'].dropna()], label_3="Gigaword",
                           perc=True
                       ),
                       ["Sent. Begin", "Sent. Middle", "Sent. End"],
                       "% DM at Postion",
                       label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                       color_1='#1DB954', color_2='#cecece', color_3='#7CACED')

    '''08:
    Number of DM at certain positions in a sentence
    '''
    plot_data_barchart("Number of DM at a certain Position in a Sentence",
                       compute_yvalues_positions(
                           [data.spotify_data['dm_pos_sent_begin'].dropna(),
                            data.spotify_data['dm_pos_sent_middle'].dropna(),
                            data.spotify_data['dm_pos_sent_end'].dropna()], label_1="Spotify",
                           data_2=[data.ny_data['dm_pos_sent_begin'].dropna(),
                                   data.ny_data['dm_pos_sent_middle'].dropna(),
                                   data.ny_data['dm_pos_sent_end'].dropna()], label_2="NYTimes",
                           data_3=[data.gig_data['dm_pos_sent_begin'].dropna(),
                                   data.gig_data['dm_pos_sent_middle'].dropna(),
                                   data.gig_data['dm_pos_sent_end'].dropna()], label_3="Gigaword"
                       ),
                       ["begin", "middle", "end"],
                       "# DM at Postion",
                       label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                       color_1='#1DB954', color_2='#cecece', color_3='#7CACED')

    '''09:
    Piechart of DM at certain positions in a sentence per Dataset
    '''
    plot_dm_positions_sent_piechart("Number of DM in a Sentence at Position:",
                                    [[data.spotify_data['dm_pos_sent_begin'].dropna(),
                                      data.spotify_data['dm_pos_sent_middle'].dropna(),
                                      data.spotify_data['dm_pos_sent_end'].dropna()],
                                     [data.ny_data['dm_pos_sent_begin'].dropna(),
                                      data.ny_data['dm_pos_sent_middle'].dropna(),
                                      data.ny_data['dm_pos_sent_end'].dropna()],
                                     [data.gig_data['dm_pos_sent_begin'].dropna(),
                                      data.gig_data['dm_pos_sent_middle'].dropna(),
                                      data.gig_data['dm_pos_sent_end'].dropna()]
                                     ],
                                    ["Spotify Data", "NYTimes Data", "Gigaword Data"],
                                    ['#1DB954', '#cecece', '#7CACED'])


if __name__ == '__main__':
    main()
