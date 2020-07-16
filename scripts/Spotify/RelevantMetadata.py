import sys
import json
import os


class RelevantMetadata:

    def __init__(self):
        self.root_folder = "../../../corpora/podcasts/relevant_transcripts"
        self.outfile = "../../data/Spotify/metadata/relevant_metadata.json"
        self.show_counter = 0
        self.episode_counter = 0
        self.word_counter = 0

    def read_files(self):
        for root, dirs, files in os.walk(self.root_folder):
            for dirname in dirs:
                self.show_counter += 1
            for filename in files:
                self.episode_counter += 1
                filepath = os.path.join(root, filename)
                with open(filepath, 'r') as textfile:
                    text = textfile.read()
                    self.word_counter += len(text.split())
        self.write_data()

    def write_data(self):
        with open(self.outfile, 'w') as out:
            json.dump({"total_shows": self.show_counter,
                       "total_episodes": self.episode_counter,
                       "total_words": self.word_counter,
                       "mean_words_per_episode":(self.word_counter / self.episode_counter)},
                      out,
                      indent=2)


def main():
    """
    Argument 1: file to read (../../data/Spotify/genres.json)
    Argument 2: file to write (../../data/Spotify/genre_list.json)
    """
    metadata = RelevantMetadata()
    metadata.read_files()


if __name__ == '__main__':
    main()