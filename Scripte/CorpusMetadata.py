import json

class CorpusMetadata():
    '''
    extract the Metadata from radiotalk.json
    '''
    
    def __init__(self, filename):
        self.meta_file = filename
        self.entry_ctr = 0 
        self.regular_entry_counter = 0
        self.irregular_entry_ctr = 0
        self.shows = 0
        self.callsigns = set()

    def add_entry(self):
        self.entry_ctr += 1
    
    def add_entries(self, number):
        self.entry_ctr += number

    def add_irregular_entry(self):
        self.irregular_entry_ctr += 1
    
    def add_regular_entry(self):
        self.regular_entry_counter += 1
    
    def add_callsign(self, callsign):
        self.callsigns.add(callsign)

    def add_show(self, callsign, snippets):
        #sets only add an entry if it's not already contained
        self.add_show(1)
        self.add_callsign(callsign)
        self.regular_entry_counter += snippets

    def add_show(self, number):
        self.shows += number

    def write_metadata(self):
        with open (self.meta_file, 'w') as metafile:
            json.dump({
                        "total_entries": self.entry_ctr,
                        "regular_entries": self.regular_entry_counter,
                        "irregular_entries": self.irregular_entry_ctr,
                        "total_shows": self.shows, 
                        "total_callsigns": len(self.callsigns), 
                        "all_callsigns": list(self.callsigns)
                        }, 
                        metafile, 
                        indent=2)
