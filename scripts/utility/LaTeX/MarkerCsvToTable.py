import pandas as pd
import os


def get_csv_files(rootdir):
    for r, d, f in os.walk(rootdir):
        for file in f:
            if 'deltas.csv' in file:
                convert_marker_deltas(os.path.join(r, file))


def convert_marker_deltas(file):
    data = pd.read_csv(file)

    table = ""
    columns = data.shape[1]

    for i in range(data.shape[0]):
        column_count = 0
        for column in data:
            column_count += 1

            entry = str(data[column][i])

            table += entry

            if column_count != columns:
                table += " & "
            else:
                table += r" \\"
                table += "\n"
                table += r"\hline"
                table += "\n"

    with open(file.replace(".csv", ".txt"), "w") as txtfile:
        txtfile.write(table)


def main():

    get_csv_files("../../../data/plots/discourseTypes/marker/tables/")


if __name__ == '__main__':
    main()