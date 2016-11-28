import csv
import json
import pandas as pd

with open('xaa.json', 'rb') as f:
    data = f.readlines()

data = map(lambda x: x.rstrip(), data)

data_json_str = "[" + ','.join(data) + "]"

# now, load it into pandas
data_df = pd.read_json(data_json_str)

print data_df

data_df.to_csv('jsoncsv.csv',encoding='utf-8')