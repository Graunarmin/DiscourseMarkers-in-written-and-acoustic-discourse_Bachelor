import json
import sys

'''use main.py to execute the code with keyword 'parser' '''
class CorpusParser:

    def __init__(self, filename, arguments):
        #ToDo:
        #use arguments to specify what should be extracted, e.g. show_names or cities

        self.filename = filename
        self.currentCity = None
        #{"cityName":{'Ctr':123, 'Signatures':{123,345,567,789}}}
        self.cities = {}
        self.current_show = None
        self.show_counter = 0
        self.irregular_json = None
        self.firstEntry = True;

    def read_lines(self):
        '''read in the file line by line, processing each line before loading the next one'''

        json_object = None

        with open(self.filename) as file:
            for cnt, row in enumerate(file):
                line = row.strip()
                #print("Line {}: {}".format(cnt, line))
                flag = self.get_flag(line)

                '''determine whether the line is a complete json object
                or just the beginning/middle/end of one'''
                if flag is "c" and json_object is None: 
                    json_object = line
                    self.process_json(json_object)
                    json_object = None
                elif flag is "s":
                    json_object = line
                elif flag is "m":
                    json_object += line
                elif flag is "e":
                    json_object += line
                    self.process_json(json_object)
                    json_object = None

        with open("shows.json", 'a') as outfile:
            outfile.write("}")

    def process_json(self, json_object):
        '''load the string as json and extract the needed information'''
        json_obj = json.loads(json_object)

        #self.extract_cities(json_obj)
        self.extract_shownames(json_obj)

    def extract_cities(self, json_obj):
        '''extract city-information and write them to a file'''
        try:
            if json_obj["city"] in self.cities:
                self.cities[json_obj["city"]]["Counter"] += 1
                #print(json_obj["signature"])
                self.cities[json_obj["city"]]["Signature"].append(json_obj["signature"])
            else:
                self.cities[json_obj["city"]] = {"Counter" : 1, 
                                                "Signature":[json_obj["signature"]]}
        except KeyError as key:
            json_obj["CityKeyError"] = format(key)
            self.irregulObjects.append(json_obj)

    def extract_shownames(self, json_obj):
        '''extract show_name-information and write them to a file'''

        try:
            if json_obj["show_name"] != self.current_show:
                self.start_new_show(json_obj)
                
            self.show_counter += 1

        except KeyError as key:
            json_obj["ShowKeyError"] = format(key)
            self.write_json("irregularObjects.json",json_obj)
    
    def start_new_show(self, json_obj):
        '''a new show is about to start. Time to write the collected data into a file and start fresh'''
        if self.current_show is not None:
            self.write_json("shows.json", {self.current_show : self.show_counter})
        else:
            with open("shows.json", 'w') as outfile:
                outfile.write("{")
        self.current_show = json_obj["show_name"]
        self.show_counter = 0

    def write_json(self, out_filename, data):
        '''write json-object to file'''
        with open(out_filename, 'a') as outfile:
            text = json.dumps(data)
            #json.dump(data, outfile,indent=2)
            #format the first entry correctly
            if self.firstEntry:
                outfile.write(text.replace("{","").replace("}",""))
                self.firstEntry = False
            #following entries need a comma to separate them
            else:
                outfile.write(text.replace("{",",\n").replace("}",""))

    '''Helper functions to determine wheter the string is a completed json-object'''

    def get_flag(self, line):
        if self.is_complete_object(line):
            return "c"
        elif self.is_start_of_object(line):
            return "s"
        elif self.is_end_of_object(line):
            return "e"
        elif self.is_middle(line):
            return "m"
        else:
            return "f"

    def is_complete_object(self, line):
        return self.is_start_of_object(line) and self.is_end_of_object(line)

    def is_start_of_object(self, line):
        return line[0] is "{"

    def is_end_of_object(self, line):
        return line[len(line)-1] is "}"

    def is_middle(self, line):
        return (not "{"in line and not "}" in line)

def main():
    file = sys.argv[1]
    parser = CorpusParser(file)
    parser.read_lines()

if __name__ == '__main__':
    main()