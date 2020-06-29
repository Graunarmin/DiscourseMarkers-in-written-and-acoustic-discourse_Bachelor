import json
import sys


class SnippetMerger:

    def __init__(self, data, out, seperate):
        self.snippet_file = data
        self.out_file = out
        self.separate = seperate
        self.current_show = None

        self.read_in_snippets()

    def read_in_snippets(self):
        with open(self.snippet_file) as file:
            snippets = json.load(file)
            for show in snippets:
                self.current_show = show
                self.merge_snippets(snippets[show])

    def merge_snippets(self, content):
        """
        sort all the snippets of the current show into a dict,
        keys are the IDs of the audio_chunks the snippets belong to.
        """
        sorted_by_audio_id = {}
        for snippet in content:
            # make a dict with the dates as keys
            # Then sort the respective snippets by the last part of the id
            audio_chunk_id = content[snippet].split("/")
            audio_id = "/".join(audio_chunk_id[:len(audio_chunk_id) - 2])
            snippet_id = audio_chunk_id[len(audio_chunk_id) - 1]

            if audio_id in sorted_by_audio_id:
                sorted_by_audio_id[audio_id][snippet_id] = snippet
            else:
                sorted_by_audio_id[audio_id] = {}
                sorted_by_audio_id[audio_id][snippet_id] = snippet
        # now all the snippets should be sorted under their respective id,
        # but they are not in the correct order yet.
        self.sort_snippets(sorted_by_audio_id)

    def sort_snippets(self, sorted_by_audio_id):
        """
        Sort each audio_chunk entry by the snippet id, so they are in the order they were said
        and merge them together to a string
        """
        whole_texts = {}
        for audio_id in sorted_by_audio_id:
            sorted_content = sorted(sorted_by_audio_id[audio_id].items())
            text = ""
            for snippet_tuple in sorted_content:
                text += snippet_tuple[1].strip()
                text += self.separate + " "
            whole_texts[audio_id] = text
        self.write_show_content(whole_texts)

    def write_show_content(self, texts):
        with open(self.out_file, 'a') as outfile:
            json.dump({self.current_show:
                           texts},
                      outfile)
            outfile.write("\n")


# --------- MAIN -----------
def main():
    """
    Argument 1: json file that contains all the snippets (../bigData/news_snippets.json)
    Argument 2: out file name (../bigData/news_texts.json)
    Argument 3: if the text is to be separated by full-stops, type y, otherwise type n
    """
    user_in = process_input(sys.argv)
    merger = SnippetMerger(user_in[0], user_in[1], user_in[2])


def process_input(user_in):
    if user_in[3] == "y":
        return [user_in[1], user_in[2], "."]
    elif user_in[3] == "n":
        return [user_in[1], user_in[2], ""]


if __name__ == '__main__':
    main()
