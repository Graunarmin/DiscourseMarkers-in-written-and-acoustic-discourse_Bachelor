from classes import DatasetScores as ds
from classes import DatasetMarkerScores as dms


# -------- Read in data ----------
class GenreData:
    def __init__(self,
                 news_scores, discussion_scores, science_scores,
                 documentary_scores, ted_scores,
                 news_scores_opt=None, discussion_scores_opt=None, science_scores_opt=None,
                 documentary_scores_opt=None, ted_scores_opt=None,
                 general=True,
                 markertypes=None):

        if general:
            self.news = ds.DatasetScores(news_scores, news_scores_opt)
            self.discussion = ds.DatasetScores(discussion_scores, discussion_scores_opt)
            self.science = ds.DatasetScores(science_scores, science_scores_opt)
            self.documentary = ds.DatasetScores(documentary_scores, documentary_scores_opt)
            self.presentation = ds.DatasetScores(ted_scores, ted_scores_opt)

        else:
            self.news = dms.DatasetMarkerScores(news_scores, news_scores_opt, markertypes)
            self.discussion = dms.DatasetMarkerScores(discussion_scores, discussion_scores_opt, markertypes)
            self.science = dms.DatasetMarkerScores(science_scores, science_scores_opt, markertypes)
            self.documentary = dms.DatasetMarkerScores(documentary_scores, documentary_scores_opt, markertypes)
            self.presentation = dms.DatasetMarkerScores(ted_scores, ted_scores_opt, markertypes)

        # Colors:   [base, darker, lighter]
        self.news_color = '#7bd45d'
        self.news_shades = ['#7bd45d', '#569441', '#a2e08d']
        self.discussion_color = '#d45d7b'
        self.discussion_shades = ['#d45d7b', '#944156', '#e08da2']
        self.science_color = '#5d7bd4'
        self.science_shades = ['#5d7bd4', '#415694', '#8da2e0']
        self.documentary_color = '#ff9a1c'
        self.documentary_shades = ['#FFE494', '#b26b13', '#ffb860']
        self.presentation_color = '#e62b1e'
        self.presentation_shades = ['#e62b1e', '#73150f', '#f2958e']

        self.news_label = "News"
        self.discussion_label = "Discussion"
        self.science_label = "Science/Education"
        self.documentary_label = "Documentary"
        self.presentation_label = "Presentation"
