import json
import sys
import os
import csv


class ShowContent:

    def __init__(self, transcripts, results):

        self.data_file = "../../data/Spotify/alternative_shows.csv"
        self.transcripts_folder = transcripts
        self.result_folder = results
        self.shownames = self.read_shownames()

    def read_shownames(self):
        """
        read in sha_fow names and respective uris from csv
        """

        shows = {}
        with open(self.data_file, 'r', encoding='utf_8') as file:
            data_reader = csv.reader(file, delimiter=";")
            for row in data_reader:
                shows[row[1].replace(":", "_").replace("spotify_", "")] = {row[0]: row[3]}
        return shows

    def find_texts(self):
        """
        go through the directories and match the show_uris with the foldernames ("show_xxx")
        if there is a match: read that/the json(s) in that folder as data and get the transcripts
        from them
        """

        for root, dirs, files in os.walk(self.transcripts_folder):
            for name in dirs:
                if name in self.shownames:
                    # print(name)
                    new_root = os.path.join(root, name)
                    for n_root, n_dirs, n_files in os.walk(new_root):
                        for file_name in n_files:
                            if ".json" in file_name:
                                datafile = os.path.join(n_root, file_name)
                                path = datafile.split("/")
                                show = path[len(path)-2]
                                episode = path[len(path)-1]
                                # print(datafile)
                                with open(datafile, 'r') as file:
                                    data = json.load(file)
                                    self.collect_texts(data, episode, show)

    def collect_texts(self, data, episode, show):
        # TODO: get the text from data["alternatives"]["transcript"]
        text = ""
        for item in data["results"]:
            for alternatives in item:
                for obj in item[alternatives]:
                    for key in obj:
                        if key == "transcript":
                            text += " " + obj[key]
                            # print(text)
        self.write_episode(text, episode, show)

    def write_episode(self, text, episode, show):
        # TODO: write the collected contents to a good output format (.txt)
        #   all in one? One file per show? Other?

        path = self.result_folder + "/" + show
        if not os.path.isdir(path):
            os.makedirs(path)

        filepath = path + "/" + episode.replace(".json", ".txt")
        with open(filepath, 'w') as outfile:
            outfile.write(text, encoding='utf-8')


# ------------ MAIN -------------
def main():
    """
    Argument 1: Root folder that contains all the transcripts subdirs and files
    Argument 2: Folder where the results should be written
    """
    content = ShowContent(sys.argv[1], sys.argv[2])
    content.find_texts()


if __name__ == '__main__':
    main()