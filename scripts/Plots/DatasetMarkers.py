import json


class DatasetMarkers:

    def __init__(self, file):
        with open(file, 'r', encoding='utf-8') as data_json:
            dictionary = json.load(data_json)

        self.total_docs = dictionary['stats']['total_docs']
        self.total_markers = dictionary['stats']['total_markers']
        self.different_markers = dictionary['stats']['different_markers']
        self.total_sb = dictionary['stats']['total_sb']
        self.total_sm = dictionary['stats']['total_sm']
        self.total_se = dictionary['stats']['total_se']
        self.total_db = dictionary['stats']['total_db']
        self.total_dm = dictionary['stats']['total_dm']
        self.total_de = dictionary['stats']['total_de']
        self.marker_dict = dictionary['marker']

        del dictionary

    def get_total_marker_values(self):
        """
        Creates a dictionary with the markers as keys and their total number of occurrence in this dataset as value
        :return:
        """
        markers = {}
        for marker in self.marker_dict:
            markers[marker] = self.marker_dict[marker]['total']

        return markers

    def get_total_marker_percents(self):
        """
        Creates a dictionary with the markers as keys
        and their percentage-share in all the markers in this dataset as value
        :return:
        """
        percents = {}
        for marker in self.marker_dict:
            percents[marker] = (self.marker_dict[marker]['total'] * 100) / self.total_markers

        return percents

    def get_total_marker_statistics(self):
        """
        Creates a dictionary with the markers as keys and their average number of occurences
        (a_mean, h_mean, median, mode) over all the documents in this dataset as value-dict
        :return:
        """
        statistics = {}

        for marker in self.marker_dict:
            statistics[marker] = {}
            statistics[marker]['a_mean'] = self.marker_dict[marker]['total'] / self.total_docs
            statistics[marker]['h_mean'] = self.total_docs / self.marker_dict[marker]['inverse_sum_total']
            statistics[marker]['median'] = self.marker_dict[marker]['median_total']
            statistics[marker]['mode'] = self.marker_dict[marker]['mode_total'][0]

        return statistics

    def get_markers(self):
        """
        :return: a list of all the markers in this dataset
        """
        markers = []
        for marker in self.marker_dict:
            markers.append(marker)
        return markers

    def get_all_marker_values(self, marker):
        """
        Creates a List with all the values for a marker:
        [total, a_mean, h_mean, median, mode]
        :param marker:
        :return:
        """
        if marker in self.marker_dict:
            marker_values = [self.marker_dict[marker]['total'],
                             self.marker_dict[marker]['total'] / self.total_docs,
                             self.total_docs / self.marker_dict[marker]['inverse_sum_total'],
                             self.marker_dict[marker]['median_total'],
                             self.marker_dict[marker]['mode_total'][0]]
        else:
            marker_values = [0] * 5

        return marker_values
