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
        general=False,
        markertypes=markertypes)

    '''
        01: Durchschnittliches Vorkommen jedes Markertypes pro total Wordcount
        '''
    markertype_per_text_average_wc = [[data.dialog.get_average_for_markerclass('Temporal'),
                                       data.monolog.get_average_for_markerclass('Temporal'),
                                       data.cmonolog.get_average_for_markerclass('Temporal'),
                                       data.speech.get_average_for_markerclass('Temporal')],
                                      [data.dialog.get_average_for_markerclass('Contingency'),
                                       data.monolog.get_average_for_markerclass('Contingency'),
                                       data.cmonolog.get_average_for_markerclass('Contingency'),
                                       data.speech.get_average_for_markerclass('Contingency')],
                                      [data.dialog.get_average_for_markerclass('Comparison'),
                                       data.monolog.get_average_for_markerclass('Comparison'),
                                       data.cmonolog.get_average_for_markerclass('Comparison'),
                                       data.speech.get_average_for_markerclass('Comparison')],
                                      [data.dialog.get_average_for_markerclass('Expansion'),
                                       data.monolog.get_average_for_markerclass('Expansion'),
                                       data.cmonolog.get_average_for_markerclass('Expansion'),
                                       data.speech.get_average_for_markerclass('Expansion')],
                                      ]

    mtp.draw_barchart_subplots("Average Occurence of Markertypes per total Wordcount",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label],
                               markertype_per_text_average_wc,
                               [data.dialog_color, data.monolog_color, data.cmonolog_color, data.speech_color])

    hp.marker_dataframe("01_markertypes_average-per-wc",
                        ["Temporal", "Contingency", "Comparison", "Expansion"],
                        markertype_per_text_average_wc,
                        [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label])

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

    hp.marker_dataframe("02_markertypes_average-per-text",
                        ["Temporal", "Contingency", "Comparison", "Expansion"],
                        markertype_per_text_average_text,
                        [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label])

    '''
    03: Vorkommen jedes Markertypes pro Datensatz in %
    '''
    markertype_per_text_average_text = [[data.dialog.get_percentage_for_markerclass('Temporal'),
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
                               markertype_per_text_average_text,
                               [data.dialog_color, data.monolog_color, data.cmonolog_color, data.speech_color])

    hp.marker_dataframe("03_markertypes_percentage",
                        ["Temporal", "Contingency", "Comparison", "Expansion"],
                        markertype_per_text_average_text,
                        [data.dialog_label, data.monolog_label, data.cmonolog_label, data.speech_label])

    '''
    04: Total Occurence per Markertype
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

    hp.marker_dataframe("04_mt-average-all-data",
                        ["Temporal", "Contingency", "Comparison", "Expansion"],
                        markertype_total,
                        ["Discourse Type Data"])


if __name__ == '__main__':
    main()
