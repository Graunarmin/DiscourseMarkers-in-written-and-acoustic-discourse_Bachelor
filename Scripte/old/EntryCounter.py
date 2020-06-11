import sys
import json

class EntryCounter:
    '''
    Counts the irregular entries
    '''

    def __init__(self, data):
        self.data_file = data
        self.entry_ctr = 0
        self.key_errors = set()
        self.count_entries()

    def count_entries(self):
        with open(self.data_file) as file:
            for row in file:
                self.entry_ctr += 1
                json_object = json.loads(row)
                #self.key_errors.add(json_object["ShowKeyError"])
        
        self.write_data()
    
    def write_data(self):
        with open("../data/ireggular_metadata.json", 'w') as metafile:
            json.dump({"Total Entries": self.entry_ctr},
                        metafile,
                        indent=2)

def main():
    '''
    Argument: file with data (radiotalk.json)
    '''
    
    counter = EntryCounter(sys.argv[1])

if __name__ == '__main__':
    main()