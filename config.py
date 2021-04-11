import os


class Config:

    def __init__(self):
        """
        Constructor

        """

        self.synonyms = {'cresol_cresylic acid (mixed isomers)': 'cresol (mixed isomers)',
                         'methyl chloride (chloromethane)': 'chloromethane',
                         'xylenes (mixed isomers)': 'xylene (mixed isomers)',
                         'hexane': 'n-hexane'}

        self.identifiers = {'46113': '46102', '02270': '02158'}

        self.warehouse = os.path.join(os.getcwd(), 'warehouse')

    @staticmethod
    def source() -> dict:
        """
        node = 'https://www.epa.gov/sites/production/files/2018-08/nata2014v2_national'
        'node{}'.format(...)

        :return:
        """

        node = 'https://www.epa.gov/sites/production/files/2018-08/nata2014v2_national_{}'

        strings = {node.format('cancerrisk_by_tract_srcgrp.xlsx'): 'cancerRiskSource',
                   node.format('cancerrisk_by_tract_poll.xlsx'): 'cancerRiskPollutants',
                   node.format('resphi_by_tract_srcgrp.xlsx'): 'respiratoryIndexSource',
                   node.format('resphi_by_tract_poll.xlsx'): 'respiratoryIndexPollutants',
                   node.format('neurhi_by_tract_srcgrp.xlsx'): 'neurologicalIndexSource',
                   node.format('neurhi_by_tract_poll.xlsx'): 'neurologicalIndexPollutants',
                   node.format('liverhi_by_tract_srcgrp.xlsx'): 'liverIndexSource',
                   node.format('liverhi_by_tract_poll.xlsx'): 'liverIndexPollutants',
                   node.format('kidnhi_by_tract_srcgrp.xlsx'): 'kidneyIndexSource',
                   node.format('kidnhi_by_tract_poll.xlsx'): 'kidneyIndexPollutants',
                   node.format('immuhi_by_tract_srcgrp.xlsx'): 'immunologicalIndexSource',
                   node.format('immuhi_by_tract_poll.xlsx'): 'immunologicalIndexPollutants'}

        return strings
