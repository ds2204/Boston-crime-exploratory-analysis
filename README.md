# Boston Crime and Exploratory Data Analysis

Maintained for **ds2204**. This collection contains three supplied coursework analyses: Boston police offense records, Walmart weekly sales, and Netflix historical prices. Original coursework attribution is retained in [ATTRIBUTION.md](ATTRIBUTION.md); this is not a claim of sole authorship.

## Contents and execution

- [Boston notebook](boston_crime_analysis.ipynb): combines four annual CSV files, examines offense categories, streets, shooting flags, seasonality, and UCR reporting categories.
- [Walmart notebook](walmart_sales_analysis.ipynb): descriptive sales totals and highest-sales store/month pairs.
- [Netflix notebook](netflix_stock_analysis.ipynb): uses the supplied historical CSV offline; calculates chronological daily returns and monthly volume.
- Original PDF/DOCX reports remain as historical records. Their names and author credits are preserved. They may contain conclusions or code screenshots superseded by the corrected notebooks.

Use Python 3.12 and run from this directory:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

Open each notebook and Run All. No personal drive paths or live web access are required. Original data files are byte-for-byte preserved. The notebooks now use `pd.concat`, portable paths, and chronological returns. Optional original web acquisition is provided in [fetch_netflix.py](fetch_netflix.py); the historical website layout may change.

## Data and interpretation

The four crime CSVs contain 353,253 offense rows before deduplication, covering 2015–2018. One incident may have multiple offenses. Missing shooting flags remain unknown. Street counts are not population-adjusted safety scores. The 2015 record begins mid-year, so raw annual totals are not like-for-like crime-rate comparisons.

Walmart contains 6,435 store-week rows; the first and last years have incomplete coverage. Annual totals are descriptive, not normalized growth rates. Netflix contains 244 historical rows; the snapshot is not a current market feed, and share volume does not measure the number of traders.

Dataset references are retained from the supplied reports: [Walmart source](https://www.kaggle.com/datasets/rutuspatel/walmart-dataset-retail), Boston source references in the original project report, and the FinancialContent URL in the Netflix notebook. Redistribution terms were not supplied for the datasets; confirm them before public release.

See [AUDIT.md](AUDIT.md) for file-by-file disposition and test limitations. No license was included; do not assume permission to relicense the coursework or reports.

Run `python validate_notebooks.py` for offline sequential cell execution and saved plots. Reproduced plots are in [figures/](figures/); validation outputs go to ignored `artifacts/`.
