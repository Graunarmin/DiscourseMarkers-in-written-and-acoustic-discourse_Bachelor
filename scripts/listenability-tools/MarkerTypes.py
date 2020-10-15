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


# ---------- PARSER CLASS ----------
class XMLParser:

    def __init__(self, xml_file):
        self.root = parse_xml(xml_file)

    def get_sense(self):
        outfile = "../../data/listenability-tools/main_senses.json"
        sense_relations = {}
        main_senses = {}

        for entry in self.root:
            word = entry.attrib["word"]
            # print(entry.tag, entry.attrib)
            for syn in entry.findall("syn"):
                for sem in syn.findall("sem"):
                    relation = sem.find("pdtb2_relation").attrib
                    print(relation)
                    frequency = 0
                    try:
                        frequency = int(relation['pdtb_freq'])
                    except KeyError as k:
                        print("No key here: ", k)
                    relations = relation["sense"].split(".")
                    if relations[0] not in main_senses:
                        main_senses[relations[0]] = {word : frequency}
                    else:
                        if word not in main_senses[relations[0]]:
                            main_senses[relations[0]][word] = frequency
                        else:
                            main_senses[relations[0]][word] += frequency
                    # for rel in relations:
                    #     if rel not in sense_relations:
                    #         print("not yet in list: " + rel)
                    #         sense_relations[rel] = [word]
                    #     else:
                    #         if word not in sense_relations[rel]:
                    #             sense_relations[rel].append(word)

        types = main_senses
        write_list(types, outfile)

    def get_frequencies(self):
        outfile = "../../data/listenability-tools/marker_frequencies.json"
        words = {}

        for entry in self.root:
            word = entry.attrib["word"]
            for syn in entry.findall("syn"):
                for sem in syn.findall("sem"):
                    relation = sem.find("pdtb2_relation").attrib
                    print(relation)
                    frequency = 0
                    try:
                        frequency = int(relation['pdtb_freq'])
                    except KeyError as k:
                        print("No key here: ", k)
                    relations = relation["sense"].split(".")
                    sense = relations[0]
                    if word not in words:
                        words[word] = {sense:frequency}
                    else:
                        if sense not in words[word]:
                            words[word][sense] = frequency
                        else:
                            words[word][sense] += frequency

        types = words
        write_list(types, outfile)

    def get_cat(self):
        outfile = "../../data/listenability-tools/marker-categories.json"
        cats = set()
        for entry in self.root:
            word = entry.attrib["word"]
            # print(entry.tag, entry.attrib)
            for syn in entry.findall("syn"):
                for category in syn.findall("cat"):
                    cats.add(category.text)
        categories = sorted(list(cats))
        write_list(categories, outfile)


# ------------ MAIN -------------
def main():
    """
    Argument 1: xml file ("../../data/listenability-tools/en_dimlex.xml")
    """
    xmlfile = "../../data/listenability-tools/en_dimlex.xml"

    parser = XMLParser(xmlfile)
    # parser.get_sense()
    # parser.get_cat()
    parser.get_frequencies()


if __name__ == '__main__':
    main()
