import sys
import json
import csv


class CsvDescriptionWriter:

    def __init__(self, infile, outfile):
        self.data_file = infile
        self.out = outfile

    def read_json(self):
        csv_data = [["Name", "Relevance", "Genre", "Tags", "Description", "URI", "Category"]]
        with open(self.data_file, "r") as datafile:
            data = json.load(datafile)
            for show in data:
                csv_data.append([show, "", ', '.join(data[show]["genre"]), "", data[show]["description"],
                                 data[show]["show_uri"], ""])

            del data

        print(len(csv_data))
        self.write_csv(csv_data)

    def write_csv(self, csv_data):
        with open(self.out, 'w') as outfile:
            csv_writer = csv.writer(outfile, delimiter=";")
            csv_writer.writerows(csv_data)


# ------------ MAIN -------------
def main():
    """
    Argument 1: json file that contains the descriptions
    Argument 2: csv out file
    """
    description_csv = CsvDescriptionWriter(sys.argv[1], sys.argv[2])
    description_csv.read_json()


if __name__ == '__main__':
    main()
