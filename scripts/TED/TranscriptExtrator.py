import os
import sys


# ---------- STATIC FUNCTIONS ------------
def write_transctipt(text, path, name):
    """
    write the transcripts to files
    """
    filepath = path + name + ".txt"
    with open(filepath, 'wb') as outfile:
        outfile.write(text.encode('utf-8'))


# ---------- CLASS -----------
class TranscriptExtractor:

    def __init__(self, speeches):
        self.speech_folder = speeches
        self.begin_tag = "<NA>"
        self.trancript_path = "../../bigData/TED/transcripts/raw/"
        self.simple_punctuation_path = "../../bigData/TED/transcripts/punctuation/simple/"
        self.bert_punctuation_path = "../../bigData/TED/transcripts/punctuation/bert/pre/"

    def read_files(self):
        """
        read in and open the files from the given path
        """
        for root, dirs, files in os.walk(self.speech_folder):
            for file_name in files:
                if ".stm" in file_name:
                    filepath = os.path.join(root, file_name)
                    name = file_name.split("_")[0]
                    self.extract_transcript(filepath, name)

    def extract_transcript(self, path, name):
        """
        Extract the actual text from the stm file, that also contains a title,
        timestamp and other metadata in every row. This metadata needs to be
        filtered out.
        """
        char_list = []
        with open(path, 'r', encoding='utf_8') as file:
            data = file.read()
            '''text is read in char per char'''
            for char in data:
                char_list.append(char)

            '''create a text from all the chars'''
            text = "".join(char_list)

            '''then split it as to remove the title in front if each line'''
            splitted_text = text.split("<NA>")

            '''each text line is connected with the next title through a "\n"'''
            second_split = []
            for entry in splitted_text:
                second_split.append(entry.split("\n"))

            '''now each sub-array is a 2-tuple of [text,title] 
            (except for first and last entry):
            [[title], [text, title], [text, title] , ... ,[text]]'''

            text_list = []
            for entry in second_split:
                text_list.append(entry[0])

            '''remove the first entry, which is only a title'''
            del text_list[0]

            self.raw(text_list, name)
            self.simple_punctuation(text_list, name)
            self.bert_preprocessing(text_list, name)

    def raw(self, text_list, name):
        """
        prepare the text as a raw text without any punctuation attempt
        """
        transcript = "".join(text_list)

        if not os.path.isdir(self.trancript_path):
            os.makedirs(self.trancript_path)

        write_transctipt(transcript, self.trancript_path, name)

    def simple_punctuation(self, text_list, name):
        """
        add a full-stop at every "break"
        """
        transcript = ".".join(text_list)
        transcript += "."

        if not os.path.isdir(self.simple_punctuation_path):
            os.makedirs(self.simple_punctuation_path)

        write_transctipt(transcript, self.simple_punctuation_path, name)

    def bert_preprocessing(self, text_list, name):
        """
        preprocess text for BERT Punctuation by adding [MASK] at every break
        """
        transcript = "[MASK]".join(text_list)
        transcript += "[MASK]"

        if not os.path.isdir(self.bert_punctuation_path):
            os.makedirs(self.bert_punctuation_path)

        write_transctipt(transcript, self.bert_punctuation_path, name)


# ------------ MAIN -------------
def main():
    """
    Argument 1: Path to the folder that contains the speeches as .stm files
    """
    extract = TranscriptExtractor(sys.argv[1])
    extract.read_files()


if __name__ == '__main__':
    main()
