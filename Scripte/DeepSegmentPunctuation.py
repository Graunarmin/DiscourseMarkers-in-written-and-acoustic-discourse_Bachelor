from deepsegment import DeepSegment
import json
import sys
import logging


class DeepSegmentPunctuation:
    """
    first try to add Punctuation inbetween the snippets using the deepsegment module
    """

    def __init__(self, data, outfile):
        self.data_file = data
        self.outfile = outfile
        self.segmenter = DeepSegment('en')
        logging.getLogger("imported_module").setLevel(logging.ERROR)

        self.load_json_objects()

    def load_json_objects(self):
        with open(self.data_file) as file:
            for row in file:
                json_object = json.loads(row)
                # there is only one key (show) in every json,
                # but we still need to "loop" to get it
                for show in json_object:
                    texts = ""
                    texts = self.add_punctuation(json_object[show])

                    print("Writing ", show)
                    self.write_show_content(show, texts)

    def add_punctuation(self, json_obj):

        texts = {}
        for date in json_obj:
            sentences = self.segmenter.segment_long(json_obj[date], n_window=len(json_obj[date]))
            text = ""
            for sentence in sentences:
                text += sentence
                text += ". "
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

    punctuation = Punctuation(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
