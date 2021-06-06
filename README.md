<br>

About the [National Air Toxics Assessment](https://www.epa.gov/national-air-toxics-assessment) of the United 
States [Environmental Protection Agency](https://www.epa.gov/)

<br>

* [Development Environment](#development-environment)
* [Notes](#notes)

<br>

## Development Environment

Locally, it uses the development environment `environment`; the environment is detailed within [spots](https://github.
com/vetiveria/spots#development-environment).  The `requirements.txt` file is created via

```shell
    pip freeze -r docs/filter.txt > requirements.txt
```

And, `.pylintrc` is created via command

```shell
    pylint --generate-rcfile > .pylintrc
```

<br>
<br>

## Notes


### Exploring the Underlying Concentrations

The concentration measures, estimates, per tract can be explored via chemical database files.  For each toxic chemical tracked by the Environmental Protection Agencythe Agency provides a concentrations database file.  The `concentrations` notebook illustrates how such files can be queried via Python:

* concentrations.ipynb <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vetiveria/risk/blob/develop/notebooks/concentrations.ipynb)

<br>

### Pollutants Data

* base/root: https://www.epa.gov/sites/production/files/2018-08/nata2014v2_national_

  * cancerrisk_by_tract_poll.xlsx  
  * resphi_by_tract_poll.xlsx  
  * neurhi_by_tract_poll.xlsx  
  * liverhi_by_tract_poll.xlsx  
  * kidnhi_by_tract_poll.xlsx  
  * immuhi_by_tract_poll.xlsx

<br>

### Risk Groups Data

* base/root: https://www.epa.gov/sites/production/files/2018-08/nata2014v2_national_

  * cancerrisk_by_tract_srcgrp.xlsx  
  * resphi_by_tract_srcgrp.xlsx  
  * neurhi_by_tract_srcgrp.xlsx  
  * liverhi_by_tract_srcgrp.xlsx  
  * kidnhi_by_tract_srcgrp.xlsx  
  * immuhi_by_tract_srcgrp.xlsx
