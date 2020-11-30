import pandas as pd
from helpers import DataFrames as df
from helpers.DataFrames import save_dataframe
from helpers.Statistics import compute_marker_deltas


def list_all_markers(data1, data2=None, data3=None, data4=None):
    markers = data1.get_markers()

    if data2 is not None:
        for marker in data2.get_markers():
            if marker not in markers:
                markers.append(marker)

    if data3 is not None:
        for marker in data3.get_markers():
            if marker not in markers:
                markers.append(marker)

    if data4 is not None:
        for marker in data4.get_markers():
            if marker not in markers:
                markers.append(marker)

    return markers


def create_marker_table(title, datalist, names):
    """
    Create a list of all the markers that occur in the given datasets and
    print the list with the occurrence-values as a pandas dataframe
    :param title:
    :param datalist:
    :param names:
    :return:
    """
    markers = []
    # create a list of all the markers that occur in the datasets
    for i in range(len(datalist)):
        for j in range(2):
            if j % 2 == 0:
                markers = markers + [m for m in datalist[i][j] if m not in markers]

    # then create a dictionary in form of a pandas dataframe to store the values for each marker for each dataset
    marker_frame = {}
    for marker in markers:
        marker_frame[marker] = []

        for i in range(len(datalist)):
            for j in range(2):
                if j % 2 == 1:
                    if marker in datalist[i][0]:
                        marker_index = datalist[i][0].index(marker)
                        marker_frame[marker].append(datalist[i][j][marker_index])
                    else:
                        marker_frame[marker].append(0)

    marker_frame['Data'] = names
    values_dataframe = pd.DataFrame(marker_frame)
    values_dataframe.set_index('Data', inplace=True)
    save_dataframe(title, values_dataframe.transpose())

    compute_marker_deltas(title, values_dataframe)
    return markers, marker_frame


def compile_most_common_marker_list(title, datalist, names):
    """
    Create a List of all the markers that appear in the given datasets
    and return one list with all the markers and up to five additional lists with the
    respective numbers of occurences in each dataset
    :param title:
    :param datalist:
    :param names:
    :return:
    """
    markers, marker_frame = create_marker_table(title, datalist, names)

    values1 = []
    values2 = None
    values3 = None
    values4 = None
    values5 = None

    # split up the marker_frame dict into four lists, each of which contains
    # the marker values for the specific dataset
    for marker in markers:
        values1.append(marker_frame[marker][0])
    if len(datalist) > 1:
        values2 = []
        for marker in markers:
            values2.append(marker_frame[marker][1])
    if len(datalist) > 2:
        values3 = []
        for marker in markers:
            values3.append(marker_frame[marker][2])
    if len(datalist) > 3:
        values4 = []
        for marker in markers:
            values4.append(marker_frame[marker][3])
    if len(datalist) > 4:
        values5 = []
        for marker in markers:
            values5.append(marker_frame[marker][4])

    return markers, [values1, values2, values3, values4, values5]


def most_common_markers_list(title, datalist, names, top_x=15):
    most_common_markers = []
    for data in datalist:
        for marker in data.most_common(top_x):
            if marker[0] not in most_common_markers:
                most_common_markers.append(marker[0])

    valuelists = []
    for i in range(len(datalist)):
        valuelists.append([])

    for marker in most_common_markers:
        for data, values in zip(datalist, valuelists):
            values.append(data[marker])

    df.markers_dataframe(title, names, most_common_markers, valuelists)

    return most_common_markers, valuelists

