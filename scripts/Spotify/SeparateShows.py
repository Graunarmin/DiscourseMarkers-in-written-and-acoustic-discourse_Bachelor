import pandas as pd


def separate_shows_into_genres(genrelist, csvfile):
    """
    Split up the original csv file with the spotify scores
    firstly into 4 genre-specific files, each containing only the scores for their respective genre,
    and secondly into 3 discourse-type specific files
    :param genrelist: the json list that knows which show belongs to which genre and discourse type
    :param csvfile: the csv file with all the spotify scores
    :return:
    """

    original_csv_df = pd.read_csv(csvfile)
    genres_df = pd.read_csv(genrelist)

    genres = {}
    types = {}
    genres_df.set_index('URI', inplace=True)

    for show in genres_df.index:
        uri = show.split(':')[2]
        genres[uri] = genres_df.loc[show, 'Category']
        types[uri] = genres_df.loc[show, 'Type']

    science = pd.DataFrame()
    science_docs = []
    news = pd.DataFrame()
    news_docs = []
    discussion = pd.DataFrame()
    discussion_docs = []
    documentary = pd.DataFrame()
    documentary_docs = []

    monolog = pd.DataFrame()
    # create a list that can later be converted into a pandas column and so
    # be added to the dataframe
    monolog_docs = []
    dialog = pd.DataFrame()
    dialog_docs = []
    both = pd.DataFrame()
    both_docs = []

    original_csv_df.set_index('document', inplace=True)

    for doc in original_csv_df.index:
        show_id = doc.split("_")[1].split("/")[0]
        if genres[show_id] == 'Science/Education':
            # append the docname to the document-list
            science_docs.append(doc)
            # append the row with all scores to the correct dataframe
            # (index column is excluded for some reason - therefore the list above)
            science = science.append(original_csv_df.loc[doc])
        elif genres[show_id] == 'Documentary':
            documentary_docs.append(doc)
            documentary = documentary.append(original_csv_df.loc[doc])
        elif genres[show_id] == 'Opinion/Discussion':
            discussion_docs.append(doc)
            discussion = discussion.append(original_csv_df.loc[doc])
        elif genres[show_id] == 'News':
            news_docs.append(doc)
            news = news.append(original_csv_df.loc[doc])
        else:
            print("Invalid genre at " + show_id + ": " + genres[show_id])

        if types[show_id] == 'Monolog':
            monolog_docs.append(doc)
            monolog = monolog.append(original_csv_df.loc[doc])
        elif types[show_id] == 'Dialog':
            dialog_docs.append(doc)
            dialog = dialog.append(original_csv_df.loc[doc])
        elif types[show_id] == 'Cooperative-Monolog':
            both_docs.append(doc)
            both = both.append(original_csv_df.loc[doc])
        else:
            print("Invalid type: " + types[show_id])

    science['document'] = science_docs
    science.to_csv("../../data/Spotify/genres/science-shows_short.csv", index=False)
    discussion['document'] = discussion_docs
    discussion.to_csv("../../data/Spotify/genres/discussion-shows_short.csv", index=False)
    news['document'] = news_docs
    news.to_csv("../../data/Spotify/genres/news-shows_short.csv", index=False)
    documentary['document'] = documentary_docs
    documentary.to_csv("../../data/Spotify/genres/documentary-shows_short.csv", index=False)

    monolog['document'] = monolog_docs
    monolog.to_csv("../../data/Spotify/discourse-types/monolog-shows_short.csv", index=False)
    dialog['document'] = dialog_docs
    dialog.to_csv("../../data/Spotify/discourse-types/dialog-shows_short.csv", index=False)
    both['document'] = both_docs
    both.to_csv("../../data/Spotify/discourse-types/cooperative-monolog-shows_short.csv", index=False)


# --------- MAIN -----------
def main():
    separate_shows_into_genres("../../data/Spotify/relevant_shows/show-genres-types.csv",
                               "../../bigData/listenability-tools/scores/spotify-scores_short.csv")


if __name__ == '__main__':
    main()
