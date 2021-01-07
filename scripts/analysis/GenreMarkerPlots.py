import helpers.DataFrames
import helpers.Statistics
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
        news_scores_opt="../../bigData/listenability-tools/Spotify/genres/scores/marker-scores/news-marker.csv",
        discussion_scores_opt="../../bigData/listenability-tools/Spotify/genres/scores/marker-scores/discussion-marker.csv",
        science_scores_opt="../../bigData/listenability-tools/Spotify/genres/scores/marker-scores/science-marker.csv",
        documentary_scores_opt="../../bigData/listenability-tools/Spotify/genres/scores/marker-scores/documentary-marker.csv",
        ted_scores_opt="../../bigData/listenability-tools/discourse-types/scores/marker-scores/ted-marker.csv",
        general=False,
        markertypes=markertypes)

    '''
    T-Test for total values per Document
    '''
    news = data.news.get_markerclass_columns()
    discussion = data.discussion.get_markerclass_columns()
    science = data.science.get_markerclass_columns()
    documentary = data.documentary.get_markerclass_columns()
    presentation = data.presentation.get_markerclass_columns()

    helpers.Statistics.effectsize_and_significance("temporal-per-document_statistics",
                                                   [news['temporal'], discussion['temporal'], science['temporal'],
                                                    documentary['temporal'], presentation['temporal']],
                                                   [data.news_label, data.discussion_label, data.science_label,
                                                    data.documentary_label, data.presentation_label])

    helpers.Statistics.effectsize_and_significance("contingency-per-document_statistics",
                                                   [news['contingency'], discussion['contingency'],
                                                    science['contingency'],
                                                    documentary['contingency'], presentation['contingency']],
                                                   [data.news_label, data.discussion_label, data.science_label,
                                                    data.documentary_label, data.presentation_label])

    helpers.Statistics.effectsize_and_significance("comparison-per-document_statistics",
                                                   [news['comparison'], discussion['comparison'], science['comparison'],
                                                    documentary['comparison'], presentation['comparison']],
                                                   [data.news_label, data.discussion_label, data.science_label,
                                                    data.documentary_label, data.presentation_label])

    helpers.Statistics.effectsize_and_significance("expansion-per-document_statistics",
                                                   [news['expansion'], discussion['expansion'], science['expansion'],
                                                    documentary['expansion'], presentation['expansion']],
                                                   [data.news_label, data.discussion_label, data.science_label,
                                                    data.documentary_label, data.presentation_label])
    '''
    01: Total Occurence per Markertype
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

    helpers.DataFrames.markertype_dataframe("01_mt-average-all-data_genre",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_total,
                                            ["Discourse Type Data"])

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

    helpers.DataFrames.markertype_dataframe("02_markertypes_average-per-text_genre",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_per_text_average_text,
                                            [data.news_label, data.discussion_label, data.science_label,
                                             data.documentary_label, data.presentation_label])

    '''
    03: Vorkommen jedes Markertypes pro Datensatz in %
    '''
    markertype_per_text_perc = [[data.news.get_percentage_for_markerclass('Temporal'),
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
                               markertype_per_text_perc,
                               [data.news_color, data.discussion_color, data.science_color,
                                data.documentary_color, data.presentation_color])

    helpers.DataFrames.markertype_dataframe("03_markertypes_percentage_genre",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_per_text_perc,
                                            [data.news_label, data.discussion_label, data.science_label,
                                             data.documentary_label, data.presentation_label])

    '''
    04: Prozentualer Anteil an allen Markern der Textsorte
    '''
    markertype_per_text_perc_m = [[data.news.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.discussion.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.science.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.documentary.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.presentation.get_percentage_for_markerclass('Temporal', perc='marker')],
                                  [data.news.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.discussion.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.science.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.documentary.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.presentation.get_percentage_for_markerclass('Contingency', perc='marker')],
                                  [data.news.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.discussion.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.science.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.documentary.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.presentation.get_percentage_for_markerclass('Comparison', perc='marker')],
                                  [data.news.get_percentage_for_markerclass('Expansion', perc='marker'),
                                   data.discussion.get_percentage_for_markerclass('Expansion', perc='marker'),
                                   data.science.get_percentage_for_markerclass('Expansion', perc='marker'),
                                   data.documentary.get_percentage_for_markerclass('Expansion', perc='marker'),
                                   data.presentation.get_percentage_for_markerclass('Expansion', perc='marker')],
                                  ]

    mtp.draw_barchart_subplots("Share of Markertypes in all Markers of a Texttype (%)",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.news_label, data.discussion_label, data.science_label,
                                data.documentary_label, data.presentation_label],
                               markertype_per_text_perc_m,
                               [data.news_color, data.discussion_color, data.science_color,
                                data.documentary_color, data.presentation_color])

    helpers.DataFrames.markertype_dataframe("04_markertypes_percentage-marker_genre",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertype_per_text_perc_m,
                                            [data.news_label, data.discussion_label, data.science_label,
                                             data.documentary_label, data.presentation_label])

    '''
    05: Prozentualer Anteil an allen Markern der Textsorte
    '''
    markertype_per_text_perc_m = [[data.news.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.news.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.news.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.news.get_percentage_for_markerclass('Expansion', perc='marker')],
                                  [data.discussion.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.discussion.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.discussion.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.discussion.get_percentage_for_markerclass('Expansion', perc='marker')],
                                  [data.science.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.science.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.science.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.science.get_percentage_for_markerclass('Expansion', perc='marker')],
                                  [data.documentary.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.documentary.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.documentary.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.documentary.get_percentage_for_markerclass('Expansion', perc='marker')],
                                  [data.presentation.get_percentage_for_markerclass('Temporal', perc='marker'),
                                   data.presentation.get_percentage_for_markerclass('Contingency', perc='marker'),
                                   data.presentation.get_percentage_for_markerclass('Comparison', perc='marker'),
                                   data.presentation.get_percentage_for_markerclass('Expansion', perc='marker')]
                                  ]

    mtp.draw_barchart_subplots("Share of Markertypes in all Markers of a Texttype (%)",
                               [data.news_label, data.discussion_label, data.science_label,
                                data.documentary_label, data.presentation_label],
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               markertype_per_text_perc_m,
                               [markertypes.temporal_color, markertypes.contingency_color,
                                markertypes.comparison_color, markertypes.expansion_color],
                               rows=3)

    helpers.DataFrames.markertype_dataframe("05_markertypes_percentage-marker_genre",
                                            [data.news_label, data.discussion_label, data.science_label,
                                             data.documentary_label, data.presentation_label],
                                            markertype_per_text_perc_m,
                                            ["Temporal", "Contingency", "Comparison", "Expansion"]
                                            )

    ''' ---------- MARKER LEVEL -----------'''

    """
    Top 15 Markers per Class per Texttype
    """
    '''Temporal'''
    temporal = [data.news.get_most_common_markers(marker_type="Temporal"),
                data.discussion.get_most_common_markers(marker_type="Temporal"),
                data.science.get_most_common_markers(marker_type="Temporal"),
                data.documentary.get_most_common_markers(marker_type="Temporal"),
                data.presentation.get_most_common_markers(marker_type="Temporal")]

    mc_temporal, values_temporal = hp.most_common_markers_list("01_mc-temp_genre",
                                                               temporal,
                                                               [data.news_label, data.discussion_label,
                                                                data.science_label, data.documentary_label,
                                                                data.presentation_label])

    mtp.horizontal_barchart("Most common Temporal Markers - Share in all Temporal Markers in %",
                            values_temporal, mc_temporal,
                            [data.news_color, data.discussion_color, data.science_color,
                             data.documentary_color, data.presentation_color],
                            [data.news_label, data.discussion_label, data.science_label,
                             data.documentary_label, data.presentation_label],
                            "Share in all Temporal Markers")

    '''Contingency'''
    contingency = [data.news.get_most_common_markers(marker_type="Contingency"),
                   data.discussion.get_most_common_markers(marker_type="Contingency"),
                   data.science.get_most_common_markers(marker_type="Contingency"),
                   data.documentary.get_most_common_markers(marker_type="Contingency"),
                   data.presentation.get_most_common_markers(marker_type="Contingency")]

    mc_contingency, values_contingency = hp.most_common_markers_list("02_mc-contingency_genre",
                                                                     contingency,
                                                                     [data.news_label, data.discussion_label,
                                                                      data.science_label, data.documentary_label,
                                                                      data.presentation_label])

    mtp.horizontal_barchart("Most common Contingency Markers - Share in all Contingency Markers in %",
                            values_contingency, mc_contingency,
                            [data.news_color, data.discussion_color, data.science_color,
                             data.documentary_color, data.presentation_color],
                            [data.news_label, data.discussion_label, data.science_label,
                             data.documentary_label, data.presentation_label],
                            "Share in all Contingency Markers")

    '''Comparison'''
    comparison = [data.news.get_most_common_markers(marker_type="Comparison"),
                  data.discussion.get_most_common_markers(marker_type="Comparison"),
                  data.science.get_most_common_markers(marker_type="Comparison"),
                  data.documentary.get_most_common_markers(marker_type="Comparison"),
                  data.presentation.get_most_common_markers(marker_type="Comparison")]

    mc_comparison, values_comparison = hp.most_common_markers_list("03_mc-comparison_genre",
                                                                   comparison,
                                                                   [data.news_label, data.discussion_label,
                                                                    data.science_label, data.documentary_label,
                                                                    data.presentation_label])

    mtp.horizontal_barchart("Most common Comparison Markers - Share in all Comparison Markers in %",
                            values_comparison, mc_comparison,
                            [data.news_color, data.discussion_color, data.science_color,
                             data.documentary_color, data.presentation_color],
                            [data.news_label, data.discussion_label, data.science_label,
                             data.documentary_label, data.presentation_label],
                            "Share in all Comparison Markers")

    '''Expansion'''
    expansion = [data.news.get_most_common_markers(marker_type="Expansion"),
                 data.discussion.get_most_common_markers(marker_type="Expansion"),
                 data.science.get_most_common_markers(marker_type="Expansion"),
                 data.documentary.get_most_common_markers(marker_type="Expansion"),
                 data.presentation.get_most_common_markers(marker_type="Expansion")]

    mc_expansion, values_expansion = hp.most_common_markers_list("04_mc-expansion_genre",
                                                                 expansion,
                                                                 [data.news_label, data.discussion_label,
                                                                  data.science_label, data.documentary_label,
                                                                  data.presentation_label])

    mtp.horizontal_barchart("Most common Expansion Markers - Share in all Expansion Markers in %",
                            values_expansion, mc_expansion,
                            [data.news_color, data.discussion_color, data.science_color,
                             data.documentary_color, data.presentation_color],
                            [data.news_label, data.discussion_label, data.science_label,
                             data.documentary_label, data.presentation_label],
                            "Share in all Expansion Markers")


if __name__ == '__main__':
    main()
