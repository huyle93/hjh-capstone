#Court Documents HJH Capstone UNH

## Table of contents

- [Project Organization](#folder-structure)
- [Developer Note](#developer-note)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)

==============================

The goal of the project is to design a searchable database containing both state and county court records. This database will enable users to perform analysis and find the right attorney.

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── raw            <- The original, immutable data dump from scraping
    │   ├── interim        <- Intermediate data that has been transformed to usable format.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── dataset        <- Storing data such as mongodb, json dataset or sql.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data_retriever           <- Scripts to scrape or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    ├── webapp
    │   ├── restapi        <- JSON RESTful API
    │   └── webapp         <- An app
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


-------------

## Developer Note (Setting up your environment)

- [Using PyCharm](https://www.jetbrains.com/help/pycharm-edu/creating-virtual-environment.html)
- - Highly recommended using PyCharm to create virtualenv and install packages from requirements.txt
---
- [Anaconda-Spyder](https://www.anaconda.com/)
- - Make sure you are using Spyder version >= 3.2.8 (There is a bug from Spyder which causes error to connect to Google API)
- [Python3](https://docs.python.org/3/)
- - This project is written on Python 3 or greater (prefer >= 3.5)
- [nltk](http://www.nltk.org/data.html)
- - nltk "popular" package is required
>``` import nltk ```

>``` nltk.download("popular") ```
- [Google Cloud Language](https://cloud.google.com/docs/authentication/getting-started)
### Set up Google Cloud API Credentials
- 1. You need to request a JSON API key from Huy Le
- 2. Change that JSON file to: ``` cloudPlatform_apiKey.json ```
- 3. Add this to your .bashrc or .zshrc
>``` export GOOGLE_APPLICATION_CREDENTIALS="[PATH_TO_THIS_DIRECTORY]/src/features/cloudPlatform_apiKey.json" ```
- 4. Move the ``` cloudPlatform_apiKey.json ``` to ``` hjh-capstone/src/features/ ```
- DONE
---
### For everything else

>``` pip install -r requirements.txt ```

## Creators

Huy Le (developer), Heli Amin

## Copyright and license

This project is not allowed to use for commercial purposes without permission

<p><small>Project structure based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
