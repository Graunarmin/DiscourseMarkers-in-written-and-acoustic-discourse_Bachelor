import json


class MarkerTypes:

    def __init__(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as datafile:
            self.data = json.load(datafile)

        self.temporal_color = '#f4d078'
        self.contingency_color = '#ec6262'
        self.comparison_color = '#8aa8bf'
        self.expansion_color = '#A8BF8A'

    def get_type_dict(self):
        """
        Creates and returns a dictionary with the markers as keys
        and their main-sense as values
        :return: a dictionary with the markers as keys and their main-sense as values
        """
        markers = {}
        for marker in self.data:
            markers[marker] = self.data[marker]['main_sense']
        return markers

    def get_marker_type(self, marker):
        """
        Gets the type (main-sense) of the specified marker
        :param marker: the marker of which to get the type
        :return:
        """
        return self.data[marker]['main_sense']

    def get_all_types(self, marker):
        """
        Returns a list of all types this marker can have
        :param marker:
        :return:
        """
        return self.data[marker]['senses']

    def get_error_rate(self, marker):
        """
        Gets the error rate when using the main-sense of the specified marker
        :param marker:
        :return:
        """
        return self.data[marker]['error_rate']
