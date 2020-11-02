import CreatePlots as cp
import MarkerPlots as mp
import DatasetScores as ds


# -------- Read in data ----------
class GenreData:
    def __init__(self,
                 news_scores, news_dict, discussion_scores, discussion_dict,
                 science_scores, science_dict, documentary_scores, documentary_dict,
                 markertypes=None):
        self.news = ds.DatasetScores(news_scores, news_dict, markertypes=markertypes)
        self.discussion = ds.DatasetScores(discussion_scores, discussion_dict, markertypes=markertypes)
        self.science = ds.DatasetScores(science_scores, science_dict, markertypes=markertypes)
        self.documentary = ds.DatasetScores(documentary_scores, documentary_dict, markertypes=markertypes)

        # Colors:   [base, darker, lighter]
        self.spotify_color = '#1DB954'
        self.spotify_shades = ['#1DB954', '#0e5c2a', '#8edca9']
        self.ted_color = '#e62b1e'
        self.ted_shades = ['#e62b1e', '#73150f', '#f2958e']
        self.ny_color = '#FFA700'
        self.ny_shades = ['#FFA700', '#7f5300', '#ffd37f']
        self.gig_color = '#227DFB'
        self.gig_shades = ['#227DFB', '#113e7d', '#90befd']