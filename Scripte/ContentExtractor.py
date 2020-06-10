import csv
import json
import pickle
import sys

class ContentExtractor():

    def __init__(self, shows, data):
        self.csv_filename = shows
        self.data_filename = data
        self.show_names = []
        self.read_csv()
        self.content = {}
        self.read_lines()   
        #piece together snippets from the same audiochunk:
        #year-month-day/callsign/timestamp(?)/snippetID

    def read_csv(self):
        #read in the csv-file
        with open(self.csv_filename, 'r') as csv_file:
            show_reader= csv.reader(csv_file, delimiter = ';')
            #for each show name: 
            #   get content + audio_chunk_id
            for row in show_reader:
                self.show_names.append(row[1])
    
    def read_lines(self):
        '''read in the file line by line, processing each line before loading the next one'''

        json_object = None

        with open(self.data_filename) as file:
            for row in file:
                line = row.decode('utf-8').strip()
                json_obj = json.load(line)
                self.get_content(json_obj)
        
        self.write_json()

    def get_content(self, line):
        #for each show name: 
        #   go through the data and extract the "content" + the "audio_chunk_id":
        #   {show1:{content1:audioID1, content2:audioID2,...}, show2:{...},...}
        try:
            if line["show_name"] in self.show_names:
                if self.content[line["show_name"]]:
                    self.content[line["show_name"]][line["content"]] = line["audio_chunk_id"]
                else:
                    self.content[line["show_name"]] = {line["content"]:line["audio_chunk_id"]}
            else: 
                pass
        except KeyError as k_error:
            #add some error handling
            pass

    def write_json(self):
        with open("../data/snippets.json", 'w') as outfile:
            json.dump(self.content, outfile, indent=2)

def main():
    
    extractor = ContentExtractor(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()