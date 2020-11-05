import CreatePlots as cp
import MarkerPlots as mp
import DatasetScores as ds
import Helpers as hp


# -------- Read in data ----------
class GenreData:
    def __init__(self,
                 dialog_scores, dialog_dict, monolog_scores, monolog_dict,
                 cmonolog_scores, cmonolog_dict,
                 ted_scores, ted_dict,
                 markertypes=None):
        self.dialog = ds.DatasetScores(dialog_scores, dialog_dict, markertypes=markertypes)
        self.monolog = ds.DatasetScores(monolog_scores, monolog_dict, markertypes=markertypes)
        self.cmonolog = ds.DatasetScores(cmonolog_scores, cmonolog_dict, markertypes=markertypes)
        self.speech = ds.DatasetScores(ted_scores, ted_dict, markertypes=markertypes)

        # Colors:   [base, darker, lighter]
        self.dialog_color = '#7bd45d'
        self.dialog_shades = ['#7bd45d', '#569441', '#a2e08d']
        self.monolog_color = '#d45d7b'
        self.monolog_shades = ['#d45d7b', '#944156', '#e08da2']
        self.cmonolog_color = '#5d7bd4'
        self.cmonolog_shades = ['#5d7bd4', '#415694', '#8da2e0']
        self.speech_color = '#e62b1e'
        self.speech_shades = ['#e62b1e', '#73150f', '#f2958e']


