import os
import pandas as pd


def get_csv_files(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if ".csv" in file:
                if "statistics" not in file and "Statistics" not in file:
                    round_numbers(os.path.join(subdir, file))


def round_numbers(filepath):
    print(filepath)
    data = pd.read_csv(filepath, index_col=0)
    rounded_data = data.applymap(rounder)
    rounded_data.to_csv(filepath.replace("bigData", "data"))


def rounder(x):
    if isinstance(x, str):
        return x
    return round(x, 2)


def main():
    get_csv_files("../../data/listenability-tools/plots/discourseTypes/")


if __name__ == '__main__':
    main()