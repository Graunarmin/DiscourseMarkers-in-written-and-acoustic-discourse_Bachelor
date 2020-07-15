import json
import sys
import os
import csv


class ShowContent:

    def __init__(self, shows, transcripts, results):

        self.data_file = shows
        self.transcripts_folder = transcripts
        self.result_folder = results
        self.show_uris = self.read_shownames()

    def read_shownames(self):
        """
        read in sha_fow names and respective uris from csv
        shows = {"show_uri": ["show_name","show_category"], ...}
        """

        shows = {}
        with open(self.data_file, 'r', encoding='utf_8') as file:
            data_reader = csv.reader(file, delimiter=";")
            for row in data_reader:
                shows[row[1].replace(":", "_").replace("spotify_", "")] = [row[0], row[4]]
        return shows

    def find_texts(self):
        """
        go through the directories and match the show_uris with the foldernames ("show_xxx")
        if there is a match: read that/the json(s) in that folder as data and get the transcripts
        from them
        """

        for root, dirs, files in os.walk(self.transcripts_folder):
            for name in dirs:
                if name in self.show_uris:
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
        """
        get the text from data["results"]
        Format:
        {"results":[{"alternatives":[{"transcript":"...",...},{...},...]},
                    {"alternatives":[{"transcript":"...",...},{...},...]},
                    ...
                    ]
        }
        """
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
        """
        write the collected contents to output (.txt)
        """
        # TODO: which format all in one? One file per show? Per Episode?

        path = self.result_folder + "/" + show
        if not os.path.isdir(path):
            os.makedirs(path)

        filepath = path + "/" + episode.replace(".json", ".txt")
        with open(filepath, 'wb') as outfile:
            outfile.write(text.encode('utf-8'))


# ------------ MAIN -------------
def main():
    """
    Argument 1: csv file that contains the relevant show names und URIs
    Argument 2: Root folder that contains all the transcripts subdirs and files
    Argument 3: Folder where the results should be written
    """
    content = ShowContent(sys.argv[1], sys.argv[2])
    content.find_texts()


if __name__ == '__main__':
    main()
