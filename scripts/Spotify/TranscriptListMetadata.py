import sys
import csv
import os
import json


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
        with open(self.datafile, 'r') as datafile:
            data_reader = csv.reader(datafile, delimiter=";")
            for row in data_reader:
                shows[row[1].replace(":", "_").replace("spotify_", "")] = {
                    "genre": row[2],
                    "category": row[4],
                    "episode_list": []
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
                shows_found[name]
                new_root = os.path.join(root, name)
                for n_root, n_dirs, n_files in os.walk(new_root):
                    for file_name in n_files:
                        if ".txt" in file_name:
                            self.show_uris[name]["episode_list"].append(file_name.replace(".txt", ""))

    def write_data(self):
        pass
