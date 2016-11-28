import pandas as pd
import numpy as np
from pandas.tools.plotting import scatter_matrix

df = pd.read_csv(r'features.csv', header = None)
scatter_matrix(df, alpha=0.5, figsize=(12, 12), diagonal='kde')
