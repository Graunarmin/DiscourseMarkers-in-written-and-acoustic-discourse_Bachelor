import helpers.DataFrames
import helpers.Statistics
from plotting import CreatePlots as cp
from datasets import GenreData as gd
from helpers import Helpers as hp


def main():
    g_data = gd.GenreData(
        "../../bigData/listenability-tools/Spotify/genres/scores/news-scores_short.csv",
        "../../bigData/listenability-tools/Spotify/genres/scores/discussion-scores_short.csv",
        "../../bigData/listenability-tools/Spotify/genres/scores/science-scores_short.csv",
        "../../bigData/listenability-tools/Spotify/genres/scores/documentary-scores_short.csv",
        "../../bigData/listenability-tools/discourse-types/scores/ted-scores_short.csv",
        news_scores_opt=
        "../../bigData/listenability-tools/Spotify/genres/scores/sentence-scores/news-sentence-scores.json",
        discussion_scores_opt=
        "../../bigData/listenability-tools/Spotify/genres/scores/sentence-scores/discussion-sentence-scores.json",
        science_scores_opt=
        "../../bigData/listenability-tools/Spotify/genres/scores/sentence-scores/science-sentence-scores.json",
        documentary_scores_opt=
        "../../bigData/listenability-tools/Spotify/genres/scores/sentence-scores/documentary-sentence-scores.json",
        ted_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/sentence-scores/ted-sentence-scores.json")

    '''01:
    Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''
    # dm_per_text_perc = [g_data.news.get_percent_dm_per_text_statistics(),
    #                     g_data.discussion.get_percent_dm_per_text_statistics(),
    #                     g_data.science.get_percent_dm_per_text_statistics(),
    #                     g_data.documentary.get_percent_dm_per_text_statistics(),
    #                     g_data.presentation.get_percent_dm_per_text_statistics()]
    #
    # cp.plot_vertical_barchart("Percent Discourse Markers per Text",
    #                           dm_per_text_perc,
    #                           # ["Min", "Mean", "Mode", "Max"],
    #                           ["Mean", "Mode"],
    #                           "Percentage of Markers in all Words of a Text",
    #                           label_1="News", label_2="Discussion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           label_5="Presentation",
    #                           color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                           color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                           color_5=g_data.presentation_color)
    #
    # helpers.DataFrames.create_dataframe("DM-per-text-percent_Values",
    #                                     ['Min', 'Mean', 'Mode', 'Max'],
    #                                     dm_per_text_perc[0], data2=dm_per_text_perc[1], data3=dm_per_text_perc[2],
    #                                     data4=dm_per_text_perc[3], data5=dm_per_text_perc[4],
    #                                     label1="News", label2="Discussion",
    #                                     label3="Science/Education", label4="Documentary",
    #                                     label5="Presentation")
    #
    # ecdf_dm_per_text_perc = [g_data.news.get_percent_dm_per_text_column(),
    #                          g_data.discussion.get_percent_dm_per_text_column(),
    #                          g_data.science.get_percent_dm_per_text_column(),
    #                          g_data.documentary.get_percent_dm_per_text_column(),
    #                          g_data.presentation.get_percent_dm_per_text_column()]
    #
    # helpers.Statistics.effectsize_and_significance("DM-per-text-percent_Statistics",
    #                                                ecdf_dm_per_text_perc,
    #                                                ["News", "Discussion", "Science/Education", "Documentary", "Presentation"])
    #
    '''
    Empirical Distribution Function
    '''
    cp.plot_edf("% of Discourse Markers per Text",
                "% DM per Text", "% of Texts",
                [g_data.news.get_percent_dm_per_text_column(collected=True),
                 g_data.discussion.get_percent_dm_per_text_column(collected=True),
                 g_data.science.get_percent_dm_per_text_column(collected=True),
                 g_data.documentary.get_percent_dm_per_text_column(collected=True),
                 g_data.presentation.get_percent_dm_per_text_column(collected=True)],
                ["News", "Discussion", "Science/Education", "Documentary", "Presentation"],
                [g_data.news_color, g_data.discussion_color, g_data.science_color,
                 g_data.documentary_color, g_data.presentation_color])
    #
    # cp.plot_ecdf(ecdf_dm_per_text_perc,
    #              "ECDF for % of Discourse Markers per Text", "% DM per Text", "ECDF (% of Texts)",
    #              ["News", "Discussion", "Science/Education", "Documentary", "Presentation"],
    #              [g_data.news_color, g_data.discussion_color, g_data.science_color,
    #               g_data.documentary_color, g_data.presentation_color])
    #
    # '''02:
    # Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    # min/mean/max(dm_count_doc)
    # '''
    # total_dm_count = [g_data.news.get_total_dm_per_text_statistics(),
    #                   g_data.discussion.get_total_dm_per_text_statistics(),
    #                   g_data.science.get_total_dm_per_text_statistics(),
    #                   g_data.documentary.get_total_dm_per_text_statistics(),
    #                   g_data.presentation.get_total_dm_per_text_statistics()]
    #
    # cp.plot_vertical_barchart("Number Discourse Markers per Text",
    #                           total_dm_count,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Marker Occurrences Total",
    #                           label_1="News", label_2="Discussion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           label_5="Presentation",
    #                           color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                           color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                           color_5=g_data.presentation_color)
    #
    # helpers.DataFrames.create_dataframe("DM-per-text-total_Values",
    #                                     ['Min', 'Mean', 'Mode', 'Max'],
    #                                     total_dm_count[0], data2=total_dm_count[1], data3=total_dm_count[2],
    #                                     data4=total_dm_count[3], data5=total_dm_count[4],
    #                                     label1="News", label2="Discussion",
    #                                     label3="Science/Education", label4="Documentary",
    #                                     label5="Presentation")
    #
    # total_dm_count_columns = [g_data.news.get_total_dm_per_text_column(),
    #                           g_data.discussion.get_total_dm_per_text_column(),
    #                           g_data.science.get_total_dm_per_text_column(),
    #                           g_data.documentary.get_total_dm_per_text_column(),
    #                           g_data.presentation.get_total_dm_per_text_column()]
    #
    # helpers.Statistics.effectsize_and_significance("DM-per-text-total_Statistics",
    #                                                total_dm_count_columns,
    #                                                ["News", "Discussion", "Science/Education", "Documentary", "Presentation"])
    #
    # '''
    # 03: Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    # min/mean/max(dm_sentences_perc)
    # '''
    # dm_sentences_perc = [g_data.news.get_percent_dm_sentences_statistics(),
    #                      g_data.discussion.get_percent_dm_sentences_statistics(),
    #                      g_data.science.get_percent_dm_sentences_statistics(),
    #                      g_data.documentary.get_percent_dm_sentences_statistics()]
    #
    # cp.plot_vertical_barchart("Percent of Sentences with DM per Text",
    #                           dm_sentences_perc,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "% Sentences containing DM per Text",
    #                           label_1="News", label_2="Discussion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                           color_3=g_data.science_color, color_4=g_data.documentary_color)
    #
    # helpers.DataFrames.create_dataframe("DM-sentences-percent_Values",
    #                                     ['Min', 'Mean', 'Mode', 'Max'],
    #                                     dm_sentences_perc[0], data2=dm_sentences_perc[1], data3=dm_sentences_perc[2],
    #                                     data4=dm_sentences_perc[3],
    #                                     label1="News", label2="Discussion",
    #                                     label3="Science/Education", label4="Documentary")
    #
    # dm_sentences_perc_column = [g_data.news.get_percent_dm_sentences_column(),
    #                             g_data.discussion.get_percent_dm_sentences_column(),
    #                             g_data.science.get_percent_dm_sentences_column(),
    #                             g_data.documentary.get_percent_dm_sentences_column()]
    #
    # helpers.Statistics.effectsize_and_significance("DM-sentences-percent_Statistics",
    #                                                dm_sentences_perc_column,
    #                                                ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # '''
    # Empirical Distribution Function
    # '''
    # cp.plot_edf("EDF for % of Sentences containing Discourse Markers per Text",
    #             "% DM Sentences per Text", "% of Texts",
    #             [g_data.news.get_percent_dm_sentences_column(collected=True),
    #              g_data.discussion.get_percent_dm_sentences_column(collected=True),
    #              g_data.science.get_percent_dm_sentences_column(collected=True),
    #              g_data.documentary.get_percent_dm_sentences_column(collected=True)],
    #             ["News", "Discussion", "Science/Education", "Documentary", "Presentation"],
    #             [g_data.news_color, g_data.discussion_color, g_data.science_color,
    #              g_data.documentary_color]
    #             )
    #
    # cp.plot_ecdf(dm_sentences_perc_column,
    #              "ECDF for % of Sentences containing Discourse Markers per Text",
    #              "% DM Sentences per Text", "ECDF (% of Texts)",
    #              ["News", "Discussion", "Science/Education", "Documentary", "Presentation"],
    #              [g_data.news_color, g_data.discussion_color, g_data.science_color,
    #               g_data.documentary_color])
    #
    # '''
    # 04: Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    # min/mean/max(dm_sentences)
    # '''
    # dm_sentences_total = [g_data.news.get_total_dm_sentences_statistics(),
    #                       g_data.discussion.get_total_dm_sentences_statistics(),
    #                       g_data.science.get_total_dm_sentences_statistics(),
    #                       g_data.documentary.get_total_dm_sentences_statistics()]
    #
    # cp.plot_vertical_barchart("Number of Sentences containing  DM per Text",
    #                           dm_sentences_total,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Number of Sentences containing DM",
    #                           label_1="News", label_2="Discussion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                           color_3=g_data.science_color, color_4=g_data.documentary_color)
    #
    # helpers.DataFrames.create_dataframe("DM-sentences-total_Values",
    #                                     ['Min', 'Mean', 'Mode', 'Max'],
    #                                     dm_sentences_total[0], data2=dm_sentences_total[1],
    #                                     data3=dm_sentences_total[2], data4=dm_sentences_total[3],
    #                                     label1="News", label2="Discussion",
    #                                     label3="Science/Education", label4="Documentary")
    #
    # dm_sentences_total_column = [g_data.news.get_total_dm_sentences_column(),
    #                              g_data.discussion.get_total_dm_sentences_column(),
    #                              g_data.science.get_total_dm_sentences_column(),
    #                              g_data.documentary.get_total_dm_sentences_column()]
    #
    # helpers.Statistics.effectsize_and_significance("DM-sentences-total_Statistics",
    #                                                dm_sentences_total_column,
    #                                                ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # '''
    # 05_a: Number of DM per sentence
    # '''
    # dm_per_sent_total = [g_data.news.get_total_dm_per_sentence_statistics(),
    #                      g_data.discussion.get_total_dm_per_sentence_statistics(),
    #                      g_data.science.get_total_dm_per_sentence_statistics(),
    #                      g_data.documentary.get_total_dm_per_sentence_statistics()]
    #
    # cp.plot_vertical_barchart("Number of Discourse Markers per Sentence",
    #                           dm_per_sent_total,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Number of Markers per Sentence",
    #                           label_1="News", label_2="Discussion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                           color_3=g_data.science_color, color_4=g_data.documentary_color)
    #
    # helpers.DataFrames.create_dataframe("DM-per-sentence_Values",
    #                                     ['Min', 'Mean', 'Mode', 'Max'],
    #                                     dm_per_sent_total[0], data2=dm_per_sent_total[1],
    #                                     data3=dm_per_sent_total[2], data4=dm_per_sent_total[3],
    #                                     label1="News", label2="Discussion",
    #                                     label3="Science/Education", label4="Documentary")
    #
    # dm_per_sentence_column = [g_data.news.get_dm_per_sentence(),
    #                           g_data.discussion.get_dm_per_sentence(),
    #                           g_data.science.get_dm_per_sentence(),
    #                           g_data.documentary.get_dm_per_sentence()]
    #
    # helpers.Statistics.effectsize_and_significance("DM-per-sentence_Statistics",
    #                                                dm_per_sentence_column,
    #                                                ["News", "Discussion", "Science/Education", "Documentary"])
    #
    '''
    05_b: Histogram with Number of DM per Sentence per Dataset
    '''
    dm_per_sent = [g_data.news.compute_dm_per_sentence(),
                   g_data.discussion.compute_dm_per_sentence(),
                   g_data.science.compute_dm_per_sentence(),
                   g_data.documentary.compute_dm_per_sentence()]
    #
    # cp.draw_simple_barchart("Number of Discourse Markers per Sentence",
    #                         ["News", "Discussion", "Science/Education", "Documentary"],
    #                         dm_per_sent,
    #                         [g_data.news_color, g_data.discussion_color, g_data.science_color,
    #                          g_data.documentary_color])
    #
    '''
    Empirical Distribution Function
    '''
    cp.plot_edf("Discourse Markers per Sentence",
                "DM per Sentence", "% of Sentences",
                dm_per_sent,
                ["News", "Discussion", "Science/Education", "Documentary"],
                [g_data.news_color, g_data.discussion_color, g_data.science_color,
                 g_data.documentary_color])
    #
    # cp.plot_ecdf(dm_per_sentence_column,
    #              "ECDF for % Discourse Markers per Sentence",
    #              "DM per Sentence", "ECDF (% of Sentences)",
    #              ["News", "Discussion", "Science/Education", "Documentary"],
    #              [g_data.news_color, g_data.discussion_color, g_data.science_color,
    #               g_data.documentary_color])
    #
    # '''
    # ---- Sentence Positions ----
    # '''
    #
    # '''
    # 06: Percentage of DM at certain positions in a sentence
    # '''
    # dm_pos_sent = [g_data.news.get_percent_dm_positions_sentence(),
    #                g_data.discussion.get_percent_dm_positions_sentence(),
    #                g_data.science.get_percent_dm_positions_sentence(),
    #                g_data.documentary.get_percent_dm_positions_sentence()]
    #
    # cp.plot_vertical_barchart("% of DM in a Position in a Sentence",
    #                           dm_pos_sent,
    #                           ['Begin', 'Middle', 'End'],
    #                           "% DM at Postion",
    #                           label_1="News", label_2="Discussion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                           color_3=g_data.science_color, color_4=g_data.documentary_color)
    #
    # helpers.DataFrames.create_dataframe("sentence-positions-pecentages_Values",
    #                                     ['Begin', 'Middle', 'End'],
    #                                     dm_pos_sent[0], data2=dm_pos_sent[1],
    #                                     data3=dm_pos_sent[2], data4=dm_pos_sent[3],
    #                                     label1="News", label2="Discussion",
    #                                     label3="Science/Education", label4="Documentary")
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_begin",
    #                                                [g_data.news.get_sent_begin_column(perc=True),
    #                                 g_data.discussion.get_sent_begin_column(perc=True),
    #                                 g_data.science.get_sent_begin_column(perc=True),
    #                                 g_data.documentary.get_sent_begin_column(perc=True)],
    #                                                ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_middle",
    #                                                [g_data.news.get_sent_middle_column(perc=True),
    #                                 g_data.discussion.get_sent_middle_column(perc=True),
    #                                 g_data.science.get_sent_middle_column(perc=True),
    #                                 g_data.documentary.get_sent_middle_column(perc=True)],
    #                                                ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_end",
    #                                                [g_data.news.get_sent_end_column(perc=True),
    #                                 g_data.discussion.get_sent_end_column(perc=True),
    #                                 g_data.science.get_sent_end_column(perc=True),
    #                                 g_data.documentary.get_sent_end_column(perc=True)],
    #                                                ["News", "Discussion", "Science/Education", "Documentary"])
    # '''
    # 07: Number of DM at certain positions in a sentence
    # '''
    # dm_pos_sent_total = [g_data.news.get_total_dm_positions_sentence(),
    #                      g_data.discussion.get_total_dm_positions_sentence(),
    #                      g_data.science.get_total_dm_positions_sentence(),
    #                      g_data.documentary.get_total_dm_positions_sentence()]
    #
    # cp.plot_vertical_barchart("Number of DM at a certain Position in a Sentence",
    #                           dm_pos_sent_total,
    #                           ["Begin", "Middle", "End"],
    #                           "# DM at Postion",
    #                           label_1="News", label_2="Discussion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                           color_3=g_data.science_color, color_4=g_data.documentary_color)
    #
    # helpers.DataFrames.create_dataframe("sentence-positions-totals_Values",
    #                                     ["Begin", "Middle", "End"],
    #                                     dm_pos_sent_total[0], data2=dm_pos_sent_total[1],
    #                                     data3=dm_pos_sent_total[2], data4=dm_pos_sent_total[3],
    #                                     label1="News", label2="Discussion",
    #                                     label3="Science/Education", label4="Documentary")
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-totals_Statistics_begin",
    #                                                [g_data.news.get_sent_begin_column(),
    #                                 g_data.discussion.get_sent_begin_column(),
    #                                 g_data.science.get_sent_begin_column(),
    #                                 g_data.documentary.get_sent_begin_column()],
    #                                                ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-totals_Statistics_middle",
    #                                                [g_data.news.get_sent_middle_column(),
    #                                 g_data.discussion.get_sent_middle_column(),
    #                                 g_data.science.get_sent_middle_column(),
    #                                 g_data.documentary.get_sent_middle_column()],
    #                                                ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # helpers.Statistics.effectsize_and_significance("sentence-positions-totals_Statistics_end",
    #                                                [g_data.news.get_sent_end_column(),
    #                                 g_data.discussion.get_sent_end_column(),
    #                                 g_data.science.get_sent_end_column(),
    #                                 g_data.documentary.get_sent_end_column()],
    #                                                ["News", "Discussion", "Science/Education", "Documentary"])
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
    # '''
    # 08: Percentage of DM at certain positions in a document
    # '''
    # dm_pos_doc_perc = [g_data.news.get_percent_dm_positions_document(),
    #                    g_data.discussion.get_percent_dm_positions_document(),
    #                    g_data.science.get_percent_dm_positions_document(),
    #                    g_data.documentary.get_percent_dm_positions_document(),
    #                    g_data.presentation.get_percent_dm_positions_document()]
    #
    # cp.plot_vertical_barchart("% of DM in a Position in a Document",
    #                           dm_pos_doc_perc,
    #                           ["Begin", "Middle", "End"],
    #                           "% DM at Postion",
    #                           label_1="News", label_2="Discussion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           label_5="Presentation",
    #                           color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                           color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                           color_5=g_data.presentation_color)
    #
    # helpers.DataFrames.create_dataframe("document-positions-percentages_Values",
    #                                     ["Begin", "Middle", "End"],
    #                                     dm_pos_doc_perc[0], data2=dm_pos_doc_perc[1], data3=dm_pos_doc_perc[2],
    #                                     data4=dm_pos_doc_perc[3], data5=dm_pos_doc_perc[4],
    #                                     label1="News", label2="Discussion",
    #                                     label3="Science/Education", label4="Documentary",
    #                                     label5="Presentation")
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_begin",
    #                                                [g_data.news.get_doc_begin_column(perc=True),
    #                                 g_data.discussion.get_doc_begin_column(perc=True),
    #                                 g_data.science.get_doc_begin_column(perc=True),
    #                                 g_data.documentary.get_doc_begin_column(perc=True),
    #                                 g_data.presentation.get_doc_begin_column(perc=True)],
    #                                                ["News", "Discussion", "Science/Education", "Documentary", "Presentation"])
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_middle",
    #                                                [g_data.news.get_doc_middle_column(perc=True),
    #                                 g_data.discussion.get_doc_middle_column(perc=True),
    #                                 g_data.science.get_doc_middle_column(perc=True),
    #                                 g_data.documentary.get_doc_middle_column(perc=True),
    #                                 g_data.presentation.get_doc_middle_column(perc=True)],
    #                                                ["News", "Discussion", "Science/Education", "Documentary", "Presentation"])
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_end",
    #                                                [g_data.news.get_doc_end_column(perc=True),
    #                                 g_data.discussion.get_doc_end_column(perc=True),
    #                                 g_data.science.get_doc_end_column(perc=True),
    #                                 g_data.documentary.get_doc_end_column(perc=True),
    #                                 g_data.presentation.get_doc_end_column(perc=True)],
    #                                                ["News", "Discussion", "Science/Education", "Documentary", "Presentation"])
    #
    # '''
    # 09: Number of DM at certain positions in a document
    # '''
    # dm_pos_doc_total = [g_data.news.get_total_dm_positions_document(),
    #                     g_data.discussion.get_total_dm_positions_document(),
    #                     g_data.science.get_total_dm_positions_document(),
    #                     g_data.documentary.get_total_dm_positions_document(),
    #                     g_data.presentation.get_total_dm_positions_document()]
    #
    # cp.plot_vertical_barchart("Number of DM at a certain Position in a Document",
    #                           dm_pos_doc_total,
    #                           ["Begin", "Middle", "End"],
    #                           "# DM at Postion",
    #                           label_1="News", label_2="Discussion",
    #                           label_3="Science/Education", label_4="Documentary",
    #                           label_5="Presentation",
    #                           color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                           color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                           color_5=g_data.presentation_color)
    #
    # helpers.DataFrames.create_dataframe("document-positions-totals_Values",
    #                                     ["Begin", "Middle", "End"],
    #                                     dm_pos_doc_total[0], data2=dm_pos_doc_total[1], data3=dm_pos_doc_total[2],
    #                                     data4=dm_pos_doc_total[3], data5=dm_pos_doc_total[4],
    #                                     label1="News", label2="Discussion",
    #                                     label3="Science/Education", label4="Documentary",
    #                                     label5="Presentation")
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-totals_Statistics_begin",
    #                                                [g_data.news.get_doc_begin_column(),
    #                                 g_data.discussion.get_doc_begin_column(),
    #                                 g_data.science.get_doc_begin_column(),
    #                                 g_data.documentary.get_doc_begin_column(),
    #                                 g_data.presentation.get_doc_begin_column()],
    #                                                ["News", "Discussion", "Science/Education", "Documentary", "Presentation"])
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-totals_Statistics_middle",
    #                                                [g_data.news.get_doc_middle_column(),
    #                                 g_data.discussion.get_doc_middle_column(),
    #                                 g_data.science.get_doc_middle_column(),
    #                                 g_data.documentary.get_doc_middle_column(),
    #                                 g_data.presentation.get_doc_middle_column()],
    #                                                ["News", "Discussion", "Science/Education", "Documentary", "Presentation"])
    #
    # helpers.Statistics.effectsize_and_significance("document-positions-totals_Statistics_end",
    #                                                [g_data.news.get_doc_end_column(),
    #                                 g_data.discussion.get_doc_end_column(),
    #                                 g_data.science.get_doc_end_column(),
    #                                 g_data.documentary.get_doc_end_column(),
    #                                 g_data.presentation.get_doc_end_column()],
    #                                                ["News", "Discussion", "Science/Education", "Documentary", "Presentation"])
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
    # most_common_markers = [g_data.news.get_most_common_markers(15, average=True, share='Doc'),
    #                        g_data.discussion.get_most_common_markers(15, average=True, share='Doc'),
    #                        g_data.science.get_most_common_markers(15, average=True, share='Doc'),
    #                        g_data.documentary.get_most_common_markers(15, average=True, share='Doc'),
    #                        g_data.speech.get_most_common_markers(15, average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Average-per-Document_mcm",
    #                                                        most_common_markers,
    #                                                        ["News", "Discussion", "Science/Education", "Documentary",
    #                                                         "Presentation"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Document",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             label_5="Presentation", color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                             color_5=g_data.speech_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers per Genre", "Average Number of Occurences per Document",
    # #                             most_common_markers[0],
    # #                             "News", data.news_color,
    # #                             data2=most_common_markers[1],
    # #                             label2="Discussion", color2=data.discussion_color,
    # #                             data3=most_common_markers[2],
    # #                             label3="Science/Education", color3=data.science_color,
    # #                             data4=most_common_markers[3],
    # #                             label4="Documentary", color4=data.documentary_color,
    # #                             data5=most_common_markers[4],
    # #                             label5="Presentation", color5=data.speech_color,
    # #                             share=True)
    #
    # '''
    # 01_b: Most Common Markers per Genre - Average per Sentence
    # '''
    # most_common_markers = [g_data.news.get_most_common_markers(15, average=True, share='Sent'),
    #                        g_data.discussion.get_most_common_markers(15, average=True, share='Sent'),
    #                        g_data.science.get_most_common_markers(15, average=True, share='Sent'),
    #                        g_data.documentary.get_most_common_markers(15, average=True, share='Sent')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Average-per-Sentence_mcm",
    #                                                        most_common_markers,
    #                                                        ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Sentence",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color)
    #
    # '''
    # 01_c: Most Common Markers per Genre - Average per Total Wordcount
    # '''
    # most_common_markers = [g_data.news.get_most_common_markers(15, average=True, share='Word'),
    #                        g_data.discussion.get_most_common_markers(15, average=True, share='Word'),
    #                        g_data.science.get_most_common_markers(15, average=True, share='Word'),
    #                        g_data.documentary.get_most_common_markers(15, average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Average-per-total-Wordcount_mcm",
    #                                                        most_common_markers,
    #                                                        ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per total Wordcount",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color)
    #
    # '''
    # 02_a: Most Common Markers per Genre - In Percent (share in all Markers)
    # '''
    # most_common_markers_perc = [g_data.news.get_most_common_markers(15, perc=True, share='Marker'),
    #                             g_data.discussion.get_most_common_markers(15, perc=True, share='Marker'),
    #                             g_data.science.get_most_common_markers(15, perc=True, share='Marker'),
    #                             g_data.documentary.get_most_common_markers(15, perc=True, share='Marker'),
    #                             g_data.speech.get_most_common_markers(15, perc=True, share='Marker')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Marker-share-percent_mcm",
    #                                                        most_common_markers_perc,
    #                                                        ["News", "Discussion", "Science/Education",
    #                                                         "Documentary", "Presentation"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers in %", markers, x_values, "Share in all Markers",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             label_5="Presentation",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                             color_5=g_data.speech_color)
    #
    # '''
    # 02_b: Most Common Markers per Genre - In Percent (share in all Words)
    # '''
    # most_common_markers_perc = [g_data.news.get_most_common_markers(15, perc=True, share='Word'),
    #                             g_data.discussion.get_most_common_markers(15, perc=True, share='Word'),
    #                             g_data.science.get_most_common_markers(15, perc=True, share='Word'),
    #                             g_data.documentary.get_most_common_markers(15, perc=True, share='Word'),
    #                             g_data.speech.get_most_common_markers(15, perc=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Wordcount-share-percent_mcm",
    #                                                        most_common_markers_perc,
    #                                                        ["News", "Discussion", "Science/Education",
    #                                                         "Documentary", "Presentation"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers in %", markers, x_values, "Share in all Words",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             label_5="Presentation",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                             color_5=g_data.speech_color)
    #
    # # mp.most_common_markers_plot("Most Common Markers per Genre in %", "Share in all Markers",
    # #                             most_common_markers_perc[0],
    # #                             "News", data.news_color,
    # #                             data2=most_common_markers_perc[1],
    # #                             label2="Discussion", color2=data.discussion_color,
    # #                             data3=most_common_markers_perc[2],
    # #                             label3="Science/Education", color3=data.science_color,
    # #                             data4=most_common_markers_perc[3],
    # #                             label4="Documentary", color4=data.documentary_color,
    # #                             data5=most_common_markers_perc[4],
    # #                             label5="Presentation", color5=data.speech_color,
    # #                             share=True)
    #
    # '''
    # 03_a_1: Most Common Markers per Genre - Sentence Begin (per Doc)
    # '''
    # mc_sent_begin = [g_data.news.get_most_common_markers(15, position="sb", average=True, share='Doc'),
    #                  g_data.discussion.get_most_common_markers(15, position="sb", average=True, share='Doc'),
    #                  g_data.science.get_most_common_markers(15, position="sb", average=True, share='Doc'),
    #                  g_data.documentary.get_most_common_markers(15, position="sb", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SB_per-doc_mcm",
    #                                                        mc_sent_begin,
    #                                                        ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Begin", markers, x_values,
    #                             "Average per Document",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color)
    #
    # '''
    # 03_a_2: Most Common Markers per Genre - Sentence Begin (per total WC)
    # '''
    # mc_sent_begin = [g_data.news.get_most_common_markers(15, position="sb", average=True, share='Word'),
    #                  g_data.discussion.get_most_common_markers(15, position="sb", average=True, share='Word'),
    #                  g_data.science.get_most_common_markers(15, position="sb", average=True, share='Word'),
    #                  g_data.documentary.get_most_common_markers(15, position="sb", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SB_per-wc_mcm",
    #                                                        mc_sent_begin,
    #                                                        ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Begin", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color)
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
    # mc_sent_middle = [g_data.news.get_most_common_markers(15, position="sm", average=True, share='Doc'),
    #                   g_data.discussion.get_most_common_markers(15, position="sm", average=True, share='Doc'),
    #                   g_data.science.get_most_common_markers(15, position="sm", average=True, share='Doc'),
    #                   g_data.documentary.get_most_common_markers(15, position="sm", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SM_per-doc_mcm",
    #                                                        mc_sent_middle,
    #                                                        ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Middle", markers, x_values,
    #                             "Average per Document",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color)
    #
    # '''
    # 03_b_2: Most Common Markers per Genre - Sentence Middle (per total WC)
    # '''
    # mc_sent_middle = [g_data.news.get_most_common_markers(15, position="sm", average=True, share='Word'),
    #                   g_data.discussion.get_most_common_markers(15, position="sm", average=True, share='Word'),
    #                   g_data.science.get_most_common_markers(15, position="sm", average=True, share='Word'),
    #                   g_data.documentary.get_most_common_markers(15, position="sm", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SM_per-wc_mcm",
    #                                                        mc_sent_middle,
    #                                                        ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Middle", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color)
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
    # mc_sent_end = [g_data.news.get_most_common_markers(15, position="se", average=True, share='Doc'),
    #                g_data.discussion.get_most_common_markers(15, position="se", average=True, share='Doc'),
    #                g_data.science.get_most_common_markers(15, position="se", average=True, share='Doc'),
    #                g_data.documentary.get_most_common_markers(15, position="se", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SE_per-doc_mcm",
    #                                                        mc_sent_end,
    #                                                        ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence End", markers, x_values,
    #                             "Average per Document",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color)
    #
    # '''
    # 03_c_2: Most Common Markers per Genre - Sentence End (per total WC)
    # '''
    # mc_sent_end = [g_data.news.get_most_common_markers(15, position="se", average=True, share='Word'),
    #                g_data.discussion.get_most_common_markers(15, position="se", average=True, share='Word'),
    #                g_data.science.get_most_common_markers(15, position="se", average=True, share='Word'),
    #                g_data.documentary.get_most_common_markers(15, position="se", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("SE_per-wc_mcm",
    #                                                        mc_sent_end,
    #                                                        ["News", "Discussion", "Science/Education", "Documentary"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence End", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color)
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
    # mc_doc_begin = [g_data.news.get_most_common_markers(15, position="db", average=True, share='Doc'),
    #                 g_data.discussion.get_most_common_markers(15, position="db", average=True, share='Doc'),
    #                 g_data.science.get_most_common_markers(15, position="db", average=True, share='Doc'),
    #                 g_data.documentary.get_most_common_markers(15, position="db", average=True, share='Doc'),
    #                 g_data.speech.get_most_common_markers(15, position="db", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DB_per-doc_mcm",
    #                                                        mc_doc_begin,
    #                                                        ["News", "Discussion", "Science/Education",
    #                                                         "Documentary", "Presentation"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Begin", markers, x_values,
    #                             "Average per Document",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             label_5="Presentation",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                             color_5=g_data.speech_color)
    #
    # '''
    # 04_a_2: Most Common Markers per Genre - Document Begin (per total WC)
    # '''
    # mc_doc_begin = [g_data.news.get_most_common_markers(15, position="db", average=True, share='Word'),
    #                 g_data.discussion.get_most_common_markers(15, position="db", average=True, share='Word'),
    #                 g_data.science.get_most_common_markers(15, position="db", average=True, share='Word'),
    #                 g_data.documentary.get_most_common_markers(15, position="db", average=True, share='Word'),
    #                 g_data.speech.get_most_common_markers(15, position="db", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DB_per-wc_mcm",
    #                                                        mc_doc_begin,
    #                                                        ["News", "Discussion", "Science/Education",
    #                                                         "Documentary", "Presentation"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Begin", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             label_5="Presentation",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                             color_5=g_data.speech_color)
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
    # mc_doc_middle = [g_data.news.get_most_common_markers(15, position="dm", average=True, share='Doc'),
    #                  g_data.discussion.get_most_common_markers(15, position="dm", average=True, share='Doc'),
    #                  g_data.science.get_most_common_markers(15, position="dm", average=True, share='Doc'),
    #                  g_data.documentary.get_most_common_markers(15, position="dm", average=True, share='Doc'),
    #                  g_data.speech.get_most_common_markers(15, position="dm", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DM_per-doc_mcm",
    #                                                        mc_doc_middle,
    #                                                        ["News", "Discussion", "Science/Education",
    #                                                         "Documentary", "Presentation"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Middle", markers, x_values,
    #                             "Average per Document",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             label_5="Presentation",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                             color_5=g_data.speech_color)
    #
    # '''
    # 04_b_2: Most Common Markers per Genre - Document Middle (per total WC)
    # '''
    # mc_doc_middle = [g_data.news.get_most_common_markers(15, position="dm", average=True, share='Word'),
    #                  g_data.discussion.get_most_common_markers(15, position="dm", average=True, share='Word'),
    #                  g_data.science.get_most_common_markers(15, position="dm", average=True, share='Word'),
    #                  g_data.documentary.get_most_common_markers(15, position="dm", average=True, share='Word'),
    #                  g_data.speech.get_most_common_markers(15, position="dm", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DM_per-wc_mcm",
    #                                                        mc_doc_middle,
    #                                                        ["News", "Discussion", "Science/Education",
    #                                                         "Documentary", "Presentation"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Middle", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             label_5="Presentation",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                             color_5=g_data.speech_color)
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
    # mc_doc_end = [g_data.news.get_most_common_markers(15, position="de", average=True, share='Doc'),
    #               g_data.discussion.get_most_common_markers(15, position="de", average=True, share='Doc'),
    #               g_data.science.get_most_common_markers(15, position="de", average=True, share='Doc'),
    #               g_data.documentary.get_most_common_markers(15, position="de", average=True, share='Doc'),
    #               g_data.speech.get_most_common_markers(15, position="de", average=True, share='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DE_per-doc_mcm",
    #                                                        mc_doc_end,
    #                                                        ["News", "Discussion", "Science/Education",
    #                                                         "Documentary", "Presentation"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document End", markers, x_values,
    #                             "Average per Document",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             label_5="Presentation",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                             color_5=g_data.speech_color)
    #
    # '''
    # 04_c_1: Most Common Markers per Genre - Document End (per total Wordcount)
    # '''
    # mc_doc_end = [g_data.news.get_most_common_markers(15, position="de", average=True, share='Word'),
    #               g_data.discussion.get_most_common_markers(15, position="de", average=True, share='Word'),
    #               g_data.science.get_most_common_markers(15, position="de", average=True, share='Word'),
    #               g_data.documentary.get_most_common_markers(15, position="de", average=True, share='Word'),
    #               g_data.speech.get_most_common_markers(15, position="de", average=True, share='Word')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("DE_per-wc_mcm",
    #                                                        mc_doc_end,
    #                                                        ["News", "Discussion", "Science/Education",
    #                                                         "Documentary", "Presentation"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document End", markers, x_values,
    #                             "Average per total Wordcount",
    #                             "News", label_2="Discussion", label_3="Science/Education", label_4="Documentary",
    #                             label_5="Presentation",
    #                             color_1=g_data.news_color, color_2=g_data.discussion_color,
    #                             color_3=g_data.science_color, color_4=g_data.documentary_color,
    #                             color_5=g_data.speech_color)

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
