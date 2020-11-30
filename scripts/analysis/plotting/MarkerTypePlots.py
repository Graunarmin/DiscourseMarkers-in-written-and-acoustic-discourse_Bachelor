import matplotlib.pyplot as plt
import numpy as np


def increase_row_column(row, column, max_columns):
    column += 1
    if column == max_columns:
        column = 0
        row += 1
    return row, column


def draw_barchart_subplots(figuretitle, titles, xlabels, data, colors, rows=2):
    """
    :param rows:
    :param figuretitle: Title of the whole figure
    :param titles: the titles for the subplots, i.e. the names of the marker-types
    :param xlabels: the labels for the x-axis, i.e. the names of the text-categories
    :param data: the averages for each text/marker-type
    :param colors: the color for each text-category
    :return: /
    """

    plt.style.use('fivethirtyeight')
    width = 0.5
    fig, axes = plt.subplots(ncols=2, nrows=rows, sharex=True, sharey=True)

    row, column = 0, 0
    x_indexes = np.arange(len(xlabels))
    for markertype in range(len(data)):
        for textcategory in range(len(data[markertype])):
            axes[row][column].bar(x_indexes[textcategory], data[markertype][textcategory],
                                  width=width, color=colors[textcategory])
            axes[row][column].set_title(titles[markertype])
            for tick in axes[row][column].get_xticklabels():
                tick.set_rotation(15)
                tick.set_size(12)

        row, column = increase_row_column(row, column, 2)

    # in case there is an odd number of plots:
    if len(data) % 2 != 0:
        # move the labels of the last (empty) plot to the one above it, so that the ticks don' show, only the labels
        axes[row - 1][column].xaxis.set_tick_params(labelbottom=True, rotation=15, labelsize=12, width=0)
        # and then delete the last (empty) plot
        fig.delaxes(axes[row][column])

    plt.xticks(ticks=x_indexes, labels=xlabels)
    fig.suptitle(figuretitle)
    plt.tight_layout()
    plt.show()


def draw_barchart(data, title, xlabels, colors, ylabel):
    plt.style.use('fivethirtyeight')
    width = 0.5

    x_indexes = np.arange(len(data))

    for markertype in range(len(data)):
        plt.bar(x_indexes[markertype], data[markertype], width=width, color=colors[markertype])

    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks(ticks=x_indexes, labels=xlabels)
    plt.tight_layout()
    plt.show()


def compute_bar_offset(width, number_of_data):
    if number_of_data == 1:
        return [0]
    elif number_of_data == 2:
        return [(-width / 4) * 3, (width / 4) * 3]
    elif number_of_data == 3:
        return [(-width / 4) * 6, 0, (width / 4) * 6]
    elif number_of_data == 4:
        return [(-width / 4) * 9, (-width / 4) * 3, (width / 4) * 3, (width / 4) * 9]
    elif number_of_data == 5:
        return [(-width / 4) * 12, (-width / 4) * 6, 0, (width / 4) * 6, (width / 4) * 12]


def horizontal_barchart(title, data, ylabels, colors, datalabels, xlabel):
    plt.style.use('fivethirtyeight')
    width = 0.1

    y_indexes = np.arange(len(data[0]))
    offsets = compute_bar_offset(width, len(data))

    for values, offset, color, label in zip(data, offsets, colors, datalabels):
        plt.barh(y_indexes + offset, values, height=width, color=color, label=label)

    plt.xlabel(xlabel)
    plt.yticks(ticks=y_indexes, labels=ylabels)

    plt.title(title)
    plt.legend()

    plt.tight_layout()
    plt.show()




