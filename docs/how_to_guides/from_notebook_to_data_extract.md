## Using a notebook / jupyter lab

Once you have the notebook or lab working your view should look something like this (lab displayed below). You need nothing else to run the pipeline.

![Jupyter Lab](/how_to_guides/notebook.jpg)

If you don't have a strong preference I recommend using the lab as it has more features and provides a very satisfactory browser based programming environment completely for free on almost any machine.

## Why a notebook?

Data based projects tend to be very iterative. Notebooks although terrible for production allow a lot of experimentation and testing which is what is needed while learning. They allow us here to strike an optimal balance between all the sites as they minimise the need for software engineering skill while maximising results and visibility for the analyst.

## Opening a notebook

First navigate to the data extraction folder. Then open the data extraction notebook - `data_extraction.ipynb`

It should look something like this:

![Extraction](/how_to_guides/extraction.jpg)

## Importing packages

In order to use the notebook you need to first import the packages. This is done in the first line of the notebook with the lines:

```python
import numpy as np
import pandas as pd

import avoidable_admissions as aa
```

if this doesn't work it is because python can't find the avoidable admissions package inside the repository. A quick way to fix this is to copy this into the data_extraction folder but if you ran through the previous steps in order it should work as the setup.py file looks for this at install and logs its location so python can find it.

The other way to solve the problem is too complicated for the scope of this guide so I recommend copying needed modules into the same root folder as the notebook for now. The priority here is to get going not have a perfect folder structure.
