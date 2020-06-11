import sys
import json
import CorpusMetadata as CM

class MetadataFilteredShows:
    
    def __init__(self, data):
        self.data_file = data
        self.shows = None
        self.snippets = 0
        self.callsigns = set()

        self.meta_file = "../data/merged_shows_metadataT.json"
        self.metadata = CM.CorpusMetadata(self.meta_file)

        self.count_entries()

    def count_entries(self):
        with open(self.data_file) as file:
            self.shows = json.load(file)
        
        self.metadata.add_show(len(self.shows))
        self.count_snippets()
        self.count_callsigns()
        self.metadata.write_metadata()
        #self.write_data()

    def count_snippets(self):
        for show in self.shows:
            self.metadata.add_entries(self.shows[show]["total"])

    def count_callsigns(self):
        for show in self.shows:
            self.metadata.add_callsign(self.shows[show]["callsign"])

    def write_data(self):
        with open("../data/merged_shows_metadata.json", 'w') as metafile:
            json.dump({"total_shows": len(self.shows), 
                        "total_snipptes": self.snippets, 
                        "total_callsigns": len(self.callsigns),
                        "all_callsigs":list(self.callsigns)},
                        metafile,
                        indent=2)

def main():
    '''
    Argument: File with data, here: ../data/merged_shows.json"
    '''

    metadata = MetadataFilteredShows(sys.argv[1])

if __name__ == '__main__':
    main()