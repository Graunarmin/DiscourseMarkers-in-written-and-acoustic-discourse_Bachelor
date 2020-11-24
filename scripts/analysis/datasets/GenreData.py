from classes import DatasetScores as ds


# -------- Read in data ----------
class GenreData:
    def __init__(self,
                 news_scores, news_sentences, news_dict,
                 discussion_scores, discussion_sentences, discussion_dict,
                 science_scores, science_sentences, science_dict,
                 documentary_scores, documentary_sentences, documentary_dict,
                 ted_scores, ted_sentences, ted_dict,
                 markertypes=None):
        self.news = ds.DatasetScores(news_scores, news_sentences, news_dict, markertypes=markertypes)
        self.discussion = ds.DatasetScores(discussion_scores, discussion_sentences, discussion_dict, markertypes=markertypes)
        self.science = ds.DatasetScores(science_scores, science_sentences, science_dict, markertypes=markertypes)
        self.documentary = ds.DatasetScores(documentary_scores, documentary_sentences, documentary_dict, markertypes=markertypes)
        self.speech = ds.DatasetScores(ted_scores, ted_sentences, ted_dict, markertypes=markertypes)

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