## Data preprocessing
- After loading the raw data, we observed that there were some missing values. We cleaned the data by utilizing the functions imported from `cleaning.py`.
- We first used `fill_missing_median` for the numerical rows and normalized them by `normalize_data`. We then applied `drop_missing` to drop missing values (if any).
- Finally, we saved the cleaned dataset to `/data/processed/`.