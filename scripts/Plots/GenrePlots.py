import CreatePlots as cp
import MarkerPlots as mp
import DatasetScores as ds
import Helpers as hp


# -------- Read in data ----------
class GenreData:
    def __init__(self,
                 news_scores, news_dict, discussion_scores, discussion_dict,
                 science_scores, science_dict, documentary_scores, documentary_dict,
                 ted_scores, ted_dict,
                 markertypes=None):
        self.news = ds.DatasetScores(news_scores, news_dict, markertypes=markertypes)
        self.discussion = ds.DatasetScores(discussion_scores, discussion_dict, markertypes=markertypes)
        self.science = ds.DatasetScores(science_scores, science_dict, markertypes=markertypes)
        self.documentary = ds.DatasetScores(documentary_scores, documentary_dict, markertypes=markertypes)
        self.speech = ds.DatasetScores(ted_scores, ted_dict, markertypes=markertypes)

        # Colors:   [base, darker, lighter]
        self.news_color = '#7bd45d'
        self.news_shades = ['#7bd45d', '#569441', '#a2e08d']
        self.discussion_color = '#d45d7b'
        self.discussion_shades = ['#d45d7b', '#944156', '#e08da2']
        self.science_color = '#5d7bd4'
        self.science_shades = ['#5d7bd4', '#415694', '#8da2e0']
        self.documentary_color = '#ff9a1c'
        self.documentary_shades = ['#FFE494', '#b26b13', '#ffb860']
        self.speech_color = '#e62b1e'
        self.speech_shades = ['#e62b1e', '#73150f', '#f2958e']


