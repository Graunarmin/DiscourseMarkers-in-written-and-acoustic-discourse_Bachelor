from classes import DatasetScores as ds
from classes import DatasetMarkerScores as dms


class ConversationTypeData:
    def __init__(self,
                 dialog_scores, monolog_scores, cmonolog_scores, ted_scores,
                 dialog_sentences=None, monolog_sentences=None,
                 cmonolog_sentences=None, ted_sentences=None,
                 general=True,
                 markertypes=None):

        if general:
            self.dialog = ds.DatasetScores(dialog_scores, dialog_sentences)
            self.monolog = ds.DatasetScores(monolog_scores, monolog_sentences)
            self.cmonolog = ds.DatasetScores(cmonolog_scores, cmonolog_sentences)
            self.speech = ds.DatasetScores(ted_scores, ted_sentences)
        else:
            self.dialog = dms.DatasetMarkerScores(dialog_scores, markertypes)
            self.monolog = dms.DatasetMarkerScores(monolog_scores, markertypes)
            self.cmonolog = dms.DatasetMarkerScores(cmonolog_scores, markertypes)
            self.speech = dms.DatasetMarkerScores(ted_scores, markertypes)

        # Colors:   [base, darker, lighter]
        self.dialog_color = '#9a1cff'
        self.dialog_shades = ['#9a1cff', '#6b13b2', '#b860ff']
        self.monolog_color = '#1cff9a'
        self.monolog_shades = ['#1cff9a', '#13b26b', '#60ffb8']
        self.cmonolog_color = '#ff9a1c'
        self.cmonolog_shades = ['#FFE494', '#b26b13', '#ffb860']
        self.speech_color = '#e62b1e'
        self.speech_shades = ['#e62b1e', '#73150f', '#f2958e']