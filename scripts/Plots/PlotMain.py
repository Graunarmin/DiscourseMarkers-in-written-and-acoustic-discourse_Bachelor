import CreatePlots as cp
import MarkerPlots as mp
import DatasetScores as ds
import Helpers as hp


# -------- Read in data ----------
class CorpusData:
    def __init__(self,
                 spotify_scores, spotify_dict,
                 ted_scores, ted_dict,
                 ny_scores, ny_dict,
                 gig_scores, gig_dict,
                 markertypes=None):
        self.spotify = ds.DatasetScores(spotify_scores, spotify_dict, markertypes=markertypes)
        self.ted = ds.DatasetScores(ted_scores, ted_dict, markertypes=markertypes)
        self.ny = ds.DatasetScores(ny_scores, ny_dict, markertypes=markertypes)
        self.gig = ds.DatasetScores(gig_scores, gig_dict, markertypes=markertypes)

        # Colors:   [base, darker, lighter]
        self.spotify_color = '#1DB954'
        self.spotify_shades = ['#1DB954', '#0e5c2a', '#8edca9']
        self.ted_color = '#e62b1e'
        self.ted_shades = ['#e62b1e', '#73150f', '#f2958e']
        self.ny_color = '#FFA700'
        self.ny_shades = ['#FFA700', '#7f5300', '#ffd37f']
        self.gig_color = '#227DFB'
        self.gig_shades = ['#227DFB', '#113e7d', '#90befd']


