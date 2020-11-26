import json
import pandas as pd
import ast
import statistics
import sys
from collections import Counter


def read_csv(in_file, out_file):

    csv_data = pd.read_csv(in_file)
    data = csv_data['dm_counts_dict']
    names = csv_data['document']

    marker_frame = {'document': names,
                    'dm_counts_dict': []}
    for doc in data:
        marker_occurences = {}
        if doc != "{}":
            dm_dict = ast.literal_eval(doc)
            for marker in dm_dict:
                marker_occurences[marker] = int(dm_dict[marker]['sent_begin']) + int(dm_dict[marker]['sent_middle']) + int(dm_dict[marker]['sent_end'])

        marker_frame['dm_counts_dict'].append(str(marker_occurences))

    values_dataframe = pd.DataFrame(marker_frame)
    values_dataframe.set_index('document', inplace=True)
    values_dataframe.to_csv(out_file)


def main():
    read_csv(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()