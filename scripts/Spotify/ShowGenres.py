import pandas as pd


def create_new_csv(filepath):
    """
    Reads in the csv file containing all the information about the shows
    and writes the name, uri, category (genre) and type (discourse type) columns
    to a new file
    :param filepath:
    :return:
    """
    old_csv = pd.read_csv(filepath, delimiter=";")
    columns = ['Name', 'URI', 'Category', 'Type']
    new_csv = old_csv[columns]
    new_csv.to_csv("../../data/Spotify/relevant_shows/show-genres.csv", index=False)


def main():
    create_new_csv("../../data/Spotify/relevant_shows/relevant_shows.csv")


if __name__ == '__main__':
    main()
