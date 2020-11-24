import pandas as pd
import ast
import json

"""
retrieve the sentence counts from the scores and then delete that column from the counts
"""


def seperate_sentence_counts(csvfile, outname):
    original_csv_df = pd.read_csv(csvfile)
    sentence_data = get_sentence_counts(original_csv_df)
    write_json(sentence_data, outname)


def get_sentence_counts(data):
    """
    Returns a list of counts that indicates how many sentences in this dataset contain
    as many discourse markers.
    E.g.: if  three sentences each contain 2 DM, 2 is added to the list 3 times
    :return: a list of all the counts
    """
    values = {}

    for doc in data['dm_count_sent'].dropna():
        doc_counts = ast.literal_eval(doc)

        for dm_counter in doc_counts:
            if dm_counter not in values:
                values[dm_counter] = int(doc_counts[dm_counter])
            else:
                values[dm_counter] += int(doc_counts[dm_counter])

    return values


def write_json(data, outname):
    with open(outname, 'w') as out:
        json.dump(data, out, indent=2)


def delete_sentence_count_row(csvfile, outfile):
    original_csv_df = pd.read_csv(csvfile)
    data = original_csv_df.drop(columns='dm_count_sent')
    data.set_index("document", inplace=True)
    data.to_csv(outfile)


# --------- MAIN -----------
def main():
    """
    Argument 1: data file
    Argument 2: target out file
    """
    # seperate_sentence_counts("../../bigData/listenability-tools/discourse-types/scores/gigaword-scores_short.csv",
    # "../../bigData/listenability-tools/discourse-types/scores/gigaword-sentence-scores.json")

    delete_sentence_count_row(
        "../../bigData/listenability-tools/Spotify/genres/big-scores/medium/documentary-scores_short.csv",
        "../../bigData/listenability-tools/Spotify/genres/scores/documentary-scores_short.csv")


if __name__ == '__main__':
    main()
