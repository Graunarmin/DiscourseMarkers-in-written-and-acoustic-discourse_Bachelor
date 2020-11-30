from classes import DatasetScores as ds
from classes import DatasetMarkerScores as dms


class DiscourseTypeData:
    def __init__(self,
                 spotify_scores, ted_scores, ny_scores, gig_scores,
                 spotify_scores_opt=None, ted_scores_opt=None,
                 ny_scores_opt=None, gig_scores_opt=None,
                 general=True,
                 markertypes=None):

        if general:
            self.spotify = ds.DatasetScores(spotify_scores, spotify_scores_opt)
            self.ted = ds.DatasetScores(ted_scores, ted_scores_opt)
            self.ny = ds.DatasetScores(ny_scores, ny_scores_opt)
            self.gig = ds.DatasetScores(gig_scores, gig_scores_opt)

        else:
            self.spotify = dms.DatasetMarkerScores(spotify_scores, spotify_scores_opt, markertypes)
            self.ted = dms.DatasetMarkerScores(ted_scores, ted_scores_opt, markertypes)
            self.ny = dms.DatasetMarkerScores(ny_scores, ny_scores_opt, markertypes)
            self.gig = dms.DatasetMarkerScores(gig_scores, gig_scores_opt, markertypes)

        # Colors:   [base, darker, lighter]
        self.spotify_color = '#1DB954'
        self.spotify_shades = ['#1DB954', '#0e5c2a', '#8edca9']
        self.ted_color = '#e62b1e'
        self.ted_shades = ['#e62b1e', '#73150f', '#f2958e']
        self.ny_color = '#FFA700'
        self.ny_shades = ['#FFA700', '#7f5300', '#ffd37f']
        self.gig_color = '#227DFB'
        self.gig_shades = ['#227DFB', '#113e7d', '#90befd']

        self.spotify_label = "Spotify"
        self.ted_label = "TED"
        self.ny_label = "NYTimes"
        self.gig_label = "Gigaword"
