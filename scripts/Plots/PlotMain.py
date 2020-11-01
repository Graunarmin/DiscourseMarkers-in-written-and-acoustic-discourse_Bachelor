import CreatePlots as cp
import MarkerPlots as mp
import DatasetScores as ds


# -------- Read in data ----------
class CorpusData:
    def __init__(self,
                 spotify_scores, spotify_dict,
                 ted_scores, ted_dict,
                 ny_scores, ny_dict,
                 gig_scores, gig_dict,
                 genrelist=None, markertypes=None):
        self.spotify = ds.DatasetScores(spotify_scores, spotify_dict, genrelist=genrelist, markertypes=markertypes)
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
    data = CorpusData("../../bigData/listenability-tools/scores/spotify-scores_short.csv",
                      "../../bigData/listenability-tools/dict/spotify-dict.json",
                      "../../bigData/listenability-tools/scores/ted-scores_short.csv",
                      "../../bigData/listenability-tools/dict/ted-dict.json",
                      "../../bigData/listenability-tools/scores/nytimes-scores_short.csv",
                      "../../bigData/listenability-tools/dict/nytimes-dict.json",
                      "../../bigData/listenability-tools/scores/gigaword-scores_short.csv",
                      "../../bigData/listenability-tools/dict/gigaword-dict.json",
                      genrelist="../../data/Spotify/relevant_shows/relevant_shows.csv",
                      markertypes="../../data/listenability-tools/main-senses/words_main-sense.json")

    '''01:
    Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''
    cp.plot_vertical_barchart("Percent Discourse Markers per Text",
                              [data.spotify.get_percent_dm_count_statistics(),
                               data.ted.get_percent_dm_count_statistics(),
                               data.ny.get_percent_dm_count_statistics(),
                               data.gig.get_percent_dm_count_statistics()],
                              ["Min", "A_Mean", "H_Mean", "Median", "Mode", "Max"],
                              "Percent Markers",
                              label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                              color_1=data.spotify_color, color_2=data.ted_color,
                              color_3=data.ny_color, color_4=data.gig_color
                              )

    '''02:
    Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_count_doc)
    '''
    cp.plot_vertical_barchart("Number Discourse Markers per Text",
                              [data.spotify.get_total_dm_count_statistics(),
                               data.ted.get_total_dm_count_statistics(),
                               data.ny.get_total_dm_count_statistics(),
                               data.ny.get_total_dm_count_statistics()],
                              ["Min", "A_Mean", "H_Mean", "Median", "Mode", "Max"],
                              "Number Markers",
                              label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                              color_1=data.spotify_color, color_2=data.ted_color,
                              color_3=data.ny_color, color_4=data.gig_color
                              )

    '''03:
    Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    min/mean/max(dm_sentences_perc)
    '''
    cp.plot_vertical_barchart("Percent of Sentences with DM per Text",
                              [data.spotify.get_percent_dm_sentences_statistics(),
                               data.ny.get_percent_dm_sentences_statistics(),
                               data.gig.get_percent_dm_sentences_statistics()],
                              ["Min", "A_Mean", "H_Mean", "Median", "Mode", "Max"],
                              "% Sentences containing DM",
                              label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                              color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)

    '''04:
    Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    min/mean/max(dm_sentences)
    '''
    cp.plot_vertical_barchart("Number of Sentences with DM per Text",
                              [data.spotify.get_total_dm_sentences_statistics(),
                               data.ny.get_total_dm_sentences_statistics(),
                               data.gig.get_total_dm_sentences_statistics()],
                              ["Min", "A_Mean", "H_Mean", "Median", "Mode", "Max"],
                              "# Sentences containing DM",
                              label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                              color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)

    # '''05:
    # Number of DM per sentence
    # '''
    # cp.plot_vertical_barchart("Number of Discourse Markers per Sentence",
    #                           [data.spotify.get_total_dm_per_sentence_statistics(),
    #                            data.ny.get_total_dm_per_sentence_statistics(),
    #                            data.gig.get_total_dm_per_sentence_statistics()],
    #                           ["Min", "A_Mean", "H_Mean", "Median", "Mode", "Max"],
    #                           "# Markers per Sentence",
    #                           label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                           color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)
    #
    # '''06:
    # Histogram with Number of DM per Sentence per Dataset
    # '''
    # cp.draw_simple_barchart("Number of Discourse Markers per Sentence",
    #                         ["Spotify", "NYTimes", "Gigaword"],
    #                         [data.spotify.compute_dm_per_sentence(),
    #                          data.ny.compute_dm_per_sentence(),
    #                          data.gig.compute_dm_per_sentence()],
    #                         [data.spotify_color, data.ny_color, data.gig_color])
    #
    '''07:
    Percentage of DM at certain positions in a sentence
    '''
    cp.plot_vertical_barchart("% of DM in a Position in a Sentence",
                              [data.spotify.get_percent_dm_positions_sentence(),
                               data.ny.get_percent_dm_positions_sentence(),
                               data.gig.get_percent_dm_positions_sentence()],
                              ["begin", "middle", "end"],
                              "% DM at Postion",
                              label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                              color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)

    '''08:
    Number of DM at certain positions in a sentence
    '''
    cp.plot_vertical_barchart("Number of DM at a certain Position in a Sentence",
                              [data.spotify.get_total_dm_positions_sentence(),
                               data.ny.get_total_dm_positions_sentence(),
                               data.gig.get_total_dm_positions_sentence()],
                              ["begin", "middle", "end"],
                              "# DM at Postion",
                              label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
                              color_1=data.spotify_color, color_2=data.ny_color, color_3=data.gig_color)
    #
    # '''09:
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
    Document Positions
    '''
    cp.plot_vertical_barchart("% of DM in a Position in a Document",
                              [data.spotify.get_percent_dm_positions_document(),
                               data.ted.get_percent_dm_positions_document(),
                               data.ny.get_percent_dm_positions_document(),
                               data.gig.get_percent_dm_positions_document()],
                              ["begin", "middle", "end"],
                              "% DM at Postion",
                              label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                              color_1=data.spotify_color, color_2=data.ted_color,
                              color_3=data.ny_color, color_4=data.gig_color)

    cp.plot_vertical_barchart("Number of DM at a certain Position in a Document",
                              [data.spotify.get_total_dm_positions_document(),
                               data.ted.get_total_dm_positions_document(),
                               data.ny.get_total_dm_positions_document(),
                               data.gig.get_total_dm_positions_document()],
                              ["begin", "middle", "end"],
                              "# DM at Postion",
                              label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
                              color_1=data.spotify_color, color_2=data.ted_color,
                              color_3=data.ny_color, color_4=data.gig_color)
    #
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

    '''10:
    Number of Occurences per Discourse Marker per Dataset
    '''

    mp.most_common_markers_plot("Most Common Markers per Dataset", "Number of Occurences",
                                data.spotify.get_most_common_markers(15),
                                "Spotify", data.spotify_color,
                                data2=data.ted.get_most_common_markers(15),
                                label2="TED", color2=data.ted_color,
                                data3=data.ny.get_most_common_markers(15),
                                label3="NYTimes", color3=data.ny_color,
                                data4=data.gig.get_most_common_markers(15),
                                label4="Gigaword", color4=data.gig_color)

    mp.most_common_markers_plot("Most Common Markers per Dataset in %", "Share in all Markers",
                                data.spotify.get_most_common_markers(15, perc=True),
                                "Spotify", data.spotify_color,
                                data2=data.ted.get_most_common_markers(15, perc=True),
                                label2="TED", color2=data.ted_color,
                                data3=data.ny.get_most_common_markers(15, perc=True),
                                label3="NYTimes",
                                color3=data.ny_color,
                                data4=data.gig.get_most_common_markers(15, perc=True),
                                label4="Gigaword",
                                color4=data.gig_color, share=True)

    mp.most_common_markers_plot("Most Common Markers: Sentence Begin", "Share in all Markers at Sent. Begin",
                                data.spotify.get_most_common_markers(15, position="sb", perc=True),
                                "Spotify", data.spotify_color,
                                data2=data.ny.get_most_common_markers(15, position="sb", perc=True),
                                label2="NYTimes", color2=data.ny_color,
                                data3=data.gig.get_most_common_markers(15, position="sb", perc=True),
                                label3="Gigaword", color3=data.gig_color, share=True)

    mp.most_common_markers_plot("Most Common Markers: Sentence Middle", "Share in all Markers at Sent. Middle",
                                data.spotify.get_most_common_markers(15, position="sm", perc=True),
                                "Spotify", data.spotify_color,
                                data2=data.ny.get_most_common_markers(15, position="sm", perc=True),
                                label2="NYTimes", color2=data.ny_color,
                                data3=data.gig.get_most_common_markers(15, position="sm", perc=True),
                                label3="Gigaword", color3=data.gig_color, share=True)

    mp.most_common_markers_plot("Most Common Markers: Sentence End", "Share in all Markers at Sent. End",
                                data.spotify.get_most_common_markers(15, position="se", perc=True),
                                "Spotify", data.spotify_color,
                                data2=data.ny.get_most_common_markers(15, position="se", perc=True),
                                label2="NYTimes", color2=data.ny_color,
                                data3=data.gig.get_most_common_markers(15, position="se", perc=True),
                                label3="Gigaword", color3=data.gig_color, share=True)

    mp.most_common_markers_plot("Most Common Markers: Document Begin", "Share in all Markers at Doc. Begin",
                                data.spotify.get_most_common_markers(15, position="db", perc=True),
                                "Spotify", data.spotify_color,
                                data2=data.ted.get_most_common_markers(15, position="db", perc=True),
                                label2="TED", color2=data.ted_color,
                                data3=data.ny.get_most_common_markers(15, position="db", perc=True),
                                label3="NYTimes", color3=data.ny_color,
                                data4=data.gig.get_most_common_markers(15, position="db", perc=True),
                                label4="Gigaword", color4=data.gig_color, share=True)

    mp.most_common_markers_plot("Most Common Markers: Document Middle", "Share in all Markers at Doc. Middle",
                                data.spotify.get_most_common_markers(15, position="dm", perc=True),
                                "Spotify", data.spotify_color,
                                data2=data.ted.get_most_common_markers(15, position="dm", perc=True),
                                label2="TED", color2=data.ted_color,
                                data3=data.ny.get_most_common_markers(15, position="dm", perc=True),
                                label3="NYTimes", color3=data.ny_color,
                                data4=data.gig.get_most_common_markers(15, position="dm", perc=True),
                                label4="Gigaword", color4=data.gig_color, share=True)

    mp.most_common_markers_plot("Most Common Markers: Document End", "Share in all Markers at Doc. End",
                                data.spotify.get_most_common_markers(15, position="de", perc=True),
                                "Spotify", data.spotify_color,
                                data2=data.ted.get_most_common_markers(15, position="de", perc=True),
                                label2="TED", color2=data.ted_color,
                                data3=data.ny.get_most_common_markers(15, position="de", perc=True),
                                label3="NYTimes", color3=data.ny_color,
                                data4=data.gig.get_most_common_markers(15, position="de", perc=True),
                                label4="Gigaword", color4=data.gig_color, share=True)

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
