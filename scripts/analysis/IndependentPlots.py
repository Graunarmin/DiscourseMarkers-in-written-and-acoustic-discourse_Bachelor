import helpers.DataFrames
from classes import MarkerTypes as mt
from plotting import MarkerTypePlots as mtp
from helpers import Helpers as hp


def main():
    markertypes = mt.MarkerTypes("../../data/listenability-tools/main-senses/words_main-sense.json")

    markertypes_per_type = markertypes.get_number_of_markers()
    mtp.draw_barchart(markertypes_per_type,
                      "Total Number of Markers for each Markertype",
                      ["Temporal", "Contingency", "Comparison", "Expansion"],
                      [markertypes.temporal_color, markertypes.contingency_color,
                       markertypes.comparison_color, markertypes.expansion_color],
                      "Total Number of Markers"
                      )

    helpers.DataFrames.markertype_dataframe("markers-per-type",
                                            ["Temporal", "Contingency", "Comparison", "Expansion"],
                                            markertypes_per_type,
                                            [""])


if __name__ == '__main__':
    main()
