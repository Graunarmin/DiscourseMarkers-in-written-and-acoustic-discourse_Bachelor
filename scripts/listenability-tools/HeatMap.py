import pandas as pd

"""
Get Data for the Heatmaps in Chapter 5
"""
def read_data():

    dialog = pd.read_csv("../../bigData/listenability-tools/Spotify/conversation-types/scores/dialog-scores_short.csv")
    monolog = pd.read_csv("../../bigData/listenability-tools/Spotify/conversation-types/scores/monolog-scores_short.csv")
    cmonolog = pd.read_csv("../../bigData/listenability-tools/Spotify/conversation-types/scores/cooperative-monolog-scores_short.csv")
    ted = pd.read_csv("../../bigData/listenability-tools/discourse-types/scores/ted-scores_short.csv")
    news = pd.read_csv("../../bigData/listenability-tools/Spotify/genres/scores/news-scores_short.csv")
    discussion = pd.read_csv("../../bigData/listenability-tools/Spotify/genres/scores/discussion-scores_short.csv")
    science = pd.read_csv("../../bigData/listenability-tools/Spotify/genres/scores/science-scores_short.csv")
    documentary = pd.read_csv("../../bigData/listenability-tools/Spotify/genres/scores/documentary-scores_short.csv")

    conversation_types = [dialog, monolog, cmonolog, ted]
    c_type_names = ["Dialog", "Monolog", "Coop-Monolog", "Speech"]
    genres = [news, discussion, science, documentary, ted]
    genre_names = ["News", "Discussion", "Science/Education", "Documentary", "Presentation"]

    episodes_dict = {}
    words_dict = {}

    for i in range(len(conversation_types)):
        episodes_dict[c_type_names[i]] = []
        words_dict[c_type_names[i]] = []
        for j in range(len(genres)):
            matches = 0
            words = 0
            for episode, wordcount in zip(genres[j]['document'], genres[j]['word_count_doc']):
                if episode in list(conversation_types[i]['document']):
                    matches += 1
                    words += wordcount

            episodes_dict[c_type_names[i]].append(matches)
            words_dict[c_type_names[i]].append(int(words))

    create_dataframe(episodes_dict, genre_names, "episodes")
    create_dataframe(words_dict, genre_names, "words")


def create_dataframe(frame_dict, genre_names, title):
    frame_dict['Genres'] = genre_names

    values_dataframe = pd.DataFrame(frame_dict)
    values_dataframe.set_index('Genres', inplace=True)
    values_dataframe.to_csv("../../data/listenability-tools/tables/" + title + ".csv")


def main():
    read_data()


if __name__ == '__main__':
    main()

