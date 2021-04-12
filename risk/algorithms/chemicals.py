import pandas as pd


class Chemicals:
    """
    Class Chemicals
    """

    def __init__(self):
        """
        Constructor

        """

        self.url = "https://raw.githubusercontent.com/vetiveria/spots/develop/resources/references/" \
                   "chemicalsEnvirofacts.csv"

        self.usecols = ["TRI_CHEM_INFO.TRI_CHEM_ID",	"TRI_CHEM_INFO.CHEM_NAME", "TRI_CHEM_INFO.CAAC_IND",
                        "TRI_CHEM_INFO.CARC_IND", "TRI_CHEM_INFO.R3350_IND"]

        self.dtype = {"TRI_CHEM_INFO.TRI_CHEM_ID": str, "TRI_CHEM_INFO.CHEM_NAME": str,
                      "TRI_CHEM_INFO.CAAC_IND": int, "TRI_CHEM_INFO.CARC_IND": int,
                      "TRI_CHEM_INFO.R3350_IND": int}

        self.rename = ["tri_chem_id", "chemical", "air_pollutant", "carcinogenic", "R3350_pollutant"]

    def read(self) -> pd.DataFrame:
        """

        :return:
        """

        try:
            data = pd.read_csv(filepath_or_buffer=self.url, header=0, usecols=self.usecols,
                               dtype=self.dtype, encoding='utf-8')
        except OSError as err:
            raise Exception(err.strerror) in err

        return data

    def exc(self):
        """

        :return:
        """

        data = self.read()
        data.columns = self.rename
        data.loc[:, 'chemical'] = data['chemical'].str.lower()

        return data
