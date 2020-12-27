import helpers.DataFrames
import helpers.Statistics
from plotting import CreatePlots as cp
from datasets import CorpusData as cd
from helpers import Helpers as hp


def main():
    d_data = cd.CorpusData(
        "../../bigData/listenability-tools/discourse-types/scores/spotify-scores_short.csv",
        "../../bigData/listenability-tools/discourse-types/scores/ted-scores_short.csv",
        "../../bigData/listenability-tools/discourse-types/scores/nytimes-scores_short.csv",
        "../../bigData/listenability-tools/discourse-types/scores/gigaword-scores_short.csv",
        spotify_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/sentence-scores/spotify-sentence-scores.json",
        ted_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/sentence-scores/ted-sentence-scores.json",
        ny_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/sentence-scores/nytimes-sentence-scores.json",
        gig_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/sentence-scores/gigaword-sentence-scores.json"
    )

    '''
    01: Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''

    dm_count_perc = [d_data.spotify.get_percent_dm_per_text_statistics(),
                     d_data.ted.get_percent_dm_per_text_statistics(),
                     d_data.ny.get_percent_dm_per_text_statistics(),
                     d_data.gig.get_percent_dm_per_text_statistics()]

    cp.plot_vertical_barchart("Percent Discourse Markers per Text",
                              dm_count_perc,
                              ["Min", "Mean", "Mode", "Max"],
                              "Percentage of Markers in all Words of a Text",
                              label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                              color_1=d_data.spotify_color, color_2=d_data.ted_color,
                              color_3=d_data.ny_color, color_4=d_data.gig_color)

    # Add a plot with spoken vs. written

    helpers.DataFrames.create_dataframe("DM-per-text-percent_Values",
                                        ['Min', 'Mean', 'Mode', 'Max'],
                                        dm_count_perc[0], data2=dm_count_perc[1], data3=dm_count_perc[2],
                                        data4=dm_count_perc[3],
                                        label1="Spotify", label2="TED",
                                        label3="NYTimes", label4="Gigaword")

    ecdfd_dm_percents = [d_data.spotify.get_percent_dm_per_text_column(),
                         d_data.ted.get_percent_dm_per_text_column(),
                         d_data.ny.get_percent_dm_per_text_column(),
                         d_data.gig.get_percent_dm_per_text_column()]

    helpers.Statistics.effectsize_and_significance("DM-per-text-percent_Statistics",
                                                   [[*ecdfd_dm_percents[0], *ecdfd_dm_percents[1]],
                                    [*ecdfd_dm_percents[2], *ecdfd_dm_percents[3]]],
                                                   ["Spoken", "Written"])

    '''
    Empirical Distribution Function
    '''

    cp.plot_edf("EDF for  % of Discourse Markers per Text",
                "% DM per Text", "EDF (% of Texts)",
                [d_data.spotify.get_percent_dm_per_text_column(collected=True),
                 d_data.ted.get_percent_dm_per_text_column(collected=True),
                 d_data.ny.get_percent_dm_per_text_column(collected=True),
                 d_data.gig.get_percent_dm_per_text_column(collected=True)],
                ["Spotify", "TED", "New York Times", "Gigaword"],
                [d_data.spotify_color, d_data.ted_color, d_data.ny_color,
                 d_data.gig_color]
                )

    cp.plot_ecdf(ecdfd_dm_percents,
                 "ECDF for % of Discourse Markers per Text", "% DM per Text", "ECDF (% of Texts)",
                 ["Spotify", "TED", "New York Times", "Gigaword"],
                 [d_data.spotify_color, d_data.ted_color, d_data.ny_color,
                  d_data.gig_color])

    '''
    02: Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_count_doc)
    '''
    dm_count_total = [d_data.spotify.get_total_dm_per_text_statistics(),
                      d_data.ted.get_total_dm_per_text_statistics(),
                      d_data.ny.get_total_dm_per_text_statistics(),
                      d_data.gig.get_total_dm_per_text_statistics()]

    cp.plot_vertical_barchart("Number Discourse Markers per Text",
                              dm_count_total,
                              ["Min", "Mean", "Mode", "Max"],
                              "Marker Occurrences Total",
                              label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                              color_1=d_data.spotify_color, color_2=d_data.ted_color,
                              color_3=d_data.ny_color, color_4=d_data.gig_color)

    helpers.DataFrames.create_dataframe("DM-per-text-total_Values",
                                        ['Min', 'Mean', 'Mode', 'Max'],
                                        dm_count_total[0], data2=dm_count_total[1], data3=dm_count_total[2],
                                        data4=dm_count_total[3],
                                        label1="Spotify", label2="TED",
                                        label3="NYTimes", label4="Gigaword")

    dm_count_total_column = [d_data.spotify.get_total_dm_per_text_column(),
                             d_data.ted.get_total_dm_per_text_column(),
                             d_data.ny.get_total_dm_per_text_column(),
                             d_data.gig.get_total_dm_per_text_column()]

    helpers.Statistics.effectsize_and_significance("DM-per-text-total_Statistics",
                                                   [[*dm_count_total_column[0], *dm_count_total_column[1]],
                                    [*dm_count_total_column[2], *dm_count_total_column[3]]],
                                                   ["Spoken", "Written"])

    '''
    03: Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    min/mean/max(dm_sentences_perc)
    '''
    dm_sentences_perc = [d_data.spotify.get_percent_dm_sentences_statistics(),
                         d_data.ny.get_percent_dm_sentences_statistics(),
                         d_data.gig.get_percent_dm_sentences_statistics()]

    cp.plot_vertical_barchart("Percent of Sentences with DM per Text",
                              dm_sentences_perc,
                              ["Min", "Mean", "Mode", "Max"],
                              "% Sentences containing DM per Text",
                              label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                              color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)

    helpers.DataFrames.create_dataframe("DM-sentences-percent_Values",
                                        ['Min', 'Mean', 'Mode', 'Max'],
                                        dm_sentences_perc[0], data2=dm_sentences_perc[1], data3=dm_sentences_perc[2],
                                        label1="Spotify",
                                        label2="NYTimes", label3="Gigaword")

    dm_sentences_perc_column = [d_data.spotify.get_percent_dm_sentences_column(),
                                d_data.ny.get_percent_dm_sentences_column(),
                                d_data.gig.get_percent_dm_sentences_column()]

    helpers.Statistics.effectsize_and_significance("DM-sentences-percent_Statistics",
                                                   [dm_sentences_perc_column[0],
                                    [*dm_sentences_perc_column[1], *dm_sentences_perc_column[2]]],
                                                   ["Spotify", "Written"])

    '''
    Empirical Distribution Function
    '''
    cp.plot_edf("EDF for % of Sentences containing Discourse Markers per Text",
                "% DM Sentences per Text", "EDF (% of Texts)",
                [d_data.spotify.get_percent_dm_sentences_column(collected=True),
                 d_data.ny.get_percent_dm_sentences_column(collected=True),
                 d_data.gig.get_percent_dm_sentences_column(collected=True)],
                ["Spotify", "New York Times", "Gigaword"],
                [d_data.spotify_color, d_data.ny_color,
                 d_data.gig_color])

    cp.plot_ecdf(dm_sentences_perc_column,
                 "ECDF for % of Sentences containing Discourse Markers per Text",
                 "% DM Sentences per Text", "ECDF (% of Texts)",
                 ["Spotify", "New York Times", "Gigaword"],
                 [d_data.spotify_color, d_data.ny_color,
                  d_data.gig_color])

    '''
    04: Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_sentences)
    '''
    dm_sentences_total = [d_data.spotify.get_total_dm_sentences_statistics(),
                          d_data.ny.get_total_dm_sentences_statistics(),
                          d_data.gig.get_total_dm_sentences_statistics()]

    cp.plot_vertical_barchart("Number of Sentences containing DM per Text",
                              dm_sentences_total,
                              ["Min", "Mean", "Mode", "Max"],
                              "Number of Sentences containing DM",
                              label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                              color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)

    helpers.DataFrames.create_dataframe("DM-sentences-total_Values",
                                        ['Min', 'Mean', 'Mode', 'Max'],
                                        dm_sentences_total[0], data2=dm_sentences_total[1], data3=dm_sentences_total[2],
                                        label1="Spotify",
                                        label2="NYTimes", label3="Gigaword")

    dm_sentences_total_column = [d_data.spotify.get_total_dm_sentences_column(),
                                 d_data.ny.get_total_dm_sentences_column(),
                                 d_data.gig.get_total_dm_sentences_column()]

    helpers.Statistics.effectsize_and_significance("DM-sentences-total_Statistics",
                                                   [dm_sentences_total_column[0],
                                    [*dm_sentences_total_column[1], *dm_sentences_total_column[2]]],
                                                   ["Spotify", "Written"])

    '''
    05_a: Number of DM per sentence
    '''
    dm_per_sentence = [d_data.spotify.get_total_dm_per_sentence_statistics(),
                       d_data.ny.get_total_dm_per_sentence_statistics(),
                       d_data.gig.get_total_dm_per_sentence_statistics()]

    cp.plot_vertical_barchart("Number of Discourse Markers per Sentence",
                              dm_per_sentence,
                              ["Min", "Mean", "Mode", "Max"],
                              "Number of Markers per Sentence",
                              label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                              color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)

    helpers.DataFrames.create_dataframe("DM-per-sentence_Values",
                                        ['Min', 'Mean', 'Mode', 'Max'],
                                        dm_per_sentence[0], data2=dm_per_sentence[1], data3=dm_per_sentence[2],
                                        label1="Spotify",
                                        label2="NYTimes", label3="Gigaword")

    dm_per_sentence_column = [d_data.spotify.get_dm_per_sentence(),
                              d_data.ny.get_dm_per_sentence(),
                              d_data.gig.get_dm_per_sentence()]

    helpers.Statistics.effectsize_and_significance("DM-per-sentence_Statistics",
                                                   [dm_per_sentence_column[0],
                                    [*dm_per_sentence_column[1], *dm_per_sentence_column[2]]],
                                                   ["Spotify", "Written"])

    '''
    05_b: Histogram with Number of DM per Sentence per Dataset
    '''
    dm_per_sent = [d_data.spotify.compute_dm_per_sentence(),
                   d_data.ny.compute_dm_per_sentence(),
                   d_data.gig.compute_dm_per_sentence()]

    cp.draw_simple_barchart("Number of Discourse Markers per Sentence",
                            ["Spotify", "NYTimes", "Gigaword"],
                            dm_per_sent,
                            [d_data.spotify_color, d_data.ny_color, d_data.gig_color])

    '''
    Empirical Distribution Function
    '''
    cp.plot_edf("EDF for % Discourse Markers per Sentence",
                "DM per Sentence", "% of Sentences",
                dm_per_sent,
                ["Spotify", "New York Times", "Gigaword"],
                [d_data.spotify_color, d_data.ny_color, d_data.gig_color])

    cp.plot_ecdf(dm_per_sentence_column,
                 "ECDF for % Discourse Markers per Sentence",
                 "DM per Sentence", "ECDF (% of Sentences)",
                 ["Spotify", "New York Times", "Gigaword"],
                 [d_data.spotify_color, d_data.ny_color, d_data.gig_color])

    '''
    ---- Sentence Positions ----
    '''

    '''
    06: Percentage of DM at certain positions in a sentence
    '''
    dm_pos_sent_perc = [d_data.spotify.get_percent_dm_positions_sentence(),
                        d_data.ny.get_percent_dm_positions_sentence(),
                        d_data.gig.get_percent_dm_positions_sentence()]

    cp.plot_vertical_barchart("% of DM in a Position in a Sentence",
                              dm_pos_sent_perc,
                              ["Begin", "Middle", "End"],
                              "% DM at Postion",
                              label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                              color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)

    helpers.DataFrames.create_dataframe("sentence-positions-pecentages_Values",
                                        ['Begin', 'Middle', 'End'],
                                        dm_pos_sent_perc[0], data2=dm_pos_sent_perc[1], data3=dm_pos_sent_perc[2],
                                        label1="Spotify",
                                        label2="NYTimes", label3="Gigaword")

    helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_begin",
                                                   [d_data.spotify.get_sent_begin_column(perc=True),
                                    [*d_data.ny.get_sent_begin_column(perc=True),
                                     *d_data.gig.get_sent_begin_column(perc=True)]],
                                                   ["Spotify", "Written"])

    helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_middle",
                                                   [d_data.spotify.get_sent_middle_column(perc=True),
                                    [*d_data.ny.get_sent_middle_column(perc=True),
                                     *d_data.gig.get_sent_middle_column(perc=True)]],
                                                   ["Spotify", "Written"])

    helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_end",
                                                   [d_data.spotify.get_sent_end_column(perc=True),
                                    [*d_data.ny.get_sent_end_column(perc=True),
                                     *d_data.gig.get_sent_end_column(perc=True)]],
                                                   ["Spotify", "Written"])

    '''
    07: Number of DM at certain positions in a sentence
    '''
    dm_pos_sent_total = [d_data.spotify.get_total_dm_positions_sentence(),
                         d_data.ny.get_total_dm_positions_sentence(),
                         d_data.gig.get_total_dm_positions_sentence()]

    cp.plot_vertical_barchart("Number of DM at a certain Position in a Sentence",
                              dm_pos_sent_total,
                              ["Begin", "Middle", "End"],
                              "Number of DM at Postion",
                              label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                              color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)

    helpers.DataFrames.create_dataframe("sentence-positions-totals_Values",
                                        ['Begin', 'Middle', 'End'],
                                        dm_pos_sent_total[0], data2=dm_pos_sent_total[1], data3=dm_pos_sent_total[2],
                                        label1="Spotify",
                                        label2="NYTimes", label3="Gigaword")

    helpers.Statistics.effectsize_and_significance("sentence-positions-totals_Statistics_begin",
                                                   [d_data.spotify.get_sent_begin_column(),
                                    [*d_data.ny.get_sent_begin_column(),
                                     *d_data.gig.get_sent_begin_column()]],
                                                   ["Spotify", "Written"])

    helpers.Statistics.effectsize_and_significance("sentence-positions-totals_Statistics_middle",
                                                   [d_data.spotify.get_sent_middle_column(),
                                    [*d_data.ny.get_sent_middle_column(),
                                     *d_data.gig.get_sent_middle_column()]],
                                                   ["Spotify", "Written"])

    helpers.Statistics.effectsize_and_significance("sentence-positions-totals_Statistics_end",
                                                   [d_data.spotify.get_sent_end_column(),
                                    [*d_data.ny.get_sent_end_column(),
                                     *d_data.gig.get_sent_end_column()]],
                                                   ["Spotify", "Written"])

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

    '''
    08: Percentage of DM at certain positions in a Document
    '''
    dm_pos_doc_perc = [d_data.spotify.get_percent_dm_positions_document(),
                       d_data.ted.get_percent_dm_positions_document(),
                       d_data.ny.get_percent_dm_positions_document(),
                       d_data.gig.get_percent_dm_positions_document()]

    cp.plot_vertical_barchart("% of DM in a Position in a Document",
                              dm_pos_doc_perc,
                              ["Begin", "Middle", "End"],
                              "% DM at Postion",
                              label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                              color_1=d_data.spotify_color, color_2=d_data.ted_color,
                              color_3=d_data.ny_color, color_4=d_data.gig_color)

    helpers.DataFrames.create_dataframe("document-positions-percentages_Values",
                                        ['Begin', 'Middle', 'End'],
                                        dm_pos_doc_perc[0], data2=dm_pos_doc_perc[1], data3=dm_pos_doc_perc[2], data4=dm_pos_doc_perc[3],
                                        label1="Spotify", label2="TED",
                                        label3="NYTimes", label4="Gigaword")

    helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_begin",
                                                   [[*d_data.spotify.get_doc_begin_column(perc=True),
                                     *d_data.ted.get_doc_begin_column(perc=True)],
                                    [*d_data.ny.get_doc_begin_column(perc=True),
                                     *d_data.gig.get_doc_begin_column(perc=True)]],
                                                   ["Spoken", "Written"])

    helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_middle",
                                                   [[*d_data.spotify.get_doc_middle_column(perc=True),
                                     *d_data.ted.get_doc_middle_column(perc=True)],
                                    [*d_data.ny.get_doc_middle_column(perc=True),
                                     *d_data.gig.get_doc_middle_column(perc=True)]],
                                                   ["Spoken", "Written"])

    helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_end",
                                                   [[*d_data.spotify.get_doc_end_column(perc=True),
                                     *d_data.ted.get_doc_end_column(perc=True)],
                                    [*d_data.ny.get_doc_end_column(perc=True),
                                     *d_data.gig.get_doc_end_column(perc=True)]],
                                                   ["Spoken", "Written"])

    '''
    09: Number of DM at certain positions in a Document
    '''
    dm_pos_doc_total = [d_data.spotify.get_total_dm_positions_document(),
                        d_data.ted.get_total_dm_positions_document(),
                        d_data.ny.get_total_dm_positions_document(),
                        d_data.gig.get_total_dm_positions_document()]

    cp.plot_vertical_barchart("Number of DM at a certain Position in a Document",
                              dm_pos_doc_total,
                              ["Begin", "Middle", "End"],
                              "# DM at Postion",
                              label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                              color_1=d_data.spotify_color, color_2=d_data.ted_color,
                              color_3=d_data.ny_color, color_4=d_data.gig_color)

    helpers.DataFrames.create_dataframe("document-positions-totals_Values",
                                        ['Begin', 'Middle', 'End'],
                                        dm_pos_doc_total[0], data2=dm_pos_doc_total[1], data3=dm_pos_doc_total[2],
                                        data4=dm_pos_doc_total[3],
                                        label1="Spotify", label2="TED",
                                        label3="NYTimes", label4="Gigaword")

    helpers.Statistics.effectsize_and_significance("document-positions-totals_Statistics_begin",
                                                   [[*d_data.spotify.get_doc_begin_column(),
                                     *d_data.ted.get_doc_begin_column()],
                                    [*d_data.ny.get_doc_begin_column(),
                                     *d_data.gig.get_doc_begin_column()]],
                                                   ["Spoken", "Written"])

    helpers.Statistics.effectsize_and_significance("document-positions-totals_Statistics_middle",
                                                   [[*d_data.spotify.get_doc_middle_column(),
                                     *d_data.ted.get_doc_middle_column()],
                                    [*d_data.ny.get_doc_middle_column(),
                                     *d_data.gig.get_doc_middle_column()]],
                                                   ["Spoken", "Written"])

    helpers.Statistics.effectsize_and_significance("document-positions-totals_Statistics_end",
                                                   [[*d_data.spotify.get_doc_end_column(),
                                     *d_data.ted.get_doc_end_column()],
                                    [*d_data.ny.get_doc_end_column(),
                                     *d_data.gig.get_doc_end_column()]],
                                                   ["Spoken", "Written"])

    # cp.plot_dm_position_piechart("Positions of Discourse Markers in the Documents",
    #                              [data.spotify.get_document_position_values(),
    #                               data.ted.get_document_position_values(),
    #                               data.ny.get_document_position_values(),
    #                               data.gig.get_document_position_values()
    #                               ],
    #                              ["Spotify Data", "TED Data", "NYTimes Data", "Gigaword Data"],
    #                              [data.spotify_shades,
    #                               data.ted_shades,
    #                               data.ny_shades,
    #                               data.gig_shades])

    '''
    --- Number of Occurences per Discourse Marker per Dataset ---
    '''

    # '''
    # 01_a: Most Common Markers - Average per Doc
    # '''
    # most_common_markers = [d_data.spotify.get_most_common_markers(15, average=True, share='Doc'),
    #                        d_data.ted.get_most_common_markers(15, average=True, share='Doc'),
    #                        d_data.ny.get_most_common_markers(15, average=True, share='Doc'),
    #                        d_data.gig.get_most_common_markers(15, average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Average-per-Document_mcm",
    #                                                        most_common_markers,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Document",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ted_color,
    #                             color_3=d_data.ny_color, color_4=d_data.gig_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers per Genre", "Average Number of Occurences per Document",
    # #                             most_common_markers[0],
    # #                             "Spotify", data.spotify_color,
    # #                             data2=most_common_markers[1],
    # #                             label2="TED", color2=data.ted_color,
    # #                             data3=most_common_markers[2],
    # #                             label3="NYTimes", color3=data.ny_color,
    # #                             data4=most_common_markers[3],
    # #                             label4="Gigaword", color4=data.gig_color,
    # #                             share=True)
    #
    # '''
    # 01_b: Most Common Markers - Average per Sentence
    # '''
    # most_common_markers_sent = [d_data.spotify.get_most_common_markers(15, average=True, share='Sent'),
    #                             d_data.ny.get_most_common_markers(15, average=True, share='Sent'),
    #                             d_data.gig.get_most_common_markers(15, average=True, share='Sent')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Average-per-Sentence_mcm",
    #                                                        most_common_markers_sent,
    #                                                        ["Spotify", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Sentence",
    #                             "Spotify", label_2="NYTimes", label_3="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)
    #
    # '''
    # 01_c: Most Common Markers - Average per Total Wordcount
    # '''
    # most_common_markers_sent = [d_data.spotify.get_most_common_markers(15, average=True, share='Word'),
    #                             d_data.ny.get_most_common_markers(15, average=True, share='Word'),
    #                             d_data.gig.get_most_common_markers(15, average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Average-per-total-Wordcount_mcm",
    #                                                        most_common_markers_sent,
    #                                                        ["Spotify", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per total Wordcount",
    #                             "Spotify", label_2="NYTimes", label_3="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)
    #
    # '''
    # 02_a: Most Common Markers - In Percent (share in all Markers)
    # '''
    # most_common_markers_perc = [d_data.spotify.get_most_common_markers(15, perc=True, share='Marker'),
    #                             d_data.ted.get_most_common_markers(15, perc=True, share='Marker'),
    #                             d_data.ny.get_most_common_markers(15, perc=True, share='Marker'),
    #                             d_data.gig.get_most_common_markers(15, perc=True, share='Marker')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Marker-share-percent_mcm",
    #                                                        most_common_markers_perc,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers in %", markers, x_values, "Share in all Markers",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ted_color,
    #                             color_3=d_data.ny_color, color_4=d_data.gig_color)
    #
    # '''
    # 02_b: Most Common Markers - In Percent (share in all Words)
    # '''
    # most_common_markers_perc = [d_data.spotify.get_most_common_markers(15, perc=True, share='Word'),
    #                             d_data.ted.get_most_common_markers(15, perc=True, share='Word'),
    #                             d_data.ny.get_most_common_markers(15, perc=True, share='Word'),
    #                             d_data.gig.get_most_common_markers(15, perc=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Wordcount-share-percent_mcm",
    #                                                        most_common_markers_perc,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers in %", markers, x_values, "Share in all Words",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ted_color,
    #                             color_3=d_data.ny_color, color_4=d_data.gig_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers in %", "Share in all Markers",
    # #                             most_common_markers_perc[0],
    # #                             "Spotify", data.spotify_color,
    # #                             data2=most_common_markers_perc[1],
    # #                             label2="TED", color2=data.ted_color,
    # #                             data3=most_common_markers_perc[2],
    # #                             label3="NYTimes", color3=data.ny_color,
    # #                             data4=most_common_markers_perc[3],
    # #                             label4="Gigaword", color4=data.gig_color,
    # #                             share=True)
    # '''
    # 03_a_1: Most Common Markers - Sentence Begin (per Doc)
    # '''
    # mc_sent_begin = [d_data.spotify.get_most_common_markers(15, position="sb", average=True, share='Doc'),
    #                  d_data.ny.get_most_common_markers(15, position="sb", average=True, share='Doc'),
    #                  d_data.gig.get_most_common_markers(15, position="sb", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SB_per-doc_mcm",
    #                                                        mc_sent_begin,
    #                                                        ["Spotify", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Begin", markers, x_values,
    #                             "Average per Document",
    #                             "Spotify", label_2="NYTimes", label_3="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)
    #
    # '''
    # 03_a_2: Most Common Markers - Sentence Begin (per total WC)
    # '''
    # mc_sent_begin = [d_data.spotify.get_most_common_markers(15, position="sb", average=True, share='Word'),
    #                  d_data.ny.get_most_common_markers(15, position="sb", average=True, share='Word'),
    #                  d_data.gig.get_most_common_markers(15, position="sb", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SB_per-wc_mcm",
    #                                                        mc_sent_begin,
    #                                                        ["Spotify", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Begin", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Spotify", label_2="NYTimes", label_3="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers: Sentence Begin", "Share in all Markers at Sent. Begin",
    # #                             mc_sent_begin[0],
    # #                             "Spotify", data.spotify_color,
    # #                             data2=mc_sent_begin[1],
    # #                             label2="NYTimes", color2=data.ny_color,
    # #                             data3=mc_sent_begin[2],
    # #                             label3="Gigaword", color3=data.gig_color, share=True)
    #
    # '''
    # 03_b_1: Most Common Markers - Sentence Middle (per Doc)
    # '''
    # mc_sent_middle = [d_data.spotify.get_most_common_markers(15, position="sm", average=True, share='Doc'),
    #                   d_data.ny.get_most_common_markers(15, position="sm", average=True, share='Doc'),
    #                   d_data.gig.get_most_common_markers(15, position="sm", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SM_per-doc_mcm",
    #                                                        mc_sent_middle,
    #                                                        ["Spotify", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Middle", markers, x_values,
    #                             "Average per Document",
    #                             "Spotify", label_2="NYTimes", label_3="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)
    #
    # '''
    # 03_b_2: Most Common Markers - Sentence Middle (per total WC)
    # '''
    # mc_sent_middle = [d_data.spotify.get_most_common_markers(15, position="sm", average=True, share='Word'),
    #                   d_data.ny.get_most_common_markers(15, position="sm", average=True, share='Word'),
    #                   d_data.gig.get_most_common_markers(15, position="sm", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SM_per-wc_mcm",
    #                                                        mc_sent_middle,
    #                                                        ["Spotify", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Middle", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Spotify", label_2="NYTimes", label_3="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers: Sentence Middle", "Share in all Markers at Sent. Middle",
    # #                             mc_sent_middle[0],
    # #                             "Spotify", data.spotify_color,
    # #                             data2=mc_sent_middle[1],
    # #                             label2="NYTimes", color2=data.ny_color,
    # #                             data3=mc_sent_middle[2],
    # #                             label3="Gigaword", color3=data.gig_color, share=True)
    # '''
    # 03_c_1: Most Common Markers - Sentence End (per Doc)
    # '''
    # mc_sent_end = [d_data.spotify.get_most_common_markers(15, position="se", average=True, share='Doc'),
    #                d_data.ny.get_most_common_markers(15, position="se", average=True, share='Doc'),
    #                d_data.gig.get_most_common_markers(15, position="se", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SE_per-doc_mcm",
    #                                                        mc_sent_end,
    #                                                        ["Spotify", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence End", markers, x_values,
    #                             "Average per Document",
    #                             "Spotify", label_2="NYTimes", label_3="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)
    #
    # '''
    # 03_c_2: Most Common Markers - Sentence End (per total WC)
    # '''
    # mc_sent_end = [d_data.spotify.get_most_common_markers(15, position="se", average=True, share='Word'),
    #                d_data.ny.get_most_common_markers(15, position="se", average=True, share='Word'),
    #                d_data.gig.get_most_common_markers(15, position="se", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SE_per-wc_mcm",
    #                                                        mc_sent_end,
    #                                                        ["Spotify", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence End", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Spotify", label_2="NYTimes", label_3="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ny_color, color_3=d_data.gig_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers: Sentence End", "Share in all Markers at Sent. End",
    # #                             data.spotify.get_most_common_markers(15, position="se", perc=True),
    # #                             "Spotify", data.spotify_color,
    # #                             data2=data.ny.get_most_common_markers(15, position="se", perc=True),
    # #                             label2="NYTimes", color2=data.ny_color,
    # #                             data3=data.gig.get_most_common_markers(15, position="se", perc=True),
    # #                             label3="Gigaword", color3=data.gig_color, share=True)
    # #
    # '''
    # 04_a_1: Most Common Markers - Document Begin (per Doc)
    # '''
    # mc_doc_begin = [d_data.spotify.get_most_common_markers(15, position="db", average=True, share='Doc'),
    #                 d_data.ted.get_most_common_markers(15, position="db", average=True, share='Doc'),
    #                 d_data.ny.get_most_common_markers(15, position="db", average=True, share='Doc'),
    #                 d_data.gig.get_most_common_markers(15, position="db", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DB_per-doc_mcm",
    #                                                        mc_doc_begin,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Begin", markers, x_values,
    #                             "Average per Document",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ted_color,
    #                             color_3=d_data.ny_color, color_4=d_data.gig_color)
    #
    # '''
    # 04_a_2: Most Common Markers - Document Begin (per total WC)
    # '''
    # mc_doc_begin = [d_data.spotify.get_most_common_markers(15, position="db", average=True, share='Word'),
    #                 d_data.ted.get_most_common_markers(15, position="db", average=True, share='Word'),
    #                 d_data.ny.get_most_common_markers(15, position="db", average=True, share='Word'),
    #                 d_data.gig.get_most_common_markers(15, position="db", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DB_per-wc_mcm",
    #                                                        mc_doc_begin,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Begin", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ted_color,
    #                             color_3=d_data.ny_color, color_4=d_data.gig_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers: Document Begin", "Share in all Markers at Doc. Begin",
    # #                             data.spotify.get_most_common_markers(15, position="db", perc=True),
    # #                             "Spotify", data.spotify_color,
    # #                             data2=data.ted.get_most_common_markers(15, position="db", perc=True),
    # #                             label2="TED", color2=data.ted_color,
    # #                             data3=data.ny.get_most_common_markers(15, position="db", perc=True),
    # #                             label3="NYTimes", color3=data.ny_color,
    # #                             data4=data.gig.get_most_common_markers(15, position="db", perc=True),
    # #                             label4="Gigaword", color4=data.gig_color, share=True)
    #
    # '''
    # 04_b_1: Most Common Markers - Document Middle (per Doc)
    # '''
    # mc_doc_middle = [d_data.spotify.get_most_common_markers(15, position="dm", average=True, share='Doc'),
    #                  d_data.ted.get_most_common_markers(15, position="dm", average=True, share='Doc'),
    #                  d_data.ny.get_most_common_markers(15, position="dm", average=True, share='Doc'),
    #                  d_data.gig.get_most_common_markers(15, position="dm", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DM_per-doc_mcm",
    #                                                        mc_doc_middle,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Middle", markers, x_values,
    #                             "Average per Document",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ted_color,
    #                             color_3=d_data.ny_color, color_4=d_data.gig_color)
    #
    # '''
    # 04_b_2: Most Common Markers - Document Middle (per total WC)
    # '''
    # mc_doc_middle = [d_data.spotify.get_most_common_markers(15, position="dm", average=True, share='Word'),
    #                  d_data.ted.get_most_common_markers(15, position="dm", average=True, share='Word'),
    #                  d_data.ny.get_most_common_markers(15, position="dm", average=True, share='Word'),
    #                  d_data.gig.get_most_common_markers(15, position="dm", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DM_per-wc_mcm",
    #                                                        mc_doc_middle,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Middle", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ted_color,
    #                             color_3=d_data.ny_color, color_4=d_data.gig_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers: Document Middle", "Share in all Markers at Doc. Middle",
    # #                             data.spotify.get_most_common_markers(15, position="dm", perc=True),
    # #                             "Spotify", data.spotify_color,
    # #                             data2=data.ted.get_most_common_markers(15, position="dm", perc=True),
    # #                             label2="TED", color2=data.ted_color,
    # #                             data3=data.ny.get_most_common_markers(15, position="dm", perc=True),
    # #                             label3="NYTimes", color3=data.ny_color,
    # #                             data4=data.gig.get_most_common_markers(15, position="dm", perc=True),
    # #                             label4="Gigaword", color4=data.gig_color, share=True)
    # '''
    # 04_c_1: Most Common Markers - Document End (per Doc)
    # '''
    # mc_doc_end = [d_data.spotify.get_most_common_markers(15, position="de", average=True, share='Doc'),
    #               d_data.ted.get_most_common_markers(15, position="de", average=True, share='Doc'),
    #               d_data.ny.get_most_common_markers(15, position="de", average=True, share='Doc'),
    #               d_data.gig.get_most_common_markers(15, position="de", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DE_per-doc_mcm",
    #                                                        mc_doc_end,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document End", markers, x_values,
    #                             "Average per Document",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ted_color,
    #                             color_3=d_data.ny_color, color_4=d_data.gig_color)
    #
    # '''
    # 04_c_2: Most Common Markers - Document End (per total WC)
    # '''
    # mc_doc_end = [d_data.spotify.get_most_common_markers(15, position="de", average=True, share='Word'),
    #               d_data.ted.get_most_common_markers(15, position="de", average=True, share='Word'),
    #               d_data.ny.get_most_common_markers(15, position="de", average=True, share='Word'),
    #               d_data.gig.get_most_common_markers(15, position="de", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DE_per-wc_mcm",
    #                                                        mc_doc_end,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document End", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=d_data.spotify_color, color_2=d_data.ted_color,
    #                             color_3=d_data.ny_color, color_4=d_data.gig_color)

    # mp.most_common_markers_plot("Most Common Markers: Document End", "Share in all Markers at Doc. End",
    #                             data.spotify.get_most_common_markers(15, position="de", perc=True),
    #                             "Spotify", data.spotify_color,
    #                             data2=data.ted.get_most_common_markers(15, position="de", perc=True),
    #                             label2="TED", color2=data.ted_color,
    #                             data3=data.ny.get_most_common_markers(15, position="de", perc=True),
    #                             label3="NYTimes", color3=data.ny_color,
    #                             data4=data.gig.get_most_common_markers(15, position="de", perc=True),
    #                             label4="Gigaword", color4=data.gig_color, share=True)

    # '''
    # One Plot for each Marker, containing their total number, a_mean, h_mean, mediean and mode in each dataset
    # '''
    # markerlist, y_values = mp.prepare_marker_subplots(data.spotify, data.ted, data.ny, data.gig)
    # mp.plot_marker_subplots("Number of Occurrences per Marker",
    #                         markerlist, y_values, ["a_m.", "h_m.", "med.", "mode"],
    #                         "Spotify", "TED", "NYTimes", "Gigaword",
    #                         color1=data.spotify_color, color2=data.ted_color,
    #                         color3=data.ny_color, color4=data.gig_color)


if __name__ == '__main__':
    main()
