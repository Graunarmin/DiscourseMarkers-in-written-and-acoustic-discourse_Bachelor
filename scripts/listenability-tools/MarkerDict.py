import json
import pandas as pd
import ast
import statistics
import sys
from collections import Counter


class MarkerDict:

    def __init__(self, infile, outfile):
        self.in_file = infile
        self.out_file = outfile
        self.marker_occurences = {}
        self.doc_count = 0
        self.marker_count = 0

    def read_csv(self):
        csv_data = pd.read_csv(self.in_file)
        data = csv_data['dm_counts_dict']
        for doc in data:
            self.doc_count += 1
            if doc != "{}":
                dm_dict = ast.literal_eval(doc)
                for marker in dm_dict:
                    if marker not in self.marker_occurences:
                        self.marker_occurences[marker] = dm_dict[marker]
                        self.marker_count += dm_dict[marker]['total']
                        if dm_dict[marker]['total'] != 0:
                            self.marker_occurences[marker]['inverse_sum_total'] = 1 / dm_dict[marker]['total']
                        else:
                            self.marker_occurences[marker]['inverse_sum_total'] = 0
                        if dm_dict[marker]['sent_begin'] != 0:
                            self.marker_occurences[marker]['inverse_sum_sb'] = 1 / dm_dict[marker]['sent_begin']
                        else:
                            self.marker_occurences[marker]['inverse_sum_sb'] = 0
                        if dm_dict[marker]['sent_middle'] != 0:
                            self.marker_occurences[marker]['inverse_sum_sm'] = 1 / dm_dict[marker]['sent_middle']
                        else:
                            self.marker_occurences[marker]['inverse_sum_sm'] = 0
                        if dm_dict[marker]['sent_end'] != 0:
                            self.marker_occurences[marker]['inverse_sum_se'] = 1 / dm_dict[marker]['sent_end']
                        else:
                            self.marker_occurences[marker]['inverse_sum_se'] = 0
                        if dm_dict[marker]['doc_begin'] != 0:
                            self.marker_occurences[marker]['inverse_sum_db'] = 1 / dm_dict[marker]['doc_begin']
                        else:
                            self.marker_occurences[marker]['inverse_sum_db'] = 0
                        if dm_dict[marker]['doc_middle'] != 0:
                            self.marker_occurences[marker]['inverse_sum_dm'] = 1 / dm_dict[marker]['doc_middle']
                        else:
                            self.marker_occurences[marker]['inverse_sum_dm'] = 0
                        if dm_dict[marker]['doc_end'] != 0:
                            self.marker_occurences[marker]['inverse_sum_de'] = 1 / dm_dict[marker]['doc_end']
                        else:
                            self.marker_occurences[marker]['inverse_sum_de'] = 0
                        self.marker_occurences[marker]['median_total'] = [dm_dict[marker]['total']]
                        self.marker_occurences[marker]['median_sb'] = [dm_dict[marker]['sent_begin']]
                        self.marker_occurences[marker]['median_sm'] = [dm_dict[marker]['sent_middle']]
                        self.marker_occurences[marker]['median_se'] = [dm_dict[marker]['sent_end']]
                        self.marker_occurences[marker]['median_db'] = [dm_dict[marker]['doc_begin']]
                        self.marker_occurences[marker]['median_dm'] = [dm_dict[marker]['doc_middle']]
                        self.marker_occurences[marker]['median_de'] = [dm_dict[marker]['doc_end']]
                    else:
                        self.marker_count += dm_dict[marker]['total']
                        for key in dm_dict[marker]:
                            self.marker_occurences[marker][key] += dm_dict[marker][key]
                        if dm_dict[marker]['total'] != 0:
                            self.marker_occurences[marker]['inverse_sum_total'] += 1 / dm_dict[marker]['total']
                        if dm_dict[marker]['sent_begin'] != 0:
                            self.marker_occurences[marker]['inverse_sum_sb'] += 1 / dm_dict[marker]['sent_begin']
                        if dm_dict[marker]['sent_middle'] != 0:
                            self.marker_occurences[marker]['inverse_sum_sm'] += 1 / dm_dict[marker]['sent_middle']
                        if dm_dict[marker]['sent_end'] != 0:
                            self.marker_occurences[marker]['inverse_sum_se'] += 1 / dm_dict[marker]['sent_end']
                        if dm_dict[marker]['doc_begin'] != 0:
                            self.marker_occurences[marker]['inverse_sum_db'] += 1 / dm_dict[marker]['doc_begin']
                        if dm_dict[marker]['doc_middle'] != 0:
                            self.marker_occurences[marker]['inverse_sum_dm'] += 1 / dm_dict[marker]['doc_middle']
                        if dm_dict[marker]['doc_end'] != 0:
                            self.marker_occurences[marker]['inverse_sum_de'] += 1 / dm_dict[marker]['doc_end']
                        self.marker_occurences[marker]['median_total'].append(dm_dict[marker]['total'])
                        self.marker_occurences[marker]['median_sb'].append(dm_dict[marker]['sent_begin'])
                        self.marker_occurences[marker]['median_sm'].append(dm_dict[marker]['sent_middle'])
                        self.marker_occurences[marker]['median_se'].append(dm_dict[marker]['sent_end'])
                        self.marker_occurences[marker]['median_db'].append(dm_dict[marker]['doc_begin'])
                        self.marker_occurences[marker]['median_dm'].append(dm_dict[marker]['doc_middle'])
                        self.marker_occurences[marker]['median_de'].append(dm_dict[marker]['doc_end'])

        self.compute_data()

    def compute_data(self):
        csv_doc = {'marker': {}, 'stats': {}}
        for marker in self.marker_occurences:
            csv_doc['marker'][marker] = {'total': self.marker_occurences[marker]['total'],
                                         'sent_begin': self.marker_occurences[marker]['sent_begin'],
                                         'sent_middle': self.marker_occurences[marker]['sent_middle'],
                                         'sent_end': self.marker_occurences[marker]['sent_end'],
                                         'doc_begin': self.marker_occurences[marker]['doc_begin'],
                                         'doc_middle': self.marker_occurences[marker]['doc_middle'],
                                         'doc_end': self.marker_occurences[marker]['doc_end'],
                                         'inverse_sum_total': self.marker_occurences[marker]['inverse_sum_total'],
                                         'inverse_sum_sb': self.marker_occurences[marker]['inverse_sum_sb'],
                                         'inverse_sum_sm': self.marker_occurences[marker]['inverse_sum_sm'],
                                         'inverse_sum_se': self.marker_occurences[marker]['inverse_sum_se'],
                                         'inverse_sum_db': self.marker_occurences[marker]['inverse_sum_db'],
                                         'inverse_sum_dm': self.marker_occurences[marker]['inverse_sum_dm'],
                                         'inverse_sum_de': self.marker_occurences[marker]['inverse_sum_de'],
                                         'median_total': statistics.median(
                                             self.marker_occurences[marker]['median_total']),
                                         'median_sb': statistics.median(self.marker_occurences[marker]['median_sb']),
                                         'median_sm': statistics.median(self.marker_occurences[marker]['median_sm']),
                                         'median_se': statistics.median(self.marker_occurences[marker]['median_se']),
                                         'median_db': statistics.median(self.marker_occurences[marker]['median_db']),
                                         'median_dm': statistics.median(self.marker_occurences[marker]['median_dm']),
                                         'median_de': statistics.median(self.marker_occurences[marker]['median_de']),
                                         'mode_total': Counter(
                                             self.marker_occurences[marker]['median_total']).most_common(1),
                                         'mode_sb': Counter(self.marker_occurences[marker]['median_sb']).most_common(1),
                                         'mode_sm': Counter(self.marker_occurences[marker]['median_sm']).most_common(1),
                                         'mode_se': Counter(self.marker_occurences[marker]['median_se']).most_common(1),
                                         'mode_db': Counter(self.marker_occurences[marker]['median_db']).most_common(1),
                                         'mode_dm': Counter(self.marker_occurences[marker]['median_dm']).most_common(1),
                                         'mode_de': Counter(self.marker_occurences[marker]['median_de']).most_common(1)
                                         }
        csv_doc['stats']['total_docs'] = self.doc_count
        csv_doc['stats']['total_markers'] = self.marker_count
        csv_doc['stats']['different_markers'] = len(self.marker_occurences)
        csv_doc['stats']['total_sb'] = sum([self.marker_occurences[marker]['sent_begin'] for marker in self.marker_occurences])
        csv_doc['stats']['total_sm'] = sum([self.marker_occurences[marker]['sent_middle'] for marker in self.marker_occurences])
        csv_doc['stats']['total_se'] = sum([self.marker_occurences[marker]['sent_end'] for marker in self.marker_occurences])
        csv_doc['stats']['total_db'] = sum([self.marker_occurences[marker]['doc_begin'] for marker in self.marker_occurences])
        csv_doc['stats']['total_dm'] = sum([self.marker_occurences[marker]['doc_middle'] for marker in self.marker_occurences])
        csv_doc['stats']['total_de'] = sum([self.marker_occurences[marker]['doc_end'] for marker in self.marker_occurences])

        self.write_json(csv_doc)

    def write_json(self, data):
        with open(self.out_file, 'w') as out:
            json.dump(data, out, indent=2)


# --------- MAIN -----------
def main():
    """
    Argument 1: data file, here xy-scores.csv
    Argument 2: target out file, here xy-dict.json
    """
    # marker_dict = MarkerDict(sys.argv[1], sys.argv[2])
    marker_dict = MarkerDict("../../data/Spotify/discourse-types/cooperative-monolog-shows.csv",
                             "../../data/Spotify/discourse-types/cooperative-monolog-shows_dict.json")
    marker_dict.read_csv()


if __name__ == '__main__':
    main()
