import pandas as pd


def read_data(file, outfile):
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


def main():
    # read_data("../../data/RadioTalk/radiotalk_relevant-shows.csv",
    #           "../../data/RadioTalk/radiotalk_relevant-shows_latex.txt")

    # read_data("../../data/Spotify/relevant_shows/spotify_relevat-shows.csv",
    #           "../../data/Spotify/relevant_shows/sptify_relevant-shows_latex.txt")

    read_marker_data("../../data/listenability-tools/marker-table_er.csv",
                     "../../data/listenability-tools/marker-table-er_latex.txt")


if __name__ == '__main__':
    main()
