import pandas as pd


class Updates:

    def __init__(self):
        """

        """

    @staticmethod
    def tract(series: pd.Series, initial: str, latest: str):
        """
        The county & tract GEOID update function.

        :param series:
        :param initial:
        :param latest:
        """

        return series.replace(to_replace='^({})'.format(initial), value=latest, regex=True)

    def exc(self, blob: pd.DataFrame, identifiers: dict):
        """

        :param blob:
        :param identifiers:
        :return:
        """

        for initial, latest in identifiers.items():

            indices: pd.Series = blob['countygeoid'] == initial
            if not indices.any():
                continue
            else:
                excerpt = blob.loc[indices].copy()
                excerpt.loc[:, 'countygeoid'] = latest
                excerpt.loc[:, 'tractgeoid'] = self.tract(series=excerpt['tractgeoid'], initial=initial, latest=latest)
                blob.loc[indices, :] = excerpt.values

        return blob
