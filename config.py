import os


class Config:

    def __init__(self):
        """
        Constructor

        """

        self.unresolved = ['diesel pm',  'hexamethylene diisocyanate', 'isophorone', 'coke oven emissions', 'ethyl carbamate (urethane) chloride (chloroethane)', 'pahpom']

        self.synonyms = {'cresol_cresylic acid (mixed isomers)': 'cresol (mixed isomers)',
                         'methyl chloride (chloromethane)': 'chloromethane',
                         'xylenes (mixed isomers)': 'xylene (mixed isomers)',
                         'hexane': 'n-hexane',
                         '1,2-epoxybutane': '1,2-butylene oxide',
                         '1,3-dichloropropene': '1,3-dichloropropylene',
                         '2,4-toluene diisocyanate': 'toluene-2,4-diisocyanate',
                         "4,4'-methylenediphenyl diisocyanate (mdi)": "4,4'-methylenedi(phenyl isocyanate)",
                         'bis(2-ethylhexyl)phthalate (dehp)': 'di(2-ethylhexyl) phthalate',
                         'chromium vi (hexavalent)': 'chromium',
                         'ethylene dibromide (dibromoethane)': '1,2-dibromoethane',
                         'hydrochloric acid (hydrogen chloride [gas only])':
                             'hydrochloric acid (acid aerosols including mists, vapors, gas, fog, and other airborne forms of any particle size)',
                         'methyl bromide (bromomethane)': 'bromomethane',
                         'methylene chloride': 'dichloromethane',
                         'propylene dichloride (1,2-dichloropropane)': '1,2-dichloropropane',
                         '1,2,3,4,5,6-hexachlorocyclyhexane': 'alpha-hexachlorocyclohexane',
                         'ethylene dichloride (1,2-dichloroethane)': '1,2-dichloroethane',
                         'dimethyl formamide': 'n,n-dimethylformamide',
                         'ethylidene dichloride (1,1-dichloroethane)': 'ethylidene dichloride',
                         "4,4'-methylene bis(2-chloroaniline)": "4,4'-methylenebis(2-chloroaniline)",
                         'arsenic compounds(inorganic including arsine)': 'arsenic compounds',
                         'dichloroethyl ether (bis[2-chloroethyl]ether)': 'bis(2-chloroethyl) ether',
                         'hexachlorobutadiene': 'hexachloro-1,3-butadiene',
                         'polychlorinated biphenyls (aroclors)': 'polychlorinated biphenyls',
                         '2,4-toluene diamine': '2,4-diaminotoluene',
                         'toxaphene (chlorinated camphene)': 'toxaphene'}

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

        strings = {node.format('cancerrisk_by_tract_poll.xlsx'): 'cancerRiskPollutants',
                   node.format('resphi_by_tract_poll.xlsx'): 'respiratoryIndexPollutants',
                   node.format('neurhi_by_tract_poll.xlsx'): 'neurologicalIndexPollutants',
                   node.format('liverhi_by_tract_poll.xlsx'): 'liverIndexPollutants',
                   node.format('kidnhi_by_tract_poll.xlsx'): 'kidneyIndexPollutants',
                   node.format('immuhi_by_tract_poll.xlsx'): 'immunologicalIndexPollutants'}

        return strings
