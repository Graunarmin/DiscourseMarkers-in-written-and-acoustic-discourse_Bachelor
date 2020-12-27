import json


def read_data(file1, file2, outname):
    with open(file1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)

    with open(file2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)

    combine_sentence_scores(data1, data2, outname)


def combine_sentence_scores(data1, data2, outname):
    combined = {}
    for key in data1:
        if key in data2:
            combined[key] = data1[key] + data2[key]
        else:
            combined[key] = data1[key]

    for key in data2:
        if key not in combined:
            combined[key] = data2[key]

    write_json(combined, outname)


def write_json(combined, outname):
    with open(outname, 'w') as out:
        json.dump(combined, out, indent=2)


def main():
    read_data("../../bigData/listenability-tools/discourse-types/scores/sentence-scores/nytimes-sentence-scores.json",
              "../../bigData/listenability-tools/discourse-types/scores/sentence-scores/gigaword-sentence-scores.json",
              "../../bigData/listenability-tools/discourse-types/scores/sentence-scores/written-sentence-scores.json")


if __name__ == '__main__':
    main()