import sys
import csv
import json


class TestDataRelevantShows:
    """
    find out if the testdataset contains any of the selected relevant shows.
    If yes: run the ShowContent.py Script on the "new" Transcripts
    """

    def __init__(self, shownames, metadata, outfile):
        self.datafile = shownames
        self.metadata = metadata
        self.outfile = outfile
        self.shownames = self.read_relevant_shows()

    def read_relevant_shows(self):
        shows = []
        with open(self.datafile, 'r') as datafile:
            data_reader = csv.reader(datafile, delimiter=";")
            for row in data_reader:
                shows.append(row[1])
        # print(len(shows))
        # print(shows)
        return shows

    def find_shows(self):
        with open(self.metadata, 'r') as meta:
            meta_reader = csv.reader(meta, delimiter="\t")
            for row in meta_reader:
                # print(row[0])
                if row[0] in self.shownames:
                    print(row[1])


def main():
    """
    Argument 1: Path to file containing all relevant shownames (csv)
    Argument 2: Path to file containing the metadata from the testdataset (tsv)
    Argument 3: Name for outfile
    """
    search = TestDataRelevantShows(sys.argv[1], sys.argv[2], sys.argv[3])
    search.find_shows()


if __name__ == '__main__':
    main()