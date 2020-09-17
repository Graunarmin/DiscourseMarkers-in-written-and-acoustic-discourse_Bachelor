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
        outfile = "../../data/listenability-tools/marker-senses.json"
        relations_set = set()

        for entry in self.root:
            word = entry.attrib["word"]
            # print(entry.tag, entry.attrib)
            for syn in entry.findall("syn"):
                for sem in syn.findall("sem"):
                    relation = sem.find("pdtb2_relation").attrib
                    relations = relation["sense"].split(".")
                    for rel in relations:
                        relations_set.add(rel)

        types = sorted(list(relations_set))
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
    parser.get_sense()
    parser.get_cat()


if __name__ == '__main__':
    main()
