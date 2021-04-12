<br>

## Risk

About the [National Air Toxics Assessment](https://www.epa.gov/national-air-toxics-assessment) of the United 
States [Environmental Protection Agency](https://www.epa.gov/)

<br>

### Development Environment

In preparation for Docker, etc.

<br>

#### Anaconda

Refer to [spots](https://github.com/vetiveria/spots#development-environment)

<br>

#### Requirements

In relation to requirements.txt

```markdown
    pip freeze -r docs/filter.txt > requirements.txt
```

<br>

#### Conventions

```markdown
    pylint --generate-rcfile > .pylintrc
```

<br>
<br>

### Notes

#### Exploring Underlying Concentrations

Examples:

* concentrations.ipynb <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vetiveria/risk/blob/develop/notebooks/concentrations.ipynb)

<br>

#### Pollutants Data

* base/root: https://www.epa.gov/sites/production/files/2018-08/nata2014v2_national_

  * cancerrisk_by_tract_poll.xlsx  
  * resphi_by_tract_poll.xlsx  
  * neurhi_by_tract_poll.xlsx  
  * liverhi_by_tract_poll.xlsx  
  * kidnhi_by_tract_poll.xlsx  
  * immuhi_by_tract_poll.xlsx

<br>

#### Risk Groups Data

* base/root: https://www.epa.gov/sites/production/files/2018-08/nata2014v2_national_

  * cancerrisk_by_tract_srcgrp.xlsx  
  * resphi_by_tract_srcgrp.xlsx  
  * neurhi_by_tract_srcgrp.xlsx  
  * liverhi_by_tract_srcgrp.xlsx  
  * kidnhi_by_tract_srcgrp.xlsx  
  * immuhi_by_tract_srcgrp.xlsx
