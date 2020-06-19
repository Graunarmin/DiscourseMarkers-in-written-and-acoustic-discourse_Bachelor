import csv
import json
import sys

class TestData():
    '''
    Create a test dataset for testing ways to punctate as accurate as possible.
    20 Snippets from 10 Shows
    '''

    def __init__(self, shownames, data, outfile):
        self.csv_filename = shownames
        self.show_names = []
        self.get_show_names()

        self.data_file = data
        self.out_file = outfile
        self.read_show_data()

    def get_show_names(self):
        '''read in the csv-file to create a list of all relevant show names'''

        with open(self.csv_filename, 'r') as csv_file:
            show_reader= csv.reader(csv_file, delimiter = ';')

            for row in show_reader:
                self.show_names.append(row[0])

    def read_show_data(self):
        '''
        read in the data file line by line, 
        processing each line before loading the next one
        '''
        with open(self.data_filename) as file:
            for row in file:
                line = json.loads(row)
                #there is only one key but to get it we still need to "loop"
                for show in line:
                    if line in self.show_names:
                        self.add_show()

    def add_show(self):
        pass

    def sort_snippets(self):
        pass

    def write_json(self):
        pass


def main():
    '''
    Argument 1: csv file that contains all relevant show names (../data/TestData_news-shows.csv)
    Argument 2: json file that contains all the data (../bigData/news_snippets.json)
    Argument 3: outfile name
    '''

    testData = TestData(sys.argv[1], sys.argv[2], sys.argv[2])

if __name__ == '__main__':
    main()