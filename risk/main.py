import os
import sys

import logging
import collections


def main():

    # Prepare the directories
    directories.cleanup(listof=[configurations.warehouse])
    directories.create(listof=[configurations.warehouse])

    # Example
    url = 'https://www.epa.gov/sites/production/files/2018-08/nata2014v2_national_neurhi_by_tract_poll.xlsx'
    descriptor = 'neurologicalIndexPollutants'

    # Hence
    data = estimates.exc(url=url)
    logger.info(data.info())

    # Update old geographic codes
    data = updates.exc(blob=data.copy(), identifiers=configurations.identifiers)

    # A number of the field names are pollutant names, but not all the names are standard names.  The
    # pollutants function returns a DataFrame of mapped names wherein the field 'chemical' always has
    # the standard names.  This ensures the retrievability of each pollutant's chemical identification code.
    toxins = pollutants.exc(compounds=list(data.columns[5:]))

    # ... retrieve each pollutant's chemical identification code
    toxins = toxins.merge(chemicals.exc(), how='left', on='chemical')

    # ... the mapping of pollutant field name & chemical identification code; dictionary form
    mappings = toxins[['field', 'tri_chem_id']].set_index(keys='field', drop=True, inplace=False)\
        .to_dict(orient='dict')['tri_chem_id']

    # Hence, rename the pollutant fields
    data.rename(columns=mappings, inplace=True)
    collections.namedtuple(typename='Files', field_names=['data', ''])


if __name__ == '__main__':

    # Root
    root = os.getcwd()
    sys.path.append(root)

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Configurations
    import config

    configurations = config.Config()

    # Libraries
    import risk.functions.directories
    import risk.algorithms.estimates
    import risk.algorithms.pollutants
    import risk.algorithms.chemicals
    import risk.geography.updates

    directories = risk.functions.directories.Directories()
    estimates = risk.algorithms.estimates.Estimates()
    pollutants = risk.algorithms.pollutants.Pollutants(synonyms=configurations.synonyms)
    chemicals = risk.algorithms.chemicals.Chemicals()
    updates = risk.geography.updates.Updates()

    main()
