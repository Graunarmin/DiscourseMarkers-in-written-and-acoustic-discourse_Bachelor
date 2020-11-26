from datasets import GenreData as cd
from classes import MarkerTypes as mt
from plotting import MarkerTypePlots as mtp
from helpers import Helpers as hp


def main():
    markertypes = mt.MarkerTypes(
        "../../data/listenability-tools/main-senses/words_main-sense.json")

    data = cd.GenreData(
        "../../bigData/listenability-tools/Spotify/genres/dict/news_dict.json",
        "../../bigData/listenability-tools/Spotify/genres/dict/discussion_dict.json",
        "../../bigData/listenability-tools/Spotify/genres/dict/science_dict.json",
        "../../bigData/listenability-tools/Spotify/genres/dict/documentary_dict.json",
        "../../bigData/listenability-tools/discourse-types/dict/ted-dict.json",
        news_scores_opt="../../bigData/listenability-tools/Spotify/genres/marker-scores/news_dict.json",
        general=False,
        markertypes=markertypes)

    '''
    01: Durchschnittliches Vorkommen jedes Markertypes pro total Wordcount
    '''
    markertype_per_text_average_wc = [[data.news.get_average_for_markerclass('Temporal'),
                                       data.discussion.get_average_for_markerclass('Temporal'),
                                       data.science.get_average_for_markerclass('Temporal'),
                                       data.documentary.get_average_for_markerclass('Temporal'),
                                       data.presentation.get_average_for_markerclass('Temporal')],
                                      [data.news.get_average_for_markerclass('Contingency'),
                                       data.discussion.get_average_for_markerclass('Contingency'),
                                       data.science.get_average_for_markerclass('Contingency'),
                                       data.documentary.get_average_for_markerclass('Contingency'),
                                       data.presentation.get_average_for_markerclass('Contingency')],
                                      [data.news.get_average_for_markerclass('Comparison'),
                                       data.discussion.get_average_for_markerclass('Comparison'),
                                       data.science.get_average_for_markerclass('Comparison'),
                                       data.documentary.get_average_for_markerclass('Comparison'),
                                       data.presentation.get_average_for_markerclass('Comparison')],
                                      [data.news.get_average_for_markerclass('Expansion'),
                                       data.discussion.get_average_for_markerclass('Expansion'),
                                       data.science.get_average_for_markerclass('Expansion'),
                                       data.documentary.get_average_for_markerclass('Expansion'),
                                       data.presentation.get_average_for_markerclass('Expansion')],
                                      ]

    mtp.draw_barchart_subplots("Average Occurence of Markertypes per total Wordcount",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.news_label, data.discussion_label, data.science_label,
                                data.documentary_label, data.presentation_label],
                               markertype_per_text_average_wc,
                               [data.news_color, data.discussion_color, data.science_color,
                                data.documentary_color, data.presentation_color])

    hp.marker_dataframe("01_markertypes_average-per-wc",
                        ["Temporal", "Contingency", "Comparison", "Expansion"],
                        markertype_per_text_average_wc,
                        [data.news_label, data.discussion_label, data.science_label,
                         data.documentary_label, data.presentation_label])

    '''
    02: Durchschnittliches Vorkommen jedes Markertypes pro Text
    '''
    markertype_per_text_average_text = [[data.news.get_average_for_markerclass('Temporal', average='doc'),
                                         data.discussion.get_average_for_markerclass('Temporal', average='doc'),
                                         data.science.get_average_for_markerclass('Temporal', average='doc'),
                                         data.documentary.get_average_for_markerclass('Temporal', average='doc'),
                                         data.presentation.get_average_for_markerclass('Temporal', average='doc')],
                                        [data.news.get_average_for_markerclass('Contingency', average='doc'),
                                         data.discussion.get_average_for_markerclass('Contingency', average='doc'),
                                         data.science.get_average_for_markerclass('Contingency', average='doc'),
                                         data.documentary.get_average_for_markerclass('Contingency', average='doc'),
                                         data.presentation.get_average_for_markerclass('Contingency', average='doc')],
                                        [data.news.get_average_for_markerclass('Comparison', average='doc'),
                                         data.discussion.get_average_for_markerclass('Comparison', average='doc'),
                                         data.science.get_average_for_markerclass('Comparison', average='doc'),
                                         data.documentary.get_average_for_markerclass('Comparison', average='doc'),
                                         data.presentation.get_average_for_markerclass('Comparison', average='doc')],
                                        [data.news.get_average_for_markerclass('Expansion', average='doc'),
                                         data.discussion.get_average_for_markerclass('Expansion', average='doc'),
                                         data.science.get_average_for_markerclass('Expansion', average='doc'),
                                         data.documentary.get_average_for_markerclass('Expansion', average='doc'),
                                         data.presentation.get_average_for_markerclass('Expansion', average='doc')],
                                        ]

    mtp.draw_barchart_subplots("Average Occurence of Markertypes per Text",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.news_label, data.discussion_label, data.science_label,
                                data.documentary_label, data.presentation_label],
                               markertype_per_text_average_text,
                               [data.news_color, data.discussion_color, data.science_color,
                                data.documentary_color, data.presentation_color])

    hp.marker_dataframe("02_markertypes_average-per-text",
                        ["Temporal", "Contingency", "Comparison", "Expansion"],
                        markertype_per_text_average_text,
                        [data.news_label, data.discussion_label, data.science_label,
                         data.documentary_label, data.presentation_label])

    '''
    03: Vorkommen jedes Markertypes pro Datensatz in %
    '''
    markertype_per_text_average_text = [[data.news.get_percentage_for_markerclass('Temporal'),
                                         data.discussion.get_percentage_for_markerclass('Temporal'),
                                         data.science.get_percentage_for_markerclass('Temporal'),
                                         data.documentary.get_percentage_for_markerclass('Temporal'),
                                         data.presentation.get_percentage_for_markerclass('Temporal')],
                                        [data.news.get_percentage_for_markerclass('Contingency'),
                                         data.discussion.get_percentage_for_markerclass('Contingency'),
                                         data.science.get_percentage_for_markerclass('Contingency'),
                                         data.documentary.get_percentage_for_markerclass('Contingency'),
                                         data.presentation.get_percentage_for_markerclass('Contingency')],
                                        [data.news.get_percentage_for_markerclass('Comparison'),
                                         data.discussion.get_percentage_for_markerclass('Comparison'),
                                         data.science.get_percentage_for_markerclass('Comparison'),
                                         data.documentary.get_percentage_for_markerclass('Comparison'),
                                         data.presentation.get_percentage_for_markerclass('Comparison')],
                                        [data.news.get_percentage_for_markerclass('Expansion'),
                                         data.discussion.get_percentage_for_markerclass('Expansion'),
                                         data.science.get_percentage_for_markerclass('Expansion'),
                                         data.documentary.get_percentage_for_markerclass('Expansion'),
                                         data.presentation.get_percentage_for_markerclass('Expansion')],
                                        ]

    mtp.draw_barchart_subplots("Share of Markertypes in Wordcount (%)",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.news_label, data.discussion_label, data.science_label,
                                data.documentary_label, data.presentation_label],
                               markertype_per_text_average_text,
                               [data.news_color, data.discussion_color, data.science_color,
                                data.documentary_color, data.presentation_color])

    hp.marker_dataframe("03_markertypes_percentage",
                        ["Temporal", "Contingency", "Comparison", "Expansion"],
                        markertype_per_text_average_text,
                        [data.news_label, data.discussion_label, data.science_label,
                         data.documentary_label, data.presentation_label])

    '''
    04: Total Occurence per Markertype
    '''
    total_docs = (data.news.get_total_docs() + data.discussion.get_total_docs() +
                  data.science.get_total_docs() + data.documentary.get_total_docs()
                  + data.presentation.get_total_docs())

    markertype_total = [(data.news.get_total_for_markerclass('Temporal') +
                         data.discussion.get_total_for_markerclass('Temporal') +
                         data.science.get_total_for_markerclass('Temporal') +
                         data.documentary.get_total_for_markerclass('Temporal') +
                         data.presentation.get_total_for_markerclass('Temporal')) / total_docs,
                        (data.news.get_total_for_markerclass('Contingency') +
                         data.discussion.get_total_for_markerclass('Contingency') +
                         data.science.get_total_for_markerclass('Contingency') +
                         data.documentary.get_total_for_markerclass('Contingency') +
                         data.presentation.get_total_for_markerclass('Temporal')) / total_docs,
                        (data.news.get_total_for_markerclass('Comparison') +
                         data.discussion.get_total_for_markerclass('Comparison') +
                         data.science.get_total_for_markerclass('Comparison') +
                         data.documentary.get_total_for_markerclass('Comparison') +
                         data.presentation.get_total_for_markerclass('Temporal')) / total_docs,
                        (data.news.get_total_for_markerclass('Expansion') +
                         data.discussion.get_total_for_markerclass('Expansion') +
                         data.science.get_total_for_markerclass('Expansion') +
                         data.documentary.get_total_for_markerclass('Expansion') +
                         data.presentation.get_total_for_markerclass('Temporal')) / total_docs,
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
