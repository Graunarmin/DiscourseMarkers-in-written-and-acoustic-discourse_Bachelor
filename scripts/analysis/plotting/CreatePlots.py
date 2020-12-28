import matplotlib.pyplot as plt
import numpy as np


def plot_ecdf(data, title, xlabel, ylabel, datalabels, colors):
    plt.style.use('fivethirtyeight')
    for dataset, color, label in zip(data, colors, datalabels):
        xaxis = np.sort(dataset)
        yaxis = np.arange(1, len(dataset)+1)/len(dataset) * 100
        plt.plot(xaxis, yaxis, linestyle='none', marker='.', color=color, label=label)
    plt.title(title),
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.margins(0.02)
    plt.tight_layout()
    plt.show()


def plot_edf(title, xlabel, ylabel, datasets, labels, colors):
    plt.style.use('fivethirtyeight')

    for data, label, color in zip(datasets, labels, colors):
        plt.plot(data[0], data[1], color=color, label=label)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.legend()

    plt.margins(0.02)
    plt.tight_layout()
    plt.show()


def draw_simple_barchart(figuretitle, titles, data, colors):
    """
    Creates subplots, each a simple barchart for one set of y values over x values in the specified color
    :param figuretitle:
    :param titles: list of titles
    :param data: list of [[xvalues1, yvalues1],[xvalues2, yvalues2], ...] for each dataset
    :param colors: list of colors
    :return:
    """
    plt.style.use('fivethirtyeight')

    fig, axes = plt.subplots(ncols=2, nrows=2, sharex=True, sharey=True)
    row = 0
    column = 0
    for i in range(len(data)):
        axes[row][column].bar(data[i][0], data[i][1], color=colors[i])
        axes[row][column].set_title(titles[i])

        if i % 2 == 0:
            axes[row][column].set_ylabel("% of all Sentences")

        column += 1
        if column == 2:
            column = 0
            row += 1

    fig.suptitle(figuretitle)
    plt.tight_layout()
    plt.show()


def draw_one_row_simple_barchart(figuretitle, titles, data, colors):
    """
    Creates subplots, each a simple barchart for one set of y values over x values in the specified color
    :param figuretitle:
    :param titles: list of titles
    :param data: list of [[xvalues1, yvalues1],[xvalues2, yvalues2], ...] for each dataset
    :param colors: list of colors
    :return:
    """
    plt.style.use('fivethirtyeight')

    fig, axes = plt.subplots(ncols=2, nrows=1, sharex=True, sharey=True)
    axes[0][0].bar(data[0][0], data[0][1], color=colors[0])
    axes[0][0].set_title(titles[0])
    axes[0][0].set_ylabel("% of all Sentences")

    axes[0][1].bar(data[1][0], data[1][1], color=colors[1])
    axes[0][1].set_title(titles[1])

    fig.suptitle(figuretitle)
    plt.tight_layout()
    plt.show()


