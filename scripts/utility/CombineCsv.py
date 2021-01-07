import pandas as pd
import os


def read_data(files, outname):

    combined = pd.concat([pd.read_csv(file) for file in files])

    values_dataframe = pd.DataFrame(combined)
    values_dataframe.set_index('document', inplace=True)

    combined.to_csv(outname)


def get_csv_files(rootdir, outname):
    files = []
    for r, d, f in os.walk(rootdir):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))

    combine_statistics(sorted(files), outname)


def combine_statistics(files, outname):
    columns = ["Data", "0.1 significant", "P-Value", "Effectsize"]
    combined = pd.concat([pd.read_csv(file, usecols=columns) for file in files])

    values_dataframe = pd.DataFrame(combined)
    rounded_data = values_dataframe.applymap(rounder)
    rounded_data.set_index('Data', inplace=True)
    rounded_data = rounded_data.rename(columns={"0.1 significant": "< 0.05"})
    rounded_data.to_csv(outname)


def rounder(x):
    try:
        if float(x) < 0:
            return round(float(x), 3)
        if float(x) < 0.001:
            return "< 0.001"
        return round(float(x), 3)
    except ValueError:
        if isinstance(x, str):
            return x


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

    # read_data(["../../bigData/listenability-tools/discourse-types/scores/marker-scores/nytimes-marker.csv",
    #            "../../bigData/listenability-tools/discourse-types/scores/marker-scores/gigaword-marker.csv"],
    #           "../../bigData/listenability-tools/discourse-types/scores/marker-scores/written-marker.csv")

    get_csv_files("../../data/listenability-tools/plots/questions/1/A",
                  "../../data/listenability-tools/plots/questions/1/A/statistics.csv")

    get_csv_files("../../data/listenability-tools/plots/questions/1/B",
                  "../../data/listenability-tools/plots/questions/1/B/statistics.csv")

    get_csv_files("../../data/listenability-tools/plots/questions/2",
                  "../../data/listenability-tools/plots/questions/2/statistics.csv")

    get_csv_files("../../data/listenability-tools/plots/questions/3",
                  "../../data/listenability-tools/plots/questions/3/statistics.csv")

    get_csv_files("../../data/listenability-tools/plots/questions/4",
                  "../../data/listenability-tools/plots/questions/4/statistics.csv")


if __name__ == '__main__':
    main()
