import json

class ShowFilter:

    def __init__(self):
        self.in_file = "../bigData/shows.json"
        self.out_file = "../data/filtered_shows.json"
        self.filtered_shows = {}

    def read_in_shows(self):
        '''read in all shows as json object'''

        with open(self.in_file) as file:
            shows = json.load(file)

        self.filter_shows(shows)
        self.write_output()

        

    def filter_shows(self, shows):
        '''go through json and put them all into a dict:
                if the entry already exists, only add to counter'''

        for key in shows:
            if key in self.filtered_shows:
                self.filtered_shows[key] += shows[key]
            else:
                self.filtered_shows[key] = shows[key]
    
    def write_output(self):
        '''write output to json or pickle or csv'''
        with open(self.out_file, 'w') as outfile:
            json.dump(self.filtered_shows, outfile, indent=2)