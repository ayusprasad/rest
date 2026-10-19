# Restaurant Review and Sentiment Analysis

[![CI](https://github.com/ayusprasad/rest/actions/workflows/ci.yml/badge.svg)](https://github.com/ayusprasad/rest/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Data-pandas-150458?logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Analysis-Jupyter-F37626?logo=jupyter&logoColor=white)

Two Jupyter notebooks explore restaurant-review data, sentiment features, rating distributions, and business/user patterns.

## Notebooks

- restaurant_feature_engineering.ipynb builds derived review and sentiment features.
- restaurant_review_analysis.ipynb explores distributions, relationships, clustering, and profiling.

## Local setup

### Prerequisites

- Python 3.11 or newer
- JupyterLab or Jupyter Notebook
- The source CSV dataset, placed at data/restaurants.csv

### Install

~~~bash
git clone https://github.com/ayusprasad/rest.git
cd rest
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab notebooks
~~~

The notebooks validate that data/restaurants.csv exists before loading it. Generated engineered data is written under data/processed/. The CSV itself is intentionally excluded from Git.

## Quality checks

~~~bash
python -m pytest -q
~~~

GitHub Actions checks notebook structure and validates the JSON files without needing the dataset. No environment variables are required.
