import helpers.DataFrames
import helpers.Statistics
from datasets import DiscourseTypeData as cd
from classes import MarkerTypes as mt
from plotting import MarkerTypePlots as mtp
from helpers import Helpers as hp


def main():
    markertypes = mt.MarkerTypes(
        "../../data/listenability-tools/main-senses/words_main-sense.json")

    data = cd.DiscourseTypeData(
        "../../bigData/listenability-tools/discourse-types/dict/spotify-dict.json",
        "../../bigData/listenability-tools/discourse-types/dict/ted-dict.json",
        "../../bigData/listenability-tools/discourse-types/dict/nytimes-dict.json",
        "../../bigData/listenability-tools/discourse-types/dict/gigaword-dict.json",
        spotify_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/marker-scores/spotify-marker.csv",
        ted_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/marker-scores/ted-marker.csv",
        ny_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/marker-scores/nytimes-marker.csv",
        gig_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/marker-scores/gigaword-marker.csv",
        general=False,
        markertypes=markertypes)

    # '''
    # T-Test for total values per Document
    # '''
    # spotify = data.spotify.get_markerclass_columns()
    # ted = data.ted.get_markerclass_columns()
    # ny = data.ny.get_markerclass_columns()
    # gig = data.gig.get_markerclass_columns()
    #
    # helpers.Statistics.effectsize_and_significance("temporal-per-document_statistics_discourse-types_dt",
    #                                                [spotify['temporal'], ted['temporal'],
    #                                 ny['temporal'], gig['temporal']],
    #                                                [data.spotify_label, data.ted_label,
    #                                 data.ny_label, data.gig_label])
    #
    # helpers.Statistics.effectsize_and_significance("contingency-per-document_statistics_discourse-types_dt",
    #                                                [spotify['contingency'], ted['contingency'],
    #                                 ny['contingency'], gig['contingency']],
    #                                                [data.spotify_label, data.ted_label,
    #                                 data.ny_label, data.gig_label])
    #
    # helpers.Statistics.effectsize_and_significance("comparison-per-document_statistics_discourse-types_dt",
    #                                                [spotify['comparison'], ted['comparison'],
    #                                 ny['comparison'], gig['comparison']],
    #                                                [data.spotify_label, data.ted_label,
    #                                 data.ny_label, data.gig_label])
    #
    # helpers.Statistics.effectsize_and_significance("expansion-per-document_statistics_discourse-types_dt",
    #                                                [spotify['expansion'], ted['expansion'],
    #                                 ny['expansion'], gig['expansion']],
    #                                                [data.spotify_label, data.ted_label,
    #                                 data.ny_label, data.gig_label])
    #
    # '''
    # 01: Total Occurence per Markertype
    # '''
    # total_docs = (data.spotify.get_total_docs() + data.ted.get_total_docs() +
    #               data.ny.get_total_docs() + data.gig.get_total_docs())
    #
    # markertype_total = [(data.spotify.get_total_for_markerclass('Temporal') +
    #                      data.ted.get_total_for_markerclass('Temporal') +
    #                      data.ny.get_total_for_markerclass('Temporal') +
    #                      data.gig.get_total_for_markerclass('Temporal')) / total_docs,
    #                     (data.spotify.get_total_for_markerclass('Contingency') +
    #                      data.ted.get_total_for_markerclass('Contingency') +
    #                      data.ny.get_total_for_markerclass('Contingency') +
    #                      data.gig.get_total_for_markerclass('Contingency')) / total_docs,
    #                     (data.spotify.get_total_for_markerclass('Comparison') +
    #                      data.ted.get_total_for_markerclass('Comparison') +
    #                      data.ny.get_total_for_markerclass('Comparison') +
    #                      data.gig.get_total_for_markerclass('Comparison')) / total_docs,
    #                     (data.spotify.get_total_for_markerclass('Expansion') +
    #                      data.ted.get_total_for_markerclass('Expansion') +
    #                      data.ny.get_total_for_markerclass('Expansion') +
    #                      data.gig.get_total_for_markerclass('Expansion')) / total_docs,
    #                     ]
    #
    # mtp.draw_barchart(markertype_total, "Average Occurrences of Markertypes per Text in all Data",
    #                   ["Temporal", "Contingency", "Comparison", "Expansion"],
    #                   [markertypes.temporal_color, markertypes.contingency_color,
    #                    markertypes.comparison_color, markertypes.expansion_color],
    #                   "Average Occurrences per Text")
    #
    # helpers.DataFrames.markertype_dataframe("01_mt-average-all-data_dt",
    #                                         ["Temporal", "Contingency", "Comparison", "Expansion"],
    #                                         markertype_total,
    #                                         ["Discourse Type Data"])
    #
    # '''
    # 02: Durchschnittliches Vorkommen jedes Markertypes pro Text
    # '''
    # markertype_per_text_average_text = [[data.spotify.get_average_for_markerclass('Temporal', average='doc'),
    #                                      data.ted.get_average_for_markerclass('Temporal', average='doc'),
    #                                      data.ny.get_average_for_markerclass('Temporal', average='doc'),
    #                                      data.gig.get_average_for_markerclass('Temporal', average='doc')],
    #                                     [data.spotify.get_average_for_markerclass('Contingency', average='doc'),
    #                                      data.ted.get_average_for_markerclass('Contingency', average='doc'),
    #                                      data.ny.get_average_for_markerclass('Contingency', average='doc'),
    #                                      data.gig.get_average_for_markerclass('Contingency', average='doc')],
    #                                     [data.spotify.get_average_for_markerclass('Comparison', average='doc'),
    #                                      data.ted.get_average_for_markerclass('Comparison', average='doc'),
    #                                      data.ny.get_average_for_markerclass('Comparison', average='doc'),
    #                                      data.gig.get_average_for_markerclass('Comparison', average='doc')],
    #                                     [data.spotify.get_average_for_markerclass('Expansion', average='doc'),
    #                                      data.ted.get_average_for_markerclass('Expansion', average='doc'),
    #                                      data.ny.get_average_for_markerclass('Expansion', average='doc'),
    #                                      data.gig.get_average_for_markerclass('Expansion', average='doc')],
    #                                     ]
    #
    # mtp.draw_barchart_subplots("Average Occurence of Markertypes per Text",
    #                            ["Temporal", "Contingency", "Comparison", "Expansion"],
    #                            [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
    #                            markertype_per_text_average_text,
    #                            [data.spotify_color, data.ted_color, data.ny_color, data.gig_color])
    #
    # helpers.DataFrames.markertype_dataframe("02_markertypes_average-per-text_dt",
    #                                         ["Temporal", "Contingency", "Comparison", "Expansion"],
    #                                         markertype_per_text_average_text,
    #                                         [data.spotify_label, data.ted_label, data.ny_label, data.gig_label])
    #
    # '''
    # 03: Vorkommen jedes Markertypes pro Datensatz in %
    # '''
    # markertype_per_text_perc = [[data.spotify.get_percentage_for_markerclass('Temporal'),
    #                              data.ted.get_percentage_for_markerclass('Temporal'),
    #                              data.ny.get_percentage_for_markerclass('Temporal'),
    #                              data.gig.get_percentage_for_markerclass('Temporal')],
    #                             [data.spotify.get_percentage_for_markerclass('Contingency'),
    #                              data.ted.get_percentage_for_markerclass('Contingency'),
    #                              data.ny.get_percentage_for_markerclass('Contingency'),
    #                              data.gig.get_percentage_for_markerclass('Contingency')],
    #                             [data.spotify.get_percentage_for_markerclass('Comparison'),
    #                              data.ted.get_percentage_for_markerclass('Comparison'),
    #                              data.ny.get_percentage_for_markerclass('Comparison'),
    #                              data.gig.get_percentage_for_markerclass('Comparison')],
    #                             [data.spotify.get_percentage_for_markerclass('Expansion'),
    #                              data.ted.get_percentage_for_markerclass('Expansion'),
    #                              data.ny.get_percentage_for_markerclass('Expansion'),
    #                              data.gig.get_percentage_for_markerclass('Expansion')],
    #                             ]
    #
    # mtp.draw_barchart_subplots("Share of Markertypes in Wordcount (%)",
    #                            ["Temporal", "Contingency", "Comparison", "Expansion"],
    #                            [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
    #                            markertype_per_text_perc,
    #                            [data.spotify_color, data.ted_color, data.ny_color, data.gig_color])
    #
    # helpers.DataFrames.markertype_dataframe("03_markertypes_percentage_dt",
    #                                         ["Temporal", "Contingency", "Comparison", "Expansion"],
    #                                         markertype_per_text_perc,
    #                                         [data.spotify_label, data.ted_label, data.ny_label, data.gig_label])
    #
    # '''
    # 04: Vorkommen jedes Markertypes pro Datensatz in %
    # '''
    # markertype_per_text_perc_m = [[data.spotify.get_percentage_for_markerclass('Temporal', perc='marker'),
    #                                data.ted.get_percentage_for_markerclass('Temporal', perc='marker'),
    #                                data.ny.get_percentage_for_markerclass('Temporal', perc='marker'),
    #                                data.gig.get_percentage_for_markerclass('Temporal', perc='marker')],
    #                               [data.spotify.get_percentage_for_markerclass('Contingency', perc='marker'),
    #                                data.ted.get_percentage_for_markerclass('Contingency', perc='marker'),
    #                                data.ny.get_percentage_for_markerclass('Contingency', perc='marker'),
    #                                data.gig.get_percentage_for_markerclass('Contingency', perc='marker')],
    #                               [data.spotify.get_percentage_for_markerclass('Comparison', perc='marker'),
    #                                data.ted.get_percentage_for_markerclass('Comparison', perc='marker'),
    #                                data.ny.get_percentage_for_markerclass('Comparison', perc='marker'),
    #                                data.gig.get_percentage_for_markerclass('Comparison', perc='marker')],
    #                               [data.spotify.get_percentage_for_markerclass('Expansion', perc='marker'),
    #                                data.ted.get_percentage_for_markerclass('Expansion', perc='marker'),
    #                                data.ny.get_percentage_for_markerclass('Expansion', perc='marker'),
    #                                data.gig.get_percentage_for_markerclass('Expansion', perc='marker')],
    #                               ]
    #
    # mtp.draw_barchart_subplots("Share of Markertypes in all Markers of a Texttype (%)",
    #                            ["Temporal", "Contingency", "Comparison", "Expansion"],
    #                            [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
    #                            markertype_per_text_perc_m,
    #                            [data.spotify_color, data.ted_color, data.ny_color, data.gig_color])
    #
    # helpers.DataFrames.markertype_dataframe("04_markertypes_percentage-marker_dt",
    #                                         ["Temporal", "Contingency", "Comparison", "Expansion"],
    #                                         markertype_per_text_perc_m,
    #                                         [data.spotify_label, data.ted_label, data.ny_label, data.gig_label])
    #
    # '''
    # 05: Vorkommen jedes Markertypes pro Datensatz in %
    # '''
    # markertype_per_text_perc_m = [[data.spotify.get_percentage_for_markerclass('Temporal', perc='marker'),
    #                                data.spotify.get_percentage_for_markerclass('Contingency', perc='marker'),
    #                                data.spotify.get_percentage_for_markerclass('Comparison', perc='marker'),
    #                                data.spotify.get_percentage_for_markerclass('Expansion', perc='marker')],
    #                               [data.ted.get_percentage_for_markerclass('Temporal', perc='marker'),
    #                                data.ted.get_percentage_for_markerclass('Contingency', perc='marker'),
    #                                data.ted.get_percentage_for_markerclass('Comparison', perc='marker'),
    #                                data.ted.get_percentage_for_markerclass('Expansion', perc='marker')],
    #                               [data.ny.get_percentage_for_markerclass('Temporal', perc='marker'),
    #                                data.ny.get_percentage_for_markerclass('Contingency', perc='marker'),
    #                                data.ny.get_percentage_for_markerclass('Comparison', perc='marker'),
    #                                data.ny.get_percentage_for_markerclass('Expansion', perc='marker')],
    #                               [data.gig.get_percentage_for_markerclass('Temporal', perc='marker'),
    #                                data.gig.get_percentage_for_markerclass('Contingency', perc='marker'),
    #                                data.gig.get_percentage_for_markerclass('Comparison', perc='marker'),
    #                                data.gig.get_percentage_for_markerclass('Expansion', perc='marker')],
    #                               ]
    #
    # mtp.draw_barchart_subplots("Share of Markertypes in all Markers of a Texttype (%)",
    #                            [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
    #                            ["Temporal", "Contingency", "Comparison", "Expansion"],
    #                            markertype_per_text_perc_m,
    #                            [markertypes.temporal_color, markertypes.contingency_color,
    #                             markertypes.comparison_color, markertypes.expansion_color])
    #
    # helpers.DataFrames.markertype_dataframe("05_markertypes_percentage-marker_dt",
    #                                         [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
    #                                         markertype_per_text_perc_m,
    #                                         ["Temporal", "Contingency", "Comparison", "Expansion"])

    ''' ---------- MARKER LEVEL -----------'''

    """
    Top 15 Markers per Class per Texttype
    """
    '''Temporal'''
    temporal = [data.spotify.get_most_common_markers(marker_type="Temporal"),
                data.ted.get_most_common_markers(marker_type="Temporal"),
                data.ny.get_most_common_markers(marker_type="Temporal"),
                data.gig.get_most_common_markers(marker_type="Temporal")]

    mc_temporal, values_temporal = hp.most_common_markers_list("01_mc-temp_dt",
                                                               temporal,
                                                               [data.spotify_label, data.ted_label,
                                                                data.ny_label, data.gig_label])

    mtp.horizontal_barchart("Most common Temporal Markers - Share in all Temporal Markers in %",
                            values_temporal, mc_temporal,
                            [data.spotify_color, data.ted_color, data.ny_color, data.gig_color],
                            [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
                            "Share in all Temporal Markers")



    '''Contingency'''
    contingency = [data.spotify.get_most_common_markers(marker_type="Contingency"),
                   data.ted.get_most_common_markers(marker_type="Contingency"),
                   data.ny.get_most_common_markers(marker_type="Contingency"),
                   data.gig.get_most_common_markers(marker_type="Contingency")]

    mc_contingency, values_contingency = hp.most_common_markers_list("02_mc-contingency_dt",
                                                                     contingency,
                                                                     [data.spotify_label, data.ted_label,
                                                                      data.ny_label, data.gig_label])

    mtp.horizontal_barchart("Most common Contingency Markers - Share in all Contingency Markers in %",
                            values_contingency, mc_contingency,
                            [data.spotify_color, data.ted_color, data.ny_color, data.gig_color],
                            [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
                            "Share in all Contingency Markers")

    '''Comparison'''
    comparison = [data.spotify.get_most_common_markers(marker_type="Comparison"),
                  data.ted.get_most_common_markers(marker_type="Comparison"),
                  data.ny.get_most_common_markers(marker_type="Comparison"),
                  data.gig.get_most_common_markers(marker_type="Comparison")]

    mc_comparison, values_comparison = hp.most_common_markers_list("03_mc-comparison_dt",
                                                                   comparison,
                                                                   [data.spotify_label, data.ted_label,
                                                                    data.ny_label, data.gig_label])

    mtp.horizontal_barchart("Most common Comparison Markers - Share in all Comparison Markers in %",
                            values_comparison, mc_comparison,
                            [data.spotify_color, data.ted_color, data.ny_color, data.gig_color],
                            [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
                            "Share in all Comparison Markers")

    '''Expansion'''
    expansion = [data.spotify.get_most_common_markers(marker_type="Expansion"),
                 data.ted.get_most_common_markers(marker_type="Expansion"),
                 data.ny.get_most_common_markers(marker_type="Expansion"),
                 data.gig.get_most_common_markers(marker_type="Expansion")]

    mc_expansion, values_expansion = hp.most_common_markers_list("04_mc-expansion_dt",
                                                                 expansion,
                                                                 [data.spotify_label, data.ted_label,
                                                                  data.ny_label, data.gig_label])

    mtp.horizontal_barchart("Most common Expansion Markers - Share in all Expansion Markers in %",
                            values_expansion, mc_expansion,
                            [data.spotify_color, data.ted_color, data.ny_color, data.gig_color],
                            [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
                            "Share in all Expansion Markers")


if __name__ == '__main__':
    main()
