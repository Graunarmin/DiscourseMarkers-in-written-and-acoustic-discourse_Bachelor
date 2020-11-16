from classes import DatasetScores as ds


class DiscourseTypeData:
    def __init__(self,
                 dialog_scores, dialog_dict, monolog_scores, monolog_dict,
                 cmonolog_scores, cmonolog_dict,
                 ted_scores, ted_dict,
                 markertypes=None):
        self.dialog = ds.DatasetScores(dialog_scores, dialog_dict, markertypes=markertypes)
        self.monolog = ds.DatasetScores(monolog_scores, monolog_dict, markertypes=markertypes)
        self.cmonolog = ds.DatasetScores(cmonolog_scores, cmonolog_dict, markertypes=markertypes)
        self.speech = ds.DatasetScores(ted_scores, ted_dict, markertypes=markertypes)

        # Colors:   [base, darker, lighter]
        self.dialog_color = '#7bd45d'
        self.dialog_shades = ['#7bd45d', '#569441', '#a2e08d']
        self.monolog_color = '#d45d7b'
        self.monolog_shades = ['#d45d7b', '#944156', '#e08da2']
        self.cmonolog_color = '#5d7bd4'
        self.cmonolog_shades = ['#5d7bd4', '#415694', '#8da2e0']
        self.speech_color = '#e62b1e'
        self.speech_shades = ['#e62b1e', '#73150f', '#f2958e']