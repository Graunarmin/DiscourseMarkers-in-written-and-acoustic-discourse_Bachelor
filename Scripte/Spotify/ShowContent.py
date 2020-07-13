import json
import sys
import os


class ShowContent:

    def __init__(self):
        self.shownames = self.read_shownames()

    def read_shownames(self):
        shows = {}
        # TODO: read in show names and respective uris from csv
        return shows

    def collect_texts(self):
        # TODO: go through the directories and match the show_uris with the filenames
        #   if there is a match: read that json as data and get the text
        #   from data["alternatives"]["transcripts"]
        pass

    def write_output(self):
        # TODO: write the collected contents to a good output format (.txt)
        #   all in one? One file per show? Other?
        pass


# ------------ MAIN -------------
def main():
    """
    Optional Docstring
    """
    content = ShowContent()


if __name__ == '__main__':
    main()