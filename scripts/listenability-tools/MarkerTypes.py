import xml.etree.ElementTree as ET
import sys
import json


def parse_xml(xmlfile, outfile):
    """
    parses the xml file containing all the discourse markers and
    retrieves their semantical sense listed under 'pdtb2_relation'.
    Writes the result to '../../data/listenability-tools/marker-types.json

    :param xmlfile: the xml file to be parsed
    :param outfile: the file to which the results are written
    :return: nothing
    """
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    relations_set = set()

    for entry in root:
        # print(entry.tag, entry.attrib)
        for syn in entry.findall("syn"):
            for sem in syn.findall("sem"):
                relation = sem.find("pdtb2_relation").attrib
                relations = relation["sense"].split(".")
                for rel in relations:
                    relations_set.add(rel)

    # print(len(relations_set))
    # print(relations_set)
    types = sorted(list(relations_set))
    write_list(types, outfile)


def write_list(data, outfile):
    """
    Writes the results to the given outputfile
    :param data:
    :param outfile:
    :return:
    """

    with open(outfile, 'w') as out:
        json.dump(data,
                  out,
                  indent=2)


# ------------ MAIN -------------
def main():
    """
    Argument 1: xml file ("../../data/listenability-tools/en_dimlex.xml")
    """
    xmlfile = "../../data/listenability-tools/en_dimlex.xml"
    outfile = "../../data/listenability-tools/marker-types.json"

    parse_xml(xmlfile, outfile)


if __name__ == '__main__':
    main()