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


def most_common_markers_plot(figuretitle, xlabel,
                             data1, label1, color1,
                             data2=None, label2=None, color2=None,
                             data3=None, label3=None, color3=None,
                             data4=None, label4=None, color4=None,
                             data5=None, label5=None, color5=None,
                             share=False):

    plt.style.use('fivethirtyeight')
    width = 0.5
    plt.rc('ytick', labelsize=10)
    plt.rc('xtick', labelsize=9)

    if not data2 and not data3 and not data4 and not data5:
        fig, ax = plt.subplots()
        ax.barh(data1[0], data1[1], height=width, color=color1, label=label1)

        ax.legend()
        ax.set_title(label1)
        ax.set_xlabel(xlabel)

    elif not data3 and not data4 and not data5:
        if share:
            fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=1, sharex=True)
        else:
            fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=1)
        ax1.barh(data1[0], data1[1], height=width, color=color1, label=label1)
        ax2.barh(data2[0], data2[1], height=width, color=color2, label=label2)

        ax1.set_title(label1)
        ax1.set_xlabel(xlabel)

        ax2.set_title(label2)
        ax2.set_xlabel(xlabel)

    elif not data4 and not data5:
        if share:
            fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, sharex=True)
        else:
            fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
        ax1.barh(data1[0], data1[1], height=width, color=color1, label=label1)
        ax2.barh(data2[0], data2[1], height=width, color=color2, label=label2)
        ax3.barh(data3[0], data3[1], height=width, color=color3, label=label3)

        ax1.set_title(label1)

        ax2.set_title(label2)
        ax2.set_xlabel(xlabel)

        ax3.set_title(label3)

    elif not data5:
        if share:
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharex=True)
        else:
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
        ax1.barh(data1[0], data1[1], height=width, color=color1, label=label1)
        ax2.barh(data2[0], data2[1], height=width, color=color2, label=label2)
        ax3.barh(data3[0], data3[1], height=width, color=color3, label=label3)
        ax4.barh(data4[0], data4[1], height=width, color=color4, label=label4)

        ax1.set_title(label1)

        ax2.set_title(label2)

        ax3.set_title(label3)
        ax3.set_xlabel(xlabel)

        ax4.set_title(label4)
        ax4.set_xlabel(xlabel)

    else:
        if share:
            fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3, sharex=True)
        else:
            fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3)
        ax1.barh(data1[0], data1[1], height=width, color=color1, label=label1)
        ax2.barh(data2[0], data2[1], height=width, color=color2, label=label2)
        ax3.barh(data3[0], data3[1], height=width, color=color3, label=label3)
        ax4.barh(data4[0], data4[1], height=width, color=color4, label=label4)
        ax5.barh(data5[0], data5[1], height=width, color=color5, label=label5)

        ax1.set_title(label1)

        ax2.set_title(label2)

        ax3.set_title(label3)

        ax4.set_title(label4)

        ax5.set_title(label5)
        ax5.set_xlabel(xlabel)

    fig.suptitle(figuretitle)

    plt.tight_layout()
    plt.show()


# --------- MAIN -----------
def main():
    pass


if __name__ == '__main__':
    main()
