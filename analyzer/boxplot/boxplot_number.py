import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

country_list = ['AU', 'CA', 'CH', 'GE', 'IN', 'JP', 'KR', 'UK', 'US', 'total']
#country_list = ['total']
for c in country_list:
    for n_s in ['number', 'size']: # plot for object number or size
        for ad in ['without_ad_block', 'with_ad_block']:

            data = pd.DataFrame.from_csv('../../data/{}/{}_total.txt'.format(c, ad), sep='\t')

            type_list = ['image', 'javascript', 'css',
                        'html', 'audio', 'video',
                        'xml', 'others_app', 'others_text']

            if n_s == 'size':
                var_list = [i+'_size' for i in type_list]
                for col in var_list:
                    data[col] = data[col] / (data['total_size'].astype(float) + data['others_app_size'] + data['others_text_size'])
            elif n_s == 'number':
                var_list = [i+'_number' for i in type_list]
                for col in var_list:
                    data[col] = data[col] / (data['total_number'].astype(float) + data['others_app_number'] + data['others_text_number'])


            fig = plt.figure('{0}_{1}: {2}'.format(c, type, ad))
            plt.boxplot(data[var_list].as_matrix())
            plt.xticks(range(1,len(type_list)+1), type_list, rotation=-45)
            plt.ylabel('Fraction of Object {}'.format(n_s.upper()))
            plt.ylim([0,1.0])
            plt.title('Country: {0}  ({1})\nDistribution for the Fraction of Object {2}'.format(c, ad, n_s.upper()))
            plt.tight_layout()
            fig.savefig('{0}/{1}_{2}.png'.format(c, ad, n_s))
            plt.close()