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

        types = senses
        write_list(types, outfile)


# ------------ MAIN -------------
def main():
    """
    Argument 1: xml file ("../../data/listenability-tools/en_dimlex.xml")
    """
    xmlfile = "../../data/listenability-tools/en_dimlex.xml"

    parser = XMLParser(xmlfile)
    parser.get_number_of_senses()


if __name__ == '__main__':
    main()