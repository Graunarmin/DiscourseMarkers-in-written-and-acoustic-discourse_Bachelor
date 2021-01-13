import helpers.DataFrames
import helpers.Statistics
from plotting import CreatePlots as cp
from datasets import ConversationTypeData as ctd
from helpers import Helpers as hp


def main():
    c_data = ctd.ConversationTypeData(
        "../../bigData/listenability-tools/Spotify/conversation-types/scores/dialog-scores_short.csv",
        "../../bigData/listenability-tools/Spotify/conversation-types/scores/monolog-scores_short.csv",
        "../../bigData/listenability-tools/Spotify/conversation-types/scores/cooperative-monolog-scores_short.csv",
        "../../bigData/listenability-tools/discourse-types/scores/ted-scores_short.csv",
        dialog_scores_opt=
        "../../bigData/listenability-tools/Spotify/conversation-types/scores/sentence-scores/dialog-sentence-scores.json",
        monolog_scores_opt=
        "../../bigData/listenability-tools/Spotify/conversation-types/scores/sentence-scores/monolog-sentence-scores.json",
        cmonolog_scores_opt=
        "../../bigData/listenability-tools/Spotify/conversation-types/scores/sentence-scores/cooperative-monolog-sentence-scores.json",
        ted_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/sentence-scores/ted-sentence-scores.json")

    '''01:
    Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''
    # dm_per_text_perc = [c_data.dialog.get_percent_dm_per_text_statistics(),
    #                     c_data.monolog.get_percent_dm_per_text_statistics(),
    #                     c_data.cmonolog.get_percent_dm_per_text_statistics(),
    #                     c_data.speech.get_percent_dm_per_text_statistics()]
    #
    # cp.plot_vertical_barchart("Percent Discourse Markers per Text",
    #                           dm_per_text_perc,
    #                           # ["Min", "Mean", "Mode", "Max"],
    #                           ["Mean", "Mode"],
    #                           "Percentage of Markers in all Words of a Text",
    #                           label_1="Dialog", label_2="Monolog",
    #                           label_3="Cooperative-Monolog", label_4="Speech",
    #                           color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                           color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
    #
    # helpers.DataFrames.create_dataframe("DM-per-text-percent_Values",
    #                                     ['Min', 'Mean', 'Mode', 'Max'],
    #                                     dm_per_text_perc[0], data2=dm_per_text_perc[1], data3=dm_per_text_perc[2],
    #                                     data4=dm_per_text_perc[3],
    #                                     label1="Dialog", label2="Monolog",
    #                                     label3="Cooperative-Monolog", label4="Speech")
    #
    # ecdf_dm_percents = [c_data.dialog.get_percent_dm_per_text_column(),
    #                     c_data.monolog.get_percent_dm_per_text_column(),
    #                     c_data.cmonolog.get_percent_dm_per_text_column(),
    #                     c_data.speech.get_percent_dm_per_text_column()]
    #
    # helpers.Statistics.effectsize_and_significance("DM-per-text-percent_Statistics",
    #                                                ecdf_dm_percents,
    #                                                ["Dialog", "Monolog", "Cooperative Monolog", "Speech"])
    #
    '''
    Empirical Distribution Function
    '''
    cp.plot_edf("% of Discourse Markers per Text",
                "% DM per Text", "% of Texts",
                [c_data.dialog.get_percent_dm_per_text_column(collected=True),
                 c_data.monolog.get_percent_dm_per_text_column(collected=True),
                 c_data.cmonolog.get_percent_dm_per_text_column(collected=True),
                 c_data.speech.get_percent_dm_per_text_column(collected=True)],
                ["Dialog", "Monolog", "Cooperative Monolog", "Speech"],
                [c_data.dialog_color, c_data.monolog_color, c_data.cmonolog_color, c_data.speech_color])
    #
    # cp.plot_ecdf(ecdf_dm_percents,
    #              "ECDF for % of Discourse Markers per Text", "% DM per Text", "ECDF (% of Texts)",
    #              ["Dialog", "Monolog", "Cooperative Monolog", "Speech"],
    #              [c_data.dialog_color, c_data.monolog_color, c_data.cmonolog_color, c_data.speech_color])
    #
    # '''02:
    # Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    # min/mean/max(dm_count_doc)
    # '''
    # total_dm_count = [c_data.dialog.get_total_dm_per_text_statistics(),
    #                   c_data.monolog.get_total_dm_per_text_statistics(),
    #                   c_data.cmonolog.get_total_dm_per_text_statistics(),
    #                   c_data.speech.get_total_dm_per_text_statistics()]
    #
    # cp.plot_vertical_barchart("Number Discourse Markers per Text",
    #                           total_dm_count,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Number Markers",
    #                           label_1="Dialog", label_2="Monolog",
    #                           label_3="Cooperative-Monolog", label_4="Speech",
    #                           color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                           color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
    #
    # helpers.DataFrames.create_dataframe("DM-per-text-total_Values",
    #                                     ['Min', 'Mean', 'Mode', 'Max'],
    #                                     total_dm_count[0], data2=total_dm_count[1], data3=total_dm_count[2],
    #                                     data4=total_dm_count[3],
    #                                     label1="Dialog", label2="Monolog",
    #                                     label3="Cooperative-Monolog", label4="Speech")
    #
    # total_dm_count_columns = [c_data.dialog.get_total_dm_per_text_column(),
    #                           c_data.monolog.get_total_dm_per_text_column(),
    #                           c_data.cmonolog.get_total_dm_per_text_column(),
    #                           c_data.speech.get_total_dm_per_text_column()]
    #
    # helpers.Statistics.effectsize_and_significance("DM-per-text-total_Statistics",
    #                                                total_dm_count_columns,
    #                                                ["Dialog", "Monolog", "Cooperative Monolog", "Speech"])
    #
    # '''03:
    # Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    # min/mean/max(dm_sentences_perc)
    # '''
    # dm_sentences_perc = [c_data.dialog.get_percent_dm_sentences_statistics(),
    #                      c_data.monolog.get_percent_dm_sentences_statistics(),
    #                      c_data.cmonolog.get_percent_dm_sentences_statistics()]
    #
    # cp.plot_vertical_barchart("Percent of Sentences with DM per Text",
    #                           dm_sentences_perc,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "% Sentences containing DM per Text",
    #                           label_1="Dialog", label_2="Monolog",
    #                           label_3="Cooperative-Monolog",
    #                           color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                           color_3=c_data.cmonolog_color)
    #
    # helpers.DataFrames.create_dataframe("DM-sentences-percent_Values",
    #                                     ['Min', 'Mean', 'Mode', 'Max'],
    #                                     dm_sentences_perc[0], data2=dm_sentences_perc[1], data3=dm_sentences_perc[2],
    #                                     label1="Dialog", label2="Monolog",
    #                                     label3="Cooperative-Monolog")
    #
    # dm_sentences_perc_column = [c_data.dialog.get_percent_dm_sentences_column(),
    #                             c_data.monolog.get_percent_dm_sentences_column(),
    #                             c_data.cmonolog.get_percent_dm_sentences_column()]
    #
    # helpers.Statistics.effectsize_and_significance("DM-sentences-percent_Statistics",
    #                                                dm_sentences_perc_column,
    #                                                ["Dialog", "Monolog", "Cooperative Monolog"])
    #
    # '''
    # Empirical Distribution Function
    # '''
    # cp.plot_edf("EDF for % of Sentences containing Discourse Markers per Text",
    #             "% DM Sentences per Text", "% of Texts",
    #             [c_data.dialog.get_percent_dm_sentences_column(collected=True),
    #              c_data.monolog.get_percent_dm_sentences_column(collected=True),
    #              c_data.cmonolog.get_percent_dm_sentences_column(collected=True)],
    #             ["Dialog", "Monolog", "Cooperative Monolog"],
    #             [c_data.dialog_color, c_data.monolog_color,
    #              c_data.cmonolog_color])
    #
    # cp.plot_ecdf(dm_sentences_perc_column,
    #              "ECDF for % of Sentences containing Discourse Markers per Text",
    #              "% DM Sentences per Text", "ECDF (% of Texts)",
    #              ["Dialog", "Monolog", "Cooperative Monolog"],
    #              [c_data.dialog_color, c_data.monolog_color,
    #               c_data.cmonolog_color])
    #
    # '''04:
    # Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    # min/mean/max(dm_sentences)
    # '''
    # dm_sentences_total = [c_data.dialog.get_total_dm_sentences_statistics(),
    #                       c_data.monolog.get_total_dm_sentences_statistics(),
    #                       c_data.cmonolog.get_total_dm_sentences_statistics()]
    #
    # cp.plot_vertical_barchart("Number of Sentences containing  DM per Text",
    #                           dm_sentences_total,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Number of Sentences containing DM",
    #                           label_1="Dialog", label_2="Monolog",
    #                           label_3="Cooperative-Monolog",
    #                           color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                           color_3=c_data.cmonolog_color)
    #
    # helpers.DataFrames.create_dataframe("DM-sentences-total_Values",
    #                                     ['Min', 'Mean', 'Mode', 'Max'],
    #                                     dm_sentences_total[0], data2=dm_sentences_total[1],
    #                                     data3=dm_sentences_total[2],
    #                                     label1="Dialog", label2="Monolog",
    #                                     label3="Cooperative-Monolog")
    #
    # dm_sentences_total_column = [c_data.dialog.get_total_dm_sentences_column(),
    #                              c_data.monolog.get_total_dm_sentences_column(),
    #                              c_data.cmonolog.get_total_dm_sentences_column()]
    # helpers.Statistics.effectsize_and_significance("DM-sentences-total_Statistics",
    #                                                dm_sentences_total_column,
    #                                                ["Dialog", "Monolog", "Cooperative Monolog"])
    #
    # '''
    # 05_a: Number of DM per sentence
    # '''
    # dm_per_sent_total = [c_data.dialog.get_total_dm_per_sentence_statistics(),
    #                      c_data.monolog.get_total_dm_per_sentence_statistics(),
    #                      c_data.cmonolog.get_total_dm_per_sentence_statistics()]
    #
    # cp.plot_vertical_barchart("Number of Discourse Markers per Sentence",
    #                           dm_per_sent_total,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Number of Markers per Sentence",
    #                           label_1="Dialog", label_2="Monolog",
    #                           label_3="Cooperative-Monolog",
    #                           color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                           color_3=c_data.cmonolog_color)
    #
    # helpers.DataFrames.create_dataframe("DM-per-sentence_Values",
    #                                     ['Min', 'Mean', 'Mode', 'Max'],
    #                                     dm_per_sent_total[0], data2=dm_per_sent_total[1],
    #                                     data3=dm_per_sent_total[2],
    #                                     label1="Dialog", label2="Monolog",
    #                                     label3="Cooperative-Monolog")
    #
    # dm_per_sentence_column = [c_data.dialog.get_dm_per_sentence(),
    #                           c_data.monolog.get_dm_per_sentence(),
    #                           c_data.cmonolog.get_dm_per_sentence()]
    #
    # helpers.Statistics.effectsize_and_significance("DM-per-sentence_Statistics",
    #                                                dm_per_sentence_column,
    #                                                ["Dialog", "Monolog", "Cooperative Monolog"])

    '''
    05_b: Histogram with Number of DM per Sentence per Dataset
    '''
    dm_per_sent = [c_data.dialog.compute_dm_per_sentence(),
                   c_data.monolog.compute_dm_per_sentence(),
                   c_data.cmonolog.compute_dm_per_sentence()]

    # cp.draw_simple_barchart("Number of Discourse Markers per Sentence",
    #                         ["Dialog", "Monolog", "Cooperative Monolog"],
    #                         dm_per_sent,
    #                         [c_data.dialog_color, c_data.monolog_color, c_data.cmonolog_color])

    '''
   Empirical Distribution Function
   '''
    cp.plot_edf("Discourse Markers per Sentence",
                "DM per Sentence", "% of Sentences",
                dm_per_sent,
                ["Dialog", "Monolog", "Cooperative Monolog"],
                [c_data.dialog_color, c_data.monolog_color, c_data.cmonolog_color])

    # cp.plot_ecdf(dm_per_sentence_column,
    #              "ECDF for % Discourse Markers per Sentence",
    #              "DM per Sentence", "ECDF (% of Sentences)",
    #              ["Dialog", "Monolog", "Cooperative Monolog"],
    #              [c_data.dialog_color, c_data.monolog_color, c_data.cmonolog_color])
    #
    # '''
    # ---- Sentence Positions ----
    # '''
    #
    # '''
    # 06: Percentage of DM at certain positions in a sentence
    # '''
    # dm_pos_sent = [c_data.dialog.get_percent_dm_positions_sentence(),
    #                c_data.monolog.get_percent_dm_positions_sentence(),
    #                c_data.cmonolog.get_percent_dm_positions_sentence()]
    #
    # cp.plot_vertical_barchart("% of DM in a Position in a Sentence",
    #                           dm_pos_sent,
    #                           ['Begin', 'Middle', 'End'],
    #                           "% DM at Postion",
    #                           label_1="Dialog", label_2="Monolog",
    #                           label_3="Cooperative-Monolog",
    #                           color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                           color_3=c_data.cmonolog_color)
    #
    # helpers.DataFrames.create_dataframe("sentence-positions-pecentages_Values",
    #                                     ['Begin', 'Middle', 'End'],
    #                                     dm_pos_sent[0], data2=dm_pos_sent[1],
    #                                     data3=dm_pos_sent[2],
    #                                     label1="Dialog", label2="Monolog",
    #                                     label3="Cooperative-Monolog")
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_begin",
    #                                                [c_data.dialog.get_sent_begin_column(perc=True),
    #                                 c_data.monolog.get_sent_begin_column(perc=True),
    #                                 c_data.cmonolog.get_sent_begin_column(perc=True)],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog"])
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_middle",
    #                                                [c_data.dialog.get_sent_middle_column(perc=True),
    #                                 c_data.monolog.get_sent_middle_column(perc=True),
    #                                 c_data.cmonolog.get_sent_middle_column(perc=True)],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog"])
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_end",
    #                                                [c_data.dialog.get_sent_end_column(perc=True),
    #                                 c_data.monolog.get_sent_end_column(perc=True),
    #                                 c_data.cmonolog.get_sent_end_column(perc=True)],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog"])
    # '''
    # 07: Number of DM at certain positions in a sentence
    # '''
    # dm_pos_sent_total = [c_data.dialog.get_total_dm_positions_sentence(),
    #                      c_data.monolog.get_total_dm_positions_sentence(),
    #                      c_data.cmonolog.get_total_dm_positions_sentence()]
    #
    # cp.plot_vertical_barchart("Number of DM at a certain Position in a Sentence",
    #                           dm_pos_sent_total,
    #                           ["Begin", "Middle", "End"],
    #                           "# DM at Postion",
    #                           label_1="Dialog", label_2="Monolog",
    #                           label_3="Cooperative-Monolog",
    #                           color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                           color_3=c_data.cmonolog_color)
    #
    # helpers.DataFrames.create_dataframe("sentence-positions-totals_Values",
    #                                     ["Begin", "Middle", "End"],
    #                                     dm_pos_sent_total[0], data2=dm_pos_sent_total[1],
    #                                     data3=dm_pos_sent_total[2],
    #                                     label1="Dialog", label2="Monolog",
    #                                     label3="Cooperative-Monolog")
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-totals_Statistics_begin",
    #                                                [c_data.dialog.get_sent_begin_column(),
    #                                 c_data.monolog.get_sent_begin_column(),
    #                                 c_data.cmonolog.get_sent_begin_column()],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog"])
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-totals_Statistics_middle",
    #                                                [c_data.dialog.get_sent_middle_column(),
    #                                 c_data.monolog.get_sent_middle_column(),
    #                                 c_data.cmonolog.get_sent_middle_column()],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog"])
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-totals_Statistics_end",
    #                                                [c_data.dialog.get_sent_end_column(),
    #                                 c_data.monolog.get_sent_end_column(),
    #                                 c_data.cmonolog.get_sent_end_column()],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog"])
    #
    # # '''
    # # Piechart of DM at certain positions in a sentence per Dataset
    # # '''
    # # cp.plot_dm_position_piechart("Number of DM in a Sentence at Position:",
    # #                              [data.spotify.get_sentence_position_values(),
    # #                               data.ny.get_sentence_position_values(),
    # #                               data.gig.get_sentence_position_values()
    # #                               ],
    # #                              ["Spotify Data", "NYTimes Data", "Gigaword Data"],
    # #                              [data.spotify_shades,
    # #                               data.ny_shades,
    # #                               data.gig_shades])
    # '''
    # ---- Document Positions ----
    # '''
    #
    # '''08:
    # Percentage of DM at certain positions in a document
    # '''
    # dm_pos_doc_perc = [c_data.dialog.get_percent_dm_positions_document(),
    #                    c_data.monolog.get_percent_dm_positions_document(),
    #                    c_data.cmonolog.get_percent_dm_positions_document(),
    #                    c_data.speech.get_percent_dm_positions_document()]
    #
    # cp.plot_vertical_barchart("% of DM in a Position in a Document",
    #                           dm_pos_doc_perc,
    #                           ["Begin", "Middle", "End"],
    #                           "% DM at Postion",
    #                           label_1="Dialog", label_2="Monolog",
    #                           label_3="Cooperative-Monolog", label_4="Speech",
    #                           color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                           color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
    #
    # helpers.DataFrames.create_dataframe("document-positions-percentages_Values",
    #                                     ["Begin", "Middle", "End"],
    #                                     dm_pos_doc_perc[0], data2=dm_pos_doc_perc[1], data3=dm_pos_doc_perc[2],
    #                                     data4=dm_pos_doc_perc[3],
    #                                     label1="Dialog", label2="Monolog",
    #                                     label3="Cooperative-Monolog", label4="Speech")
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_begin",
    #                                                [c_data.dialog.get_doc_begin_column(perc=True),
    #                                 c_data.monolog.get_doc_begin_column(perc=True),
    #                                 c_data.cmonolog.get_doc_begin_column(perc=True),
    #                                 c_data.speech.get_doc_begin_column(perc=True)],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog", "Speech"])
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_middle",
    #                                                [c_data.dialog.get_doc_middle_column(perc=True),
    #                                 c_data.monolog.get_doc_middle_column(perc=True),
    #                                 c_data.cmonolog.get_doc_middle_column(perc=True),
    #                                 c_data.speech.get_doc_middle_column(perc=True)],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog", "Speech"])
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_end",
    #                                                [c_data.dialog.get_doc_end_column(perc=True),
    #                                 c_data.monolog.get_doc_end_column(perc=True),
    #                                 c_data.cmonolog.get_doc_end_column(perc=True),
    #                                 c_data.speech.get_doc_end_column(perc=True)],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog", "Speech"])
    #
    # '''
    # 09: Number of DM at certain positions in a document
    # '''
    # dm_pos_doc_total = [c_data.dialog.get_total_dm_positions_document(),
    #                     c_data.monolog.get_total_dm_positions_document(),
    #                     c_data.cmonolog.get_total_dm_positions_document(),
    #                     c_data.speech.get_total_dm_positions_document()]
    #
    # cp.plot_vertical_barchart("Number of DM at a certain Position in a Document",
    #                           dm_pos_doc_total,
    #                           ["Begin", "Middle", "End"],
    #                           "# DM at Postion",
    #                           label_1="Dialog", label_2="Monolog",
    #                           label_3="Cooperative-Monolog", label_4="Speech",
    #                           color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                           color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
    #
    # helpers.DataFrames.create_dataframe("document-positions-totals_Values",
    #                                     ["Begin", "Middle", "End"],
    #                                     dm_pos_doc_total[0], data2=dm_pos_doc_total[1], data3=dm_pos_doc_total[2],
    #                                     data4=dm_pos_doc_total[3],
    #                                     label1="Dialog", label2="Monolog",
    #                                     label3="Cooperative-Monolog", label4="Speech"
    #                                     )
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-totals_Statistics_begin",
    #                                                [c_data.dialog.get_doc_begin_column(),
    #                                 c_data.monolog.get_doc_begin_column(),
    #                                 c_data.cmonolog.get_doc_begin_column(),
    #                                 c_data.speech.get_doc_begin_column()],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog", "Speech"])
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-totals_Statistics_middle",
    #                                                [c_data.dialog.get_doc_middle_column(),
    #                                 c_data.monolog.get_doc_middle_column(),
    #                                 c_data.cmonolog.get_doc_middle_column(),
    #                                 c_data.speech.get_doc_middle_column()],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog", "Speech"])
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-totals_Statistics_end",
    #                                                [c_data.dialog.get_doc_end_column(),
    #                                 c_data.monolog.get_doc_end_column(),
    #                                 c_data.cmonolog.get_doc_end_column(),
    #                                 c_data.speech.get_doc_end_column()],
    #                                                ["Dialog", "Monolog", "Cooperative Monolog", "Speech"])
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

    # '''
    # 01_a: Most Common Markers per Genre - Average per Doc
    # '''
    # most_common_markers = [c_data.dialog.get_most_common_markers(15, average=True, share='Doc'),
    #                        c_data.monolog.get_most_common_markers(15, average=True, share='Doc'),
    #                        c_data.cmonolog.get_most_common_markers(15, average=True, share='Doc'),
    #                        c_data.speech.get_most_common_markers(15, average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Average-per-Document_mcm",
    #                                                        most_common_markers,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Document",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers per Genre", "Average Number of Occurences per Document",
    # #                             most_common_markers[0],
    # #                             "News", data.news_color,
    # #                             data2=most_common_markers[1],
    # #                             label2="Discussion/Opinion", color2=data.discussion_color,
    # #                             data3=most_common_markers[2],
    # #                             label3="Science", color3=data.science_color,
    # #                             data4=most_common_markers[3],
    # #                             label4="Documentary", color4=data.documentary_color,
    # #                             data5=most_common_markers[4],
    # #                             label5="Speech", color5=data.speech_color,
    # #                             share=True)
    #
    # '''
    # 01_b: Most Common Markers per Genre - Average per Sentence
    # '''
    # most_common_markers = [c_data.dialog.get_most_common_markers(15, average=True, share='Sent'),
    #                        c_data.monolog.get_most_common_markers(15, average=True, share='Sent'),
    #                        c_data.cmonolog.get_most_common_markers(15, average=True, share='Sent')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Average-per-Sentence_mcm",
    #                                                        most_common_markers,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Sentence",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color)
    #
    # '''
    # 01_c: Most Common Markers - Average per Total Wordcount
    # '''
    # most_common_markers_sent = [c_data.dialog.get_most_common_markers(15, average=True, share='Word'),
    #                             c_data.monolog.get_most_common_markers(15, average=True, share='Word'),
    #                             c_data.cmonolog.get_most_common_markers(15, average=True, share='Word'),
    #                             c_data.speech.get_most_common_markers(15, average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Average-per-total-Wordcount_mcm",
    #                                                        most_common_markers_sent,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per total Wordcount",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
    #
    # '''
    # 02_a: Most Common Markers per Genre - In Percent (share in all Markers)
    # '''
    # most_common_markers_perc = [c_data.dialog.get_most_common_markers(15, perc=True, share='Marker'),
    #                             c_data.monolog.get_most_common_markers(15, perc=True, share='Marker'),
    #                             c_data.cmonolog.get_most_common_markers(15, perc=True, share='Marker'),
    #                             c_data.speech.get_most_common_markers(15, perc=True, share='Marker')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Marker-share-percent_mcm",
    #                                                        most_common_markers_perc,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers in %", markers, x_values, "Share in all Markers",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
    #                             label_5="Speech",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
    #
    # '''
    # 02_b: Most Common Markers - In Percent (share in all Words)
    # '''
    # most_common_markers_perc = [c_data.dialog.get_most_common_markers(15, perc=True, share='Word'),
    #                             c_data.monolog.get_most_common_markers(15, perc=True, share='Word'),
    #                             c_data.cmonolog.get_most_common_markers(15, perc=True, share='Word'),
    #                             c_data.speech.get_most_common_markers(15, perc=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Wordcount-share-percent_mcm",
    #                                                        most_common_markers_perc,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers in %", markers, x_values, "Share in all Words",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
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
    # '''
    # 03_a_1: Most Common Markers per Genre - Sentence Begin (per Doc)
    # '''
    # mc_sent_begin = [c_data.dialog.get_most_common_markers(15, position="sb", average=True, share='Doc'),
    #                  c_data.monolog.get_most_common_markers(15, position="sb", average=True, share='Doc'),
    #                  c_data.cmonolog.get_most_common_markers(15, position="sb", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SB_per-doc_mcm",
    #                                                        mc_sent_begin,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Begin", markers, x_values,
    #                             "Average per Document",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color)
    #
    # '''
    # 03_a_2: Most Common Markers - Sentence Begin (per total WC)
    # '''
    # mc_sent_begin = [c_data.dialog.get_most_common_markers(15, position="sb", average=True, share='Word'),
    #                  c_data.monolog.get_most_common_markers(15, position="sb", average=True, share='Word'),
    #                  c_data.cmonolog.get_most_common_markers(15, position="sb", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SB_per-wc_mcm",
    #                                                        mc_sent_begin,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Begin", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers: Sentence Begin", "Share in all Markers at Sent. Begin",
    # #                             data.spotify.get_most_common_markers(15, position="sb", perc=True),
    # #                             "Spotify", data.spotify_color,
    # #                             data2=data.ny.get_most_common_markers(15, position="sb", perc=True),
    # #                             label2="NYTimes", color2=data.ny_color,
    # #                             data3=data.gig.get_most_common_markers(15, position="sb", perc=True),
    # #                             label3="Gigaword", color3=data.gig_color, share=True)
    # '''
    # 03_b_1: Most Common Markers per Genre - Sentence Middle (per Doc)
    # '''
    # mc_sent_middle = [c_data.dialog.get_most_common_markers(15, position="sm", average=True, share='Doc'),
    #                   c_data.monolog.get_most_common_markers(15, position="sm", average=True, share='Doc'),
    #                   c_data.cmonolog.get_most_common_markers(15, position="sm", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SM_per-doc_mcm",
    #                                                        mc_sent_middle,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Middle", markers, x_values,
    #                             "Average per Document",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color)
    #
    # '''
    # 03_b_2: Most Common Markers - Sentence Middle (per total WC)
    # '''
    # mc_sent_middle = [c_data.dialog.get_most_common_markers(15, position="sm", average=True, share='Word'),
    #                   c_data.monolog.get_most_common_markers(15, position="sm", average=True, share='Word'),
    #                   c_data.cmonolog.get_most_common_markers(15, position="sm", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SM_per-wc_mcm",
    #                                                        mc_sent_middle,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Middle", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers: Sentence Middle", "Share in all Markers at Sent. Middle",
    # #                             data.spotify.get_most_common_markers(15, position="sm", perc=True),
    # #                             "Spotify", data.spotify_color,
    # #                             data2=data.ny.get_most_common_markers(15, position="sm", perc=True),
    # #                             label2="NYTimes", color2=data.ny_color,
    # #                             data3=data.gig.get_most_common_markers(15, position="sm", perc=True),
    # #                             label3="Gigaword", color3=data.gig_color, share=True)
    # '''
    # 03_c_1: Most Common Markers per Genre - Sentence End (per Doc)
    # '''
    # mc_sent_end = [c_data.dialog.get_most_common_markers(15, position="se", average=True, share='Doc'),
    #                c_data.monolog.get_most_common_markers(15, position="se", average=True, share='Doc'),
    #                c_data.cmonolog.get_most_common_markers(15, position="se", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SE_per-doc_mcm",
    #                                                        mc_sent_end,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence End", markers, x_values,
    #                             "Average per Document",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color)
    #
    # '''
    # 03_c_2: Most Common Markers - Sentence End (per total WC)
    # '''
    # mc_sent_end = [c_data.dialog.get_most_common_markers(15, position="se", average=True, share='Word'),
    #                c_data.monolog.get_most_common_markers(15, position="se", average=True, share='Word'),
    #                c_data.cmonolog.get_most_common_markers(15, position="se", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SE_per-wc_mcm",
    #                                                        mc_sent_end,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence End", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers: Sentence End", "Share in all Markers at Sent. End",
    # #                             data.spotify.get_most_common_markers(15, position="se", perc=True),
    # #                             "Spotify", data.spotify_color,
    # #                             data2=data.ny.get_most_common_markers(15, position="se", perc=True),
    # #                             label2="NYTimes", color2=data.ny_color,
    # #                             data3=data.gig.get_most_common_markers(15, position="se", perc=True),
    # #                             label3="Gigaword", color3=data.gig_color, share=True)
    # '''
    # 04_a_1: Most Common Markers per Genre - Document Begin (per Doc)
    # '''
    # mc_doc_begin = [c_data.dialog.get_most_common_markers(15, position="db", average=True, share='Doc'),
    #                 c_data.monolog.get_most_common_markers(15, position="db", average=True, share='Doc'),
    #                 c_data.cmonolog.get_most_common_markers(15, position="db", average=True, share='Doc'),
    #                 c_data.speech.get_most_common_markers(15, position="db", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DB_per-doc_mcm",
    #                                                        mc_doc_begin,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Begin", markers, x_values,
    #                             "Average per Document",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
    #
    # '''
    # 04_a_2: Most Common Markers - Document Begin (per total WC)
    # '''
    # mc_doc_begin = [c_data.dialog.get_most_common_markers(15, position="db", average=True, share='Word'),
    #                 c_data.monolog.get_most_common_markers(15, position="db", average=True, share='Word'),
    #                 c_data.cmonolog.get_most_common_markers(15, position="db", average=True, share='Word'),
    #                 c_data.speech.get_most_common_markers(15, position="db", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DB_per-wc_mcm",
    #                                                        mc_doc_begin,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Begin", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
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
    # '''
    # 04_b_1: Most Common Markers per Genre - Document Middle (per Doc)
    # '''
    # mc_doc_middle = [c_data.dialog.get_most_common_markers(15, position="dm", average=True, share='Doc'),
    #                  c_data.monolog.get_most_common_markers(15, position="dm", average=True, share='Doc'),
    #                  c_data.cmonolog.get_most_common_markers(15, position="dm", average=True, share='Doc'),
    #                  c_data.speech.get_most_common_markers(15, position="dm", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DM_per-doc_mcm",
    #                                                        mc_doc_middle,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Middle", markers, x_values,
    #                             "Average per Document",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
    #
    # '''
    # 04_b_2: Most Common Markers - Document Middle (per total WC)
    # '''
    # mc_doc_middle = [c_data.dialog.get_most_common_markers(15, position="dm", average=True, share='Word'),
    #                  c_data.monolog.get_most_common_markers(15, position="dm", average=True, share='Word'),
    #                  c_data.cmonolog.get_most_common_markers(15, position="dm", average=True, share='Word'),
    #                  c_data.speech.get_most_common_markers(15, position="dm", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DM_per-wc_mcm",
    #                                                        mc_doc_middle,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Middle", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
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
    # 04_c_1: Most Common Markers per Genre - Document End (per Doc)
    # '''
    # mc_doc_end = [c_data.dialog.get_most_common_markers(15, position="de", average=True, share='Doc'),
    #               c_data.monolog.get_most_common_markers(15, position="de", average=True, share='Doc'),
    #               c_data.cmonolog.get_most_common_markers(15, position="de", average=True, share='Doc'),
    #               c_data.speech.get_most_common_markers(15, position="de", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DE_per-doc_mcm",
    #                                                        mc_doc_end,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document End", markers, x_values,
    #                             "Average per Document",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color, color_4=c_data.speech_color)
    #
    # '''
    # 04_c_2: Most Common Markers - Document End (per total WC)
    # '''
    # mc_doc_end = [c_data.dialog.get_most_common_markers(15, position="de", average=True, share='Word'),
    #               c_data.monolog.get_most_common_markers(15, position="de", average=True, share='Word'),
    #               c_data.cmonolog.get_most_common_markers(15, position="de", average=True, share='Word'),
    #               c_data.speech.get_most_common_markers(15, position="de", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DE_per-wc_mcm",
    #                                                        mc_doc_end,
    #                                                        ["Monolog", "Dialog", "Cooperative Monolog", "Speech"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document End", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "Dialog", label_2="Monolog", label_3="Cooperative-Monolog", label_4="Speech",
    #                             color_1=c_data.dialog_color, color_2=c_data.monolog_color,
    #                             color_3=c_data.cmonolog_color, color_4=c_data.speech_color)

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
