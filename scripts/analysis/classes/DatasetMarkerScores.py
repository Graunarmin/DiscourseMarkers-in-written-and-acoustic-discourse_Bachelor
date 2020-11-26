from helpers import Helpers as hp
import json
from collections import Counter


class DatasetMarkerScores:

    def __init__(self, markerdict, marker_per_doc, markertypes):

        with open(markerdict, 'r', encoding='utf-8') as data_json:
            dictionary = json.load(data_json)

            self.total_docs = dictionary['stats']['total_docs']
            self.total_sentences = dictionary['stats']['total_sentences']
            self.total_words = dictionary['stats']['total_words']
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

        self.marker_types = markertypes

    def get_total_docs(self):
        return self.total_docs

    def get_total_for_markerclass(self, marker_class=None):
        total = 0
        for marker in self.marker_dict:
            if self.marker_types.get_marker_type(marker) == marker_class:
                total += self.marker_dict[marker]['total']
        return total

    def get_average_for_markerclass(self, marker_class=None, average='word'):
        if average == 'doc':
            return self.get_total_for_markerclass(marker_class) / self.total_docs
        else:
            return self.get_total_for_markerclass(marker_class) / self.total_words

    def get_percentage_for_markerclass(self, marker_class=None, perc='word'):
        if perc == 'doc':
            return self.get_total_for_markerclass(marker_class) * 100 / self.total_docs
        else:
            return self.get_total_for_markerclass(marker_class) * 100 / self.total_words



# ------- Functionaliyt concerning the marker dictionary with the single markers

    def get_total_marker_values(self, average=False, share=None):
        """
        Creates a dictionary with the markers as keys and their total number of occurrence in this dataset as value
        :return:
        """
        markers = {}
        for marker in self.marker_dict:
            if average:
                if share == 'Sent':
                    markers[marker] = self.marker_dict[marker]['total'] / self.total_sentences
                elif share == 'Word':
                    markers[marker] = self.marker_dict[marker]['total'] / self.total_words
                elif share == 'Doc':
                    markers[marker] = self.marker_dict[marker]['total'] / self.total_docs
            else:
                markers[marker] = self.marker_dict[marker]['total']

        return markers

    def get_total_marker_percents(self, share='Marker'):
        """
        Creates a dictionary with the markers as keys
        and their percentage-share in all the markers in this dataset as value
        :return:
        """
        percents = {}
        for marker in self.marker_dict:
            if share == 'Word':
                percents[marker] = (self.marker_dict[marker]['total'] * 100) / self.total_words
            else:
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
            statistics[marker]['mode'] = self.marker_dict[marker]['mode_total'][0][0]

        return statistics

    def get_markers(self):
        """
        :return: a list of all the markers in this dataset
        """
        markers = []
        for marker in self.marker_dict:
            markers.append(marker)
        return markers

    def get_marker_values_at_position(self, position, average=False, perc=False, share=None):
        """
        Creates a dict with the marker as key and the position value as value
        :param share:
        :param perc:
        :param average:
        :param position: the position to get the values for: sb, sm, se, db, dm, de
        :return:
        """

        if position == "sb":
            flag = 'sent_begin'
            perc_total = self.total_sb
        elif position == "sm":
            flag = 'sent_middle'
            perc_total = self.total_sm
        elif position == "se":
            flag = 'sent_end'
            perc_total = self.total_se
        elif position == "db":
            flag = 'doc_begin'
            perc_total = self.total_db
        elif position == "dm":
            flag = 'doc_middle'
            perc_total = self.total_dm
        elif position == "de":
            flag = 'doc_end'
            perc_total = self.total_de
        else:
            print("Wrong Position!")
            return None

        markers = {}
        for marker in self.marker_dict:
            if average:
                if share == 'Doc':
                    markers[marker] = self.marker_dict[marker][flag] / self.total_docs
                elif share == 'Word':
                    markers[marker] = self.marker_dict[marker][flag] / self.total_words
            elif perc:
                markers[marker] = self.marker_dict[marker][flag] * 100 / perc_total
            else:
                markers[marker] = self.marker_dict[marker][flag]

        return markers

    def get_all_marker_values(self, marker):
        """
        Creates a List with all the values for a marker:
        [total, a_mean, h_mean, median, mode]
        :param marker:
        :return:
        """
        if marker in self.marker_dict:
            marker_values = [  # self.marker_dict[marker]['total'],
                self.marker_dict[marker]['total'] / self.total_docs,
                self.total_docs / self.marker_dict[marker]['inverse_sum_total'],
                self.marker_dict[marker]['median_total'],
                self.marker_dict[marker]['mode_total'][0][0]]
        else:
            marker_values = [0] * 4

        return marker_values

    def get_marker_total(self, marker):
        """
        Gets the total number of occurrences for the given marker in the dataset.
        :param marker:
        :return: total number of occurrences in the dataset (0 if none)
        """
        if marker in self.marker_dict:
            return self.marker_dict[marker]['total']
        else:
            return 0

    def get_most_common_markers(self, number, perc=False, average=False, share=None, position=None):
        """
        :param number: How many markers to get (the top most x)
        :param perc: if the result is supposed to be a percentage: True, Default is False
        :param average: if the result is supposed to be an average: True, Default is False
        :param share: on which base to compute the average or share - 'Sent', 'Doc' or 'Word'
        :param position: most common marker at which position: 'sb', 'sm', 'se', 'db', 'dm', 'de'
        :return:
        """
        # averages or percentages at certain positions
        if position:
            marker_count = Counter(
                self.get_marker_values_at_position(position, average=average, perc=perc, share=share))
        # total percentages
        elif perc:
            marker_count = Counter(self.get_total_marker_percents(share=share))
        # total averages
        else:
            marker_count = Counter(self.get_total_marker_values(average=average, share=share))

        markers = []
        marker_values = []
        for item in marker_count.most_common(number):
            markers.append(item[0])
            marker_values.append(item[1])

        return markers, marker_values
