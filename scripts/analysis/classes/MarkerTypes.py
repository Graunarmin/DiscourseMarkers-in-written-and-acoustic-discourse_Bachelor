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

    def get_number_of_markers(self):

        temporal, contingency, comparison, expansion = 0, 0, 0, 0
        type_dict = self.get_type_dict()
        for marker in type_dict:
            if type_dict[marker] == 'Temporal':
                temporal += 1
            elif type_dict[marker] == 'Contingency':
                contingency += 1
            elif type_dict[marker] == 'Comparison':
                comparison += 1
            elif type_dict[marker] == 'Expansion':
                expansion += 1

        return temporal, contingency, comparison, expansion
