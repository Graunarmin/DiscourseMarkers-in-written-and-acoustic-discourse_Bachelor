import pandas as pd
from tabulate import tabulate


def save_dataframe(title, data):
    data.to_csv("../../data/listenability-tools/tables/" + title + ".csv")


def print_dataframe(title, data):
    pd.set_option('display.max_columns', 25)
    pd.options.display.width = None
    pdtabulate = lambda df: tabulate(df, headers='keys', tablefmt='psql')

    print("\n" * 1)
    print(title)
    print(pdtabulate(data))


def add_value_to_dataframe(names, frame_dict, columns, label, data):
    names.append(label)
    for column, value in zip(columns, data):
        frame_dict[column].append(value)

    return names, frame_dict


def create_dataframe(title, columns, data1, data2=None, data3=None, data4=None, data5=None,
                     label1=None, label2=None, label3=None, label4=None, label5=None):
    frame_dict = {}
    names = []
    for column in columns:
        frame_dict[column] = []

    names, frame_dict = add_value_to_dataframe(names, frame_dict, columns, label1, data1)

    if data2:
        names, frame_dict = add_value_to_dataframe(names, frame_dict, columns, label2, data2)

    if data3:
        names, frame_dict = add_value_to_dataframe(names, frame_dict, columns, label3, data3)

    if data4:
        names, frame_dict = add_value_to_dataframe(names, frame_dict, columns, label4, data4)

    if data5:
        names, frame_dict = add_value_to_dataframe(names, frame_dict, columns, label5, data5)

    frame_dict['names'] = names

    values_dataframe = pd.DataFrame(frame_dict)
    values_dataframe.set_index('names', inplace=True)
    save_dataframe(title, values_dataframe)


def markertype_dataframe(title, columns, datasets, labels):
    """
    Create a dataframe for the markertypes plots
    :param title:
    :param columns:
    :param datasets:
    :param labels:
    :return:
    """
    frame_dict = {}
    for column, data in zip(columns, datasets):
        frame_dict[column] = data

    frame_dict['Data'] = labels

    values_dataframe = pd.DataFrame(frame_dict)
    values_dataframe.set_index('Data', inplace=True)
    save_dataframe(title, values_dataframe)


def markers_dataframe(title, names, marker, values):
    frame_dict = {}

    for name, data in zip(names, values):
        frame_dict[name] = data

    frame_dict['Marker'] = marker

    values_dataframe = pd.DataFrame(frame_dict)
    values_dataframe.set_index('Marker', inplace=True)
    save_dataframe(title, values_dataframe)

    from helpers import Statistics
    Statistics.compute_marker_deltas(title, values_dataframe)

    # percentage = lambda x: round(x * 100, 2)
    #
    # deltas = values_dataframe.pct_change(axis='columns').applymap(percentage)
    # save_dataframe(title + "_deltas", deltas)




