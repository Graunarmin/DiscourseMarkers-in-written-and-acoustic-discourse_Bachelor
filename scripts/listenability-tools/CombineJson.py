import json


def read_data(file1, file2, outname):
    with open(file1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)

    with open(file2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)

    combine_json(data1, data2, outname)


def combine_json(data1, data2, outname):
    combined = {"marker": {},
                "stats": {}}

    for marker in data1["marker"]:
        combined["marker"][marker] = {}
        if marker in data2["marker"]:
            combined["marker"][marker]["total"] = \
                int(data1["marker"][marker]["total"]) + int(data2["marker"][marker]["total"])
            combined["marker"][marker]["sent_begin"] = \
                int(data1["marker"][marker]["sent_begin"]) + int(data2["marker"][marker]["sent_begin"])
            combined["marker"][marker]["sent_middle"] = \
                int(data1["marker"][marker]["sent_middle"]) + int(data2["marker"][marker]["sent_middle"])
            combined["marker"][marker]["sent_end"] = \
                int(data1["marker"][marker]["sent_end"]) + int(data2["marker"][marker]["sent_end"])
            combined["marker"][marker]["doc_begin"] = \
                int(data1["marker"][marker]["doc_begin"]) + int(data2["marker"][marker]["doc_begin"])
            combined["marker"][marker]["doc_middle"] = \
                int(data1["marker"][marker]["doc_middle"]) + int(data2["marker"][marker]["doc_middle"])
            combined["marker"][marker]["doc_end"] = \
                int(data1["marker"][marker]["doc_end"]) + int(data2["marker"][marker]["doc_end"])
        else:
            combined["marker"][marker]["total"] = int(data1["marker"][marker]["total"])
            combined["marker"][marker]["sent_begin"] = int(data1["marker"][marker]["sent_begin"])
            combined["marker"][marker]["sent_middle"] = int(data1["marker"][marker]["sent_middle"])
            combined["marker"][marker]["sent_end"] = int(data1["marker"][marker]["sent_end"])
            combined["marker"][marker]["doc_begin"] = int(data1["marker"][marker]["doc_begin"])
            combined["marker"][marker]["doc_middle"] = int(data1["marker"][marker]["doc_middle"])
            combined["marker"][marker]["doc_end"] = int(data1["marker"][marker]["doc_end"])

    for marker in data2["marker"]:
        if marker not in combined["marker"]:
            combined["marker"][marker] = {}
            combined["marker"][marker]["total"] = int(data2["marker"][marker]["total"])
            combined["marker"][marker]["sent_begin"] = int(data2["marker"][marker]["sent_begin"])
            combined["marker"][marker]["sent_middle"] = int(data2["marker"][marker]["sent_middle"])
            combined["marker"][marker]["sent_end"] = int(data2["marker"][marker]["sent_end"])
            combined["marker"][marker]["doc_begin"] = int(data2["marker"][marker]["doc_begin"])
            combined["marker"][marker]["doc_middle"] = int(data2["marker"][marker]["doc_middle"])
            combined["marker"][marker]["doc_end"] = int(data2["marker"][marker]["doc_end"])

    for stat in data1["stats"]:
        combined["stats"][stat] = int(data1["stats"][stat]) + int(data2["stats"][stat])

    combined["stats"]["different_markers"] = len(combined["marker"])

    write_json(combined, outname)


def write_json(combined, outname):
    with open(outname, 'w') as out:
        json.dump(combined, out, indent=2)


def main():
    read_data("../../bigData/listenability-tools/discourse-types/dict/spotify-dict.json",
              "../../bigData/listenability-tools/discourse-types/dict/ted-dict.json",
              "../../bigData/listenability-tools/discourse-types/dict/acustic-dict.json")

    # read_data("../../bigData/listenability-tools/discourse-types/dict/nytimes-dict.json",
    #           "../../bigData/listenability-tools/discourse-types/dict/gigaword-dict.json",
    #           "../../bigData/listenability-tools/discourse-types/dict/written-dict.json")


if __name__ == '__main__':
    main()
