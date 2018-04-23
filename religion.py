import numpy as np
import pandas as pd


f = {
    'Ccode': ['first'],
    'Nation': ['first'],

    'Christianity': ['mean'],
    'Judaism': ['mean'],
    'Islam_Sunni': ['mean'],
    'Islam_Shia': ['mean'],
    'Islam': ['mean'],
    'Buddhism': ['mean'],
    'Zoroastrian': ['mean'],
    'Hindu': ['mean'],
    'Sikh': ['mean'],
    'Shinto': ['mean'],
    'Bahai': ['mean'],
    'Taoism': ['mean'],
    'Jain': ['mean'],
    'Confucianism': ['mean'],
    'Syncretic': ['mean'],
    'Animist': ['mean'],

    'Non': ['mean'],
    'Other': ['mean'],
}

df = pd.read_csv('./religion.csv')
grouped = df.groupby(['Ccode'])
aggregated = grouped.agg(f)

for row in aggregated:
    print(row)

aggregated.to_csv('./state-religion.csv')
