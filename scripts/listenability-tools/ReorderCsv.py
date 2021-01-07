import os
import pandas as pd


def get_csv_files(rootdir, columnorder, outname):
    for r, d, f in os.walk(rootdir):
        for file in f:
            if '.csv' in file:
                order_columns(os.path.join(r, file), columnorder, outname)


def order_columns(file, columnorder, outname):
    data = pd.read_csv(file)
    ordered_frame = data[columnorder]
    ordered_frame = pd.DataFrame(ordered_frame)
    ordered_frame.set_index('Data', inplace=True)
    ordered_frame.to_csv(outname)


def main():
    order_columns("../../data/listenability-tools/plots/questions/statistics/01-a_statistics.csv",
                  ["Data", "< 0.05", "P-Value", "Effectsize"],
                  "../../data/listenability-tools/plots/questions/statistics/01-a_statistics.csv")

    order_columns("../../data/listenability-tools/plots/questions/statistics/01-b_statistics.csv",
                  ["Data", "< 0.05", "P-Value", "Effectsize"],
                  "../../data/listenability-tools/plots/questions/statistics/01-b_statistics.csv")

    order_columns("../../data/listenability-tools/plots/questions/statistics/02_statistics.csv",
                  ["Data", "< 0.05", "P-Value", "Effectsize", "Statistic"],
                  "../../data/listenability-tools/plots/questions/statistics/02_statistics.csv")

    order_columns("../../data/listenability-tools/plots/questions/statistics/03_statistics.csv",
                  ["Data", "< 0.05", "P-Value", "Effectsize", "Statistic"],
                  "../../data/listenability-tools/plots/questions/statistics/03_statistics.csv")

    order_columns("../../data/listenability-tools/plots/questions/statistics/04_statistics.csv",
                  ["Data", "< 0.05", "P-Value", "Effectsize", "Statistic"],
                  "../../data/listenability-tools/plots/questions/statistics/04_statistics.csv")


if __name__ == '__main__':
    main()