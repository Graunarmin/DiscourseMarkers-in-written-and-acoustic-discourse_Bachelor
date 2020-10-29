import matplotlib.pyplot as plt
import numpy as np
import Helpers as hp


def draw_marker_subplots(figuretitle, start, markerlist, dataset1, dataset2, dataset3, dataset4,
                         label1, label2, label3, label4,
                         color1, color2, color3, color4,
                         x_ticks):
    """
    Plots a figure with 12 subplots, one for each marker in each dataset
    """
    plt.style.use('fivethirtyeight')
    y_indexes = x_ticks[0]

    width = 0.15

    fig, axes = plt.subplots(ncols=4, nrows=3, sharey=True)

    row = 0
    column = 0
    for i in range(start, start + 12):
        if i < len(markerlist):
            axes[row][column].bar(y_indexes - (width / 4) * 9, dataset1[i], width=width, color=color1, label=label1)
            axes[row][column].bar(y_indexes - (width / 4) * 3, dataset2[i], width=width, color=color2, label=label2)
            axes[row][column].bar(y_indexes + (width / 4) * 3, dataset3[i], width=width, color=color3, label=label3)
            axes[row][column].bar(y_indexes + (width / 4) * 9, dataset4[i], width=width, color=color4, label=label4)

            axes[row][column].set_title(markerlist[i])
            axes[row][column].set_xticks(x_ticks[0])
            axes[row][column].set_xticklabels(x_ticks[1])
            # axes1[row][column].legend()

            column += 1
            if column == 4:
                column = 0
                row += 1
        else:
            break

    fig.suptitle(figuretitle)
    plt.tight_layout()
    plt.show()


def plot_marker_subplots(title, markerlist, y_values, x_labels,
                         label1, label2, label3, label4,
                         color1, color2, color3, color4):
    """
    Processes the data and calls the plot function (12 times, as there are 142 markers
    and only 12 fit in one figure)
    """
    y_values_1 = y_values[0]
    y_values_2 = y_values[1]
    y_values_3 = y_values[2]
    y_values_4 = y_values[3]

    x_values = np.arange(len(y_values_1[0]))

    for i in range(0, 144, 12):
        draw_marker_subplots(title, i, markerlist, y_values_1, y_values_2, y_values_3, y_values_4,
                             label1, label2, label3, label4,
                             color1, color2, color3, color4,
                             [x_values, x_labels])


def prepare_marker_subplots(data1, data2, data3, data4):
    """
    Creates list containing all the values for the respective dataset matching up
    with the created list of markers
    :param data1: first dataset
    :param data2: second dataset
    :param data3: third dataset
    :param data4: fourth dataset
    :return: the list of markers and a list of lists of the dataset values
    """
    markers = hp.list_all_markers(data1, data2, data3, data4)
    y_values_1 = []
    y_values_2 = []
    y_values_3 = []
    y_values_4 = []

    for marker in markers:
        y_values_1.append(data1.get_all_marker_values(marker))
        y_values_2.append(data2.get_all_marker_values(marker))
        y_values_3.append(data3.get_all_marker_values(marker))
        y_values_4.append(data4.get_all_marker_values(marker))

    return markers, [y_values_1, y_values_2, y_values_3, y_values_4]


# --------- MAIN -----------
def main():
    pass


if __name__ == '__main__':
    main()
