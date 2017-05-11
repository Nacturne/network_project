import pandas as pd

country_list = [ 'AU', 'CA', 'CH', 'GE', 'IN', 'JP', 'KR', 'UK', 'US']



df_list = []
for c in country_list:
    df = pd.read_csv('../Data/{}/redirect_code.txt'.format(c),
                     names=['301', '302', '303', '307'],
                     index_col=0)
    df_list.append(df.copy())



total_df = df_list[0]
for frame in df_list[1:]:
    total_df = pd.concat([total_df, frame]).copy()
total_df.to_csv('../Data/total/redirect_code.txt', sep='\t')


print(total_df.columns)