def draw_barchart(title, x, y_1, y_1_label,
                  y_2=None, y_2_label=None, y_3=None, y_3_label=None, y_4=None, y_4_label=None,
                  y_5=None, y_5_label=None,
                  color_1='k', color_2='k', color_3='k', color_4='k', color_5='k',
                  x_label=None, y_label=None, x_ticks=None, y_ticks=None):
    """
    Draws a Barchart of the given Data
    :param color_5:
    :param y_5_label:
    :param y_5:
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
    width = 0.1

    '''For two sets of data we need to set the bars a bit appart, otherwise they would overlap'''
    x_indexes = x_ticks[0]

    if not y_2 and not y_3 and not y_4 and not y_5:
        plt.bar(x, y_1, color=color_1)

    elif y_2 and not y_3 and not y_4 and not y_5:
        plt.bar(x_indexes - (width / 4) * 3, y_1, width=width, color=color_1, label=y_1_label)
        plt.bar(x_indexes + (width / 4) * 3, y_2, width=width, color=color_2, label=y_2_label)

    elif not y_4 and not y_5:
        plt.bar(x_indexes - (width / 4) * 6, y_1, width=width, color=color_1, label=y_1_label)
        plt.bar(x_indexes, y_2, width=width, color=color_2, label=y_2_label)
        plt.bar(x_indexes + (width / 4) * 6, y_3, width=width, color=color_3, label=y_3_label)

    elif not y_5:
        plt.bar(x_indexes - (width / 4) * 9, y_1, width=width, color=color_1, label=y_1_label)
        plt.bar(x_indexes - (width / 4) * 3, y_2, width=width, color=color_2, label=y_2_label)
        plt.bar(x_indexes + (width / 4) * 3, y_3, width=width, color=color_3, label=y_3_label)
        plt.bar(x_indexes + (width / 4) * 9, y_4, width=width, color=color_4, label=y_4_label)

    else:
        plt.bar(x_indexes - (width / 4) * 12, y_1, width=width, color=color_1, label=y_1_label)
        plt.bar(x_indexes - (width / 4) * 6, y_2, width=width, color=color_2, label=y_2_label)
        plt.bar(x_indexes, y_3, width=width, color=color_3, label=y_3_label)
        plt.bar(x_indexes + (width / 4) * 6, y_4, width=width, color=color_4, label=y_4_label)
        plt.bar(x_indexes + (width / 4) * 12, y_5, width=width, color=color_5, label=y_5_label)

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


def draw_piecharts(figuretitle, titles, slices, labels, colors, angle):
    """
    Draws a Piechart of the given data with a title and labels for the slices
    """

    fig, axes = plt.subplots(ncols=2, nrows=2, sharey=True)
    row = 0
    column = 0
    for i in range(len(titles)):
        axes[row][column].pie(slices[i], labels=labels, colors=colors[i],
                              startangle=angle, autopct='%1.1f%%')
        axes[row][column].set_title(titles[i])

        column += 1
        if column == 2:
            column = 0
            row += 1

    fig.suptitle(figuretitle)

    plt.tight_layout()
    plt.show()


def draw_horizontal_barchart(title, y_data, x_1, label_1, x_label, y_ticks, x_2=None, label_2=None,
                             x_3=None, label_3=None, x_4=None, label_4=None, x_5=None, label_5=None,
                             color_1='k', color_2='k', color_3='k', color_4='k', color_5='k'):
    """
    analysis a horizontal barchart
    :param color_5:
    :param label_5:
    :param x_5:
    :param y_ticks:
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
    width = 0.1

    y_indexes = y_ticks[0]

    if not x_2 and not x_3 and not x_4 and not x_5:
        plt.barh(y_data, x_1, height=width, color=color_1, label=label_1)

    elif not x_3 and not x_4 and not x_5:
        plt.barh(y_indexes - (width / 4) * 3, x_1, height=width, color=color_1, label=label_1)
        plt.barh(y_indexes + (width / 4) * 3, x_2, height=width, color=color_2, label=label_2)

    elif not x_4 and not x_5:
        plt.barh(y_indexes - (width / 4) * 6, x_1, height=width, color=color_1, label=label_1)
        plt.barh(y_indexes, x_2, height=width, color=color_2, label=label_2)
        plt.barh(y_indexes + (width / 4) * 6, x_3, height=width, color=color_3, label=label_3)

    elif not x_5:
        plt.barh(y_indexes - (width / 4) * 9, x_1, height=width, color=color_1, label=label_1)
        plt.barh(y_indexes - (width / 4) * 3, x_2, height=width, color=color_2, label=label_2)
        plt.barh(y_indexes + (width / 4) * 3, x_3, height=width, color=color_3, label=label_3)
        plt.barh(y_indexes + (width / 4) * 9, x_4, height=width, color=color_4, label=label_4)

    else:
        plt.barh(y_indexes - (width / 4) * 12, x_1, height=width, color=color_1, label=label_1)
        plt.barh(y_indexes - (width / 4) * 6, x_2, height=width, color=color_2, label=label_2)
        plt.barh(y_indexes, x_3, height=width, color=color_3, label=label_3)
        plt.barh(y_indexes + (width / 4) * 6, x_4, height=width, color=color_4, label=label_4)
        plt.barh(y_indexes + (width / 4) * 12, x_5, height=width, color=color_5, label=label_5)

    plt.title(title)

    plt.xlabel(x_label)
    plt.yticks(ticks=y_ticks[0], labels=y_ticks[1])

    plt.legend()

    plt.tight_layout()
    plt.show()


def draw_horizontal_subplots(title, y_data,
                             x_1, label_1, x_label, x_2=None, label_2=None, x_3=None, label_3=None,
                             x_4=None, label_4=None, x_5=None, label_5=None,
                             color_1='k', color_2='k', color_3='k', color_4='k', color_5='k'):
    plt.style.use('fivethirtyeight')
    width = 0.15

    if not x_2 and not x_3 and not x_4 and not x_5:
        fig, ax = plt.subplots()
        ax.barh(y_data, x_1, height=width, color=color_1, label=label_1)

        # ax.legend()
        ax.set_title(label_1)
        ax.set_xlabel(x_label)

    elif not x_3 and not x_4 and not x_5:
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True)
        ax1.barh(y_data, x_1, height=width, color=color_1, label=label_1)
        ax2.barh(y_data, x_2, height=width, color=color_2, label=label_2)

        # ax1.legend()
        ax1.set_title(label_1)
        ax1.set_xlabel(x_label)

        # ax2.legend()
        ax2.set_title(label_2)
        ax2.set_xlabel(x_label)

    elif not x_4 and not x_5:
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharey=True)
        ax1.barh(y_data, x_1, height=width, color=color_1, label=label_1)
        ax2.barh(y_data, x_2, height=width, color=color_2, label=label_2)
        ax3.barh(y_data, x_3, height=width, color=color_3, label=label_3)

        # ax1.legend()
        ax1.set_title(label_1)

        # ax2.legend()
        ax2.set_title(label_2)
        ax2.set_xlabel(x_label)

        # ax3.legend()
        ax3.set_title(label_3)
        ax3.set_xlabel(x_label)

    elif not x_5:
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharey=True, sharex=True)
        ax1.barh(y_data, x_1, height=width, color=color_1, label=label_1)
        ax2.barh(y_data, x_2, height=width, color=color_2, label=label_2)
        ax3.barh(y_data, x_3, height=width, color=color_3, label=label_3)
        ax4.barh(y_data, x_4, height=width, color=color_4, label=label_4)

        # ax1.legend()
        ax1.set_title(label_1)

        # ax2.legend()
        ax2.set_title(label_2)

        # ax3.legend()
        ax3.set_title(label_3)
        ax3.set_xlabel(x_label)

        # ax4.legend()
        ax4.set_title(label_4)
        ax4.set_xlabel(x_label)

    else:
        fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3, sharey=True, sharex=True)
        ax1.barh(y_data, x_1, height=width, color=color_1, label=label_1)
        ax2.barh(y_data, x_2, height=width, color=color_2, label=label_2)
        ax3.barh(y_data, x_3, height=width, color=color_3, label=label_3)
        ax4.barh(y_data, x_4, height=width, color=color_4, label=label_4)
        ax5.barh(y_data, x_5, height=width, color=color_5, label=label_5)

        # ax1.legend()
        ax1.set_title(label_1)

        # ax2.legend()
        ax2.set_title(label_2)

        # ax3.legend()
        ax3.set_title(label_3)

        # ax4.legend()
        ax4.set_title(label_4)
        ax4.set_xlabel(x_label)

        ax5.set_title(label_5)
        ax5.set_xlabel(x_label)

    fig.suptitle(title)

    plt.tight_layout()
    plt.show()


