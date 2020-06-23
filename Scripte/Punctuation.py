import json
import sys
import SimplePunctuation
import DeepSegmentPunctuation as dsp
import BertPunctuation as bp


def create_raw_text(snippet_list, delimiter):
    """
    merge the snippets together so they are one string without punctuation
    """
    text = ""
    for snippet_tuple in snippet_list:
        text += snippet_tuple[1]
        text += delimiter
    return text


class Punctuation:

    def __init__(self, data_file):
        self.data = data_file
        self.simple_data = {}
        self.simple_out = "../data/simple_punct.json"
        self.deep_data = {}
        self.deep_out = "../data/deep_punct.json"
        self.bert_data = {}
        self.bert_out = "../data/bert_punct.json"

    def read_json(self):
        """
        read in the json file containing the test data
        """
        with open(self.data) as file:
            data = json.load(file)
            for show in data:
                self.add_punctuation_simple(show, data[show])
                self.add_punctuation_deepsegemnt(show, data[show])
                self.add_punctuation_bert(show, data[show])

    def add_punctuation_simple(self, show, content):
        """
        simply add a full-stop after each snippet
        """
        text = create_raw_text(content, ". ")
        self.simple_data[show] = text

    def add_punctuation_deepsegemnt(self, show, content):
        """
        add punctuation using the deepsegment module
        """

        # first put all snippets together separated by a whitespace
        text = create_raw_text(content, " ")

        # then add punctation using deepsegment
        punct = dsp.DeepSegmentPunctuation()
        self.deep_data[show] = punct.punctuate_text(text)

    def add_punctuation_bert(self, show, content):
        """
        add punctuation using the pre-trained BERT
        """
        # first put all snippets together separated by [MASK]
        text = create_raw_text(content, " [Mask] ")
        punct = bp.BertPunctuation()
        self.bert_data[show] = punct.punctuate_text(text)

    def write_output(self, show, content, out_file):
        with open(out_file, 'a') as outfile:
            pass


def main():
    """
    Argument 1: json file that holds the snippets without punctuation (../data/test_data.json)
    """

    punctuation = Punctuation(sys.argv[1])


if __name__ == '__main__':
    main()