def main():
    data = GenreData("../../bigData/listenability-tools/Spotify/discourse-types/scores/dialog-scores_short.csv",
                     "../../bigData/listenability-tools/Spotify/discourse-types/dict/dialog_dict.json",
                     "../../bigData/listenability-tools/Spotify/discourse-types/scores/monolog-scores_short.csv",
                     "../../bigData/listenability-tools/Spotify/discourse-types/dict/monolog_dict.json",
                     "../../bigData/listenability-tools/Spotify/discourse-types/scores/cooperative-monolog-scores_short.csv",
                     "../../bigData/listenability-tools/Spotify/discourse-types/dict/cooperative-monolog_dict.json",
                     "../../bigData/listenability-tools/datasets/scores/ted-scores_short.csv",
                     "../../bigData/listenability-tools/datasets/dict/ted-dict.json",
                     markertypes="../../data/listenability-tools/main-senses/words_main-sense.json")

    '''01:
    Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''
    dm_per_text_perc = [data.dialog.get_percent_dm_count_statistics(),
                        data.monolog.get_percent_dm_count_statistics(),
                        data.cmonolog.get_percent_dm_count_statistics(),
                        data.speech.get_percent_dm_count_statistics()]

    cp.plot_vertical_barchart("Percent Discourse Markers per Text",
                              dm_per_text_perc,
                              ["Min", "Mean", "Mode", "Max"],
                              "Percent Markers",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog", label_4="Speech",
                              color_1=data.dialog_color, color_2=data.monolog_color,
                              color_3=data.cmonolog_color, color_4=data.speech_color)

    hp.show_dataframe("Percent Discourse Markers per Text",
                      ['Min', 'Mean', 'Mode', 'Max'],
                      dm_per_text_perc[0], data2=dm_per_text_perc[1], data3=dm_per_text_perc[2],
                      data4=dm_per_text_perc[3],
                      label1="Dialog", label2="Monolog",
                      label3="Cooperative-Monolog", label4="Speech")

    hp.effectsize_and_significance("Percent Discourse Markers per Text",
                                   dm_per_text_perc,
                                   ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    '''02:
    Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_count_doc)
    '''
    total_dm_count = [data.dialog.get_total_dm_count_statistics(),
                      data.monolog.get_total_dm_count_statistics(),
                      data.cmonolog.get_total_dm_count_statistics(),
                      data.speech.get_total_dm_count_statistics()]

    cp.plot_vertical_barchart("Number Discourse Markers per Text",
                              total_dm_count,
                              ["Min", "Mean", "Mode", "Max"],
                              "Number Markers",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog", label_4="Speech",
                              color_1=data.dialog_color, color_2=data.monolog_color,
                              color_3=data.cmonolog_color, color_4=data.speech_color)

    hp.show_dataframe("Number Discourse Markers per Text",
                      ['Min', 'Mean', 'Mode', 'Max'],
                      total_dm_count[0], data2=total_dm_count[1], data3=total_dm_count[2],
                      data4=total_dm_count[3],
                      label1="Dialog", label2="Monolog",
                      label3="Cooperative-Monolog", label4="Speech")

    hp.effectsize_and_significance("Number Discourse Markers per Text",
                                   total_dm_count,
                                   ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    '''03:
    Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    min/mean/max(dm_sentences_perc)
    '''
    dm_sentences_perc = [data.dialog.get_percent_dm_sentences_statistics(),
                         data.monolog.get_percent_dm_sentences_statistics(),
                         data.cmonolog.get_percent_dm_sentences_statistics()]

    cp.plot_vertical_barchart("Percent of Sentences with DM per Text",
                              dm_sentences_perc,
                              ["Min", "Mean", "Mode", "Max"],
                              "% Sentences containing DM",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog",
                              color_1=data.dialog_color, color_2=data.monolog_color,
                              color_3=data.cmonolog_color)

    hp.show_dataframe("Percent of Sentences with DM per Text",
                      ['Min', 'Mean', 'Mode', 'Max'],
                      dm_sentences_perc[0], data2=dm_sentences_perc[1], data3=dm_sentences_perc[2],
                      label1="Dialog", label2="Monolog",
                      label3="Cooperative-Monolog")

    hp.effectsize_and_significance("Percent of Sentences with DM per Text",
                                   dm_sentences_perc,
                                   ["Monolog", "Dialog", "Cooperative Monolog"])

    '''04:
    Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_sentences)
    '''
    dm_sentences_total = [data.dialog.get_total_dm_sentences_statistics(),
                          data.monolog.get_total_dm_sentences_statistics(),
                          data.cmonolog.get_total_dm_sentences_statistics()]

    cp.plot_vertical_barchart("Number of Sentences with DM per Text",
                              dm_sentences_total,
                              ["Min", "Mean", "Mode", "Max"],
                              "# Sentences containing DM",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog",
                              color_1=data.dialog_color, color_2=data.monolog_color,
                              color_3=data.cmonolog_color)

    hp.show_dataframe("Number of Sentences with DM per Text",
                      ['Min', 'Mean', 'Mode', 'Max'],
                      dm_sentences_total[0], data2=dm_sentences_total[1],
                      data3=dm_sentences_total[2],
                      label1="Dialog", label2="Monolog",
                      label3="Cooperative-Monolog")

    hp.effectsize_and_significance("Number of Sentences with DM per Text",
                                   dm_sentences_total,
                                   ["Monolog", "Dialog", "Cooperative Monolog"])

    '''
    05_a: Number of DM per sentence
    '''
    dm_per_sent_total = [data.dialog.get_total_dm_per_sentence_statistics(),
                         data.monolog.get_total_dm_per_sentence_statistics(),
                         data.cmonolog.get_total_dm_per_sentence_statistics()]

    cp.plot_vertical_barchart("Number of Discourse Markers per Sentence",
                              dm_per_sent_total,
                              ["Min", "Mean", "Mode", "Max"],
                              "# Markers per Sentence",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog",
                              color_1=data.dialog_color, color_2=data.monolog_color,
                              color_3=data.cmonolog_color)

    hp.show_dataframe("Number of Discourse Markers per Sentence",
                      ['Min', 'Mean', 'Mode', 'Max'],
                      dm_per_sent_total[0], data2=dm_per_sent_total[1],
                      data3=dm_per_sent_total[2],
                      label1="Dialog", label2="Monolog",
                      label3="Cooperative-Monolog")

    hp.effectsize_and_significance("Number of Discourse Markers per Sentence",
                                   dm_per_sent_total,
                                   ["Monolog", "Dialog", "Cooperative Monolog"])

    '''
    05_b: Histogram with Number of DM per Sentence per Dataset
    '''
    dm_per_sent = [data.dialog.compute_dm_per_sentence(),
                   data.monolog.compute_dm_per_sentence(),
                   data.cmonolog.compute_dm_per_sentence()]

    cp.draw_simple_barchart("Number of Discourse Markers per Sentence",
                            ["Monolog", "Dialog", "Cooperative Monolog"],
                            dm_per_sent,
                            [data.dialog_color, data.monolog_color, data.cmonolog_color])

    '''
    ---- Sentence Positions ----
    '''

    '''
    06: Percentage of DM at certain positions in a sentence
    '''
    dm_pos_sent = [data.dialog.get_percent_dm_positions_sentence(),
                   data.monolog.get_percent_dm_positions_sentence(),
                   data.cmonolog.get_percent_dm_positions_sentence()]

    cp.plot_vertical_barchart("% of DM in a Position in a Sentence",
                              dm_pos_sent,
                              ['Begin', 'Middle', 'End'],
                              "% DM at Postion",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog",
                              color_1=data.dialog_color, color_2=data.monolog_color,
                              color_3=data.cmonolog_color)

    hp.show_dataframe("% of DM in a Position in a Sentence",
                      ['Begin', 'Middle', 'End'],
                      dm_pos_sent[0], data2=dm_pos_sent[1],
                      data3=dm_pos_sent[2],
                      label1="Dialog", label2="Monolog",
                      label3="Cooperative-Monolog")

    hp.effectsize_and_significance("% of DM in a Position in a Sentence",
                                   dm_pos_sent,
                                   ["Monolog", "Dialog", "Cooperative Monolog"])
    '''
    07: Number of DM at certain positions in a sentence
    '''
    dm_pos_sent_total = [data.dialog.get_total_dm_positions_sentence(),
                         data.monolog.get_total_dm_positions_sentence(),
                         data.cmonolog.get_total_dm_positions_sentence()]

    cp.plot_vertical_barchart("Number of DM at a certain Position in a Sentence",
                              dm_pos_sent_total,
                              ["Begin", "Middle", "End"],
                              "# DM at Postion",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog",
                              color_1=data.dialog_color, color_2=data.monolog_color,
                              color_3=data.cmonolog_color)

    hp.show_dataframe("Number of DM at a certain Position in a Sentence",
                      ["Begin", "Middle", "End"],
                      dm_pos_sent_total[0], data2=dm_pos_sent_total[1],
                      data3=dm_pos_sent_total[2],
                      label1="Dialog", label2="Monolog",
                      label3="Cooperative-Monolog")

    hp.effectsize_and_significance("Number of DM at a certain Position in a Sentence",
                                   dm_pos_sent_total,
                                   ["Monolog", "Dialog", "Cooperative Monolog"])

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

    '''08:
    Percentage of DM at certain positions in a document
    '''
    dm_pos_doc_perc = [data.dialog.get_percent_dm_positions_document(),
                       data.monolog.get_percent_dm_positions_document(),
                       data.cmonolog.get_percent_dm_positions_document(),
                       data.speech.get_percent_dm_positions_document()]

    cp.plot_vertical_barchart("% of DM in a Position in a Document",
                              dm_pos_doc_perc,
                              ["Begin", "Middle", "End"],
                              "% DM at Postion",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog", label_4="Speech",
                              color_1=data.dialog_color, color_2=data.monolog_color,
                              color_3=data.cmonolog_color, color_4=data.speech_color)

    hp.show_dataframe("% of DM in a Position in a Document",
                      ["Begin", "Middle", "End"],
                      dm_pos_doc_perc[0], data2=dm_pos_doc_perc[1], data3=dm_pos_doc_perc[2],
                      data4=dm_pos_doc_perc[3],
                      label1="Dialog", label2="Monolog",
                      label3="Cooperative-Monolog", label4="Speech")

    hp.effectsize_and_significance("% of DM in a Position in a Document",
                                   dm_pos_doc_perc,
                                   ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    '''
    09: Number of DM at certain positions in a document
    '''
    dm_pos_doc_total = [data.dialog.get_total_dm_positions_document(),
                        data.monolog.get_total_dm_positions_document(),
                        data.cmonolog.get_total_dm_positions_document(),
                        data.speech.get_percent_dm_positions_document()]

    cp.plot_vertical_barchart("Number of DM at a certain Position in a Document",
                              dm_pos_doc_total,
                              ["Begin", "Middle", "End"],
                              "# DM at Postion",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog", label_4="Speech",
                              color_1=data.dialog_color, color_2=data.monolog_color,
                              color_3=data.cmonolog_color, color_4=data.speech_color)

    hp.show_dataframe("Number of DM at a certain Position in a Document",
                      ["Begin", "Middle", "End"],
                      dm_pos_doc_total[0], data2=dm_pos_doc_total[1], data3=dm_pos_doc_total[2],
                      data4=dm_pos_doc_total[3],
                      label1="Dialog", label2="Monolog",
                      label3="Cooperative-Monolog", label4="Speech"
                      )

    hp.effectsize_and_significance("Number of DM at a certain Position in a Document",
                                   dm_pos_doc_total,
                                   ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])
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
    most_common_markers = [data.dialog.get_most_common_markers(15, average='Doc'),
                           data.monolog.get_most_common_markers(15, average='Doc'),
                           data.cmonolog.get_most_common_markers(15, average='Doc'),
                           data.speech.get_most_common_markers(15, average='Doc')]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers - Average per Document",
                                                           most_common_markers,
                                                           ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
                                color_1=data.dialog_color, color_2=data.monolog_color,
                                color_3=data.cmonolog_color, color_4=data.speech_color)

    hp.compute_marker_deltas("Differences between Marker Averages",
                             most_common_markers,
                             ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

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

    '''
    01_b: Most Common Markers per Genre - Average per Sentence
    '''
    most_common_markers = [data.dialog.get_most_common_markers(15, average='Sent'),
                           data.monolog.get_most_common_markers(15, average='Sent'),
                           data.cmonolog.get_most_common_markers(15, average='Sent')]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers - Average per Sentence",
                                                           most_common_markers,
                                                           ["Monolog", "Dialog", "Cooperative Monolog"])

    cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Sentence",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
                                color_1=data.dialog_color, color_2=data.monolog_color,
                                color_3=data.cmonolog_color)

    hp.compute_marker_deltas("Differences between Marker Averages",
                             most_common_markers,
                             ["Monolog", "Dialog", "Cooperative Monolog"])

    '''
    02: Most Common Markers per Genre - In Percent
    '''
    most_common_markers_perc = [data.dialog.get_most_common_markers(15, perc=True),
                                data.monolog.get_most_common_markers(15, perc=True),
                                data.cmonolog.get_most_common_markers(15, perc=True),
                                data.speech.get_most_common_markers(15, perc=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers in %",
                                                           most_common_markers_perc,
                                                           ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    cp.plot_horizontal_barchart("Most Common Markers in %", markers, x_values, "Share in all Markers",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
                                label_5="Speech",
                                color_1=data.dialog_color, color_2=data.monolog_color,
                                color_3=data.cmonolog_color, color_4=data.speech_color)

    hp.compute_marker_deltas("Differences between Marker Averages",
                             most_common_markers_perc,
                             ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    # mp.most_common_markers_plot("Most Common Markers per Genre in %", "Share in all Markers",
    #                             most_common_markers_perc[0],
    #                             "News", data.news_color,
    #                             data2=most_common_markers_perc[1],
    #                             label2="Discussion/Opinion", color2=data.discussion_color,
    #                             data3=most_common_markers_perc[2],
    #                             label3="Science", color3=data.science_color,
    #                             data4=most_common_markers_perc[3],
    #                             label4="Documentary", color4=data.documentary_color,
    #                             data5=most_common_markers_perc[4],
    #                             label5="Speech", color5=data.speech_color,
    #                             share=True)

    '''
    03_a: Most Common Markers per Genre - Sentence Begin
    '''
    mc_sent_begin = [data.dialog.get_most_common_markers(15, position="sb", average=True),
                     data.monolog.get_most_common_markers(15, position="sb", average=True),
                     data.cmonolog.get_most_common_markers(15, position="sb", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Sentence Begin",
                                                           mc_sent_begin,
                                                           ["Monolog", "Dialog", "Cooperative Monolog"])

    cp.plot_horizontal_barchart("Most Common Markers: Sentence Begin", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
                                color_1=data.dialog_color, color_2=data.monolog_color,
                                color_3=data.cmonolog_color)

    hp.compute_marker_deltas("Differences between Marker Averages : Sentence Begin",
                             mc_sent_begin,
                             ["Monolog", "Dialog", "Cooperative Monolog"])

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
    mc_sent_middle = [data.dialog.get_most_common_markers(15, position="sm", average=True),
                      data.monolog.get_most_common_markers(15, position="sm", average=True),
                      data.cmonolog.get_most_common_markers(15, position="sm", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Sentence Middle",
                                                           mc_sent_middle,
                                                           ["Monolog", "Dialog", "Cooperative Monolog"])

    cp.plot_horizontal_barchart("Most Common Markers: Sentence Middle", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
                                color_1=data.dialog_color, color_2=data.monolog_color,
                                color_3=data.cmonolog_color)

    hp.compute_marker_deltas("Differences between Marker Averages : Sentence Middle",
                             mc_sent_middle,
                             ["Monolog", "Dialog", "Cooperative Monolog"])

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
    mc_sent_end = [data.dialog.get_most_common_markers(15, position="se", average=True),
                   data.monolog.get_most_common_markers(15, position="se", average=True),
                   data.cmonolog.get_most_common_markers(15, position="se", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Sentence End",
                                                           mc_sent_end,
                                                           ["Monolog", "Dialog", "Cooperative Monolog"])

    cp.plot_horizontal_barchart("Most Common Markers: Sentence End", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
                                color_1=data.dialog_color, color_2=data.monolog_color,
                                color_3=data.cmonolog_color)

    hp.compute_marker_deltas("Differences between Marker Averages : Sentence End",
                             mc_sent_end,
                             ["Monolog", "Dialog", "Cooperative Monolog"])

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
    mc_doc_begin = [data.dialog.get_most_common_markers(15, position="db", average=True),
                    data.monolog.get_most_common_markers(15, position="db", average=True),
                    data.cmonolog.get_most_common_markers(15, position="db", average=True),
                    data.speech.get_most_common_markers(15, position="db", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Document Begin",
                                                           mc_doc_begin,
                                                           ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    cp.plot_horizontal_barchart("Most Common Markers: Document Begin", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
                                color_1=data.dialog_color, color_2=data.monolog_color,
                                color_3=data.cmonolog_color, color_4=data.speech_color)

    hp.compute_marker_deltas("Differences between Marker Averages : Document Begin",
                             mc_doc_begin,
                             ["News", "Discussion", "Science", "Documentary", "Speech"])

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
    mc_doc_middle = [data.dialog.get_most_common_markers(15, position="dm", average=True),
                     data.monolog.get_most_common_markers(15, position="dm", average=True),
                     data.cmonolog.get_most_common_markers(15, position="dm", average=True),
                     data.speech.get_most_common_markers(15, position="dm", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Document Middle",
                                                           mc_doc_middle,
                                                           ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    cp.plot_horizontal_barchart("Most Common Markers: Document Middle", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
                                color_1=data.dialog_color, color_2=data.monolog_color,
                                color_3=data.cmonolog_color, color_4=data.speech_color)

    hp.compute_marker_deltas("Differences between Marker Averages : Document Middle",
                             mc_doc_middle,
                             ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

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
    mc_doc_end = [data.dialog.get_most_common_markers(15, position="de", average=True),
                  data.monolog.get_most_common_markers(15, position="de", average=True),
                  data.cmonolog.get_most_common_markers(15, position="de", average=True),
                  data.speech.get_most_common_markers(15, position="de", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Document End",
                                                           mc_doc_end,
                                                           ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    cp.plot_horizontal_barchart("Most Common Markers: Document End", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
                                color_1=data.dialog_color, color_2=data.monolog_color,
                                color_3=data.cmonolog_color, color_4=data.speech_color)

    hp.compute_marker_deltas("Differences between Marker Averages : Document End",
                             mc_doc_end,
                             ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

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
