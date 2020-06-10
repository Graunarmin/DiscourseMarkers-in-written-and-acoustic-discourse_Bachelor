import json
import sys

class ShowFilter:

    def __init__(self, data, outfile):
        self.in_file = data
        self.out_file = outfile
        self.filtered_shows = {}
        
        self.read_in_shows()

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
                self.filtered_shows[key][total] += shows[key][1]
            else:
                self.filtered_shows[key] = {}
                self.filtered_shows[key]["total"] = shows[key][1]
                self.filtered_shows[key]["callsign"] = shows[key][0]
    
    def write_output(self):
        '''write output to json or pickle or csv'''
        with open(self.out_file, 'w') as outfile:
            json.dump(self.filtered_shows, outfile, indent=2)


def main():
    show_filter = ShowFilter(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()