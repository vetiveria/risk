import pandas as pd


class Pollutants:
    """
    Class Pollutants

    """

    def __init__(self, synonyms: dict):
        """
        Constructor

        :param synonyms: A mapping of source & standard chemical names for cases wherein the
                         source does not use a standard name.  Hereafter, standard names can
                         be used to extract Chemical Abstract Service registry numbers.
        """

        self.synonyms = synonyms

    def analogue(self, key):
        """

        :param key: The dictionary key, which must be the name of a chemical according to a source
        :return:
        """

        return self.synonyms[key]

    def exc(self, compounds: list):
        """

        :param compounds: The names of the chemicals according to the data source
        :return:
        """

        analogues = {compound: self.analogue(compound) if compound in self.synonyms.keys() else compound
                     for compound in compounds}

        names = pd.DataFrame.from_dict(data=analogues, orient='index', columns=['chemical'])
        names.reset_index(drop=False, inplace=True)
        names.columns = ['field', 'chemical']

        return names
