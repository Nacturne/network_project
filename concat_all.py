import pandas as pd


df_list = []
df_block_list = []

contry_list = [ 'AU', 'CA', 'CH', 'GE', 'IN', 'JP', 'KR', 'UK', 'US']

#contry_list = [ 'AU', 'CA', 'CH']

for c in contry_list:
    df = pd.DataFrame.from_csv('data/{}/without_ad_block_total.txt'.format(c), sep='\t')
    df_block = pd.DataFrame.from_csv('data/{}/with_ad_block_total.txt'.format(c), sep='\t')

    index_1 = df.index.tolist()
    index_2 = df_block.index.tolist()

    index_list = list(set(index_1).intersection(index_2))

    print('{0}:  {1}'.format(c, len(index_list)))



    df = df.loc[index_list].copy()
    df_list.append(df)

    df_block = df_block.loc[index_list].copy()
    df_block_list.append(df_block)


total_df = df_list[0].copy()
for frame in df_list[1:]:
    total_df = pd.concat([total_df, frame]).copy()
total_df.to_csv('data/total/without_ad_block_total.txt', sep='\t')

total_df_block = df_block_list[0].copy()
for frame in df_block_list[1:]:
    total_df_block = pd.concat([total_df_block, frame]).copy()
total_df_block.to_csv('data/total/with_ad_block_total.txt', sep='\t')

print(total_df_block.columns)
print(total_df.columns)
