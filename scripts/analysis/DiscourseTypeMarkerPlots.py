import helpers.DataFrames
import helpers.Statistics
from datasets import DiscourseTypeData as dtd
from classes import MarkerTypes as mt
from plotting import MarkerTypePlots as mtp
from helpers import Helpers as hp


def main():
    markertypes = mt.MarkerTypes(
        "../../data/listenability-tools/main-senses/words_main-sense.json")

    data = dtd.DiscourseTypeData(
        "../../bigData/listenability-tools/discourse-types/dict/spotify-dict.json",
        "../../bigData/listenability-tools/discourse-types/dict/acoustic-dict.json",
        "../../bigData/listenability-tools/discourse-types/dict/written-dict.json",
        spotify_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/marker-scores/spotify-marker.csv",
        acoustic_opt=
        "../../bigData/listenability-tools/discourse-types/scores/marker-scores/acoustic-marker.csv",
        written_opt=
        "../../bigData/listenability-tools/discourse-types/scores/marker-scores/written-marker.csv",
        general=False,
        markertypes=markertypes
    )

    '''
    T-Test for total values per Document
    '''
    acoustic = data.acoustic.get_markerclass_columns()
    written = data.written.get_markerclass_columns()

    helpers.Statistics.effectsize_and_significance("temporal-per-document_statistics_discourse-types_dt",
                                                   [acoustic['temporal'], written['temporal']],
                                                   [data.acoustic_label, data.written_label])

    helpers.Statistics.effectsize_and_significance("contingency-per-document_statistics_discourse-types_dt",
                                                   [acoustic['contingency'], written['contingency']],
                                                   [data.acoustic_label, data.written_label])

    helpers.Statistics.effectsize_and_significance("comparison-per-document_statistics_discourse-types_dt",
                                                   [acoustic['comparison'], written['comparison']],
                                                   [data.acoustic_label, data.written_label])

    helpers.Statistics.effectsize_and_significance("expansion-per-document_statistics_discourse-types_dt",
                                                   [acoustic['expansion'], written['expansion']],
                                                   [data.acoustic_label, data.written_label])

    '''
    01: Total Occurence per Markertype
    '''
    total_docs = (data.acoustic.get_total_docs() + data.written.get_total_docs())

    markertype_total = [(data.acoustic.get_total_for_markerclass('Temporal') +
                         data.written.get_total_for_markerclass('Temporal')) / total_docs,
                        (data.acoustic.get_total_for_markerclass('Contingency') +
                         data.written.get_total_for_markerclass('Contingency')) / total_docs,
                        (data.acoustic.get_total_for_markerclass('Comparison') +
                         data.written.get_total_for_markerclass('Comparison')) / total_docs,
                        (data.acoustic.get_total_for_markerclass('Expansion') +
                         data.written.get_total_for_markerclass('Expansion')) / total_docs,
                        ]

    mtp.draw_barchart(markertype_total, "Average Occurrences of Markertypes per Text in all Data",
                      ["Temporal", "Contingency", "Comparison", "Expansion"],
                      [markertypes.temporal_color, markertypes.contingency_color,
                       markertypes.comparison_color, markertypes.expansion_color],
                      "Average Occurrences per Text")

    helpers.DataFrames.markertype_dataframe("01_mt-average-all-data_dt",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_total,
                                            ["Discourse Type Data"])

    '''
    02: Durchschnittliches Vorkommen jedes Markertypes pro Text
    '''
    markertype_per_text_average_text = [[data.acoustic.get_average_for_markerclass('Temporal', average='doc'),
                                         data.written.get_average_for_markerclass('Temporal', average='doc')],
                                        [data.acoustic.get_average_for_markerclass('Contingency', average='doc'),
                                         data.written.get_average_for_markerclass('Contingency', average='doc')],
                                        [data.acoustic.get_average_for_markerclass('Comparison', average='doc'),
                                         data.written.get_average_for_markerclass('Comparison', average='doc')],
                                        [data.acoustic.get_average_for_markerclass('Expansion', average='doc'),
                                         data.written.get_average_for_markerclass('Expansion', average='doc')],
                                        ]

    mtp.draw_barchart_subplots("Average Occurence of Markertypes per Text",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.acoustic_label, data.written_label],
                               markertype_per_text_average_text,
                               [data.acoustic_color, data.written_color])

    helpers.DataFrames.markertype_dataframe("02_markertypes_average-per-text_dt",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_per_text_average_text,
                                            [data.acoustic_label, data.written_label])

    '''
    03: Vorkommen jedes Markertypes pro Datensatz in %
    '''
    markertype_per_text_perc = [[data.acoustic.get_percentage_for_markerclass('Temporal'),
                                 data.written.get_percentage_for_markerclass('Temporal')],
                                [data.acoustic.get_percentage_for_markerclass('Contingency'),
                                 data.written.get_percentage_for_markerclass('Contingency')],
                                [data.acoustic.get_percentage_for_markerclass('Comparison'),
                                 data.written.get_percentage_for_markerclass('Comparison')],
                                [data.acoustic.get_percentage_for_markerclass('Expansion'),
                                 data.written.get_percentage_for_markerclass('Expansion')],
                                ]

    mtp.draw_barchart_subplots("Share of Markertypes in Wordcount (%)",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.acoustic_label, data.written_label],
                               markertype_per_text_perc,
                               [data.acoustic_color, data.written_color])

    helpers.DataFrames.markertype_dataframe("03_markertypes_percentage_dt",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_per_text_perc,
                                            [data.acoustic_label, data.written_label])

    '''
    04: Vorkommen jedes Markertypes pro Datensatz in %
    '''
    markertype_per_text_perc_m = [[data.acoustic.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.written.get_percentage_for_markerclass('Temporal', perc='marker')],
                                  [data.acoustic.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.written.get_percentage_for_markerclass('Contingency', perc='marker')],
                                  [data.acoustic.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.written.get_percentage_for_markerclass('Comparison', perc='marker')],
                                  [data.acoustic.get_percentage_for_markerclass('Expansion', perc='marker'),
                                   data.written.get_percentage_for_markerclass('Expansion', perc='marker')]
                                  ]

    mtp.draw_barchart_subplots("Share of Markertypes in all Markers of a Texttype (%)",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.acoustic_label, data.written_label],
                               markertype_per_text_perc_m,
                               [data.acoustic_color, data.written_color])

    helpers.DataFrames.markertype_dataframe("04_markertypes_percentage-marker_dt",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_per_text_perc_m,
                                            [data.acoustic_label, data.written_label])

    '''
    05: Vorkommen jedes Markertypes pro Datensatz in %
    '''
    markertype_per_text_perc_m = [[data.acoustic.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.acoustic.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.acoustic.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.acoustic.get_percentage_for_markerclass('Expansion', perc='marker')],
                                  [data.written.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.written.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.written.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.written.get_percentage_for_markerclass('Expansion', perc='marker')]
                                  ]

    mtp.draw_barchart_subplots("Share of Markertypes in all Markers of a Texttype (%)",
                               [data.acoustic_label, data.written_label],
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               markertype_per_text_perc_m,
                               [markertypes.temporal_color, markertypes.contingency_color,
                                markertypes.comparison_color, markertypes.expansion_color])

    helpers.DataFrames.markertype_dataframe("05_markertypes_percentage-marker_dt",
                                            [data.acoustic_label, data.written_label],
                                            markertype_per_text_perc_m,
                                            ["Temporal", "Contingency", "Comparison", "Expansion"])

    ''' ---------- MARKER LEVEL -----------'''

    """
    Top 15 Markers per Class per Texttype
    """
    '''Temporal'''
    temporal = [data.acoustic.get_most_common_markers(marker_type="Temporal"),
                data.written.get_most_common_markers(marker_type="Temporal")]

    mc_temporal, values_temporal = hp.most_common_markers_list("01_mc-temp_dt",
                                                               temporal,
                                                               [data.acoustic_label, data.written_label])

    mtp.horizontal_barchart("Most common Temporal Markers - Share in all Temporal Markers in %",
                            values_temporal, mc_temporal,
                            [data.acoustic_color, data.written_color],
                            [data.acoustic_label, data.written_label],
                            "Share in all Temporal Markers")

    '''Contingency'''
    contingency = [data.acoustic.get_most_common_markers(marker_type="Contingency"),
                   data.written.get_most_common_markers(marker_type="Contingency")]

    mc_contingency, values_contingency = hp.most_common_markers_list("02_mc-contingency_dt",
                                                                     contingency,
                                                                     [data.acoustic_label, data.written_label])

    mtp.horizontal_barchart("Most common Contingency Markers - Share in all Contingency Markers in %",
                            values_contingency, mc_contingency,
                            [data.acoustic_color, data.written_color],
                            [data.acoustic_label, data.written_label],
                            "Share in all Contingency Markers")

    '''Comparison'''
    comparison = [data.acoustic.get_most_common_markers(marker_type="Comparison"),
                  data.written.get_most_common_markers(marker_type="Comparison")]

    mc_comparison, values_comparison = hp.most_common_markers_list("03_mc-comparison_dt",
                                                                   comparison,
                                                                   [data.acoustic_label, data.written_label])

    mtp.horizontal_barchart("Most common Comparison Markers - Share in all Comparison Markers in %",
                            values_comparison, mc_comparison,
                            [data.acoustic_color, data.written_color],
                            [data.acoustic_label, data.written_label],
                            "Share in all Comparison Markers")

    '''Expansion'''
    expansion = [data.acoustic.get_most_common_markers(marker_type="Expansion"),
                 data.written.get_most_common_markers(marker_type="Expansion")]

    mc_expansion, values_expansion = hp.most_common_markers_list("04_mc-expansion_dt",
                                                                 expansion,
                                                                 [data.acoustic_label, data.written_label])

    mtp.horizontal_barchart("Most common Expansion Markers - Share in all Expansion Markers in %",
                            values_expansion, mc_expansion,
                            [data.acoustic_color, data.written_color],
                            [data.acoustic_label, data.written_label],
                            "Share in all Expansion Markers")


if __name__ == '__main__':
    main()
