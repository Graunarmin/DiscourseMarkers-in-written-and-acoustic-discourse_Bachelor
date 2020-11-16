from classes import DatasetScores as ds


class CorpusData:
    def __init__(self,
                 spotify_scores, spotify_dict,
                 ted_scores, ted_dict,
                 ny_scores, ny_dict,
                 gig_scores, gig_dict,
                 markertypes=None):
        self.spotify = ds.DatasetScores(spotify_scores, spotify_dict, markertypes=markertypes)
        self.ted = ds.DatasetScores(ted_scores, ted_dict, markertypes=markertypes)
        self.ny = ds.DatasetScores(ny_scores, ny_dict, markertypes=markertypes)
        self.gig = ds.DatasetScores(gig_scores, gig_dict, markertypes=markertypes)

        # Colors:   [base, darker, lighter]
        self.spotify_color = '#1DB954'
        self.spotify_shades = ['#1DB954', '#0e5c2a', '#8edca9']
        self.ted_color = '#e62b1e'
        self.ted_shades = ['#e62b1e', '#73150f', '#f2958e']
        self.ny_color = '#FFA700'
        self.ny_shades = ['#FFA700', '#7f5300', '#ffd37f']
        self.gig_color = '#227DFB'
        self.gig_shades = ['#227DFB', '#113e7d', '#90befd']
