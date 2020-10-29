import CreatePlots as cp
import MarkerPlots as mp
import DatasetScores as ds


# -------- Read in data ----------
class CorpusData:
    def __init__(self, spotify_scores, spotify_dict, ted_scores, ted_dict,
                 ny_scores, ny_dict, gig_scores, gig_dict):
        self.spotify = ds.DatasetScores(spotify_scores, spotify_dict)
        self.ted = ds.DatasetScores(ted_scores, ted_dict)
        self.ny = ds.DatasetScores(ny_scores, ny_dict)
        self.gig = ds.DatasetScores(gig_scores, gig_dict)


def main():
    data = CorpusData("../../bigData/listenability-tools/scores/spotify-scores_short.csv",
                      "../../bigData/listenability-tools/dict/spotify-dict.json",
                      "../../bigData/listenability-tools/scores/ted-scores_short.csv",
                      "../../bigData/listenability-tools/dict/ted-dict.json",
                      "../../bigData/listenability-tools/scores/example-scores_short.csv",
                      "../../bigData/listenability-tools/dict/nytimes-dict.json",
                      "../../bigData/listenability-tools/scores/example-scores_short.csv",
                      "../../bigData/listenability-tools/dict/gigaword-dict.json")

    # Colors:   [base, darker, lighter]
    # greens:   ['#1DB954', '#0e5c2a', '#8edca9']
    # red:      ['#e62b1e', '#73150f', '#f2958e']
    # oranges:  ['#FFA700', '#7f5300', '#ffd37f']
    # blues:    ['#227DFB', '#113e7d', '#90befd']

    '''01:
    Prozentualer Anteil der DM an den Texten, über alle Texte
    min/mean/max(dm_words_perc)
    '''
    # cp.plot_vertical_barchart("Percent Discourse Markers per Text",
    #                           [data.spotify.get_percent_dm_count_statistics(),
    #                            data.ted.get_percent_dm_count_statistics(),
    #                            data.ny.get_percent_dm_count_statistics(),
    #                            data.gig.get_percent_dm_count_statistics()],
    #                           ["Min", "A_Mean", "H_Mean", "Median", "Mode", "Max"],
    #                           "Percent Markers",
    #                           label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                           color_1='#1DB954', color_2='#e62b1e', color_3='#FFA700', color_4='#227DFB'
    #                           )
    #
    # '''02:
    # Anzahl der DM pro Text, über alle Texte (nicht sehr aussagekräftig)
    # min/mean/max(dm_count_doc)
    # '''
    # cp.plot_vertical_barchart("Number Discourse Markers per Text",
    #                           [data.spotify.get_total_dm_count_statistics(),
    #                            data.ted.get_total_dm_count_statistics(),
    #                            data.ny.get_total_dm_count_statistics(),
    #                            data.ny.get_total_dm_count_statistics()],
    #                           ["Min", "A_Mean", "H_Mean", "Median", "Mode", "Max"],
    #                           "Number Markers",
    #                           label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                           color_1='#1DB954', color_2='#e62b1e', color_3='#FFA700', color_4='#227DFB'
    #                           )
    #
    # '''03:
    # Prozentualer Anteil der Sätze, die DM enthalten, an den Texten, über alle Texte
    # min/mean/max(dm_sentences_perc)
    # '''
    # cp.plot_vertical_barchart("Percent of Sentences with DM per Text",
    #                           [data.spotify.get_percent_dm_sentences_statistics(),
    #                            data.ny.get_percent_dm_sentences_statistics(),
    #                            data.gig.get_percent_dm_sentences_statistics()],
    #                           ["Min", "A_Mean", "H_Mean", "Median", "Mode", "Max"],
    #                           "% Sentences containing DM",
    #                           label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                           color_1='#1DB954', color_2='#FFA700', color_3='#227DFB')
    #
    # '''04:
    # Anzahl der Sätze, die DM enthalten, über alle Texte (nicht sehr aussagekräftig)
    # min/mean/max(dm_sentences)
    # '''
    # cp.plot_vertical_barchart("Number of Sentences with DM per Text",
    #                           [data.spotify.get_total_dm_sentences_statistics(),
    #                            data.ny.get_total_dm_sentences_statistics(),
    #                            data.gig.get_total_dm_sentences_statistics()],
    #                           ["Min", "A_Mean", "H_Mean", "Median", "Mode", "Max"],
    #                           "# Sentences containing DM",
    #                           label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                           color_1='#1DB954', color_2='#FFA700', color_3='#227DFB')
    #
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
    #                           color_1='#1DB954', color_2='#FFA700', color_3='#227DFB')
    #
    # '''06:
    # Histogram with Number of DM per Sentence per Dataset
    # '''
    # cp.draw_simple_barchart("Number of Discourse Markers per Sentence",
    #                         ["Spotify", "NYTimes", "Gigaword"],
    #                         [data.spotify.compute_dm_per_sentence(),
    #                          data.ny.compute_dm_per_sentence(),
    #                          data.gig.compute_dm_per_sentence()],
    #                         ['#1DB954', '#FFA700', '#227DFB'])
    #
    # '''07:
    # Percentage of DM at certain positions in a sentence
    # '''
    # cp.plot_vertical_barchart("% of DM in a Position in a Sentence",
    #                           [data.spotify.get_percent_dm_positions_sentence(),
    #                            data.ny.get_percent_dm_positions_sentence(),
    #                            data.gig.get_percent_dm_positions_sentence()],
    #                           ["begin", "middle", "end"],
    #                           "% DM at Postion",
    #                           label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                           color_1='#1DB954', color_2='#FFA700', color_3='#227DFB')
    #
    # '''08:
    # Number of DM at certain positions in a sentence
    # '''
    # cp.plot_vertical_barchart("Number of DM at a certain Position in a Sentence",
    #                           [data.spotify.get_total_dm_positions_sentence(),
    #                            data.ny.get_total_dm_positions_sentence(),
    #                            data.gig.get_total_dm_positions_sentence()],
    #                           ["begin", "middle", "end"],
    #                           "# DM at Postion",
    #                           label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                           color_1='#1DB954', color_2='#FFA700', color_3='#227DFB')

    # '''09:
    # Piechart of DM at certain positions in a sentence per Dataset
    # '''
    # cp.plot_dm_positions_sent_piechart("Number of DM in a Sentence at Position:",
    #                                    [data.spotify.get_sentence_position_values(),
    #                                     data.ny.get_sentence_position_values(),
    #                                     data.gig.get_sentence_position_values()
    #                                     ],
    #                                    ["Spotify Data", "NYTimes Data", "Gigaword Data"],
    #                                    [['#1DB954', '#0e5c2a', '#8edca9'],
    #                                     ['#FFA700', '#7f5300', '#ffd37f'],
    #                                     ['#227DFB', '#113e7d', '#90befd']])

    # cp.plot_vertical_barchart("% of DM in a Position in a Document",
    #                           [data.spotify.get_percent_dm_positions_document(),
    #                            data.ted.get_percent_dm_positions_document(),
    #                            data.ny.get_percent_dm_positions_document(),
    #                            data.gig.get_percent_dm_positions_document()],
    #                           ["begin", "middle", "end"],
    #                           "% DM at Postion",
    #                           label_1="Spotify", label_2="NYTimes", label_3="Gigaword",
    #                           color_1='#1DB954', color_2='#FFA700', color_3='#227DFB')
    #
    # cp.plot_vertical_barchart("Number of DM at a certain Position in a Document",
    #                           [data.spotify.get_total_dm_positions_document(),
    #                            data.ted.get_total_dm_positions_document(),
    #                            data.ny.get_total_dm_positions_document(),
    #                            data.gig.get_total_dm_positions_document()],
    #                           ["begin", "middle", "end"],
    #                           "# DM at Postion",
    #                           label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                           color_1='#1DB954', color_2='#e62b1e', color_3='#FFA700', color_4='#227DFB')

    # cp.plot_dm_position_piechart("Positions of Discourse Markers in the Documents",
    #                              [data.spotify.get_document_position_values(),
    #                               data.ted.get_document_position_values(),
    #                               data.ny.get_document_position_values(),
    #                               data.gig.get_document_position_values()
    #                               ],
    #                              ["Spotify Data", "TED Data", "NYTimes Data", "Gigaword Data"],
    #                              [['#1DB954', '#0e5c2a', '#8edca9'],
    #                               ['#e62b1e', '#73150f', '#f2958e'],
    #                               ['#FFA700', '#7f5300', '#ffd37f'],
    #                               ['#227DFB', '#113e7d', '#90befd']])

    # '''10:
    # Number of Occurences per Discourse Marker per Dataset
    # '''
    # marker_occurences = compute_marker_occurences(data.spotify_marker, data.ted_marker,
    #                                               data.ny_marker, data.gig_marker)
    # plot_horizontal_barchart("Discourse Marker Occurrences",
    #                          marker_occurences[0],
    #                          [marker_occurences[1], marker_occurences[2],
    #                              marker_occurences[3], marker_occurences[4]],
    #                          "Number of Occurrences",
    #                          label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                          color_1='#1DB954', color_2='#e62b1e', color_3='#FFA700', color_4='#227DFB')
    #
    # plot_horizontal_barchart("Discourse Marker Occurrences",
    #                          marker_occurences[0],
    #                          [marker_occurences[1], marker_occurences[2],
    #                          marker_occurences[3], marker_occurences[4]],
    #                          "Number of Occurrences",
    #                          label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    #                          color_1='#1DB954', color_2='#e62b1e', color_3='#FFA700', color_4='#227DFB',
    #                          sub=True)
    # #
    # # '''11:
    # # Prozentualer Anteil jedes Markers an allen Markern pro Datensatz
    # # '''
    # #
    # # plot_horizontal_barchart("Discourse Marker Occurrences - Percent",
    # #                          marker_percents[0],
    # #                          [marker_percents[1], marker_percents[2], marker_percents[3], marker_percents[4]],
    # #                          "Percent of all markers",
    # #                          label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    # #                          color_1='#1DB954', color_2='#e62b1e', color_3='#FFA700', color_4='#227DFB')
    # #
    # # marker_percents = compute_marker_percentages(data.spotify_marker, data.ted_marker,
    # #                                              data.ny_marker, data.gig_marker)
    # #
    # # plot_horizontal_barchart("Discourse Marker Occurrences",
    # #                          marker_percents[0],
    # #                          [marker_percents[1], marker_percents[2], marker_percents[3], marker_percents[4]],
    # #                          "Number of Occurrences",
    # #                          label_1="Spotify", label_2="TED", label_3="NYTimes", label_4="Gigaword",
    # #                          color_1='#1DB954', color_2='#e62b1e', color_3='#FFA700', color_4='#227DFB',
    # #                          subplot=True)
    # '''
    # One Plot for each Marker, containing their total number, a_mean, h_mean, mediean and mode in each dataset
    # '''
    # markerlist, y_values = mp.prepare_marker_subplots(data.spotify, data.ted, data.ny, data.gig)
    # mp.plot_marker_subplots("Number of Occurrences per Marker",
    #                         markerlist, y_values, ["a_m.", "h_m.", "med.", "mode"],
    #                         "Spotify", "TED", "NYTimes", "Gigaword",
    #                         color1='#1DB954', color2='#e62b1e', color3='#FFA700', color4='#227DFB')
    #                         color1='#1DB954', color2='#e62b1e', color3='#FFA700', color4='#227DFB')


if __name__ == '__main__':
    main()
