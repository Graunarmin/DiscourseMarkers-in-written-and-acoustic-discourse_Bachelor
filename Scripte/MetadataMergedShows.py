import sys
import json
import CorpusMetadata as CM

class MetadataMergedShows:
    '''
    Extract Metadata from the merged show list using the CorpusMetadata module
    Argument: File with data, here: ../data/merged_shows.json"
    '''
    
    def __init__(self, data):
        self.data_file = data
        self.shows = None
        self.snippets = 0
        self.callsigns = set()

        self.meta_file = "../data/merged_shows_metadata.json"
        self.metadata = CM.CorpusMetadata(self.meta_file)

        self.load_entries()
        self.process()

    def load_entries(self):
        with open(self.data_file) as file:
            self.shows = json.load(file)
        
    def process(self):
        self.count_shows()   
        self.count_snippets()
        self.count_callsigns()
        self.metadata.write_metadata()

    def count_shows(self):
        self.metadata.add_show(len(self.shows))

    def count_snippets(self):
        for show in self.shows:
            self.metadata.add_entry(self.shows[show]["total"])

    def count_callsigns(self):
        for show in self.shows:
            self.metadata.add_callsign(self.shows[show]["callsign"])

def main():
    '''
    Argument: File with data, here: ../data/merged_shows.json"
    '''

    metadata = MetadataFilteredShows(sys.argv[1])

if __name__ == '__main__':
    main()