import os
import BertPunctuation as bp
import DeepSegmentPunctuation


# ---------- STATIC FUNCTIONS ---------
def write_result(result, path):
    with open(path, 'w') as outfile:
        outfile.write(result)


def create_short_texts(content, mask, max_length):
    """
    merge the snippets to strings that don't contain more than max_length words
    returns a list of texts
    """
    current_length = 0
    texts = []
    text = ""
    for word in content:
        if word == "<unk>":
            word = mask
        new_length = len(word)
        if (current_length + new_length) <= max_length:
            current_length += new_length
            text += word
        else:
            texts.append(text)
            current_length = new_length
            text = word

    texts.append(text)
    return texts


# -------------- CLASS --------------
class TEDPunctuation:

    def __init__(self):
        self.titles = ["911Mothers.txt", "AalaElKhani.txt", "AaronHuey.txt", "AaronKoblin.txt",
                       "AaronOConnell.txt", "AbeDavis.txt", "AbhaDawesar.txt", "AbigailMarsh.txt",
                       "AbigailWashburn.txt", "AbrahamVerghese.txt", "AchenyoIdachaba.txt", "AdamDavidson.txt"]
        self.transcript_folder = "../../bigData/TED/transcripts"
        self.bert_folder = self.transcript_folder + "/punctuation/bert/pre/"
        self.raw_folder = self.transcript_folder + "/raw/"
        self.deep_folder = self.transcript_folder + "/punctuation/deep/"
        self.bert = bp.BertPunctuation()

    def read_transcripts(self, path, function):
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if file_name in self.titles:
                    filepath = os.path.join(root, file_name)
                    name = file_name
                    with open(filepath, 'r') as file:
                        text = file.read()
                        function(text, name)

    def punctuate(self):
        self.read_transcripts(self.raw_folder, self.add_punctuation_deepsegment)
        self.read_transcripts(self.bert_folder, self.add_punctuation_bert)

    def add_punctuation_deepsegment(self, text, name):
        dsp = DeepSegmentPunctuation.DeepSegmentPunctuation()
        punct = dsp.punctuate_text(text)

        path = self.deep_folder + name
        write_result(punct, path)

    def add_punctuation_bert(self, text, name):
        mask = "[MASK]"
        punctuated_text = ""
        texts = create_short_texts(text.split(" "), mask, 400)
        for t in texts:
            if mask in t:
                punctuated_text += self.bert.punctuate_text(t, mask)
            else:
                punctuated_text += t

        path = self.bert_folder.replace("pre", "punct") + name
        write_result(punctuated_text, path)


# ------------ MAIN -------------
def main():
    """
    """
    punct = TEDPunctuation()
    punct.punctuate()


if __name__ == '__main__':
    main()
