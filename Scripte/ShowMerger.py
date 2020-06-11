import json
import sys
import CorpusMetadata as CM

class ShowMerger:
    '''
    Merge shows with the same name
    '''

    def __init__(self, data, outfile):
        self.in_file = data
        self.out_file = outfile
        self.merged_shows = {}

        self.read_in_shows()

    def read_in_shows(self):
        '''read in all shows as json object'''
        shows = []
        with open(self.in_file) as file:
            for row in file:
                show = json.loads(row)
                shows.append(show)
                    

        self.merge_shows(shows)
        print(self.merged_shows)
        #self.write_output()


    def merge_shows(self, shows):
        '''go through json and put them all into a dict:
            if the entry already exists, only add to counter'''

        for show in shows:
            for key in show:
                if key in self.merged_shows:
                    self.merged_shows[key][total] += show[key][1]
                    print(shows[key][1])
                else:
                    self.merged_shows[key] = {}
                    self.merged_shows[key]["total"] = show[key][1]
                    self.merged_shows[key]["callsign"] = show[key][0]
    
    def write_output(self):
        '''write output to json or pickle or csv'''
        with open(self.out_file, 'w') as outfile:
            json.dump(self.merged_shows, outfile, indent=2)


def main():
    '''
    Argument 1: file with all the shows (../data/all_shows.json)
    Argument 2: out file name (../data/merged_shows.json)
    '''
    show_filter = ShowMerger(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()