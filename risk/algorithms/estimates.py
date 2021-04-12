import pandas as pd
import collections


# noinspection PyUnresolvedReferences,PyProtectedMember
class Estimates:

    def __init__(self):
        """
        Constructor

        """

        Fields = collections.namedtuple(typename='Fields', field_names=['rename', 'drop'])
        self.fields = Fields._make((
            {'State': 'stusps', 'County': 'county', 'FIPS': 'countygeoid', 'Tract': 'tractgeoid'},
            ['EPA Region', 'county']))

    def read(self, url: str):
        """

        :param url:
        :return:
        """

        try:
            data = pd.read_excel(io=url, header=0, sheet_name=0, dtype={'FIPS': str, 'Tract': str})
        except OSError as err:
            raise Exception(err.strerror) in err

        data.rename(columns=self.fields.rename, inplace=True)
        data.drop(columns=self.fields.drop, inplace=True)

        return data

    def exc(self, url):
        """

        :param url:
        :return:
        """

        estimates = self.read(url)
        estimates.rename(str.strip, axis=1, inplace=True)
        estimates.rename(str.lower, axis=1, inplace=True)

        return estimates
