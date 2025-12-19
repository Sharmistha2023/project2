import pandas as pd
import logging
df = pd.read_csv('/mnt/in/Algerian_forest_fires_dataset_CLEANED.csv')
with open('/mnt/in/Algerian_forest_fires_dataset_CLEANED.csv', 'r') as f:
    print(f.read(500))
logging.info(f"DF Columns: {list(df.columns)}")
print(f"df columns: {df.columns}")
df.columns
df.drop(['day','month','year'], axis=1, inplace=True)
df.to_csv('/mnt/ou/Algerian_forest_fires_dataset_CLEANED_NEW.csv', index=False)
print("New CSV file saved!")
