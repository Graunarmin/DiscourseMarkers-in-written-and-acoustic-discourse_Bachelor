import DeepSegmentPunctuation as dsp
import json
import sys
import logging


class FirstTryPunctuation:
    """
    first try to add Punctuation inbetween the snippets using the deepsegment module
    """

    def __init__(self, data, outfile):
        self.data_file = data
        self.outfile = outfile
        self.punctuation = dsp.DeepSegmentPunctuation()
        logging.getLogger("imported_module").setLevel(logging.ERROR)

        self.load_json_objects()

    def load_json_objects(self):
        with open(self.data_file) as file:
            for row in file:
                json_object = json.loads(row)
                # there is only one key (show) in every json,
                # but we still need to "loop" to get it
                for show in json_object:
                    texts = self.process_data(json_object[show])

                    print("Writing ", show)
                    self.write_show_content(show, texts)

    def process_data(self, json_obj):
        texts = {}
        for date in json_obj:
            text = self.punctuation.punctuate_text(json_obj[date])
            texts[date] = text
        return texts

    def write_show_content(self, show, texts):
        with open(self.outfile, 'a') as outfile:
            json.dump({show: texts}, outfile)
            outfile.write("\n")


def main():
    """
    Argument 1: json file that holds the snippets without punctuation (../bigData/texts_bare.json)
    Argument 2: out file name for the texts with punctuation (../bigData/texts_punctuation.json)
    """

    punctuation = FirstTryPunctuation(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
