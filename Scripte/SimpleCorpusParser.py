import json
import sys

class SimpleCorpusParser:

    def __init__(self, data):
        self.data_file = data
        self.out_file = "../data/all_shows.json"
        self.meta_file = "../data/metadata.json"
        self.current_show = None
        self.shows = set()
        self.snippet_counter = 0
        self.current_callsign = None
        self.callsigns = set()
        self.irregular_json = None
        self.firstEntry = True;
        self.entry_ctr = 0
        
        self.read_lines()

    def read_lines(self):
        '''read in the file line by line, processing each line before loading the next one'''

        with open(self.data_file) as file:
            for row in file:
                self.entry_ctr += 1
                json_object = json.loads(row)

                self.process_json(json_object)

        #after processing and writing everything into the outfile: 
        with open(self.out_file, 'a') as outfile:
            #add the last show which gets not added before because the writing gets only triggered if a new show comes up
            self.write_json(self.out_file, {self.current_show : [self.current_callsign, self.snippet_counter]})
            #and finally add the closing bracket
            outfile.write("}")
        
        self.write_metadata()

    def process_json(self, json_object):
        '''extract the needed information'''

        #extract other information?
        self.extract_shownames(json_object)

    def extract_shownames(self, json_obj):
        '''extract show_name-information and write them to a file'''

        try:
            if json_obj["show_name"] != self.current_show:
                self.start_new_show(json_obj)
                
            self.snippet_counter += 1

        except KeyError as key:
            json_obj["ShowKeyError"] = format(key)
            self.write_irrgular_entries(json_obj)
    
    def start_new_show(self, json_obj):
        '''a new show is about to start. Time to write the collected data into a file and start fresh'''

        #write data of this show to file
        if self.current_show is not None:
            self.write_json(self.out_file, {self.current_show : [self.current_callsign, self.snippet_counter]})
        else:
            with open(self.out_file, 'w') as outfile:
                outfile.write("{")

        #set showname and callsign to the new ones and counter to 0
        self.current_show = json_obj["show_name"]
        #sets only add an entry if it's not already contained
        self.shows.add(json_obj["show_name"])
        self.current_callsign = json_obj["callsign"]
        self.callsigns.add(json_obj["callsign"])
        self.snippet_counter = 0

    def write_irrgular_entries(self, json_obj):
        with open("irregular_objects.json", 'a') as file:
            json.dump(json_obj, file, indent=2)

    def write_json(self, target_file, data):
        '''write json-object to file'''
        with open(target_file, 'a') as outfile:
            text = json.dumps(data)

            #format the first entry correctly
            if self.firstEntry:
                outfile.write(text.replace("{","").replace("}",""))
                self.firstEntry = False

            #following entries need a comma to separate them
            else:
                outfile.write(text.replace("{",",\n").replace("}",""))
    
    def write_metadata(self):
        with open (self.meta_file, 'w') as metafile:
            json.dump({"total_entries":self.entry_ctr, 
                        "total_callsigns":len(self.callsigns), 
                        "total_shows":len(self.shows)}, 
                        metafile, 
                        indent=2)
def main():
    '''Argument 1: data file, here radiotalk.json'''
    parser = SimpleCorpusParser(sys.argv[1])

if __name__ == '__main__':
    main()