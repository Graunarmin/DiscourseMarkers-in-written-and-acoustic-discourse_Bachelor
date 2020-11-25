from datasets import DiscourseTypeData as cd
from classes import MarkerTypes as mt
from plotting import MarkerTypePlots as mtp


def main():
    markertypes = mt.MarkerTypes(
        "../../data/listenability-tools/main-senses/words_main-sense.json")

    data = cd.DiscourseTypeData(
        "../../bigData/listenability-tools/discourse-types/dict/spotify-dict.json",
        "../../bigData/listenability-tools/discourse-types/dict/ted-dict.json",
        "../../bigData/listenability-tools/discourse-types/dict/nytimes-dict.json",
        "../../bigData/listenability-tools/discourse-types/dict/gigaword-dict.json",
        markertypes=markertypes)

    '''
    01: Durchschnittliches Vorkommen jedes Markertypes pro Textsorte (in %)
    '''
    markertype_per_text_percent = []

    mtp.draw_barchart_subplots("Average Occurence of Markertypes per Text in %",
                               ["Temporal", "Contingency", "Comparison", "Expansion"],
                               [data.spotify_label, data.ted_label, data.ny_label, data.gig_label],
                               markertype_per_text_percent,
                               [data.spotify_color, data.ted_color, data.ny_color, data.gig_color])

    '''
   02: Durchschnittliches Vorkommen jedes Markertypes pro Textsorte (total)
   '''


if __name__ == '__main__':
    main()
