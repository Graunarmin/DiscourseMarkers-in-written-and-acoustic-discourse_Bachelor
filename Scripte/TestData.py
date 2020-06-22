import csv
import json
import sys

class TestData():
    '''
    Create a test dataset for testing ways to punctate as accurate as possible.
    20 Snippets from 10 Shows
    '''

    def __init__(self, shownames, data, outfile):
        self.csv_file = shownames
        self.show_names = []
        self.get_show_names()

        self.data_file = data
        self.out_file = outfile
        self.show_content = {}
        self.test_data = {}
        self.read_show_data()

    def get_show_names(self):
        '''read in the csv-file to create a list of all relevant show names'''

        with open(self.csv_file, 'r') as csv_file:
            show_reader= csv.reader(csv_file, delimiter = ';')

            for row in show_reader:
                self.show_names.append(row[0])

    def read_show_data(self):
        '''
        read in the data file line by line, 
        processing each line before loading the next one
        '''
        with open(self.data_file) as file:
            data = json.load(file)
            # #each show is one json object (= one line)
            # for row in file:
            #     line = json.loads(row)
            #     #there is only one key but to get it we still need to "loop"
            for show in data:
                print(show)
                if show in self.show_names:
                    self.add_show(show,data[show])
            self.write_json()

    def add_show(self, show, content):
        sorted_by_audio_id = {}
        #sorted_by_audio_id = 
        #   {audio_id_1:{snippet_id_1:snippet_1, snippet_id_2:snippet_2}, audio_id_2:{...},...}
        for snippet in content:
            audio_chunk_id = content[snippet].split("/")
            audio_id = "/".join(audio_chunk_id[:len(audio_chunk_id)-2])
            time = audio_chunk_id[len(audio_chunk_id)-2]
            snippet_id = audio_chunk_id[len(audio_chunk_id)-1]

            if audio_id in sorted_by_audio_id:
                sorted_by_audio_id[audio_id][snippet_id] = snippet
            else:
                sorted_by_audio_id[audio_id] = {}
                sorted_by_audio_id[audio_id][snippet_id] = snippet
        
        self.test_data[show] = self.sort_snippets(sorted_by_audio_id)

    def sort_snippets(self, sorted_by_audio_id):

        for audio_id in sorted_by_audio_id:
            #get the first chunk that has 20 or more snippets
            if len(sorted_by_audio_id[audio_id]) >= 20:
                #and sort them according to their snippet_id
                return sorted(int(sorted_by_audio_id[audio_id].items()))

    def write_json(self):
        print("writing")
        with open (self.out_file, 'w') as outfile:
            json.dump(self.test_data, outfile, indent=2)


def main():
    '''
    Argument 1: csv file that contains all relevant show names (../data/TestData_news-shows.csv)
    Argument 2: json file that contains all the data (../bigData/news_snippets.json)
    Argument 3: outfile name
    '''

    testData = TestData(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main()