# ------------ PROCESS DATA ----------
def plot_vertical_barchart(title, y_values, x_labels, y_label,
                           label_1, label_2=None, label_3=None, label_4=None, label_5=None,
                           color_1='k', color_2='k', color_3='k', color_4='k', color_5='k'):
    """
    Prepare the Data for plotting
    :param label_5:
    :param color_5:
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
    y_values_2 = None
    if len(y_values) > 1:
        y_values_2 = y_values[1]
    y_values_3 = None
    if len(y_values) > 2:
        y_values_3 = y_values[2]
    y_values_4 = None
    if len(y_values) > 3:
        y_values_4 = y_values[3]
    y_values_5 = None
    if len(y_values) == 5:
        y_values_5 = y_values[4]

    x_values = np.arange(len(y_values_1))

    draw_barchart(title, x_values,
                  y_values_1, label_1, y_values_2, y_2_label=label_2,
                  y_label=y_label, x_ticks=[x_values, x_labels],
                  y_3=y_values_3, y_3_label=label_3, y_4=y_values_4, y_4_label=label_4,
                  y_5=y_values_5, y_5_label=label_5,
                  color_1=color_1, color_2=color_2, color_3=color_3, color_4=color_4, color_5=color_5)


def plot_horizontal_barchart(title, y_values, x_values, x_label,
                             label_1, label_2=None, label_3=None, label_4=None, label_5=None,
                             color_1='k', color_2='k', color_3='k', color_4='k', color_5=None,
                             subplot=False):
    """
    :param color_5:
    :param label_5:
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
    if len(x_values) > 3:
        x_values_4 = x_values[3]
    x_values_5 = None
    if len(x_values) == 5:
        x_values_5 = x_values[4]

    y_ticks = [np.arange(len(x_values_1)), y_values]

    if subplot:
        draw_horizontal_subplots(title, y_values, x_values_1, label_1,
                                 x_label=x_label,
                                 x_2=x_values_2, label_2=label_2,
                                 x_3=x_values_3, label_3=label_3,
                                 x_4=x_values_4, label_4=label_4,
                                 x_5=x_values_5, label_5=label_5,
                                 color_1=color_1, color_2=color_2, color_3=color_3,
                                 color_4=color_4, color_5=color_5)
    else:
        draw_horizontal_barchart(title, y_values, x_values_1, label_1,
                                 x_label=x_label, y_ticks=y_ticks,
                                 x_2=x_values_2, label_2=label_2,
                                 x_3=x_values_3, label_3=label_3,
                                 x_4=x_values_4, label_4=label_4,
                                 x_5=x_values_5, label_5=label_5,
                                 color_1=color_1, color_2=color_2, color_3=color_3,
                                 color_4=color_4, color_5=color_5)


def plot_dm_position_piechart(title, data, labels, colors):
    """
    Prepares the Data for Piecharts:
    One for each Dataset with slices=[counter_begin, counter_middle, counder_end]
    and one for each Position (Begin, Middle, End) with slices for each dataset
    :param: data: array that contains the datasets
    :param: labels: array of labels for the datasets
    :param: colors: array of colors for the datasets
    :return:
    """

    set_labels = ["begin", "middle", "end"]
    begin_slices = []
    middle_slices = []
    end_slices = []
    titles = []
    slices = []
    for dataset, label in zip(data, labels):
        begin_slices.append(sum(dataset[0]))
        middle_slices.append(sum(dataset[1]))
        end_slices.append(sum(dataset[2]))
        slices.append([sum(dataset[0]), sum(dataset[1]), sum(dataset[2])])
        titles.append(label)

    draw_piecharts(title, titles, slices, set_labels, colors, 0)
