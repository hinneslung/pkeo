import numpy as np
import pandas as pd

edge_df = pd.read_csv('./edges.csv')

result_df = edge_df.loc[(edge_df.Ccode != edge_df.Ccode2) & (edge_df.Side != edge_df.Side2)]
result_df.to_csv('./edges2.csv')
