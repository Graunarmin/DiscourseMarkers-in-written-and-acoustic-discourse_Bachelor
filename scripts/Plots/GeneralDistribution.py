import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics


# ----------- STATIC FUNCTIONS ------------
def percentage(part, whole):
    return (float(part) * 100)/(float(whole))


# ----------- CLASS ------------
class GeneralDistribution:

    def __init__(self):
        # The document with the least amount of DMs has x DMs
        self.dm_count_doc_min = 0
        # The document with the greatest amount of DMs has x DMs
        self.dm_count_doc_max = 0
        # The average number of DMs per Document is x
        self.dm_count_doc_mean = 0

        # The average number of sentences containing DMs per document is x
        self.dm_sentences_mean = 0

        # The average number of DMs per sentence is x
        self.dm_count_sent_mean = 0
        self.dm_count_sent_min = 0
        self.dm_count_sent_max = 0

    def read_in_data(self, data_file):
        data = pd.read_csv(data_file)

        dm_count_doc = data['dm_count_doc']
        #self.dm_count_per_doc(dm_count_doc)

        word_count_doc = data['word_count_doc']
        sentence_count_doc = data['sentence_count_doc']

        dm_sentences_perc = data['dm_sentences_perc']
        self.dm_sent_percent_per_doc(dm_sentences_perc)

        #self.dm_percent_per_doc(word_count_doc, dm_count_doc)

        dm_sentences = data['dm_sentences']
        #self.dm_sentences_mean = statistics.mean(dm_sentences)

        dm_count_mean = data['dm_count_mean']
        #self.dm_count_per_sentence(dm_count_mean)

    def dm_percent_per_doc(self, word_count, marker_count):
        percentages = []
        for word, marker in zip(word_count, marker_count):
            percentages.append(percentage(marker, word))

        min_dm_perc_per_doc = min(percentages)
        max_dm_perc_per_doc = max(percentages)
        mean_dm_perc_per_doc = statistics.mean(percentages)

        y_values = [min_dm_perc_per_doc, mean_dm_perc_per_doc, max_dm_perc_per_doc]

        x_values = np.arange(len(y_values))
        x_labels = ["Min % DM", "Mean % DM", "Max % DM"]

        plt.style.use('fivethirtyeight')
        plt.bar(x_values, y_values)

        plt.title("Percent Discourse Marker per Document")
        # plt.xlabel()
        plt.ylabel("Percent Markers")

        plt.xticks(ticks=x_values, labels=x_labels)

        plt.tight_layout()

        plt.show()

    def dm_sent_percent_per_doc(self, dm_sent):

        min_dm_perc_per_doc = min(dm_sent)
        max_dm_perc_per_doc = max(dm_sent)
        mean_dm_perc_per_doc = statistics.mean(dm_sent)

        y_values = [min_dm_perc_per_doc, mean_dm_perc_per_doc, max_dm_perc_per_doc]

        x_values = np.arange(len(y_values))
        x_labels = ["Min % DM-Sentence", "Mean % DM-Sentence", "Max % DM-Sentence"]

        plt.style.use('fivethirtyeight')
        plt.bar(x_values, y_values)

        plt.title("Percent of Sentences containing Discourse Markers per Document")
        # plt.xlabel()
        plt.ylabel("Percent Markers")

        plt.xticks(ticks=x_values, labels=x_labels)

        plt.tight_layout()

        plt.show()

    def dm_count_per_doc(self, values):
        self.dm_count_doc_min = min(values)
        self.dm_count_doc_max = max(values)
        self.dm_count_doc_mean = statistics.mean(list(values))

        y_values = [self.dm_count_doc_min, self.dm_count_doc_mean, self.dm_count_doc_max]

        x_values = np.arange(len(y_values))
        x_labels = ["Min DM", "Mean DM", "Max DM"]

        plt.style.use('fivethirtyeight')
        plt.bar(x_values, y_values)

        plt.title("Discourse Marker per Document")
        # plt.xlabel()
        plt.ylabel("Number of Markers")

        plt.xticks(ticks=x_values, labels=x_labels)

        plt.tight_layout()

        plt.show()

    def dm_count_per_sentence(self, values):
        self.dm_count_sent_mean = statistics.mean(list(values))
        self.dm_count_sent_min = min(values)
        self.dm_count_sent_max = max(values)

        y_values = [self.dm_count_sent_min, self.dm_count_sent_mean, self.dm_count_sent_max]

        x_values = np.arange(len(y_values))
        x_labels = ["Min DM", "Mean DM", "Max DM"]

        plt.style.use('fivethirtyeight')
        plt.bar(x_values, y_values)

        plt.title("Discourse Marker per Sentence")
        # plt.xlabel()
        plt.ylabel("Number of Markers")

        plt.xticks(ticks=x_values, labels=x_labels)

        plt.tight_layout()

        plt.show()


# ------------ MAIN -------------
def main():
    distribution = GeneralDistribution()
    distribution.read_in_data("../../data/listenability-tools/data.csv")


if __name__ == '__main__':
    main()
