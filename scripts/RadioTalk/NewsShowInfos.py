import csv
import json
import sys
import CorpusMetadata as CM


# --------- STATIC FUNCTIONS -----------
def write_show(show, content):
    with open("../bigData/news_snippets_data.json", 'a') as outfile:
        json.dump({show: content}, outfile)
        outfile.write("\n")


# --------------- CLASS -----------------
class NewsShowInfos:
    """
    Extract Content, additional Info and metadata from the news shows
    """

    def __init__(self, shows, data):
        self.csv_filename = shows
        self.data_filename = data
        self.filename_metadata = "../data/metadata/news_shows_metadata.json"
        self.metadata = CM.CorpusMetadata(self.filename_metadata)

        self.show_names = []
        self.read_csv()

        self.content = {}
        self.read_lines()

    def read_csv(self):
        """
        read in the csv-file to create a list of all relevant show names
        """

        with open(self.csv_filename, 'r') as csv_file:
            show_reader = csv.reader(csv_file, delimiter=';')

            # for each show name: get content + audio_chunk_id
            for row in show_reader:
                self.show_names.append(row[1])

        self.metadata.add_show(len(self.show_names))

    def read_lines(self):
        """
        read in the data file line by line,
        processing each line before loading the next one
        """

        with open(self.data_filename) as file:
            for row in file:
                line = json.loads(row)
                self.get_content(line)

        # write python-readable version
        # for show in self.content:
        #     self.write_show(show, self.content[show])

        # write a more human-readable version
        self.write_json()
        self.metadata.write_metadata()

        print("Done")

    def get_content(self, line):
        """
        for each show name:
           go through the data and extract the "content" + the "audio_chunk_id":
           {show1:{content1:audioID1, content2:audioID2,...}, show2:{...},...}
        """

        try:
            if line["show_name"] in self.show_names:
                if line["show_name"] in self.content:
                    self.content[line["show_name"]][line["content"]] = line["audio_chunk_id"]
                else:
                    self.content[line["show_name"]] = {line["content"]: line["audio_chunk_id"]}

                ''' Metadata '''
                self.metadata.add_entry(1)
                self.metadata.add_callsign(line["callsign"])

            else:
                pass
        except KeyError as k_error:
            # print("Key Error: ", format(k_error))
            pass

    def write_json(self):
        with open("../bigData/news_snippets.json", 'w') as outfile:
            json.dump(self.content, outfile, indent=2)


# --------- MAIN -----------
def main():
    """
    Argument 1: csv file that contains all relevant show names (../data/news_shows.csv)
    Argument 2: json file that contains all the data (radiotalk.json)
    """

    extractor = NewsShowInfos(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
