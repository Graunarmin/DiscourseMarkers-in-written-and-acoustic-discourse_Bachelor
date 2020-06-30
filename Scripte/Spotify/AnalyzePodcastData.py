import sys
import csv
import json
import RssReader as rss


# ------------ CLASS -------------
class Analyzer:

    def __init__(self, meta):
        self.metadata_file = meta
        self.links_outfile = "../../data/Spotify/rss_links.json"
        self.genre_outfile = "../../data/Spotify/genres.json"
        self.rss_links = self.read_in_metadata()
        self.get_genres()

    def read_in_metadata(self):
        rss_links = []
        with open(self.metadata_file, 'r', encoding='utf_8') as tsv_file:
            data_reader = csv.reader(tsv_file, delimiter="\t")
            for row in data_reader:
                rss_links.append({"show_name": row[1], "show_uri": row[0], "rss_link": row[5]})

        # write_json(rss_links, self.links_outfile)
        return rss_links

    def get_genres(self):
        """
        add the genres to a dict with a counter so we can count how many shows we have of each genre
        """
        genres = {}
        for entry in self.rss_links:
            link = entry["rss_link"]
            entry["genre"] = rss.get_genre(link)
            '''
            for each genre that was found: add it to the dict or increase the counter
            also add a list of all shows that have this genre
            genres = {GenreX: {"counter": 2, "shows": [Show1, Show2]}, GenreY:{...},...}
            '''
            for tag in entry["genre"]:
                if tag in genres:
                    genres[tag]["counter"] += 1
                    genres[tag]["shows"].append({entry["show_name"]: entry["show_uri"]})
                else:
                    genres[tag] = {}
                    genres[tag]["counter"] = 1
                    genres[tag]["shows"] = []
                    genres[tag]["shows"].append({entry["show_name"]: entry["show_uri"]})

        write_json(genres, self.genre_outfile)


# ------ STATIC FUNKTIONS -------
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
