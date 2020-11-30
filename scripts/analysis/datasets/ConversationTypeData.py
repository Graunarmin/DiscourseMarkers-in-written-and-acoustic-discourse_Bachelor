from classes import DatasetScores as ds
from classes import DatasetMarkerScores as dms


class ConversationTypeData:
    def __init__(self,
                 dialog_scores, monolog_scores, cmonolog_scores, ted_scores,
                 dialog_scores_opt=None, monolog_scores_opt=None,
                 cmonolog_scores_opt=None, ted_scores_opt=None,
                 general=True,
                 markertypes=None):

        if general:
            self.dialog = ds.DatasetScores(dialog_scores, dialog_scores_opt)
            self.monolog = ds.DatasetScores(monolog_scores, monolog_scores_opt)
            self.cmonolog = ds.DatasetScores(cmonolog_scores, cmonolog_scores_opt)
            self.speech = ds.DatasetScores(ted_scores, ted_scores_opt)
        else:
            self.dialog = dms.DatasetMarkerScores(dialog_scores, dialog_scores_opt, markertypes)
            self.monolog = dms.DatasetMarkerScores(monolog_scores, monolog_scores_opt, markertypes)
            self.cmonolog = dms.DatasetMarkerScores(cmonolog_scores, cmonolog_scores_opt, markertypes)
            self.speech = dms.DatasetMarkerScores(ted_scores, ted_scores_opt, markertypes)

        # Colors:   [base, darker, lighter]
        self.dialog_color = '#9a1cff'
        self.dialog_shades = ['#9a1cff', '#6b13b2', '#b860ff']
        self.monolog_color = '#1cff9a'
        self.monolog_shades = ['#1cff9a', '#13b26b', '#60ffb8']
        self.cmonolog_color = '#ff9a1c'
        self.cmonolog_shades = ['#FFE494', '#b26b13', '#ffb860']
        self.speech_color = '#e62b1e'
        self.speech_shades = ['#e62b1e', '#73150f', '#f2958e']

        self.dialog_label = "Dialog"
        self.monolog_label = "Monolog"
        self.cmonolog_label = "Cooperative-Monolog"
        self.speech_label = "Speech"
