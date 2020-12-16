import json
import pandas as pd
from numpy import nan as Nan


def create_marker_table(markerdict):
    with open(markerdict, 'r', encoding='utf-8') as data:
        marker_data = json.load(data)

    senses = {}
    for marker in marker_data:
        if marker_data[marker]['main_sense'] not in senses:
            senses[marker_data[marker]['main_sense']] = []

        error_rate = str(round(float(marker_data[marker]['error_rate']), 2))
        m_string = marker + " (" + error_rate + "%)"
        senses[marker_data[marker]['main_sense']].append(m_string)

    for sense in senses:
        senses[sense].sort()

    pad_dict_list(senses, Nan)

    marker_frame = pd.DataFrame(senses)
    marker_frame.to_csv("../../data/listenability-tools/main-senses/marker-table_er.csv")


def pad_dict_list(dict_list, list_padding):
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        list_length = len(dict_list[lname])
        if list_length < lmax:
            dict_list[lname] += [list_padding] * (lmax - list_length)
    return dict_list


def create_small_marker_table(markerdict):
    with open(markerdict, 'r', encoding='utf-8') as data:
        marker_data = json.load(data)

    senses = {}
    for marker in marker_data:
        if marker_data[marker]['main_sense'] not in senses:
            senses[marker_data[marker]['main_sense']] = [""]

        senses[marker_data[marker]['main_sense']][0] += marker + ", "

    marker_frame = pd.DataFrame(senses)
    marker_frame.to_csv("../../data/listenability-tools/main-senses/marker-table_small.csv")


def main():
    create_marker_table("../../data/listenability-tools/main-senses/words_main-sense.json")


if __name__ == '__main__':
    main()
