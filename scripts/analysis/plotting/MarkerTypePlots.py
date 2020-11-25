import matplotlib.pyplot as plt
import numpy as np


def increase_row_column(row, column, max_columns):
    column += 1
    if column == max_columns:
        column = 0
        row += 1
    return row, column


def draw_barchart_subplots(figuretitle, titles, xlabels, data, colors):
    """
    :param figuretitle: Title of the whole figure
    :param titles: the titles for the subplots, i.e. the names of the marker-types
    :param xlabels: the labels for the x-axis, i.e. the names of the text-categories
    :param data: the averages for each text/marker-type
    :param colors: the color for each text-category
    :return: /
    """

    plt.style.use('fivethirtyeight')

    fig, axes = plt.subplots(ncols=2, nrows=2, sharex=True, sharey=True)

    row, column = 0, 0
    for markertype in range(len(data)):
        x_values = np.arange(len(xlabels))
        for textcategory in range(len(data[markertype])):
            axes[row][column].bar(x_values, data[markertype][textcategory], color=colors[textcategory])
            axes[row][column].set_title(titles[textcategory])

        row, column = increase_row_column(row, column, 2)

    fig.suptitle(figuretitle)
    plt.tight_layout()
    plt.show()
