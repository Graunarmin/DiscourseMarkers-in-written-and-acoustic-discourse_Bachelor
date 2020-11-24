from classes import DatasetScores as ds


class ConversationTypeData:
    def __init__(self,
                 dialog_scores, dialog_sentences, dialog_dict,
                 monolog_scores, monolog_sentences, monolog_dict,
                 cmonolog_scores, cmonolog_sentences, cmonolog_dict,
                 ted_scores, ted_sentences, ted_dict,
                 markertypes=None):
        self.dialog = ds.DatasetScores(dialog_scores, dialog_sentences, dialog_dict, markertypes=markertypes)
        self.monolog = ds.DatasetScores(monolog_scores, monolog_sentences, monolog_dict, markertypes=markertypes)
        self.cmonolog = ds.DatasetScores(cmonolog_scores, cmonolog_sentences, cmonolog_dict, markertypes=markertypes)
        self.speech = ds.DatasetScores(ted_scores, ted_sentences, ted_dict, markertypes=markertypes)

        # Colors:   [base, darker, lighter]
        self.dialog_color = '#9a1cff'
        self.dialog_shades = ['#9a1cff', '#6b13b2', '#b860ff']
        self.monolog_color = '#1cff9a'
        self.monolog_shades = ['#1cff9a', '#13b26b', '#60ffb8']
        self.cmonolog_color = '#ff9a1c'
        self.cmonolog_shades = ['#FFE494', '#b26b13', '#ffb860']
        self.speech_color = '#e62b1e'
        self.speech_shades = ['#e62b1e', '#73150f', '#f2958e']