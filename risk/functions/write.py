import os

import pandas as pd

import config


class Write:

    def __init__(self):
        """

        """

        configurations = config.Config()
        self.warehouse = configurations.warehouse

    def save(self, blob: pd.DataFrame, basename: str):
        """

        :param blob:
        :param basename:
        :return:
        """

        blob.to_csv(path_or_buf=os.path.join(self.warehouse, basename),
                    header=True, index=False, encoding='utf-8')

    def exc(self, data: pd.DataFrame, toxins: pd.DataFrame, label: str):
        """

        :param data: A wide format frame of pollutant risks per tract
        :param toxins: An inventory of the pollutants and their Chemical Abstracts Service Registry Number
        :param label: A label for naming the data & toxins files
        :return:
        """

        self.save(blob=data, basename='{}NATA2014V2.csv'.format(label))
        self.save(blob=toxins, basename='{}Names.csv'.format(label))
