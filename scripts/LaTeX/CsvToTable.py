import pandas as pd

"""
Read in CSV and create the content of a latex-Table from it
"""


def int_data(file, outfile):
    data = pd.read_csv(file, sep=';')

    table = ""
    columns = data.shape[1]

    for i in range(data.shape[0]):
        column_count = 0
        for column in data:
            column_count += 1

            if is_int(data[column][i]):
                number = f"{data[column][i]:,}"
                number = number.replace(",", r"\,")
                table += number
            else:
                table += str(data[column][i])
            if column_count != columns:
                table += " & "
            else:
                table += r" \\"
                table += "\n"
                table += r"\hline"
                table += "\n"

    with open(outfile, "w") as txtfile:
        txtfile.write(table)


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def read_marker_data(file, outfile):
    data = pd.read_csv(file, sep=';')

    table = ""
    columns = data.shape[1]

    for i in range(data.shape[0]):
        column_count = 0
        for column in data:
            column_count += 1

            entry = str(str(data[column][i]))
            entry = entry.replace("(", "& ").replace(")", "").replace("%", r"\%")

            table += entry

            if column_count != columns:
                table += " & "
            else:
                table += r" \\"
                table += "\n"
                table += r"\hline"
                table += "\n"

    with open(outfile, "w") as txtfile:
        txtfile.write(table)


def convert_statistics_data(file, outfile):
    data = pd.read_csv(file)

    table = ""
    columns = data.shape[1]

    for i in range(data.shape[0]):
        column_count = 0
        for column in data:
            column_count += 1

            entry = str(str(data[column][i]))
            if column_count != 1:
                entry = entry.replace("yes", r"\color{green}\cmark")
                entry = entry.replace("no", r"\color{red}\xmark")

            table += entry

            if column_count != columns:
                table += " & "
            else:
                table += r" \\"
                table += "\n"
                table += r"\hline"
                table += "\n"

    with open(outfile, "w") as txtfile:
        txtfile.write(table)


def main():
    # int_data("../../data/RadioTalk/radiotalk_relevant-shows.csv",
    #           "../../data/RadioTalk/radiotalk_relevant-shows_latex.txt")

    # int_data("../../data/Spotify/relevant_shows/spotify_relevat-shows.csv",
    #           "../../data/Spotify/relevant_shows/sptify_relevant-shows_latex.txt")

    # read_marker_data("../../data/listenability-tools/marker-table_er.csv",
    #                  "../../data/listenability-tools/marker-table-er_latex.txt")

    # convert_statistics_data("../../data/listenability-tools/plots/questions/statistics/01-a_statistics.csv",
    #                         "../../data/listenability-tools/plots/questions/statistics/01-a_statistics.txt")

    convert_statistics_data("../../data/listenability-tools/plots/questions/statistics/01-b_statistics.csv",
                            "../../data/listenability-tools/plots/questions/statistics/01-b_statistics.txt")

    convert_statistics_data("../../data/listenability-tools/plots/questions/statistics/02_statistics.csv",
                            "../../data/listenability-tools/plots/questions/statistics/02_statistics.txt")

    convert_statistics_data("../../data/listenability-tools/plots/questions/statistics/03_statistics.csv",
                            "../../data/listenability-tools/plots/questions/statistics/03_statistics.txt")

    convert_statistics_data("../../data/listenability-tools/plots/questions/statistics/04_statistics.csv",
                            "../../data/listenability-tools/plots/questions/statistics/04_statistics.txt")


if __name__ == '__main__':
    main()
