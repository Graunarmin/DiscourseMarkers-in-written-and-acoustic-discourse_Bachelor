from deepsegment import DeepSegment
import json
import sys

class Punctuation():

    def __init__(self, data, outfile):
        self.data_file = data
        self.outfile = outfile
        

    def load_json_objects(self):
        with open (self.data_file) as file:
            for row in file:
                json_object = json.loads(row)

                self.add_punctuation(json_object)

    def add_punctuation(self, object):
        pass

    def write_text_to_file(self, text):
        pass

def main():
    '''
    Argument 1: json file that holds the snippets without punctuation
    Argument 2: out file name for the texts with punctuation
    '''

    punctuation = Punctuation(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()