def main():
    data = CorpusData("../../bigData/listenability-tools/datasets/scores/spotify-scores_short.csv",
                      "../../bigData/listenability-tools/datasets/dict/spotify-dict.json",
                      "../../bigData/listenability-tools/datasets/scores/ted-scores_short.csv",
                      "../../bigData/listenability-tools/datasets/dict/ted-dict.json",
                      "../../bigData/listenability-tools/datasets/scores/nytimes-scores_short.csv",
                      "../../bigData/listenability-tools/datasets/dict/nytimes-dict.json",
                      "../../bigData/listenability-tools/datasets/scores/gigaword-scores_short.csv",
                      "../../bigData/listenability-tools/datasets/dict/gigaword-dict.json",
                      markertypes="../../data/listenability-tools/main-senses/words_main-sense.json")

    '''01:
    Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''

    # dm_count_perc = [data.spotify.get_percent_dm_count_statistics(),
    #                  data.ted.get_percent_dm_count_statistics(),
    #                  data.ny.get_percent_dm_count_statistics(),
    #                  data.gig.get_percent_dm_count_statistics()]
    #
    # cp.plot_vertical_barchart("Percent Discourse Markers per Text",
    #                           dm_count_perc,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Marker Occurrences in %",
    #                           label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                           color_1=data.spotify_color, color_2=data.ted_color,
    #                           color_3=data.ny_color, color_4=data.gig_color)
    #
    # hp.show_dataframe("Percent Discourse Markers per Text",
    #                   ['Min', 'Mean', 'Mode', 'Max'],
    #                   dm_count_perc[0], data2=dm_count_perc[1], data3=dm_count_perc[2],
    #                   data4=dm_count_perc[3],
    #                   label1="Spotify", label2="TED",
    #                   label3="NYTimes", label4="Gigaword")
    #
    # hp.effectsize_and_significance("Percent Discourse Markers per Text",
    #                                [dm_count_perc[0] + dm_count_perc[1], dm_count_perc[2] + dm_count_perc[3]],
    #                                ["Spoken", "Written"])

    '''02:
    Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_count_doc)
    '''
    # dm_count_total = [data.spotify.get_total_dm_count_statistics(),
    #                   data.ted.get_total_dm_count_statistics(),
    #                   data.ny.get_total_dm_count_statistics(),
    #                   data.ny.get_total_dm_count_statistics()]
    #
    # cp.plot_vertical_barchart("Number Discourse Markers per Text",
    #                           dm_count_total,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Marker Occurrences Total",
    #                           label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                           color_1=data.spotify_color, color_2=data.ted_color,
    #                           color_3=data.ny_color, color_4=data.gig_color)
    #
    # hp.show_dataframe("Number Discourse Markers per Text",
    #                   ['Min', 'Mean', 'Mode', 'Max'],
    #                   dm_count_total[0], data2=dm_count_total[1], data3=dm_count_total[2],
    #                   data4=dm_count_total[3],
    #                   label1="Spotify", label2="TED",
    #                   label3="NYTimes", label4="Gigaword")
    #
    # hp.effectsize_and_significance("Number Discourse Markers per Text",
    #                                [dm_count_total[0] + dm_count_total[1],
    #                                 dm_count_total[2] + dm_count_total[3]],
    #                                ["Spoken", "Written"])
    #
    '''03:
    Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    min/mean/max(dm_sentences_perc)
    '''
    # dm_sentences_perc = [data.spotify.get_percent_dm_sentences_statistics(),
    #                      data.ny.get_percent_dm_sentences_statistics(),
    #                      data.gig.get_percent_dm_sentences_statistics()]
    #
    # cp.plot_vertical_barchart("Percent of Sentences with DM per Text",
    #                           dm_sentences_perc,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Sentences containing DM in %",
    #                           label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                           color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)
    #
    # hp.show_dataframe("Percent of Sentences with DM per Text",
    #                   ['Min', 'Mean', 'Mode', 'Max'],
    #                   dm_sentences_perc[0], data2=dm_sentences_perc[1], data3=dm_sentences_perc[2],
    #                   label1="Spotify",
    #                   label2="NYTimes", label3="Gigaword")
    #
    # hp.effectsize_and_significance("Percent of Sentences with DM per Text",
    #                                [dm_sentences_perc[0], dm_sentences_perc[1] + dm_sentences_perc[2]],
    #                                ["Spotify", "Written"])
    #
    '''04:
    Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_sentences)
    '''
    # dm_sentences_total = [data.spotify.get_total_dm_sentences_statistics(),
    #                       data.ny.get_total_dm_sentences_statistics(),
    #                       data.gig.get_total_dm_sentences_statistics()]
    #
    # cp.plot_vertical_barchart("Number of Sentences with DM per Text",
    #                           dm_sentences_total,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Number of Sentences containing DM",
    #                           label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                           color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)
    #
    # hp.show_dataframe("Number of Sentences with DM per Text",
    #                   ['Min', 'Mean', 'Mode', 'Max'],
    #                   dm_sentences_total[0], data2=dm_sentences_total[1], data3=dm_sentences_total[2],
    #                   label1="Spotify",
    #                   label2="NYTimes", label3="Gigaword")
    #
    # hp.effectsize_and_significance("Number of Sentences with DM per Text",
    #                                [dm_sentences_total[0], dm_sentences_total[1] + dm_sentences_total[2]],
    #                                ["Spotify", "Written"])
    #
    '''05_a:
    Number of DM per sentence
    '''
    # dm_per_sentence = [data.spotify.get_total_dm_per_sentence_statistics(),
    #                    data.ny.get_total_dm_per_sentence_statistics(),
    #                    data.gig.get_total_dm_per_sentence_statistics()]
    #
    # cp.plot_vertical_barchart("Number of Discourse Markers per Sentence",
    #                           dm_per_sentence,
    #                           ["Min", "Mean", "Mode", "Max"],
    #                           "Number of Markers per Sentence",
    #                           label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                           color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)
    #
    # hp.show_dataframe("Number of Discourse Markers per Sentence",
    #                   ['Min', 'Mean', 'Mode', 'Max'],
    #                   dm_per_sentence[0], data2=dm_per_sentence[1], data3=dm_per_sentence[2],
    #                   label1="Spotify",
    #                   label2="NYTimes", label3="Gigaword")
    #
    # hp.effectsize_and_significance("Number of Discourse Markers per Sentence",
    #                                [dm_per_sentence[0], dm_per_sentence[1] + dm_per_sentence[2]],
    #                                ["Spotify", "Written"])
    #
    '''05_b:
    Histogram with Number of DM per Sentence per Dataset
    '''
    # cp.draw_simple_barchart("Number of Discourse Markers per Sentence",
    #                         ["Spotify", "NYTimes", "Gigaword"],
    #                         [data.spotify.compute_dm_per_sentence(),
    #                          data.ny.compute_dm_per_sentence(),
    #                          data.gig.compute_dm_per_sentence()],
    #                         [data.spotify_color, data.ny_color, data.gig_color])
    #
    '''
    ---- Sentence Positions ----
    '''

    '''06:
    Percentage of DM at certain positions in a sentence
    '''
    # dm_pos_sent_perc = [data.spotify.get_percent_dm_positions_sentence(),
    #                     data.ny.get_percent_dm_positions_sentence(),
    #                     data.gig.get_percent_dm_positions_sentence()]
    #
    # cp.plot_vertical_barchart("% of DM in a Position in a Sentence",
    #                           dm_pos_sent_perc,
    #                           ["Begin", "Middle", "End"],
    #                           "% DM at Postion",
    #                           label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                           color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)
    #
    # hp.show_dataframe("% of DM in a Position in a Sentence",
    #                   ['Begin', 'Middle', 'End'],
    #                   dm_pos_sent_perc[0], data2=dm_pos_sent_perc[1], data3=dm_pos_sent_perc[2],
    #                   label1="Spotify",
    #                   label2="NYTimes", label3="Gigaword")
    #
    # hp.effectsize_and_significance("% of DM in a Position in a Sentence",
    #                                [dm_pos_sent_perc[0], dm_pos_sent_perc[1] + dm_pos_sent_perc[2]],
    #                                ["Spotify", "Written"])
    #
    '''07:
    Number of DM at certain positions in a sentence
    '''
    dm_pos_sent_total = [data.spotify.get_total_dm_positions_sentence(),
                         data.ny.get_total_dm_positions_sentence(),
                         data.gig.get_total_dm_positions_sentence()]

    cp.plot_vertical_barchart("Number of DM at a certain Position in a Sentence",
                              dm_pos_sent_total,
                              ["Begin", "Middle", "End"],
                              "Number of DM at Postion",
                              label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                              color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)

    hp.show_dataframe("Number of DM at a certain Position in a Sentence",
                      ['Begin', 'Middle', 'End'],
                      dm_pos_sent_total[0], data2=dm_pos_sent_total[1], data3=dm_pos_sent_total[2],
                      label1="Spotify",
                      label2="NYTimes", label3="Gigaword")

    hp.effectsize_and_significance("Number of DM at a certain Position in a Sentence",
                                   [dm_pos_sent_total[0], dm_pos_sent_total[1] + dm_pos_sent_total[2]],
                                   ["Spotify", "Written"])

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
    '''
    ---- Document Positions ----
    '''

    '''08:
    Percentage of DM at certain positions in a Document
    '''
    # dm_pos_doc_perc = [data.spotify.get_percent_dm_positions_document(),
    #                    data.ted.get_percent_dm_positions_document(),
    #                    data.ny.get_percent_dm_positions_document(),
    #                    data.gig.get_percent_dm_positions_document()]
    #
    # cp.plot_vertical_barchart("% of DM in a Position in a Document",
    #                           dm_pos_doc_perc,
    #                           ["Begin", "Middle", "End"],
    #                           "% DM at Postion",
    #                           label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                           color_1=data.spotify_color, color_2=data.ted_color,
    #                           color_3=data.ny_color, color_4=data.gig_color)
    #
    # hp.show_dataframe("% of DM in a Position in a Document",
    #                   ['Begin', 'Middle', 'End'],
    #                   dm_pos_doc_perc[0], data2=dm_pos_doc_perc[1], data3=dm_pos_doc_perc[2], data4=dm_pos_doc_perc[3],
    #                   label1="Spotify", label2="TED",
    #                   label3="NYTimes", label4="Gigaword")
    #
    # hp.effectsize_and_significance("% of DM in a Position in a Document",
    #                                [dm_pos_doc_perc[0] + dm_pos_doc_perc[1], dm_pos_doc_perc[2] + dm_pos_doc_perc[3]],
    #                                ["Spoken", "Written"])
    #
    '''09:
    Number of DM at certain positions in a Document
    '''
    # dm_pos_doc_total = [data.spotify.get_total_dm_positions_document(),
    #                     data.ted.get_total_dm_positions_document(),
    #                     data.ny.get_total_dm_positions_document(),
    #                     data.gig.get_total_dm_positions_document()]
    #
    # cp.plot_vertical_barchart("Number of DM at a certain Position in a Document",
    #                           dm_pos_doc_total,
    #                           ["Begin", "Middle", "End"],
    #                           "# DM at Postion",
    #                           label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                           color_1=data.spotify_color, color_2=data.ted_color,
    #                           color_3=data.ny_color, color_4=data.gig_color)
    #
    # hp.show_dataframe("Number of DM at a certain Position in a Document",
    #                   ['Begin', 'Middle', 'End'],
    #                   dm_pos_doc_total[0], data2=dm_pos_doc_total[1], data3=dm_pos_doc_total[2],
    #                   data4=dm_pos_doc_total[3],
    #                   label1="Spotify", label2="TED",
    #                   label3="NYTimes", label4="Gigaword")
    #
    # hp.effectsize_and_significance("Number of DM at a certain Position in a Document",
    #                                [dm_pos_doc_total[0] + dm_pos_doc_total[1],
    #                                 dm_pos_doc_total[2] + dm_pos_doc_total[3]],
    #                                ["Spoken", "Written"])
    #
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
    --- Number of Occurences per Discourse Marker per Dataset ---
    '''

    '''
    01_a: Most Common Markers - Average per Doc
    '''
    # most_common_markers = [data.spotify.get_most_common_markers(15, average='Doc'),
    #                        data.ted.get_most_common_markers(15, average='Doc'),
    #                        data.ny.get_most_common_markers(15, average='Doc'),
    #                        data.gig.get_most_common_markers(15, average='Doc')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Most Common Markers - Average per Document",
    #                                                        most_common_markers,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Document",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=data.spotify_color, color_2=data.ted_color,
    #                             color_3=data.ny_color, color_4=data.gig_color)
    #
    # hp.compute_marker_deltas("Differences between Marker Averages",
    #                          [most_common_markers[0] + most_common_markers[1],
    #                           most_common_markers[2] + most_common_markers[3]],
    #                          ["Spoken", "Written"])

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

    '''
    01_b: Most Common Markers - Average per Sentence
    '''
    # most_common_markers_sent = [data.spotify.get_most_common_markers(15, average='Sent'),
    #                             data.ny.get_most_common_markers(15, average='Sent'),
    #                             data.gig.get_most_common_markers(15, average='Sent')]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Most Common Markers - Average per Sentence",
    #                                                        most_common_markers_sent,
    #                                                        ["Spotify", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers", markers, x_values, "Average Occurrences per Sentence",
    #                             "Spotify", label_2="NYTimes", label_3="Gigaword",
    #                             color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)
    #
    # hp.compute_marker_deltas("Differences between Marker Averages",
    #                          [most_common_markers_sent[0],
    #                           most_common_markers_sent[1] + most_common_markers_sent[2]],
    #                          ["Spotify", "Written"])
    #
    '''
    02: Most Common Markers - In Percent
    '''
    most_common_markers_perc = [data.spotify.get_most_common_markers(15, perc=True),
                                data.ted.get_most_common_markers(15, perc=True),
                                data.ny.get_most_common_markers(15, perc=True),
                                data.gig.get_most_common_markers(15, perc=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers in %",
                                                           most_common_markers_perc,
                                                           ["Spotify", "TED", "NYTimes", "Gigaword"])

    cp.plot_horizontal_barchart("Most Common Markers in %", markers, x_values, "Share in all Markers",
                                "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                                color_1=data.spotify_color, color_2=data.ted_color,
                                color_3=data.ny_color, color_4=data.gig_color)

    hp.compute_marker_deltas("Differences between Marker Averages",
                             [most_common_markers_perc[0] + most_common_markers_perc[1],
                              most_common_markers_perc[2] + most_common_markers_perc[3]],
                             ["Spoken", "Written"])

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
    '''
    03_a: Most Common Markers - Sentence Begin
    '''
    mc_sent_begin = [data.spotify.get_most_common_markers(15, position="sb", average=True),
                     data.ny.get_most_common_markers(15, position="sb", average=True),
                     data.gig.get_most_common_markers(15, position="sb", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Sentence Begin",
                                                           mc_sent_begin,
                                                           ["Spotify", "NYTimes", "Gigaword"])

    cp.plot_horizontal_barchart("Most Common Markers: Sentence Begin", markers, x_values,
                                "Average per Document",
                                "Spotify", label_2="NYTimes", label_3="Gigaword",
                                color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)

    hp.compute_marker_deltas("Differences between Marker Averages : Sentence Begin",
                             [mc_sent_begin[0],
                              mc_sent_begin[1] + mc_sent_begin[2]],
                             ["Spotify", "Written"])

    # # mp.most_common_markers_plot("Most Common Markers: Sentence Begin", "Share in all Markers at Sent. Begin",
    # #                             mc_sent_begin[0],
    # #                             "Spotify", data.spotify_color,
    # #                             data2=mc_sent_begin[1],
    # #                             label2="NYTimes", color2=data.ny_color,
    # #                             data3=mc_sent_begin[2],
    # #                             label3="Gigaword", color3=data.gig_color, share=True)

    '''
    03_b: Most Common Markers - Sentence Middle
    '''
    # mc_sent_middle = [data.spotify.get_most_common_markers(15, position="sm", average=True),
    #                   data.ny.get_most_common_markers(15, position="sm", average=True),
    #                   data.gig.get_most_common_markers(15, position="sm", average=True)]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Sentence Middle",
    #                                                        mc_sent_middle,
    #                                                        ["Spotify", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence Middle", markers, x_values,
    #                             "Average per Document",
    #                             "Spotify", label_2="NYTimes", label_3="Gigaword",
    #                             color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)
    #
    # hp.compute_marker_deltas("Differences between Marker Averages : Sentence Middle",
    #                          [mc_sent_middle[0],
    #                           mc_sent_middle[1] + mc_sent_middle[2]],
    #                          ["Spotify", "Written"])
    #
    # # mp.most_common_markers_plot("Most Common Markers: Sentence Middle", "Share in all Markers at Sent. Middle",
    # #                             mc_sent_middle[0],
    # #                             "Spotify", data.spotify_color,
    # #                             data2=mc_sent_middle[1],
    # #                             label2="NYTimes", color2=data.ny_color,
    # #                             data3=mc_sent_middle[2],
    # #                             label3="Gigaword", color3=data.gig_color, share=True)
    '''
    03_c: Most Common Markers - Sentence End
    '''
    # mc_sent_end = [data.spotify.get_most_common_markers(15, position="se", average=True),
    #                data.ny.get_most_common_markers(15, position="se", average=True),
    #                data.gig.get_most_common_markers(15, position="se", average=True)]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Sentence End",
    #                                                        mc_sent_end,
    #                                                        ["Spotify", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Sentence End", markers, x_values,
    #                             "Average per Document",
    #                             "Spotify", label_2="NYTimes", label_3="Gigaword",
    #                             color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)
    #
    # hp.compute_marker_deltas("Differences between Marker Averages : Sentence End",
    #                          [mc_sent_end[0],
    #                           mc_sent_end[1] + mc_sent_end[2]],
    #                          ["Spotify", "Written"])
    #
    # # mp.most_common_markers_plot("Most Common Markers: Sentence End", "Share in all Markers at Sent. End",
    # #                             data.spotify.get_most_common_markers(15, position="se", perc=True),
    # #                             "Spotify", data.spotify_color,
    # #                             data2=data.ny.get_most_common_markers(15, position="se", perc=True),
    # #                             label2="NYTimes", color2=data.ny_color,
    # #                             data3=data.gig.get_most_common_markers(15, position="se", perc=True),
    # #                             label3="Gigaword", color3=data.gig_color, share=True)
    #
    '''
    04_a: Most Common Markers - Document Begin
    '''
    # mc_doc_begin = [data.spotify.get_most_common_markers(15, position="db", average=True),
    #                 data.ted.get_most_common_markers(15, position="db", average=True),
    #                 data.ny.get_most_common_markers(15, position="db", average=True),
    #                 data.gig.get_most_common_markers(15, position="db", average=True)]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Document Begin",
    #                                                        mc_doc_begin,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document Begin", markers, x_values,
    #                             "Average per Document",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=data.spotify_color, color_2=data.ted_color,
    #                             color_3=data.ny_color, color_4=data.gig_color)
    #
    # hp.compute_marker_deltas("Differences between Marker Averages : Document Begin",
    #                          [mc_doc_begin[0] + mc_doc_begin[1],
    #                           mc_doc_begin[2] + mc_doc_begin[3]],
    #                          ["Spoken", "Written"])
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

    '''
    04_b: Most Common Markers - Document Middle
    '''
    mc_doc_middle = [data.spotify.get_most_common_markers(15, position="dm", average=True),
                     data.ted.get_most_common_markers(15, position="dm", average=True),
                     data.ny.get_most_common_markers(15, position="dm", average=True),
                     data.gig.get_most_common_markers(15, position="dm", average=True)]

    markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Document Middle",
                                                           mc_doc_middle,
                                                           ["Spotify", "TED", "NYTimes", "Gigaword"])

    cp.plot_horizontal_barchart("Most Common Markers: Document Middle", markers, x_values,
                                "Average per Document",
                                "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                                color_1=data.spotify_color, color_2=data.ted_color,
                                color_3=data.ny_color, color_4=data.gig_color)

    hp.compute_marker_deltas("Differences between Marker Averages : Document Middle",
                             [mc_doc_middle[0] + mc_doc_middle[1],
                              mc_doc_middle[2] + mc_doc_middle[3]],
                             ["Spoken", "Written"])
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
    '''
    # 04_c: Most Common Markers - Document End
    # '''
    # mc_doc_end = [data.spotify.get_most_common_markers(15, position="de", average=True),
    #               data.ted.get_most_common_markers(15, position="de", average=True),
    #               data.ny.get_most_common_markers(15, position="de", average=True),
    #               data.gig.get_most_common_markers(15, position="de", average=True)]
    #
    # markers, x_values = hp.compile_most_common_marker_list("Most Common Markers Document End",
    #                                                        mc_doc_end,
    #                                                        ["Spotify", "TED", "NYTimes", "Gigaword"])
    #
    # cp.plot_horizontal_barchart("Most Common Markers: Document End", markers, x_values,
    #                             "Average per Document",
    #                             "Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                             color_1=data.spotify_color, color_2=data.ted_color,
    #                             color_3=data.ny_color, color_4=data.gig_color)
    #
    # hp.compute_marker_deltas("Differences between Marker Averages : Document End",
    #                          [mc_doc_end[0] + mc_doc_end[1],
    #                           mc_doc_end[2] + mc_doc_end[3]],
    #                          ["Spoken", "Written"])
    #
    # # mp.most_common_markers_plot("Most Common Markers: Document End", "Share in all Markers at Doc. End",
    # #                             data.spotify.get_most_common_markers(15, position="de", perc=True),
    # #                             "Spotify", data.spotify_color,
    # #                             data2=data.ted.get_most_common_markers(15, position="de", perc=True),
    # #                             label2="TED", color2=data.ted_color,
    # #                             data3=data.ny.get_most_common_markers(15, position="de", perc=True),
    # #                             label3="NYTimes", color3=data.ny_color,
    # #                             data4=data.gig.get_most_common_markers(15, position="de", perc=True),
    # #                             label4="Gigaword", color4=data.gig_color, share=True)
    #
    # # '''
    # # One Plot for each Marker, containing their total number, a_mean, h_mean, mediean and mode in each dataset
    # # '''
    # # markerlist, y_values = mp.prepare_marker_subplots(data.spotify, data.ted, data.ny, data.gig)
    # # mp.plot_marker_subplots("Number of Occurrences per Marker",
    # #                         markerlist, y_values, ["a_m.", "h_m.", "med.", "mode"],
    # #                         "Spotify", "TED", "NYTimes", "Gigaword",
    # #                         color1=data.spotify_color, color2=data.ted_color,
    # #                         color3=data.ny_color, color4=data.gig_color)


if __name__ == '__main__':
    main()
