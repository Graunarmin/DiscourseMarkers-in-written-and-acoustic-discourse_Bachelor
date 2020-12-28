import pandas as pd


def read_data(files, outname):
    combined = pd.concat([pd.read_csv(file) for file in files])

    values_dataframe = pd.DataFrame(combined)
    values_dataframe.set_index('document', inplace=True)

    combined.to_csv(outname)


def main():
    # read_data(["../../bigData/listenability-tools/discourse-types/scores/spotify-scores_short.csv",
    #            "../../bigData/listenability-tools/discourse-types/scores/ted-scores_short.csv"],
    #           "../../bigData/listenability-tools/discourse-types/scores/acustic-scores_short.csv")

    # read_data(["../../bigData/listenability-tools/discourse-types/scores/nytimes-scores_short.csv",
    #            "../../bigData/listenability-tools/discourse-types/scores/gigaword-scores_short.csv"],
    #           "../../bigData/listenability-tools/discourse-types/scores/written-scores_short.csv")

    # read_data(["../../bigData/listenability-tools/discourse-types/scores/marker-scores/spotify-marker.csv",
    #            "../../bigData/listenability-tools/discourse-types/scores/marker-scores/ted-marker.csv"],
    #           "../../bigData/listenability-tools/discourse-types/scores/marker-scores/acoustic-marker.csv")

    read_data(["../../bigData/listenability-tools/discourse-types/scores/marker-scores/nytimes-marker.csv",
               "../../bigData/listenability-tools/discourse-types/scores/marker-scores/gigaword-marker.csv"],
              "../../bigData/listenability-tools/discourse-types/scores/marker-scores/written-marker.csv")


if __name__ == '__main__':
    main()