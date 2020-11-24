import pandas as pd
import ast
from helpers import Helpers as hp
from classes import MarkerTypes as mt
import json
from collections import Counter


class DatasetScores:

    def __init__(self, scorefile, sentencescores, jsonfile, markertypes=None):
        self.scores = pd.read_csv(scorefile)
        self.total_sentences = sum(self.scores['sentence_count_doc'])
        self.total_words = sum(self.scores['word_count_doc'])

        with open(sentencescores, 'r', encoding='utf-8') as sentence_data:
            self.sentence_scores = json.load(sentence_data)

        if markertypes:
            self.marker_types = mt.MarkerTypes(markertypes)

        with open(jsonfile, 'r', encoding='utf-8') as data_json:
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

# --- DM per Text ----

    def get_total_dm_per_text_column(self):
        """
        Gets the 'dm_count_doc' column of the scores as a list
        :return:
        """
        return list(self.scores['dm_count_doc'].dropna())

    def get_total_dm_per_text_statistics(self):
        """
        Computes the min, mean, max of the total number of DM per Text
        :return: a list of [min, a_mean, h_mean, median, mode, max] values
        """
        return hp.compute_statistics(self.scores['dm_count_doc'].dropna())

    def get_percent_dm_per_text_column(self, collected=False):
        """
        Gets the 'dm_words_perc' column of the scores as a list
        collected returns a list of two lists, one containing the percentage of dms,
        the second one the percentage of texts containing as many dms.
        :return:
        """
        if not collected:
            return list(self.scores['dm_words_perc'].dropna())
        else:
            dm_words = {}
            for count in self.scores['dm_words_perc'].dropna():
                if int(count) not in dm_words:
                    dm_words[int(count)] = 1
                else:
                    dm_words[int(count)] += 1
            texts = []
            dms = []
            for element in sorted((dm_words.items())):
                texts.append(element[1] * 100 / self.total_docs)
                dms.append(element[0])
            return [dms, texts]

    def get_percent_dm_per_text_statistics(self):
        """
        Computes the min, mean, max of the percentage share that the DM
        have in a text
        :return: a list of [min, a_mean, h_mean, median, mode, max] values
        """
        return hp.compute_statistics(self.scores['dm_words_perc'].dropna())

# ---- DM sentences ----

    def get_total_dm_sentences_column(self):
        """
        Gets the 'dm_sentences' column of the scores as a list
        :return:
        """
        return list(self.scores['dm_sentences'].dropna())

    def get_total_dm_sentences_statistics(self):
        """
        Computes the min, mean, max of the total number of sentences
        that contain at least one DM per Text
        :return: a list of [min, a_mean, h_mean, median, mode, max] values
        """
        return hp.compute_statistics(self.scores['dm_sentences'].dropna())

    def get_percent_dm_sentences_column(self, collected=False):
        """
        Gets the 'dm_sentences_perc' column of the scores as a list
        :return:
        """
        if not collected:
            return list(self.scores['dm_sentences_perc'])
        else:
            dm_words = {}
            for count in self.scores['dm_sentences_perc'].dropna():
                if int(count) not in dm_words:
                    dm_words[int(count)] = 1
                else:
                    dm_words[int(count)] += 1
            texts = []
            dms = []
            for element in sorted((dm_words.items())):
                texts.append(element[1] * 100 / self.total_docs)
                dms.append(element[0])
            return [dms, texts]

    def get_percent_dm_sentences_statistics(self):
        """
        Computes the min, mean, max of the percentage share that sentences
        containing at least one DM have of a text
        :return:
        """
        return hp.compute_statistics(self.scores['dm_sentences_perc'].dropna())