def main():
    data = GenreData("../../bigData/listenability-tools/Spotify/genres/scores/news-scores_short.csv",
                     "../../bigData/listenability-tools/Spotify/genres/dict/news_dict.json",
                     "../../bigData/listenability-tools/Spotify/genres/scores/discussion-scores_short.csv",
                     "../../bigData/listenability-tools/Spotify/genres/dict/discussion_dict.json",
                     "../../bigData/listenability-tools/Spotify/genres/scores/science-scores_short.csv",
                     "../../bigData/listenability-tools/Spotify/genres/dict/science_dict.json",
                     "../../bigData/listenability-tools/Spotify/genres/scores/documentary-scores_short.csv",
                     "../../bigData/listenability-tools/Spotify/genres/dict/documentary_dict.json",
                     "../../bigData/listenability-tools/datasets/scores/ted-scores_short.csv",
                     "../../bigData/listenability-tools/datasets/dict/ted-dict.json",
                     markertypes="../../data/listenability-tools/main-senses/words_main-sense.json")

    '''01:
    Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''

    dm_per_text_perc = [data.news.get_percent_dm_count_statistics(),
                        data.discussion.get_percent_dm_count_statistics(),
                        data.science.get_percent_dm_count_statistics(),
                        data.documentary.get_percent_dm_count_statistics(),
                        data.speech.get_percent_dm_count_statistics()]

    # cp.plot_vertical_barchart("Percent Discourse Markers per Text",
    #                           dm_per_text_perc,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Percent Markers",
    #                           label_1="News", label_2="Discussion/Opinion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           label_5="Speech",
    #                           color_1=data.news_color, color_2=data.discussion_color,
    #                           color_3=data.science_color, color_4=data.documentary_color,
    #                           color_5=data.speech_color)
    #
    # hp.show_dataframe("Percent Discourse Markers per Text", ['min', 'mean', 'mode', 'max'],
    #                   dm_per_text_perc[0], data2=dm_per_text_perc[1], data3=dm_per_text_perc[2],
    #                   data4=dm_per_text_perc[3], data5=dm_per_text_perc[4],
    #                   label1="News", label2="Discussion/Opinion",
    #                   label3="Science/Education", label4="Documentary",
    #                   label5="Speech")

    hp.effectsize_and_significance("Percent Discourse Markers per Text",
                                   dm_per_text_perc,
                                   ["News", "Discussion", "Science", "Documentary", "Speech"])

    '''02:
    Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_count_doc)
    '''
    # total_dm_count = [data.news.get_total_dm_count_statistics(),
    #                   data.discussion.get_total_dm_count_statistics(),
    #                   data.science.get_total_dm_count_statistics(),
    #                   data.documentary.get_total_dm_count_statistics(),
    #                   data.speech.get_total_dm_count_statistics()]
    #
    # cp.plot_vertical_barchart("Number Discourse Markers per Text",
    #                           total_dm_count,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Number Markers",
    #                           label_1="News", label_2="Discussion/Opinion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           label_5="Speech",
    #                           color_1=data.news_color, color_2=data.discussion_color,
    #                           color_3=data.science_color, color_4=data.documentary_color,
    #                           color_5=data.speech_color)
    #
    # hp.show_dataframe(['min', 'mean', 'mode', 'max'],
    #                   total_dm_count[0], data2=total_dm_count[1], data3=total_dm_count[2],
    #                   data4=total_dm_count[3], data5=total_dm_count[4],
    #                   label1="News", label2="Discussion/Opinion",
    #                   label3="Science/Education", label4="Documentary",
    #                   label5="Speech")

    '''03:
    Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    min/mean/max(dm_sentences_perc)
    '''
    # dm_sentences_perc = [data.news.get_percent_dm_sentences_statistics(),
    #                      data.discussion.get_percent_dm_sentences_statistics(),
    #                      data.science.get_percent_dm_sentences_statistics(),
    #                      data.documentary.get_percent_dm_sentences_statistics()]
    #
    # cp.plot_vertical_barchart("Percent of Sentences with DM per Text",
    #                           dm_sentences_perc,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "% Sentences containing DM",
    #                           label_1="News", label_2="Discussion/Opinion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           color_1=data.news_color, color_2=data.discussion_color,
    #                           color_3=data.science_color, color_4=data.documentary_color)
    #
    # hp.show_dataframe(['min', 'mean', 'mode', 'max'],
    #                   dm_sentences_perc[0], data2=dm_sentences_perc[1], data3=dm_sentences_perc[2],
    #                   data4=dm_sentences_perc[3],
    #                   label1="News", label2="Discussion/Opinion",
    #                   label3="Science/Education", label4="Documentary")

    '''04:
    Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_sentences)
    '''
    # dm_sentences_total = [data.news.get_total_dm_sentences_statistics(),
    #                       data.discussion.get_total_dm_sentences_statistics(),
    #                       data.science.get_total_dm_sentences_statistics(),
    #                       data.documentary.get_total_dm_sentences_statistics()]
    #
    # cp.plot_vertical_barchart("Number of Sentences with DM per Text",
    #                           dm_sentences_total,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "# Sentences containing DM",
    #                           label_1="News", label_2="Discussion/Opinion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           color_1=data.news_color, color_2=data.discussion_color,
    #                           color_3=data.science_color, color_4=data.documentary_color)
    #
    # hp.show_dataframe(['min', 'mean', 'mode', 'max'],
    #                   dm_sentences_total[0], data2=dm_sentences_total[1],
    #                   data3=dm_sentences_total[2], data4=dm_sentences_total[3],
    #                   label1="News", label2="Discussion/Opinion",
    #                   label3="Science/Education", label4="Documentary")

    '''05:
    Number of DM per sentence
    '''
    # dm_per_sent_total = [data.news.get_total_dm_per_sentence_statistics(),
    #                      data.discussion.get_total_dm_per_sentence_statistics(),
    #                      data.science.get_total_dm_per_sentence_statistics(),
    #                      data.documentary.get_total_dm_per_sentence_statistics()]
    #
    # cp.plot_vertical_barchart("Number of Discourse Markers per Sentence",
    #                           dm_per_sent_total,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "# Markers per Sentence",
    #                           label_1="News", label_2="Discussion/Opinion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           color_1=data.news_color, color_2=data.discussion_color,
    #                           color_3=data.science_color, color_4=data.documentary_color)
    #
    # hp.show_dataframe(['min', 'mean', 'mode', 'max'],
    #                   dm_per_sent_total[0], data2=dm_per_sent_total[1],
    #                   data3=dm_per_sent_total[2], data4=dm_per_sent_total[3],
    #                   label1="News", label2="Discussion/Opinion",
    #                   label3="Science/Education", label4="Documentary")

    '''06:
    Histogram with Number of DM per Sentence per Dataset
    '''
    # dm_per_sent = [data.news.compute_dm_per_sentence(),
    #                data.discussion.compute_dm_per_sentence(),
    #                data.science.compute_dm_per_sentence(),
    #                data.documentary.compute_dm_per_sentence()]
    #
    # cp.draw_simple_barchart("Number of Discourse Markers per Sentence",
    #                         ["News", "Discussion/Opinion", "Science/Education", "Documentary"],
    #                         dm_per_sent,
    #                         [data.news_color, data.discussion_color, data.science_color, data.documentary_color])

    '''07:
    Percentage of DM at certain positions in a sentence
    '''
    # dm_pos_sent = [data.news.get_percent_dm_positions_sentence(),
    #                data.discussion.get_percent_dm_positions_sentence(),
    #                data.science.get_percent_dm_positions_sentence(),
    #                data.documentary.get_percent_dm_positions_sentence()]
    #
    # cp.plot_vertical_barchart("% of DM in a Position in a Sentence",
    #                           dm_pos_sent,
    #                           ["begin", "middle", "end"],
    #                           "% DM at Postion",
    #                           label_1="News", label_2="Discussion/Opinion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           color_1=data.news_color, color_2=data.discussion_color,
    #                           color_3=data.science_color, color_4=data.documentary_color)
    #
    # hp.show_dataframe(['begin', 'middle', 'end'],
    #                   dm_pos_sent[0], data2=dm_pos_sent[1],
    #                   data3=dm_pos_sent[2], data4=dm_pos_sent[3],
    #                   label1="News", label2="Discussion/Opinion",
    #                   label3="Science/Education", label4="Documentary")

    '''08:
    Number of DM at certain positions in a sentence
    '''
    # dm_pos_sent_total = [data.news.get_total_dm_positions_sentence(),
    #                      data.discussion.get_total_dm_positions_sentence(),
    #                      data.science.get_total_dm_positions_sentence(),
    #                      data.documentary.get_total_dm_positions_sentence()]
    #
    # cp.plot_vertical_barchart("Number of DM at a certain Position in a Sentence",
    #                           dm_pos_sent_total,
    #                           ["begin", "middle", "end"],
    #                           "# DM at Postion",
    #                           label_1="News", label_2="Discussion/Opinion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           color_1=data.news_color, color_2=data.discussion_color,
    #                           color_3=data.science_color, color_4=data.documentary_color)
    #
    # hp.show_dataframe(['begin', 'middle', 'end'],
    #                   dm_pos_sent_total[0], data2=dm_pos_sent_total[1],
    #                   data3=dm_pos_sent_total[2], data4=dm_pos_sent_total[3],
    #                   label1="News", label2="Discussion/Opinion",
    #                   label3="Science/Education", label4="Documentary")

    # '''
    # Piechart of DM at certain positions in a sentence per Dataset
    # '''
    # cp.plot_dm_position_piechart("Number of DM in a Sentence at Position:",
    #                              [data.spotify.get_sentence_position_values(),
    #                               data.ny.get_sentence_position_values(),
    #                               data.gig.get_sentence_position_values()
    #                               ],
    #                              ["Spotify Data", "NYTimes Data", "Gigaword Data"],
    #                              [data.spotify_shades,
    #                               data.ny_shades,
    #                               data.gig_shades])
    '''
    ---- Document Positions ----
    '''

    '''09:
    Percentage of DM at certain positions in a document
    '''
    # dm_pos_doc_perc = [data.news.get_percent_dm_positions_document(),
    #                    data.discussion.get_percent_dm_positions_document(),
    #                    data.science.get_percent_dm_positions_document(),
    #                    data.documentary.get_percent_dm_positions_document(),
    #                    data.speech.get_percent_dm_positions_document()]
    #
    # cp.plot_vertical_barchart("% of DM in a Position in a Document",
    #                           dm_pos_doc_perc,
    #                           ["begin", "middle", "end"],
    #                           "% DM at Postion",
    #                           label_1="News", label_2="Discussion/Opinion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           label_5="Speech",
    #                           color_1=data.news_color, color_2=data.discussion_color,
    #                           color_3=data.science_color, color_4=data.documentary_color,
    #                           color_5=data.speech_color)
    #
    # hp.show_dataframe(["begin", "middle", "end"],
    #                   dm_pos_doc_perc[0], data2=dm_pos_doc_perc[1], data3=dm_pos_doc_perc[2],
    #                   data4=dm_pos_doc_perc[3], data5=dm_pos_doc_perc[4],
    #                   label1="News", label2="Discussion/Opinion",
    #                   label3="Science/Education", label4="Documentary",
    #                   label5="Speech")

    '''10:
    Number of DM at certain positions in a document
    '''
    # dm_pos_doc_total = [data.news.get_total_dm_positions_document(),
    #                     data.discussion.get_total_dm_positions_document(),
    #                     data.science.get_total_dm_positions_document(),
    #                     data.documentary.get_total_dm_positions_document(),
    #                     data.speech.get_percent_dm_positions_document()]
    #
    # cp.plot_vertical_barchart("Number of DM at a certain Position in a Document",
    #                           dm_pos_doc_total,
    #                           ["begin", "middle", "end"],
    #                           "# DM at Postion",
    #                           label_1="News", label_2="Discussion/Opinion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           label_5="Speech",
    #                           color_1=data.news_color, color_2=data.discussion_color,
    #                           color_3=data.science_color, color_4=data.documentary_color,
    #                           color_5=data.speech_color)
    #
    # hp.show_dataframe(["begin", "middle", "end"],
    #                   dm_pos_doc_total[0], data2=dm_pos_doc_total[1], data3=dm_pos_doc_total[2],
    #                   data4=dm_pos_doc_total[3], data5=dm_pos_doc_total[4],
    #                   label1="News", label2="Discussion/Opinion",
    #                   label3="Science/Education", label4="Documentary",
    #                   label5="Speech")
    # # '''
    # # Piechart of DM at certain positions in a document per Dataset
    # # '''
    # #
    # # cp.plot_dm_position_piechart("Positions of Discourse Markers in the Documents",
    # #                              [data.spotify.get_document_position_values(),
    # #                               data.ted.get_document_position_values(),
    # #                               data.ny.get_document_position_values(),
    # #                               data.gig.get_document_position_values()
    # #                               ],
    # #                              ["Spotify Data", "TED Data", "NYTimes Data", "Gigaword Data"],
    # #                              [data.spotify_shades,
    # #                               data.ted_shades,
    # #                               data.ny_shades,
    # #                               data.gig_shades])

    '''
    ---- Number of Occurences per Discourse Marker per Dataset ----
    '''

    '''
    01_a: Most Common Markers per Genre - Average per Doc
    '''
    # most_common_markers = [data.news.get_most_common_markers(15, average='Doc'),
    #                        data.discussion.get_most_common_markers(15, average='Doc'),
    #                        data.science.get_most_common_markers(15, average='Doc'),
    #                        data.documentary.get_most_common_markers(15, average='Doc'),
    #                        data.speech.get_most_common_markers(15, average='Doc')]
    #
    # mp.most_common_markers_plot("Most Common Markers per Genre", "Average Number of Occurences per Document",
    #                             most_common_markers[0],
    #                             "News", data.news_color,
    #                             data2=most_common_markers[1],
    #                             label2="Discussion/Opinion", color2=data.discussion_color,
    #                             data3=most_common_markers[2],
    #                             label3="Science", color3=data.science_color,
    #                             data4=most_common_markers[3],
    #                             label4="Documentary", color4=data.documentary_color,
    #                             data5=most_common_markers[4],
    #                             label5="Speech", color5=data.speech_color,
    #                             share=True)
    #
    # markers, x_values = hp.compile_most_common_marker_list(most_common_markers,
    #                                                        ["News", "Discussion", "Science", "Documentary", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Document",
    #                             "News", label_2="Discussion", label_3="Science", label_4="Documentary",
    #                             label_5="Speech", color_1=data.news_color, color_2=data.discussion_color,
    #                             color_3=data.science_color, color_4=data.documentary_color, color_5=data.speech_color)

    '''
    01_b: Most Common Markers per Genre - Average per Sentence
    '''

    # most_common_markers = [data.news.get_most_common_markers(15, average='Sent'),
    #                        data.discussion.get_most_common_markers(15, average='Sent'),
    #                        data.science.get_most_common_markers(15, average='Sent'),
    #                        data.documentary.get_most_common_markers(15, average='Sent')]
    #
    # markers, x_values = hp.compile_most_common_marker_list(most_common_markers,
    #                                                        ["News", "Discussion", "Science", "Documentary"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Sentence",
    #                             "News", label_2="Discussion", label_3="Science", label_4="Documentary",
    #                             color_1=data.news_color, color_2=data.discussion_color,
    #                             color_3=data.science_color, color_4=data.documentary_color)

    '''
    02: Most Common Markers per Genre - In Percent
    '''
    # most_common_markers_perc = [data.news.get_most_common_markers(15, perc=True),
    #                             data.discussion.get_most_common_markers(15, perc=True),
    #                             data.science.get_most_common_markers(15, perc=True),
    #                             data.documentary.get_most_common_markers(15, perc=True),
    #                             data.speech.get_most_common_markers(15, perc=True)]
    #
    # # mp.most_common_markers_plot("Most Common Markers per Genre in %", "Share in all Markers",
    # #                             most_common_markers_perc[0],
    # #                             "News", data.news_color,
    # #                             data2=most_common_markers_perc[1],
    # #                             label2="Discussion/Opinion", color2=data.discussion_color,
    # #                             data3=most_common_markers_perc[2],
    # #                             label3="Science", color3=data.science_color,
    # #                             data4=most_common_markers_perc[3],
    # #                             label4="Documentary", color4=data.documentary_color,
    # #                             data5=most_common_markers_perc[4],
    # #                             label5="Speech", color5=data.speech_color,
    # #                             share=True)
    #
    # markers, x_values = hp.compile_most_common_marker_list(most_common_markers_perc,
    #                                                        ["News", "Discussion", "Science", "Documentary", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers per Genre in %", markers, x_values, "Share in all Markers",
    #                             "News", label_2="Discussion", label_3="Science", label_4="Documentary",
    #                             label_5="Speech",
    #                             color_1=data.news_color, color_2=data.discussion_color,
    #                             color_3=data.science_color, color_4=data.documentary_color, color_5=data.speech_color)

    '''
    03_a: Most Common Markers per Genre - Sentence Begin
    '''
    # mp.most_common_markers_plot("Most Common Markers: Sentence Begin", "Share in all Markers at Sent. Begin",
    #                             data.spotify.get_most_common_markers(15, position="sb", perc=True),
    #                             "Spotify", data.spotify_color,
    #                             data2=data.ny.get_most_common_markers(15, position="sb", perc=True),
    #                             label2="NYTimes", color2=data.ny_color,
    #                             data3=data.gig.get_most_common_markers(15, position="sb", perc=True),
    #                             label3="Gigaword", color3=data.gig_color, share=True)
    '''
    03_b: Most Common Markers per Genre - Sentence Middle
    '''
    # mp.most_common_markers_plot("Most Common Markers: Sentence Middle", "Share in all Markers at Sent. Middle",
    #                             data.spotify.get_most_common_markers(15, position="sm", perc=True),
    #                             "Spotify", data.spotify_color,
    #                             data2=data.ny.get_most_common_markers(15, position="sm", perc=True),
    #                             label2="NYTimes", color2=data.ny_color,
    #                             data3=data.gig.get_most_common_markers(15, position="sm", perc=True),
    #                             label3="Gigaword", color3=data.gig_color, share=True)
    '''
    03_c: Most Common Markers per Genre - Sentence End
    '''
    # mp.most_common_markers_plot("Most Common Markers: Sentence End", "Share in all Markers at Sent. End",
    #                             data.spotify.get_most_common_markers(15, position="se", perc=True),
    #                             "Spotify", data.spotify_color,
    #                             data2=data.ny.get_most_common_markers(15, position="se", perc=True),
    #                             label2="NYTimes", color2=data.ny_color,
    #                             data3=data.gig.get_most_common_markers(15, position="se", perc=True),
    #                             label3="Gigaword", color3=data.gig_color, share=True)
    '''
    04_a: Most Common Markers per Genre - Document Begin
    '''
    # mp.most_common_markers_plot("Most Common Markers: Document Begin", "Share in all Markers at Doc. Begin",
    #                             data.spotify.get_most_common_markers(15, position="db", perc=True),
    #                             "Spotify", data.spotify_color,
    #                             data2=data.ted.get_most_common_markers(15, position="db", perc=True),
    #                             label2="TED", color2=data.ted_color,
    #                             data3=data.ny.get_most_common_markers(15, position="db", perc=True),
    #                             label3="NYTimes", color3=data.ny_color,
    #                             data4=data.gig.get_most_common_markers(15, position="db", perc=True),
    #                             label4="Gigaword", color4=data.gig_color, share=True)
    '''
    04_b: Most Common Markers per Genre - Document Middle
    '''
    # mp.most_common_markers_plot("Most Common Markers: Document Middle", "Share in all Markers at Doc. Middle",
    #                             data.spotify.get_most_common_markers(15, position="dm", perc=True),
    #                             "Spotify", data.spotify_color,
    #                             data2=data.ted.get_most_common_markers(15, position="dm", perc=True),
    #                             label2="TED", color2=data.ted_color,
    #                             data3=data.ny.get_most_common_markers(15, position="dm", perc=True),
    #                             label3="NYTimes", color3=data.ny_color,
    #                             data4=data.gig.get_most_common_markers(15, position="dm", perc=True),
    #                             label4="Gigaword", color4=data.gig_color, share=True)
    '''
    04_c: Most Common Markers per Genre - Document End
    '''
    # mp.most_common_markers_plot("Most Common Markers: Document End", "Share in all Markers at Doc. End",
    #                             data.spotify.get_most_common_markers(15, position="de", perc=True),
    #                             "Spotify", data.spotify_color,
    #                             data2=data.ted.get_most_common_markers(15, position="de", perc=True),
    #                             label2="TED", color2=data.ted_color,
    #                             data3=data.ny.get_most_common_markers(15, position="de", perc=True),
    #                             label3="NYTimes", color3=data.ny_color,
    #                             data4=data.gig.get_most_common_markers(15, position="de", perc=True),
    #                             label4="Gigaword", color4=data.gig_color, share=True)


if __name__ == '__main__':
    main()
