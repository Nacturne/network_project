import pandas as pd

c = 'IN'
block_flag = False

if block_flag:
    ad = 'with_ad_block'
else:
    ad = 'without_ad_block'

median_data = pd.DataFrame.from_csv('data/{}/{}_main.txt'.format(c, ad), sep='\t')
red_data = pd.DataFrame.from_csv('data/{}/{}_others.txt'.format(c, ad), sep='\t')

result = pd.merge(median_data, red_data, left_index=True, right_index=True, how='inner')

result.to_csv('data/{}/{}_total.txt'.format(c, ad), sep='\t')