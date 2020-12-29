import helpers.DataFrames
import helpers.Statistics
from plotting import CreatePlots as cp
from datasets import DiscourseTypeData as dtd


def main():
    d_data = dtd.DiscourseTypeData(
        "../../bigData/listenability-tools/discourse-types/scores/spotify-scores_short.csv",
        "../../bigData/listenability-tools/discourse-types/scores/acoustic-scores_short.csv",
        "../../bigData/listenability-tools/discourse-types/scores/written-scores_short.csv",
        spotify_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/sentence-scores/spotify-sentence-scores.json",
        acoustic_opt=
        "../../bigData/listenability-tools/discourse-types/scores/sentence-scores/spotify-sentence-scores.json",
        written_opt=
        "../../bigData/listenability-tools/discourse-types/scores/sentence-scores/written-sentence-scores.json"
    )

    '''
    01: Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''

    dm_count_perc = [d_data.acoustic.get_percent_dm_per_text_statistics(),
                     d_data.written.get_percent_dm_per_text_statistics()]

    cp.plot_vertical_barchart("Percent Discourse Markers per Text",
                              dm_count_perc,
                              ["Min", "Mean", "Mode", "Max"],
                              "Percentage of Markers in all Words of a Text",
                              label_1=d_data.acoustic_label, label_2=d_data.written_label,
                              color_1=d_data.acoustic_color, color_2=d_data.written_color)

    # Add a plot with spoken vs. written

    helpers.DataFrames.create_dataframe("DM-per-text-percent_Values",
                                        ['Min', 'Mean', 'Mode', 'Max'],
                                        dm_count_perc[0], data2=dm_count_perc[1],
                                        label1=d_data.acoustic_label, label2=d_data.written_label)

    ecdfd_dm_percents = [d_data.acoustic.get_percent_dm_per_text_column(),
                         d_data.written.get_percent_dm_per_text_column()]

    helpers.Statistics.effectsize_and_significance("DM-per-text-percent_Statistics",
                                                   [ecdfd_dm_percents[0], ecdfd_dm_percents[1]],
                                                   [d_data.acoustic_color, d_data.written_label])

    '''
    Empirical Distribution Function
    '''

    cp.plot_edf("EDF for  % of Discourse Markers per Text",
                "% DM per Text", "EDF (% of Texts)",
                [d_data.acoustic.get_percent_dm_per_text_column(collected=True),
                 d_data.written.get_percent_dm_per_text_column(collected=True)],
                [d_data.acoustic_label, d_data.written_label],
                [d_data.acoustic_color, d_data.written_color]
                )

    cp.plot_ecdf(ecdfd_dm_percents,
                 "ECDF for % of Discourse Markers per Text", "% DM per Text", "ECDF (% of Texts)",
                 [d_data.acoustic_label, d_data.written_label],
                 [d_data.acoustic_color, d_data.written_color])

    '''
    03: Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    min/mean/max(dm_sentences_perc)
    '''
    dm_sentences_perc = [d_data.spotify.get_percent_dm_sentences_statistics(),
                         d_data.written.get_percent_dm_sentences_statistics()]

    cp.plot_vertical_barchart("Percent of Sentences with DM per Text",
                              dm_sentences_perc,
                              ["Min", "Mean", "Mode", "Max"],
                              "% Sentences containing DM per Text",
                              label_1=d_data.spotify_label, label_2=d_data.written_label,
                              color_1=d_data.spotify_color, color_2=d_data.written_color)

    helpers.DataFrames.create_dataframe("DM-sentences-percent_Values",
                                        ['Min', 'Mean', 'Mode', 'Max'],
                                        dm_sentences_perc[0], data2=dm_sentences_perc[1],
                                        label1=d_data.spotify_label,
                                        label2=d_data.written_label)

    dm_sentences_perc_column = [d_data.spotify.get_percent_dm_sentences_column(),
                                d_data.written.get_percent_dm_sentences_column()]

    helpers.Statistics.effectsize_and_significance("DM-sentences-percent_Statistics",
                                                   [dm_sentences_perc_column[0], dm_sentences_perc_column[1]],
                                                   [d_data.spotify_label, d_data.written_label])

    '''
    Empirical Distribution Function
    '''
    cp.plot_edf("EDF for % of Sentences containing Discourse Markers per Text",
                "% DM Sentences per Text", "EDF (% of Texts)",
                [d_data.spotify.get_percent_dm_sentences_column(collected=True),
                 d_data.written.get_percent_dm_sentences_column(collected=True)],
                [d_data.spotify_label, d_data.written_label],
                [d_data.spotify_color, d_data.written_color])

    cp.plot_ecdf(dm_sentences_perc_column,
                 "ECDF for % of Sentences containing Discourse Markers per Text",
                 "% DM Sentences per Text", "ECDF (% of Texts)",
                 [d_data.spotify_label, d_data.written_label],
                 [d_data.spotify_color, d_data.written_color])

    '''
    05_a: Number of DM per sentence
    '''
    dm_per_sentence = [d_data.spotify.get_total_dm_per_sentence_statistics(),
                       d_data.written.get_total_dm_per_sentence_statistics()]

    cp.plot_vertical_barchart("Number of Discourse Markers per Sentence",
                              dm_per_sentence,
                              ["Min", "Mean", "Mode", "Max"],
                              "Number of Markers per Sentence",
                              label_1=d_data.spotify_label, label_2=d_data.written_label,
                              color_1=d_data.spotify_color, color_2=d_data.written_color)

    helpers.DataFrames.create_dataframe("DM-per-sentence_Values",
                                        ['Min', 'Mean', 'Mode', 'Max'],
                                        dm_per_sentence[0], data2=dm_per_sentence[1],
                                        label1=d_data.spotify_label, label2=d_data.written_label)

    dm_per_sentence_column = [d_data.spotify.get_dm_per_sentence(),
                              d_data.written.get_dm_per_sentence()]

    helpers.Statistics.effectsize_and_significance("DM-per-sentence_Statistics",
                                                   [dm_per_sentence_column[0], dm_per_sentence_column[1]],
                                                   [d_data.spotify_label, d_data.written_label])

    '''
    05_b: Histogram with Number of DM per Sentence per Dataset
    '''
    dm_per_sent = [d_data.spotify.compute_dm_per_sentence(),
                   d_data.written.compute_dm_per_sentence()]

    cp.draw_one_row_simple_barchart("Number of Discourse Markers per Sentence",
                            [d_data.spotify_label, d_data.written_label],
                            dm_per_sent,
                            [d_data.spotify_color, d_data.written_color])

    '''
    Empirical Distribution Function
    '''
    cp.plot_edf("EDF for % Discourse Markers per Sentence",
                "DM per Sentence", "% of Sentences",
                dm_per_sent,
                [d_data.spotify_label, d_data.written_label],
                [d_data.spotify_color, d_data.written_color])

    cp.plot_ecdf(dm_per_sentence_column,
                 "ECDF for % Discourse Markers per Sentence",
                 "DM per Sentence", "ECDF (% of Sentences)",
                 [d_data.spotify_label, d_data.written_label],
                 [d_data.spotify_color, d_data.written_color])

    '''
    ---- Sentence Positions ----
    '''

    '''
    06: Percentage of DM at certain positions in a sentence
    '''
    dm_pos_sent_perc = [d_data.spotify.get_percent_dm_positions_sentence(),
                        d_data.written.get_percent_dm_positions_sentence()]

    cp.plot_vertical_barchart("% of DM in a Position in a Sentence",
                              dm_pos_sent_perc,
                              ["Begin", "Middle", "End"],
                              "% DM at Postion",
                              label_1=d_data.spotify_label, label_2=d_data.written_label,
                              color_1=d_data.spotify_color, color_2=d_data.written_color)

    helpers.DataFrames.create_dataframe("sentence-positions-pecentages_Values",
                                        ['Begin', 'Middle', 'End'],
                                        dm_pos_sent_perc[0], data2=dm_pos_sent_perc[1],
                                        label1=d_data.spotify_label, label2=d_data.written_label)

    helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_begin",
                                                   [d_data.spotify.get_sent_begin_column(perc=True),
                                                    d_data.written.get_sent_begin_column(perc=True)],
                                                   [d_data.spotify_label, d_data.written_label])

    helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_middle",
                                                   [d_data.spotify.get_sent_middle_column(perc=True),
                                                    d_data.written.get_sent_middle_column(perc=True)],
                                                   [d_data.spotify_label, d_data.written_label])

    helpers.Statistics.effectsize_and_significance("sentence-positions-pecentages_Statistics_end",
                                                   [d_data.spotify.get_sent_end_column(perc=True),
                                                    d_data.written.get_sent_end_column(perc=True)],
                                                   [d_data.spotify_label, d_data.written_label])

    '''
    ---- Document Positions ----
    '''

    '''
    08: Percentage of DM at certain positions in a Document
    '''
    dm_pos_doc_perc = [d_data.acoustic.get_percent_dm_positions_document(),
                       d_data.written.get_percent_dm_positions_document()]

    cp.plot_vertical_barchart("% of DM in a Position in a Document",
                              dm_pos_doc_perc,
                              ["Begin", "Middle", "End"],
                              "% DM at Postion",
                              label_1=d_data.acoustic_label, label_2=d_data.written_label,
                              color_1=d_data.acoustic_color, color_2=d_data.written_color)

    helpers.DataFrames.create_dataframe("document-positions-percentages_Values",
                                        ['Begin', 'Middle', 'End'],
                                        dm_pos_doc_perc[0], data2=dm_pos_doc_perc[1],
                                        label1=d_data.acoustic_label, label2=d_data.written_label)

    helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_begin",
                                                   [d_data.acoustic.get_doc_begin_column(perc=True),
                                                    d_data.written.get_doc_begin_column(perc=True)],
                                                   [d_data.acoustic_label, d_data.written_label])

    helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_middle",
                                                   [d_data.acoustic.get_doc_middle_column(perc=True),
                                                    d_data.written.get_doc_middle_column(perc=True)],
                                                   [d_data.acoustic_label, d_data.written_label])

    helpers.Statistics.effectsize_and_significance("document-positions-percentages_Statistics_end",
                                                   [d_data.acoustic.get_doc_end_column(perc=True),
                                                    d_data.written.get_doc_end_column(perc=True)],
                                                   [d_data.acoustic_label, d_data.written_label])


if __name__ == '__main__':
    main()