# --- DM per Sentence ---

    def get_total_dm_per_sentence_statistics(self):
        """
        Computes the min, mean, max of dm per sentence per text
        :return:
        """
        return hp.compute_statistics(self.get_dm_per_sentence())

    def compute_dm_per_sentence(self):
        """
        Create two lists, one of which contains the number of dm per sentence (x)
        and the other one (y) contains the number of sentences that contain as many dms.
        :return: a list of [[x_values],[y_values]]
        """
        values = {}

        for counter in self.sentence_scores:
            values[int(float(counter))] = self.sentence_scores[counter]

        # x values are the number of dms per sentence
        x_values = []
        # y values are the number of sentences that contain as many dms.
        y_values = []
        for element in sorted(values.items()):
            x_values.append(element[0])
            y_values.append(element[1] * 100 / self.total_sentences)

        return [x_values, y_values]

    def get_dm_per_sentence(self):
        """
        Returns a list of counts that indicates how many sentences in this dataset contain
        as many discourse markers.
        E.g.: if  three sentences each contain 2 DM, 2 is added to the list 3 times
        :return: a list of all the counts
        """
        counts = []

        for count in self.sentence_scores:
            counts.extend([int(float(count)) for i in range(int(self.sentence_scores[count]))])

        return counts

# ---- Sentence Positions ----

    def get_sent_begin_column(self, perc=False):
        if perc:
            return list(((score * 100) / whole) for score, whole in zip(self.scores['dm_pos_sent_begin'].dropna(),
                                                                        self.scores['dm_count_doc'].dropna()))
        return list(self.scores['dm_pos_sent_begin'].dropna())

    def get_sent_middle_column(self, perc=False):
        if perc:
            return list(((score * 100) / whole) for score, whole in zip(self.scores['dm_pos_sent_middle'].dropna(),
                                                                        self.scores['dm_count_doc'].dropna()))
        return list(self.scores['dm_pos_sent_middle'].dropna())

    def get_sent_end_column(self, perc=False):
        if perc:
            return list(((score * 100) / whole) for score, whole in zip(self.scores['dm_pos_sent_end'].dropna(),
                                                                        self.scores['dm_count_doc'].dropna()))
        return list(self.scores['dm_pos_sent_end'].dropna())

    def get_total_dm_positions_sentence(self):
        """
        Computes the total number of DM at the beginning, the middle and the end
        of a sentence
        :return: a list [count_begin, count_middle, count_end]
        """
        return [sum(self.get_sent_begin_column()),
                sum(self.get_sent_middle_column()),
                sum(self.get_sent_end_column())]

    def get_percent_dm_positions_sentence(self):
        """
        Computes the perceantage share of dm that stand in the beginning, the middle
        or the end of a sentence
        :return:
        """
        values = self.get_total_dm_positions_sentence()
        whole = sum(values)

        return [hp.percentage(values[0], whole),
                hp.percentage(values[1], whole),
                hp.percentage(values[2], whole)]

    def get_sentence_position_values(self):
        return [self.get_sent_begin_column(),
                self.get_sent_middle_column(),
                self.get_sent_end_column()]

# ---- Document Positions ----

    def get_doc_begin_column(self, perc=False):
        if perc:
            return list(((score * 100) / whole) for score, whole in zip(self.scores['dm_pos_doc_begin'].dropna(),
                                                                        self.scores['dm_count_doc'].dropna()))
        return list(self.scores['dm_pos_doc_begin'].dropna())

    def get_doc_middle_column(self, perc=False):
        if perc:
            return list(((score * 100) / whole) for score, whole in zip(self.scores['dm_pos_doc_middle'].dropna(),
                                                                        self.scores['dm_count_doc'].dropna()))
        return list(self.scores['dm_pos_doc_middle'].dropna())

    def get_doc_end_column(self, perc=False):
        if perc:
            return list(((score * 100) / whole) for score, whole in zip(self.scores['dm_pos_doc_end'].dropna(),
                                                                        self.scores['dm_count_doc'].dropna()))
        return list(self.scores['dm_pos_doc_end'].dropna())

    def get_total_dm_positions_document(self):
        """
        Computes the total number of DM at the beginning, the middle and the end
        of a document
        :return: a list [count_begin, count_middle, count_end]
        """
        return [sum(self.get_doc_begin_column()),
                sum(self.get_doc_middle_column()),
                sum(self.get_doc_end_column())]

    def get_percent_dm_positions_document(self):
        """
        Computes the perceantage share of dm that stand in the beginning, the middle
        or the end of a document
        :return:
        """
        values = self.get_total_dm_positions_document()
        whole = sum(values)

        return [hp.percentage(values[0], whole),
                hp.percentage(values[1], whole),
                hp.percentage(values[2], whole)]

    def get_document_position_values(self):
        return [self.get_doc_begin_column(),
                self.get_doc_middle_column(),
                self.get_doc_end_column()]

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
