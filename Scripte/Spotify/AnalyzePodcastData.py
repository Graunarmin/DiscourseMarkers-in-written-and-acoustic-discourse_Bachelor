import sys
import csv
from Spotify import RssReader as rss


class Analyzer:

    def __init__(self, meta, out):
        self.metadata_file = meta
        self.out_file = out
        self.rss_reader = rss.RssReader()
        self.rss_links = self.read_in_metadata()
        self.genres = self.get_genre_list()

    def read_in_metadata(self):
        rss_links = []
        with open(self.metadata_file, 'r') as tsv_file:
            data_reader = csv.reader(tsv_file, delimiter="\t")
            for row in data_reader:
                rss_links.append(row[5])
        return rss_links

    def get_genre_list(self):
        """
        add the genres to a dict with a counter so we can count how many shows we have of each genre
        """
        genres = []
        for link in self.rss_links:
            tags = rss.get_genre(link)
            for tag in tags:
                genres.append(tag)

        return genres


# ------------ MAIN -------------
def main():
    analyzer = Analyzer("../../../corpora/podcasts/metadata/metadata.tsv", "../../data/Spotify/genres.json")
    analyzer.read_in_metadata()


if __name__ == '__main__':
    main()
