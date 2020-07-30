import sys
import csv
import json
import RssReader as rss


# ------------ CLASS -------------
class Analyzer:

    def __init__(self, meta):
        self.metadata_file = meta
        self.links_outfile = "../../data/Spotify/rss_links.json"
        self.links_genre_outfile = "../../data/Spotify/rss_links_genre.json"
        self.genre_outfile = "../../data/Spotify/genres.json"
        self.genre_short_outfile = "../../data/Spotify/genres_short.json"
        self.rss_links = self.read_in_metadata()
        self.get_genres()

    def read_in_metadata(self):
        """
        read in the metadata from metadata.tsv and write a file with the shownames as keys.
        Their value is a dictionary with the show_uri, the rss_link and the number of episodes
        """
        rss_links = {}
        with open(self.metadata_file, 'r', encoding='utf_8') as tsv_file:
            data_reader = csv.reader(tsv_file, delimiter="\t")
            for row in data_reader:
                if row[1] in rss_links:
                    rss_links[row[1]]["episodes"] += 1
                else:
                    rss_links[row[1]] = {"show_uri": row[0], "rss_link": row[5], "episodes": 1}

        write_json(rss_links, self.links_outfile)
        return rss_links

    def get_genres(self):
        """
        add the genres to a dict with a counter so we can count how many shows (and episodes)
        we have of each genre
        """
        genres = {}
        genre_list = set()
        for entry in self.rss_links:
            link = self.rss_links[entry]["rss_link"]
            self.rss_links[entry]["genre"] = rss.get_genre(link)
            '''
            for each genre that was found: add it to the dict or increase the counter
            also add a list of all shows that have this genre
            genres = {
                      GenreX: {"counter": 2, "shows": {"show1":{"show_uri":uri, "episodes":3}}}, 
                      GenreY:{...},...
                      }
            '''
            for tag in self.rss_links[entry]["genre"]:
                if tag in genres:
                    genres[tag]["counter"] += 1
                    genres[tag]["shows"][entry] = {"show_uri": self.rss_links[entry]["show_uri"],
                                                   "episodes": self.rss_links[entry]["episodes"]}
                else:
                    genre_list.add(tag)
                    genres[tag] = {}
                    genres[tag]["counter"] = 1
                    genres[tag]["shows"] = {}
                    genres[tag]["shows"][entry] = {"show_uri": self.rss_links[entry]["show_uri"],
                                                   "episodes": self.rss_links[entry]["episodes"]}

        write_json(genres, self.genre_outfile)
        write_json(sorted(list(genre_list)), self.genre_short_outfile)
        # write the rss_links to another file, now with added genre-information
        write_json(self.rss_links, self.links_genre_outfile)


# ------ STATIC FUNCTIONS -------
def write_json(data, file):
    with open(file, 'w') as outfile:
        json.dump(data, outfile)


# ------------ MAIN -------------
def main():
    """
    Argument 1: metadata tsv file (here: "../../../corpora/podcasts/metadata/metadata.tsv")
    """
    analyzer = Analyzer(sys.argv[1])
    analyzer.read_in_metadata()


if __name__ == '__main__':
    main()
