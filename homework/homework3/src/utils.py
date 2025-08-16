import pandas as pd
import numpy as np

def get_summary_stats(df):
    
    # Numeric summary
    describe_stats = df.describe(include=[np.number]).to_dict()

    # Groupby aggregation
    by_category = (
        df.groupby("category")
          .agg(

              avg_val=("value", "mean")
          )
          .reset_index()
          .to_dict(orient="records")
    )

    return {"describe": describe_stats,"by_category": by_category}