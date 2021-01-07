import json
import sys

"""
quickly read in the (a bit messy) genres.json and create a sorted list 
of all the genres
"""


def read_genres(filename, outfile):
    genres = []
    with open(filename, 'r') as file:
        data = json.load(file)
        for genre in data:
            genres.append(genre)

    with open(outfile, 'w') as out:
        json.dump(sorted(genres), out, indent=2)


def main():
    """
    Argument 1: file to read (../../data/Spotify/genres.json)
    Argument 2: file to write (../../data/Spotify/genre_list.json)
    """
    read_genres(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
