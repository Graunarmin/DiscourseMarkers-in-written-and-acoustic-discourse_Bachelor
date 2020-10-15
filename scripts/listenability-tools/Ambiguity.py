import xml.etree.ElementTree as ET
import sys
import json


# ---------- STATIC FUNCTIONS ---------
def parse_xml(xmlfile):
    """
    parses the xml file containing all the discourse markers and
    returns the root element

    :param xmlfile: the xml file to be parsed
    :return: nothing
    """
    tree = ET.parse(xmlfile)
    return tree.getroot()


def write_list(data, outfile):
    """
    Writes the results to the given outputfile
    :param data: the data to be written
    :param outfile: the outfile the data is written to
    :return: nothing
    """

    with open(outfile, 'w') as out:
        json.dump(data,
                  out,
                  indent=2)


def main_sense_ambiguity():
    """
    creates a dictionary with the discourse markers as keys.
    Each entry contains the sense that has the highest frequency for this word as 'main_sense',
    the frequency of that sense as 'frequency',
    the error rate if this sense is chosen over the other options as 'error_rate'
    and a list of all possible senses for this word with their respective frequencies.
    :return:
    """

    filename = "../../data/listenability-tools/main-senses/marker_sense-frequencies.json"

    with open(filename, 'r') as datafile:
        data = json.load(datafile)
        words = {}
        '''words that have more than one sense'''
        more_than_one = {}

        for word in data:
            if len(data[word]) > 1:
                more_than_one[word] = data[word]
            main_sense = None
            main_sense_frequ = -1
            for sense in data[word]:
                if data[word][sense] > main_sense_frequ:
                    main_sense = sense
                    main_sense_frequ = data[word][sense]

            ''' compute the error rate for when we always choose the main sense'''
            error_rate = compute_error_rate(data[word], main_sense, main_sense_frequ)

            words[word] = {"main_sense": main_sense,
                           "frequncy": main_sense_frequ,
                           "error_rate": error_rate,
                           "senses": data[word]}

    write_list(words, "../../data/listenability-tools/words_main-sense.json")
    # write_list(more_than_one, "../../data/listenability-tools/mt1.json")


def compute_error_rate(data, main_sense, main_frequency):
    """
    computes the error rate for a word if the main sense is choosen over the other possible senses
    :param data: the data from the specific word, containing all possible senses and frequencies
    :param main_sense: the main sense we choose for this word
    :param main_frequency: the frequency of the main sense
    :return: the error rate if the main sense is chosen
    """
    other_frequencies = 0
    for sense in data:
        if sense != main_sense:
            other_frequencies += data[sense]

    if main_frequency == 0 and other_frequencies == 0:
        return 0
    else:
        return (other_frequencies * 100) / (other_frequencies + main_frequency)


# ---------- PARSER CLASS ----------
class XMLParser:

    def __init__(self, xml_file):
        self.root = parse_xml(xml_file)

    def get_number_of_senses(self):
        outfile = "../../data/listenability-tools/ambiguity.json"
        senses = {}

        for entry in self.root:
            word = entry.attrib["word"]
            senses[word] = {}
            senses[word]["sem_categories"] = 0
            for syn in entry.findall("syn"):
                for sem in syn.findall("sem"):
                    senses[word]["sem_categories"] += 1

        more_than_one = {}
        more_than_five = {}

        for word in senses:
            for cat in senses[word]:
                if senses[word][cat] > 1:
                    more_than_one[word] = senses[word][cat]
                if senses[word][cat] > 5:
                    more_than_five[word] = senses[word][cat]

        types = senses
        # write_list(types, outfile)
        write_list(more_than_one, "../../data/listenability-tools/ambiguity_1.json")
        write_list(more_than_five, "../../data/listenability-tools/ambiguity_5.json")


# ------------ MAIN -------------
def main():
    """
    Argument 1: xml file ("../../data/listenability-tools/en_dimlex.xml")
    """
    xmlfile = "../../data/listenability-tools/en_dimlex.xml"

    parser = XMLParser(xmlfile)
    # parser.get_number_of_senses()
    main_sense_ambiguity()


if __name__ == '__main__':
    main()