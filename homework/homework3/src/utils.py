import pandas as pd
import numpy as np

def get_summary_stats(df):
    
    # Numeric summary
    describe_stats = df.describe(include=[np.number]).to_dict()

    # Groupby aggregation
    by_category = (
        df.groupby("category")
          .agg(
              n_rows=("quantity", "size"),
              avg_price=("price_usd", "mean"),
              total_quantity=("quantity", "sum"),
              total_revenue=("revenue_usd", "sum")
          )
          .reset_index()
          .to_dict(orient="records")
    )

    return {"describe": describe_stats,"by_category": by_category}