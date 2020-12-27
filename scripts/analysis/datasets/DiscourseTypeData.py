from classes import DatasetScores as ds
from classes import DatasetMarkerScores as dms


class DiscourseTypeData:
    def __init__(self,
                 spotify_scores,
                 acoustic_scores, written_scores,
                 spotify_scores_opt=None,
                 acoustic_opt=None, written_opt=None,
                 general=True,
                 markertypes=None):

        if general:
            self.spotify = ds.DatasetScores(spotify_scores, spotify_scores_opt)
            self.acoustic = ds.DatasetScores(acoustic_scores, acoustic_opt)
            self.written = ds.DatasetScores(written_scores, written_opt)

        else:
            self.spotify = dms.DatasetMarkerScores(spotify_scores, spotify_scores_opt, markertypes)
            self.acoustic = dms.DatasetMarkerScores(acoustic_scores, acoustic_opt, markertypes)
            self.written = dms.DatasetMarkerScores(written_scores, written_opt, markertypes)

        # Colors:   [base, darker, lighter]
        self.spotify_color = '#1DB954'
        self.spotify_shades = ['#1DB954', '#0e5c2a', '#8edca9']
        self.acoustic_color = '#22a6b3'
        self.written_color = '#be2edd'

        self.spotify_label = "Spotify"
        self.acoustic_label = "Oral-Acoustic"
        self.written_label = "Literat-Written"