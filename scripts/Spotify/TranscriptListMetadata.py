import sys
import csv
import os
import json


# ---------- STATIC FUNCTIONS ---------
def count_totals(data):
    """
    Count how many relevant shows this dataset contains
    and how many episodes in total
    """
    shows_total = 0
    episodes_total = 0
    for show in data:
        shows_total += 1
        data[show]["total_episodes"] = len(data[show]["episode_list"])
        episodes_total += data[show]["total_episodes"]

    return [shows_total, episodes_total]


# ----------- CLASS ------------
class TranscriptListMetadata:

    def __init__(self, shownames, transcripts, out):
        self.datafile = shownames
        self.transcripts_folder = transcripts
        self.outile = out
        self.show_uris = self.read_shownames()

    def read_shownames(self):
        """
        read in the relevant shows from the csv file
        """
        shows = {}
        with open(self.datafile, 'r', encoding='utf_8') as datafile:
            data_reader = csv.reader(datafile, delimiter=";")
            for row in data_reader:
                shows[row[1].replace(":", "_").replace("spotify_", "")] = {
                    "name": row[0],
                    "genre": row[2],
                    "category": row[4]
                }

        return shows

    def match_shows(self):
        """
        traverse the folders with relevant transcripts and match the show uris with the previously
        read in shows to determine which show and how many episodes are in each of the two datasets
        (original podcast data and testset)
        """
        shows_found = {}

        for root, dirs, files in os.walk(self.transcripts_folder):
            for name in dirs:
                new_root = os.path.join(root, name)
                for n_root, n_dirs, n_files in os.walk(new_root):
                    for file_name in n_files:
                        if ".txt" in file_name:
                            shows_found[name] = {"name": self.show_uris[name]["name"],
                                                 "genre": self.show_uris[name]["genre"],
                                                 "category": self.show_uris[name]["category"],
                                                 "total_episodes": 0,
                                                 "episode_list": []}
                            shows_found[name]["episode_list"].append(file_name.replace(".txt", ""))

        self.write_data(shows_found)

    def write_data(self, data):
        totals = count_totals(data)
        with open(self.outile, 'w') as out_file:
            json.dump({"shows_total": totals[0],
                       "episodes_total": totals[1],
                       "show_list": data},
                      out_file,
                      indent=2)


# ------------ MAIN -------------
def main():
    """
    Argument 1: csv file that contains the relevant show names und URIs
    Argument 2: Root folder that contains all the transcript subdirs and files (Original and Testset)
    Argument 3: Outfile name
    """
    data = TranscriptListMetadata(sys.argv[1], sys.argv[2], sys.argv[3])
    data.match_shows()


if __name__ == '__main__':
    main()
