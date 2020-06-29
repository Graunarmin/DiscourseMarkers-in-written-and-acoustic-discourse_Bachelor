import sys
import csv
import Spotify.RssReader as rss


class Analyzer:

    def __init__(self, meta, out):
        self.metadata_file = meta
        self.out_file = out
        self.rss_reader = rss.RssReader()

    def read_in_metadata(self):
        pass

    def get_genre_list(self):
        pass
