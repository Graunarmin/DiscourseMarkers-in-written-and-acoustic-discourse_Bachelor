import helpers.DataFrames
import helpers.Statistics
from datasets import ConversationTypeData as cd
from classes import MarkerTypes as mt
from plotting import MarkerTypePlots as mtp
from helpers import Helpers as hp


def main():
    markertypes = mt.MarkerTypes(
        "../../data/listenability-tools/main-senses/words_main-sense.json")

    data = cd.ConversationTypeData(
        "../../bigData/listenability-tools/Spotify/conversation-types/dict/dialog_dict.json",
        "../../bigData/listenability-tools/Spotify/conversation-types/dict/monolog_dict.json",
        "../../bigData/listenability-tools/Spotify/conversation-types/dict/cooperative-monolog_dict.json",
        "../../bigData/listenability-tools/discourse-types/dict/ted-dict.json",
        dialog_scores_opt=
        "../../bigData/listenability-tools/Spotify/conversation-types/scores/marker-scores/dialog-marker.csv",
        monolog_scores_opt=
        "../../bigData/listenability-tools/Spotify/conversation-types/scores/marker-scores/monolog-marker.csv",
        cmonolog_scores_opt=
        "../../bigData/listenability-tools/Spotify/conversation-types/scores/marker-scores/cooperative-monolog-marker"
        ".csv",
        ted_scores_opt=
        "../../bigData/listenability-tools/discourse-types/scores/marker-scores/ted-marker.csv",
        general=False,
        markertypes=markertypes)

    # '''
    # T-Test for total values per Document
    # '''
    # dialog = data.dialog.get_markerclass_columns()
    # monolog = data.monolog.get_markerclass_columns()
    # cmonolog = data.cmonolog.get_markerclass_columns()
    # speech = data.speech.get_markerclass_columns()
    #
    # helpers.Statistics.effectsize_and_significance("temporal-per-document_statistics_conversation-types_ct",
    #                                                [dialog['temporal'], monolog['temporal'],
    #                                                 cmonolog['temporal'], speech['temporal']],
    #                                                [data.dialog_label, data.monolog_label,
    #                                                 data.cmonolog_label, data.speech_label])
    #
    # helpers.Statistics.effectsize_and_significance("contingency-per-document_statistics_conversation-types_ct",
    #                                                [dialog['contingency'], monolog['contingency'],
    #                                                 cmonolog['contingency'], speech['contingency']],
    #                                                [data.dialog_label, data.monolog_label,
    #                                                 data.cmonolog_label, data.speech_label])
    #
    # helpers.Statistics.effectsize_and_significance("comparison-per-document_statistics_conversation-types_ct",
    #                                                [dialog['comparison'], monolog['comparison'],
    #                                                 cmonolog['comparison'], speech['comparison']],
    #                                                [data.dialog_label, data.monolog_label,
    #                                                 data.cmonolog_label, data.speech_label])
    #
    # helpers.Statistics.effectsize_and_significance("expansion-per-document_statistics_conversation-types_ct",
    #                                                [dialog['expansion'], monolog['expansion'],
    #                                                 cmonolog['expansion'], speech['expansion']],
    #                                                [data.dialog_label, data.monolog_label,
    #                                                 data.cmonolog_label, data.speech_label])

    '''
    01: Total Occurence per Markertype
    '''
    total_docs = (data.dialog.get_total_docs() + data.monolog.get_total_docs() +
                  data.cmonolog.get_total_docs() + data.speech.get_total_docs())

    markertype_total = [(data.dialog.get_total_for_markerclass('Temporal') +
                         data.monolog.get_total_for_markerclass('Temporal') +
                         data.cmonolog.get_total_for_markerclass('Temporal') +
                         data.speech.get_total_for_markerclass('Temporal')) / total_docs,
                        (data.dialog.get_total_for_markerclass('Contingency') +
                         data.monolog.get_total_for_markerclass('Contingency') +
                         data.cmonolog.get_total_for_markerclass('Contingency') +
                         data.speech.get_total_for_markerclass('Contingency')) / total_docs,
                        (data.dialog.get_total_for_markerclass('Comparison') +
                         data.monolog.get_total_for_markerclass('Comparison') +
                         data.cmonolog.get_total_for_markerclass('Comparison') +
                         data.speech.get_total_for_markerclass('Comparison')) / total_docs,
                        (data.dialog.get_total_for_markerclass('Expansion') +
                         data.monolog.get_total_for_markerclass('Expansion') +
                         data.cmonolog.get_total_for_markerclass('Expansion') +
                         data.speech.get_total_for_markerclass('Expansion')) / total_docs,
                        ]

    mtp.draw_barchart(markertype_total, "Average Occurrences of Markertypes per Text in all Data",
                      ["Temporal", "Contingency", "Comparison", "Expansion"],
                      [markertypes.temporal_color, markertypes.contingency_color,
                       markertypes.comparison_color, markertypes.expansion_color],
                      "Average Occurrences per Text")

    helpers.DataFrames.markertype_dataframe("01_mt-average-all-data_ct",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_total,
                                            ["Conversation Type Data"])

    '''
    02: Durchschnittliches Vorkommen jedes Markertypes pro Text
    '''
    markertype_per_text_average_text = [[data.dialog.get_average_for_markerclass('Temporal', average='doc'),
                                         data.monolog.get_average_for_markerclass('Temporal', average='doc'),
                                         data.cmonolog.get_average_for_markerclass('Temporal', average='doc'),
                                         data.speech.get_average_for_markerclass('Temporal', average='doc')],
                                        [data.dialog.get_average_for_markerclass('Contingency', average='doc'),
                                         data.monolog.get_average_for_markerclass('Contingency', average='doc'),
                                         data.cmonolog.get_average_for_markerclass('Contingency', average='doc'),
                                         data.speech.get_average_for_markerclass('Contingency', average='doc')],
                                        [data.dialog.get_average_for_markerclass('Comparison', average='doc'),
                                         data.monolog.get_average_for_markerclass('Comparison', average='doc'),
                                         data.cmonolog.get_average_for_markerclass('Comparison', average='doc'),
                                         data.speech.get_average_for_markerclass('Comparison', average='doc')],
                                        [data.dialog.get_average_for_markerclass('Expansion', average='doc'),
                                         data.monolog.get_average_for_markerclass('Expansion', average='doc'),
                                         data.cmonolog.get_average_for_markerclass('Expansion', average='doc'),
                                         data.speech.get_average_for_markerclass('Expansion', average='doc')],
                                        ]

    mtp.draw_barchart_subplots("Average Occurence of Markertypes per Text",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label],
                               markertype_per_text_average_text,
                               [data.dialog_color, data.monolog_color, data.cmonolog_color, data.speech_color])

    helpers.DataFrames.markertype_dataframe("02_markertypes_average-per-text_ct",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_per_text_average_text,
                                            [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label])

    '''
    03: Vorkommen jedes Markertypes pro Datensatz in %
    '''
    markertype_per_text_perc = [[data.dialog.get_percentage_for_markerclass('Temporal'),
                                 data.monolog.get_percentage_for_markerclass('Temporal'),
                                 data.cmonolog.get_percentage_for_markerclass('Temporal'),
                                 data.speech.get_percentage_for_markerclass('Temporal')],
                                [data.dialog.get_percentage_for_markerclass('Contingency'),
                                 data.monolog.get_percentage_for_markerclass('Contingency'),
                                 data.cmonolog.get_percentage_for_markerclass('Contingency'),
                                 data.speech.get_percentage_for_markerclass('Contingency')],
                                [data.dialog.get_percentage_for_markerclass('Comparison'),
                                 data.monolog.get_percentage_for_markerclass('Comparison'),
                                 data.cmonolog.get_percentage_for_markerclass('Comparison'),
                                 data.speech.get_percentage_for_markerclass('Comparison')],
                                [data.dialog.get_percentage_for_markerclass('Expansion'),
                                 data.monolog.get_percentage_for_markerclass('Expansion'),
                                 data.cmonolog.get_percentage_for_markerclass('Expansion'),
                                 data.speech.get_percentage_for_markerclass('Expansion')],
                                ]

    mtp.draw_barchart_subplots("Share of Markertypes in Wordcount (%)",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label],
                               markertype_per_text_perc,
                               [data.dialog_color, data.monolog_color, data.cmonolog_color, data.speech_color])

    helpers.DataFrames.markertype_dataframe("03_markertypes_percentage_ct",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_per_text_perc,
                                            [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label])

    '''
    04: Prozentualer Anteil an allen Markern der Textsorte
    '''
    markertype_per_text_perc_m = [[data.dialog.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.monolog.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.cmonolog.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.speech.get_percentage_for_markerclass('Temporal', perc='marker')],
                                  [data.dialog.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.monolog.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.cmonolog.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.speech.get_percentage_for_markerclass('Contingency', perc='marker')],
                                  [data.dialog.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.monolog.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.cmonolog.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.speech.get_percentage_for_markerclass('Comparison', perc='marker')],
                                  [data.dialog.get_percentage_for_markerclass('Expansion', perc='marker'),
                                   data.monolog.get_percentage_for_markerclass('Expansion', perc='marker'),
                                   data.cmonolog.get_percentage_for_markerclass('Expansion', perc='marker'),
                                   data.speech.get_percentage_for_markerclass('Expansion', perc='marker')],
                                  ]

    mtp.draw_barchart_subplots("Share of Markertypes in all Markers of a Texttype (%)",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label],
                               markertype_per_text_perc_m,
                               [data.dialog_color, data.monolog_color, data.cmonolog_color, data.speech_color])

    helpers.DataFrames.markertype_dataframe("04_markertypes_percentage-marker_ct",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_per_text_perc_m,
                                            [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label])

    '''
    05: Prozentualer Anteil an allen Markern der Textsorte
    '''
    markertype_per_text_perc_m = [[data.dialog.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.dialog.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.dialog.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.dialog.get_percentage_for_markerclass('Expansion', perc='marker')],
                                  [data.monolog.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.monolog.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.monolog.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.monolog.get_percentage_for_markerclass('Expansion', perc='marker')],
                                  [data.cmonolog.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.cmonolog.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.cmonolog.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.cmonolog.get_percentage_for_markerclass('Expansion', perc='marker')],
                                  [data.speech.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.speech.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.speech.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.speech.get_percentage_for_markerclass('Expansion', perc='marker')],
                                  ]

    mtp.draw_barchart_subplots("Share of Markertypes in all Markers of a Texttype (%)",
                               [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label],
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               markertype_per_text_perc_m,
                               [markertypes.temporal_color, markertypes.contingency_color,
                                markertypes.comparison_color, markertypes.expansion_color])

    helpers.DataFrames.markertype_dataframe("05_markertypes_percentage-marker_ct",
                                            [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label],
                                            markertype_per_text_perc_m,
                                            ["Temporal", "Contingency", "Comparison", "Expansion"])

    ''' ---------- MARKER LEVEL -----------'''

    """
    Top 15 Markers per Class per Texttype
    """
    '''Temporal'''
    temporal = [data.dialog.get_most_common_markers(marker_type="Temporal"),
                data.monolog.get_most_common_markers(marker_type="Temporal"),
                data.cmonolog.get_most_common_markers(marker_type="Temporal"),
                data.speech.get_most_common_markers(marker_type="Temporal")]

    mc_temporal, values_temporal = hp.most_common_markers_list("01_mc-temp_ct",
                                                               temporal,
                                                               [data.dialog_label, data.monolog_label,
                                                                data.cmonolog_label, data.speech_label])

    mtp.horizontal_barchart("Most common Temporal Markers - Share in all Temporal Markers in %",
                            values_temporal, mc_temporal,
                            [data.dialog_color, data.monolog_color, data.cmonolog_color, data.speech_color],
                            [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label],
                            "Share in all Temporal Markers")

    '''Contingency'''
    contingency = [data.dialog.get_most_common_markers(marker_type="Contingency"),
                   data.monolog.get_most_common_markers(marker_type="Contingency"),
                   data.cmonolog.get_most_common_markers(marker_type="Contingency"),
                   data.speech.get_most_common_markers(marker_type="Contingency")]

    mc_contingency, values_contingency = hp.most_common_markers_list("02_mc-contingency_ct",
                                                                     contingency,
                                                                     [data.dialog_label, data.monolog_label,
                                                                      data.cmonolog_label, data.speech_label])

    mtp.horizontal_barchart("Most common Contingency Markers - Share in all Contingency Markers in %",
                            values_contingency, mc_contingency,
                            [data.dialog_color, data.monolog_color, data.cmonolog_color, data.speech_color],
                            [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label],
                            "Share in all Contingency Markers")

    '''Comparison'''
    comparison = [data.dialog.get_most_common_markers(marker_type="Comparison"),
                  data.monolog.get_most_common_markers(marker_type="Comparison"),
                  data.cmonolog.get_most_common_markers(marker_type="Comparison"),
                  data.speech.get_most_common_markers(marker_type="Comparison")]

    mc_comparison, values_comparison = hp.most_common_markers_list("03_mc-comparison_ct",
                                                                   comparison,
                                                                   [data.dialog_label, data.monolog_label,
                                                                    data.cmonolog_label, data.speech_label])

    mtp.horizontal_barchart("Most common Comparison Markers - Share in all Comparison Markers in %",
                            values_comparison, mc_comparison,
                            [data.dialog_color, data.monolog_color, data.cmonolog_color, data.speech_color],
                            [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label],
                            "Share in all Comparison Markers")

    '''Expansion'''
    expansion = [data.dialog.get_most_common_markers(marker_type="Expansion"),
                 data.monolog.get_most_common_markers(marker_type="Expansion"),
                 data.cmonolog.get_most_common_markers(marker_type="Expansion"),
                 data.speech.get_most_common_markers(marker_type="Expansion")]

    mc_expansion, values_expansion = hp.most_common_markers_list("04_mc-expansion_ct",
                                                                 expansion,
                                                                 [data.dialog_label, data.monolog_label,
                                                                  data.cmonolog_label, data.speech_label])

    mtp.horizontal_barchart("Most common Expansion Markers - Share in all Expansion Markers in %",
                            values_expansion, mc_expansion,
                            [data.dialog_color, data.monolog_color, data.cmonolog_color, data.speech_color],
                            [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label],
                            "Share in all Expansion Markers")


if __name__ == '__main__':
    main()
