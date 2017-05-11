import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

c = 'US'

for type in ['number', 'size']:
    for block_flag in [True, False]:

        #type = 'number'

        #block_flag = False

        if block_flag:
            ad = 'with_ad_block'
        else:
            ad = 'without_ad_block'

        data = pd.DataFrame.from_csv('data/{}/{}_total.txt'.format(c, ad), sep='\t')
        #data.drop(data.index[[184,343,386, 255]], inplace=True)

        #data.to_csv('data/valid_stats.txt', sep='\t')

        if type == 'size':
            var_list = ['image_size', 'javascript_size', 'css_size',
                        'html_size', 'audio_size', 'video_size',
                        'xml_size', 'others_app_size', 'others_text_size']
        elif type == 'number':
            var_list = ['image_number', 'javascript_number', 'css_number',
                        'html_number', 'audio_number', 'video_number',
                        'xml_number', 'others_app_number', 'others_text_number']

        if type == 'size':
            for col in var_list:
                data[col] = data[col] / (data['total_size'].astype(float) + data['others_app_size'] + data['others_text_size'])
        elif type == 'number':
            for col in var_list:
                data[col] = data[col] / (data['total_number'].astype(float) + data['others_app_number'] + data['others_text_number'])


        plt.figure('{0}_{1}: {2}'.format(c, type, ad))
        plt.boxplot(data[var_list].as_matrix())
        plt.xticks(range(1,len(var_list)+1), var_list)
        plt.ylabel('Fraction of Object Size')
        plt.ylim([0,1.0])
        plt.title('Distribution for the Fraction of Object Size')


plt.show()