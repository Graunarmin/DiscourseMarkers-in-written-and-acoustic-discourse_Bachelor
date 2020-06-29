import json
import sys
import RadioTalk.CorpusMetadata as CM


class SimpleCorpusParser:
    """
    parse the huge JSONL radiotalk.json line by line,
    extract all recorded shows with their respective callsign and number of snippets
    Shows may be added multiple times as the data is sorted and progressed day by day.
    Many shows were recorded several times on different days.
    """

    def __init__(self, data):
        self.data_file = data
        self.out_file = "../data/all_shows.json"
        self.meta_file = "../data/metadata/radioTalk_metadata.json"

        self.metadata = CM.CorpusMetadata(self.meta_file)

        self.firstEntry = True;
        self.current_show = None
        self.current_callsign = None
        self.snippet_counter = 0

        self.read_lines()

    def read_lines(self):
        """
        read in the file line by line, processing each line before loading the next one
        """

        with open(self.data_file) as file:
            for row in file:
                json_object = json.loads(row)

                self.metadata.add_entry(1)
                self.process_json(json_object)

        '''
        after processing and writing everything into the outfile:
        add the last show which gets not added before because the writing 
        gets only triggered if a new show comes up
        '''
        self.write_json({self.current_show: [self.current_callsign, self.snippet_counter]})
        self.metadata.add_show(1)
        self.metadata.add_callsign(self.current_callsign)

        self.metadata.write_metadata()

    def process_json(self, json_object):
        """
        extract the needed information
        """

        # extract other information?
        self.extract_shownames(json_object)

    def extract_shownames(self, json_obj):
        """
        extract show_name-information and write them to a file
        """

        try:
            # if we have a valid entry with a show name:
            if "show_name" in json_obj:
                # if a new show starts:
                if json_obj["show_name"] != self.current_show:
                    self.start_new_show(json_obj)

                # in any case: increase the snippet counter
                self.snippet_counter += 1
                self.metadata.add_regular_entry(1)
            else:
                self.metadata.add_irregular_entry(1)
        except KeyError as key:
            self.metadata.add_irregular_entry(1)

    def start_new_show(self, json_obj):
        """
        a new show is about to start. Time to write the collected data into a file and start fresh
        """

        # write data of this show to file
        if self.current_show is not None:
            self.write_json({self.current_show: [self.current_callsign, self.snippet_counter]})

        '''Metadata'''
        self.metadata.add_show(1)
        self.metadata.add_callsign(json_obj["callsign"])

        '''set showname and callsign to the new ones and counter to 0'''
        self.current_show = json_obj["show_name"]
        self.current_callsign = json_obj["callsign"]
        self.snippet_counter = 0

    def write_json(self, data):
        """
        write json-object to file
        """
        with open(self.out_file, 'a') as outfile:
            json.dump(data, outfile)
            outfile.write("\n")


# --------- MAIN -----------
def main():
    """
    Argument 1: data file, here radiotalk.json
    """
    parser = SimpleCorpusParser(sys.argv[1])


if __name__ == '__main__':
    main()
