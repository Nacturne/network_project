import pandas as pd
data = pd.DataFrame.from_csv('data/median_stats.txt', sep='\t')
data.drop(data.index[[184, 343, 386, 255]], inplace=True)
data.to_csv('data/valid_stats.txt',  sep='\t')