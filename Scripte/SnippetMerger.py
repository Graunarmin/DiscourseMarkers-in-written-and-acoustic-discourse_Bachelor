import json
import sys

class SnippetMerger():

    def __init__(self, data, out, seperate):
        self.snippet_file = data
        self.out_file = out
        self.separate = seperate
        self.snippets = None
        self.sorted_by_audio_id = dict()
        self.current_show = None
        self.texts = {}

        self.read_in_snippets()

    def read_in_snippets(self):
        with open (self.snippet_file) as file:
            self.snippets = json.load(file)
            for show in self.snippets:
                self.current_show = show
                self.merge_snippets(self.snippets[show])
    
    def merge_snippets(self, content):
        '''
        sort all the snippets of the current show into a dict, 
        keys are the IDs of the audio_chunks the snippets belong to.
        '''

        for snippet in content:
            #make a dict with the dates as keys
            #Then sort the respective snippets by the last part of the id
            audio_chunk_id = content[snippet].split("/")
            audio_id = "/".join(audio_chunk_id[:len(audio_chunk_id)-1])
            snippet_id = audio_chunk_id[len(audio_chunk_id)-1]

            if audio_id in self.sorted_by_audio_id:
                self.sorted_by_audio_id[audio_id][snippet_id] = snippet
            else:
                self.sorted_by_audio_id[audio_id] = {}
                self.sorted_by_audio_id[audio_id][snippet_id] = snippet
        
        #now all the snippets should be sorted under their respective id,
        #but they are not in the correct order yet.
        self.sort_snippets()
        
    
    def sort_snippets(self):
        '''
        Sort each audio_chunk entry by the snippet id, so they are in the order they were said
        and merge them together to a string
        '''

        for audio_id in self.sorted_by_audio_id:
            content = self.sorted_by_audio_id[audio_id].items()
            sorted_content = sorted(content)
            self.texts = {}
            text = ""
            for snippet_tuple in sorted_content:
                text += snippet_tuple[1].strip()
                text += self.separate + " "
            self.texts[audio_id] = text

        self.write_show_content()   
    
    def write_show_content(self):
        with open(self.out_file, 'a') as outfile:
            json.dump({self.current_show : 
                        self.texts},
                        outfile)
            outfile.write("\n")

def process_input(user_in):
    if user_in[3] == "y":
        return([user_in[1], user_in[2], "."])
    elif user_in[3] == "n":
        return([user_in[1], user_in[2], ""])

def main():
    '''
    Argument 1: json file that contains all the snippets (../bigData/news_snippets.json)
    Argument 2: out file name (../bigData/news_texts.json)
    Argument 3: if the text is to be separated by full-stops, type y, otherwise type n
    '''
    user_in = process_input(sys.argv)
    merger = SnippetMerger(user_in[0], user_in[1], user_in[2])

if __name__ == '__main__':
    main()      

