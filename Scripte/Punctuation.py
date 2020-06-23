import json
import sys
import SimplePunctuation
import DeepSegmentPunctuation
import BertPunctuation


class Punctuation:

    def __init__(self):
        pass

    def read_json(self):
        """
        read in the json file containing the test data
        """
        pass

    def add_punctuation_simple(self):
        """
        simply add punctuation after each snippet
        """
        pass

    def add_punctuation_deepsegemnt(self):
        """
        add punctuation using the deepsegment module
        """
        pass

    def add_punctuation_bert(self):
        """
        add punctuation using the pre-trained BERT
        """
        pass


def main():
    """
    Argument 1: json file that holds the snippets without punctuation (../data/te)
    Argument 2: out file name for the texts with punctuation (../bigData/texts_punctuation.json)
    """

    punctuation = Punctuation(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()




