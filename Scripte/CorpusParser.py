import json
import sys

class CorpusParser:

    def __init__(self, filename):
        self.filename = filename
        #{"cityName":{'Ctr':123, 'Signatures':{123,345,567,789}}}
        self.cities = {}
        self.show_names = {}
        self.irregularObjects = []

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

        self.process_output()

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
            if json_obj["show_name"] in self.show_names:
                self.show_names[json_obj["show_name"]] += 1
            else:
                self.show_names[json_obj["show_name"]] = 1
        except KeyError as key:
            json_obj["ShowKeyError"] = format(key)
            self.irregularObjects.append(json_obj)

    def process_output(self):
        #write_json("cities.json", self.show_names)
        self.write_json("shows.json", self.show_names)
        self.write_json("irregular_objects.json", self.irregularObjects)

    def write_json(self, out_filename, data):
        '''write json-object to file'''
        with open(out_filename, 'w') as outfile:
            json.dump(data, outfile,indent=2)

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