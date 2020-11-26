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
        general=False,
        markertypes=markertypes)

    '''
    01: Durchschnittliches Vorkommen jedes Markertypes pro total Wordcount
    '''
    markertype_per_text_average_wc = [[data.spotify.get_average_for_markerclass('Temporal'),
                                       data.ted.get_average_for_markerclass('Temporal'),
                                       data.ny.get_average_for_markerclass('Temporal'),
                                       data.gig.get_average_for_markerclass('Temporal')],
                                      [data.spotify.get_average_for_markerclass('Contingency'),
                                       data.ted.get_average_for_markerclass('Contingency'),
                                       data.ny.get_average_for_markerclass('Contingency'),
                                       data.gig.get_average_for_markerclass('Contingency')],
                                      [data.spotify.get_average_for_markerclass('Comparison'),
                                       data.ted.get_average_for_markerclass('Comparison'),
                                       data.ny.get_average_for_markerclass('Comparison'),
                                       data.gig.get_average_for_markerclass('Comparison')],
                                      [data.spotify.get_average_for_markerclass('Expansion'),
                                       data.ted.get_average_for_markerclass('Expansion'),
                                       data.ny.get_average_for_markerclass('Expansion'),
                                       data.gig.get_average_for_markerclass('Expansion')],
                                      ]

    mtp.draw_barchart_subplots("Average Occurence of Markertypes per total Wordcount",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
                               markertype_per_text_average_wc,
                               [data.spotify_color, data.ted_color, data.ny_color, data.gig_color])

    hp.marker_dataframe("01_markertypes_average-per-wc",
                        ["Temporal", "Contingency", "Comparison", "Expansion"],
                        markertype_per_text_average_wc,
                        [data.spotify_label, data.ted_label, data.ny_label, data.gig_label])

    '''
    02: Durchschnittliches Vorkommen jedes Markertypes pro Text
    '''
    markertype_per_text_average_text = [[data.spotify.get_average_for_markerclass('Temporal', average='doc'),
                                         data.ted.get_average_for_markerclass('Temporal', average='doc'),
                                         data.ny.get_average_for_markerclass('Temporal', average='doc'),
                                         data.gig.get_average_for_markerclass('Temporal', average='doc')],
                                        [data.spotify.get_average_for_markerclass('Contingency', average='doc'),
                                         data.ted.get_average_for_markerclass('Contingency', average='doc'),
                                         data.ny.get_average_for_markerclass('Contingency', average='doc'),
                                         data.gig.get_average_for_markerclass('Contingency', average='doc')],
                                        [data.spotify.get_average_for_markerclass('Comparison', average='doc'),
                                         data.ted.get_average_for_markerclass('Comparison', average='doc'),
                                         data.ny.get_average_for_markerclass('Comparison', average='doc'),
                                         data.gig.get_average_for_markerclass('Comparison', average='doc')],
                                        [data.spotify.get_average_for_markerclass('Expansion', average='doc'),
                                         data.ted.get_average_for_markerclass('Expansion', average='doc'),
                                         data.ny.get_average_for_markerclass('Expansion', average='doc'),
                                         data.gig.get_average_for_markerclass('Expansion', average='doc')],
                                        ]

    mtp.draw_barchart_subplots("Average Occurence of Markertypes per Text",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
                               markertype_per_text_average_text,
                               [data.spotify_color, data.ted_color, data.ny_color, data.gig_color])

    hp.marker_dataframe("02_markertypes_average-per-text",
                        ["Temporal", "Contingency", "Comparison", "Expansion"],
                        markertype_per_text_average_text,
                        [data.spotify_label, data.ted_label, data.ny_label, data.gig_label])

    '''
    03: Vorkommen jedes Markertypes pro Datensatz in %
    '''
    markertype_per_text_average_text = [[data.spotify.get_percentage_for_markerclass('Temporal'),
                                         data.ted.get_percentage_for_markerclass('Temporal'),
                                         data.ny.get_percentage_for_markerclass('Temporal'),
                                         data.gig.get_percentage_for_markerclass('Temporal')],
                                        [data.spotify.get_percentage_for_markerclass('Contingency'),
                                         data.ted.get_percentage_for_markerclass('Contingency'),
                                         data.ny.get_percentage_for_markerclass('Contingency'),
                                         data.gig.get_percentage_for_markerclass('Contingency')],
                                        [data.spotify.get_percentage_for_markerclass('Comparison'),
                                         data.ted.get_percentage_for_markerclass('Comparison'),
                                         data.ny.get_percentage_for_markerclass('Comparison'),
                                         data.gig.get_percentage_for_markerclass('Comparison')],
                                        [data.spotify.get_percentage_for_markerclass('Expansion'),
                                         data.ted.get_percentage_for_markerclass('Expansion'),
                                         data.ny.get_percentage_for_markerclass('Expansion'),
                                         data.gig.get_percentage_for_markerclass('Expansion')],
                                        ]

    mtp.draw_barchart_subplots("Share of Markertypes in Wordcount (%)",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
                               markertype_per_text_average_text,
                               [data.spotify_color, data.ted_color, data.ny_color, data.gig_color])

    hp.marker_dataframe("03_markertypes_percentage",
                        ["Temporal", "Contingency", "Comparison", "Expansion"],
                        markertype_per_text_average_text,
                        [data.spotify_label, data.ted_label, data.ny_label, data.gig_label])

    '''
    04: Total Occurence per Markertype
    '''
    total_docs = (data.spotify.get_total_docs() + data.ted.get_total_docs() +
                  data.ny.get_total_docs() + data.gig.get_total_docs())

    markertype_total = [(data.spotify.get_total_for_markerclass('Temporal') +
                         data.ted.get_total_for_markerclass('Temporal') +
                         data.ny.get_total_for_markerclass('Temporal') +
                         data.gig.get_total_for_markerclass('Temporal')) / total_docs,
                        (data.spotify.get_total_for_markerclass('Contingency') +
                         data.ted.get_total_for_markerclass('Contingency') +
                         data.ny.get_total_for_markerclass('Contingency') +
                         data.gig.get_total_for_markerclass('Contingency')) / total_docs,
                        (data.spotify.get_total_for_markerclass('Comparison') +
                         data.ted.get_total_for_markerclass('Comparison') +
                         data.ny.get_total_for_markerclass('Comparison') +
                         data.gig.get_total_for_markerclass('Comparison')) / total_docs,
                        (data.spotify.get_total_for_markerclass('Expansion') +
                         data.ted.get_total_for_markerclass('Expansion') +
                         data.ny.get_total_for_markerclass('Expansion') +
                         data.gig.get_total_for_markerclass('Expansion')) / total_docs,
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
