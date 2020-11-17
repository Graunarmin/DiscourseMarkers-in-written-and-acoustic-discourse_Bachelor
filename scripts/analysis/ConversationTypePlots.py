from plotting import CreatePlots as cp
from datasets import ConversationTypeData as ctd
from helpers import Helpers as hp


def main():
    c_data = ctd.ConversationTypeData(
        "../../bigData/listenability-tools/Spotify/discourse-types/scores/dialog-scores_short.csv",
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
    dm_per_text_perc = [c_data.dialog.get_percent_dm_count_statistics(),
                        c_data.monolog.get_percent_dm_count_statistics(),
                        c_data.cmonolog.get_percent_dm_count_statistics(),
                        c_data.speech.get_percent_dm_count_statistics()]

    cp.plot_vertical_barchart("Percent Discourse Markers per Text",
                              dm_per_text_perc,
                              ["Min", "Mean", "Mode", "Max"],
                              "Percent Markers",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog", label_4="Speech",
                              color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                              color_3=c_data.cmonolog_color, color_4=c_data.speech_color)

    hp.show_dataframe("Percent Discourse Markers per Text - Values",
                      ['Min', 'Mean', 'Mode', 'Max'],
                      dm_per_text_perc[0], data2=dm_per_text_perc[1], data3=dm_per_text_perc[2],
                      data4=dm_per_text_perc[3],
                      label1="Dialog", label2="Monolog",
                      label3="Cooperative-Monolog", label4="Speech")

    hp.effectsize_and_significance("Percent Discourse Markers per Text - Statistics",
                                   dm_per_text_perc,
                                   ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    '''
    Empirical Distribution Function
    '''
    dm_percents = [c_data.dialog.get_percent_dm_per_text(),
                   c_data.monolog.get_percent_dm_per_text(),
                   c_data.cmonolog.get_percent_dm_per_text(),
                   c_data.speech.get_percent_dm_per_text()]

    cp.plot_ecdf(dm_percents,
                 "ECDF for % of Discourse Markers per Text", "% DM per Text", "ECDF (% of Texts)",
                 ["Monolog", "Dialog", "Cooperative Monolog", "Speech"],
                 [c_data.dialog_color, c_data.monolog_color, c_data.cmonolog_color, c_data.speech_color])

    '''02:
    Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_count_doc)
    '''
    total_dm_count = [c_data.dialog.get_total_dm_count_statistics(),
                      c_data.monolog.get_total_dm_count_statistics(),
                      c_data.cmonolog.get_total_dm_count_statistics(),
                      c_data.speech.get_total_dm_count_statistics()]

    cp.plot_vertical_barchart("Number Discourse Markers per Text",
                              total_dm_count,
                              ["Min", "Mean", "Mode", "Max"],
                              "Number Markers",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog", label_4="Speech",
                              color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                              color_3=c_data.cmonolog_color, color_4=c_data.speech_color)

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
    dm_sentences_perc = [c_data.dialog.get_percent_dm_sentences_statistics(),
                         c_data.monolog.get_percent_dm_sentences_statistics(),
                         c_data.cmonolog.get_percent_dm_sentences_statistics()]

    cp.plot_vertical_barchart("Percent of Sentences with DM per Text",
                              dm_sentences_perc,
                              ["Min", "Mean", "Mode", "Max"],
                              "% Sentences containing DM",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog",
                              color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                              color_3=c_data.cmonolog_color)

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
    dm_sentences_total = [c_data.dialog.get_total_dm_sentences_statistics(),
                          c_data.monolog.get_total_dm_sentences_statistics(),
                          c_data.cmonolog.get_total_dm_sentences_statistics()]

    cp.plot_vertical_barchart("Number of Sentences with DM per Text",
                              dm_sentences_total,
                              ["Min", "Mean", "Mode", "Max"],
                              "# Sentences containing DM",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog",
                              color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                              color_3=c_data.cmonolog_color)

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
    dm_per_sent_total = [c_data.dialog.get_total_dm_per_sentence_statistics(),
                         c_data.monolog.get_total_dm_per_sentence_statistics(),
                         c_data.cmonolog.get_total_dm_per_sentence_statistics()]

    cp.plot_vertical_barchart("Number of Discourse Markers per Sentence",
                              dm_per_sent_total,
                              ["Min", "Mean", "Mode", "Max"],
                              "# Markers per Sentence",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog",
                              color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                              color_3=c_data.cmonolog_color)

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
    dm_per_sent = [c_data.dialog.compute_dm_per_sentence(),
                   c_data.monolog.compute_dm_per_sentence(),
                   c_data.cmonolog.compute_dm_per_sentence()]

    cp.draw_simple_barchart("Number of Discourse Markers per Sentence",
                            ["Monolog", "Dialog", "Cooperative Monolog"],
                            dm_per_sent,
                            [c_data.dialog_color, c_data.monolog_color, c_data.cmonolog_color])

    '''
    ---- Sentence Positions ----
    '''

    '''
    06: Percentage of DM at certain positions in a sentence
    '''
    dm_pos_sent = [c_data.dialog.get_percent_dm_positions_sentence(),
                   c_data.monolog.get_percent_dm_positions_sentence(),
                   c_data.cmonolog.get_percent_dm_positions_sentence()]

    cp.plot_vertical_barchart("% of DM in a Position in a Sentence",
                              dm_pos_sent,
                              ['Begin', 'Middle', 'End'],
                              "% DM at Postion",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog",
                              color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                              color_3=c_data.cmonolog_color)

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
    dm_pos_sent_total = [c_data.dialog.get_total_dm_positions_sentence(),
                         c_data.monolog.get_total_dm_positions_sentence(),
                         c_data.cmonolog.get_total_dm_positions_sentence()]

    cp.plot_vertical_barchart("Number of DM at a certain Position in a Sentence",
                              dm_pos_sent_total,
                              ["Begin", "Middle", "End"],
                              "# DM at Postion",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog",
                              color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                              color_3=c_data.cmonolog_color)

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
    dm_pos_doc_perc = [c_data.dialog.get_percent_dm_positions_document(),
                       c_data.monolog.get_percent_dm_positions_document(),
                       c_data.cmonolog.get_percent_dm_positions_document(),
                       c_data.speech.get_percent_dm_positions_document()]

    cp.plot_vertical_barchart("% of DM in a Position in a Document",
                              dm_pos_doc_perc,
                              ["Begin", "Middle", "End"],
                              "% DM at Postion",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog", label_4="Speech",
                              color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                              color_3=c_data.cmonolog_color, color_4=c_data.speech_color)

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
    dm_pos_doc_total = [c_data.dialog.get_total_dm_positions_document(),
                        c_data.monolog.get_total_dm_positions_document(),
                        c_data.cmonolog.get_total_dm_positions_document(),
                        c_data.speech.get_percent_dm_positions_document()]

    cp.plot_vertical_barchart("Number of DM at a certain Position in a Document",
                              dm_pos_doc_total,
                              ["Begin", "Middle", "End"],
                              "# DM at Postion",
                              label_1="Dialog", label_2="Monolog",
                              label_3="Cooperative-Monolog", label_4="Speech",
                              color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                              color_3=c_data.cmonolog_color, color_4=c_data.speech_color)

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
    most_common_markers = [c_data.dialog.get_most_common_markers(15, average='Doc'),
                           c_data.monolog.get_most_common_markers(15, average='Doc'),
                           c_data.cmonolog.get_most_common_markers(15, average='Doc'),
                           c_data.speech.get_most_common_markers(15, average='Doc')]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers - Average per Document",
                                                           most_common_markers,
                                                           ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
                                color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                                color_3=c_data.cmonolog_color, color_4=c_data.speech_color)

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
    most_common_markers = [c_data.dialog.get_most_common_markers(15, average='Sent'),
                           c_data.monolog.get_most_common_markers(15, average='Sent'),
                           c_data.cmonolog.get_most_common_markers(15, average='Sent')]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers - Average per Sentence",
                                                           most_common_markers,
                                                           ["Monolog", "Dialog", "Cooperative Monolog"])

    cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Sentence",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
                                color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                                color_3=c_data.cmonolog_color)

    hp.compute_marker_deltas("Differences between Marker Averages",
                             most_common_markers,
                             ["Monolog", "Dialog", "Cooperative Monolog"])

    '''
    02: Most Common Markers per Genre - In Percent
    '''
    most_common_markers_perc = [c_data.dialog.get_most_common_markers(15, perc=True),
                                c_data.monolog.get_most_common_markers(15, perc=True),
                                c_data.cmonolog.get_most_common_markers(15, perc=True),
                                c_data.speech.get_most_common_markers(15, perc=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers in %",
                                                           most_common_markers_perc,
                                                           ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    cp.plot_horizontal_barchart("Most Common Markers in %", markers, x_values, "Share in all Markers",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
                                label_5="Speech",
                                color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                                color_3=c_data.cmonolog_color, color_4=c_data.speech_color)

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
    mc_sent_begin = [c_data.dialog.get_most_common_markers(15, position="sb", average=True),
                     c_data.monolog.get_most_common_markers(15, position="sb", average=True),
                     c_data.cmonolog.get_most_common_markers(15, position="sb", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Sentence Begin",
                                                           mc_sent_begin,
                                                           ["Monolog", "Dialog", "Cooperative Monolog"])

    cp.plot_horizontal_barchart("Most Common Markers: Sentence Begin", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
                                color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                                color_3=c_data.cmonolog_color)

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
    mc_sent_middle = [c_data.dialog.get_most_common_markers(15, position="sm", average=True),
                      c_data.monolog.get_most_common_markers(15, position="sm", average=True),
                      c_data.cmonolog.get_most_common_markers(15, position="sm", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Sentence Middle",
                                                           mc_sent_middle,
                                                           ["Monolog", "Dialog", "Cooperative Monolog"])

    cp.plot_horizontal_barchart("Most Common Markers: Sentence Middle", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
                                color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                                color_3=c_data.cmonolog_color)

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
    mc_sent_end = [c_data.dialog.get_most_common_markers(15, position="se", average=True),
                   c_data.monolog.get_most_common_markers(15, position="se", average=True),
                   c_data.cmonolog.get_most_common_markers(15, position="se", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Sentence End",
                                                           mc_sent_end,
                                                           ["Monolog", "Dialog", "Cooperative Monolog"])

    cp.plot_horizontal_barchart("Most Common Markers: Sentence End", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
                                color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                                color_3=c_data.cmonolog_color)

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
    mc_doc_begin = [c_data.dialog.get_most_common_markers(15, position="db", average=True),
                    c_data.monolog.get_most_common_markers(15, position="db", average=True),
                    c_data.cmonolog.get_most_common_markers(15, position="db", average=True),
                    c_data.speech.get_most_common_markers(15, position="db", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Document Begin",
                                                           mc_doc_begin,
                                                           ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    cp.plot_horizontal_barchart("Most Common Markers: Document Begin", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
                                color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                                color_3=c_data.cmonolog_color, color_4=c_data.speech_color)

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
    mc_doc_middle = [c_data.dialog.get_most_common_markers(15, position="dm", average=True),
                     c_data.monolog.get_most_common_markers(15, position="dm", average=True),
                     c_data.cmonolog.get_most_common_markers(15, position="dm", average=True),
                     c_data.speech.get_most_common_markers(15, position="dm", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Document Middle",
                                                           mc_doc_middle,
                                                           ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    cp.plot_horizontal_barchart("Most Common Markers: Document Middle", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
                                color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                                color_3=c_data.cmonolog_color, color_4=c_data.speech_color)

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
    mc_doc_end = [c_data.dialog.get_most_common_markers(15, position="de", average=True),
                  c_data.monolog.get_most_common_markers(15, position="de", average=True),
                  c_data.cmonolog.get_most_common_markers(15, position="de", average=True),
                  c_data.speech.get_most_common_markers(15, position="de", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Document End",
                                                           mc_doc_end,
                                                           ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])

    cp.plot_horizontal_barchart("Most Common Markers: Document End", markers, x_values,
                                "Average per Document",
                                "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
                                color_1=c_data.dialog_color, color_2=c_data.monolog_color,
                                color_3=c_data.cmonolog_color, color_4=c_data.speech_color)

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