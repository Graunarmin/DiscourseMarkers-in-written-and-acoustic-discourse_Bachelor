from classes import DatasetScores as ds
from classes import DatasetMarkerScores as dms


# -------- Read in data ----------
class GenreData:
    def __init__(self,
                 news_scores, discussion_scores, science_scores,
                 documentary_scores, ted_scores,
                 news_sentences=None, discussion_sentences=None, science_sentences=None,
                 documentary_sentences=None, ted_sentences=None,
                 general=True,
                 markertypes=None):

        if general:
            self.news = ds.DatasetScores(news_scores, news_sentences)
            self.discussion = ds.DatasetScores(discussion_scores, discussion_sentences)
            self.science = ds.DatasetScores(science_scores, science_sentences)
            self.documentary = ds.DatasetScores(documentary_scores, documentary_sentences)
            self.speech = ds.DatasetScores(ted_scores, ted_sentences)

        else:
            self.news = dms.DatasetMarkerScores(news_scores, markertypes)
            self.discussion = dms.DatasetMarkerScores(discussion_scores, markertypes)
            self.science = dms.DatasetMarkerScores(science_scores, markertypes)
            self.documentary = dms.DatasetMarkerScores(documentary_scores, markertypes)
            self.speech = dms.DatasetMarkerScores(ted_scores, markertypes)

        # Colors:   [base, darker, lighter]
        self.news_color = '#7bd45d'
        self.news_shades = ['#7bd45d', '#569441', '#a2e08d']
        self.discussion_color = '#d45d7b'
        self.discussion_shades = ['#d45d7b', '#944156', '#e08da2']
        self.science_color = '#5d7bd4'
        self.science_shades = ['#5d7bd4', '#415694', '#8da2e0']
        self.documentary_color = '#ff9a1c'
        self.documentary_shades = ['#FFE494', '#b26b13', '#ffb860']
        self.speech_color = '#e62b1e'
        self.speech_shades = ['#e62b1e', '#73150f', '#f2958e']