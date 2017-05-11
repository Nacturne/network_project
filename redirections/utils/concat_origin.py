import pandas as pd

country_list = [ 'AU', 'CA', 'CH', 'GE', 'IN', 'JP', 'KR', 'UK', 'US']



df_list = []
for c in country_list:
    df = pd.read_csv('../Data/{}/origin_fraction.txt'.format(c),
                     names=['byte', 'objetc_number', 'loadtime'],
                     )
    df_list.append(df.copy())



total_df = df_list[0]
for frame in df_list[1:]:
    total_df = pd.concat([total_df, frame]).copy()
total_df.to_csv('../Data/total/origin_fraction.txt', sep='\t')


print(total_df.columns)