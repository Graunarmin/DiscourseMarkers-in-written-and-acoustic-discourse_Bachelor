import pandas as pd
from collections import Counter


"""
Get statistis about the data for the Corpora Chapter
"""


def read_data():
    data = pd.read_csv("../../data/Spotify/relevant_shows/show-genres-types.csv")
    spotify_scores = pd.read_csv("../../bigData/listenability-tools/discourse-types/scores/spotify-scores_short.csv")
    genres = Counter(data['Category'])
    c_types = Counter(data['Type'])

    total_shows = data.shape[0]
    total_episodes = spotify_scores.shape[0]
    total_words = int(sum(spotify_scores['word_count_doc']))
    news_shows = genres['News']
    discussion_shows = genres['Opinion/Discussion']
    science_shows = genres['Science/Education']
    documentary_shows = genres['Documentary']
    monolog = c_types['Monolog']
    dialog = c_types['Dialog']
    cmonolog = c_types['Cooperative-Monolog']

    print("Total Shows:", total_shows)
    print("Total Episodes: ", total_episodes)
    print("Total Words: ", total_words)
    print("News: ", news_shows)
    print("Discussion: ", discussion_shows)
    print("Science: ", science_shows)
    print("Documentary: ", documentary_shows)
    print("Dialog: ", dialog)
    print("Monolog: ", monolog)
    print("Cmonolog: ", cmonolog)


def main():
    read_data()


if __name__ == '__main__':
    main()
