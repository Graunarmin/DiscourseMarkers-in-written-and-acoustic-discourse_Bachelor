import pandas as pd
from helpers import Helpers as hp
import json


class DatasetScores:

    def __init__(self, scorefile, sentencescores):
        self.scores = pd.read_csv(scorefile)
        self.total_docs = self.scores.shape[0]
        self.total_sentences = sum(self.scores['sentence_count_doc'])
        self.total_words = sum(self.scores['word_count_doc'])

        with open(sentencescores, 'r', encoding='utf-8') as sentence_data:
            self.sentence_scores = json.load(sentence_data)

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
            return list(self.scores['dm_sentences_perc'].dropna())
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
