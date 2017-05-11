import numpy as np
import pandas as pd

from utils.HAR import HAR


def har_stats(har):
    type_list = ['image',
                 'javascript',
                 'css',
                 'html',
                 'xml',
                 'audio',
                 'video']


    result = {'others_app_size': 0, 'others_app_number': 0,
              'others_text_size': 0, 'others_text_number': 0}

    for entry in har.entries:
        mime_type = entry['response']['content']['mimeType']
        size = entry['response']['bodySize']

        flag = False
        for t in type_list:
            if t in mime_type:
                flag = True
        if not flag:
            if 'application' in mime_type:
                result['others_app_size'] = result['others_app_size'] + size
                result['others_app_number'] = result['others_app_number'] + 1
            elif 'text' in mime_type:
                result['others_text_size'] = result['others_text_size'] + size
                result['others_text_number'] = result['others_text_number'] + 1

    return result





def get_stats_others(folder_in, web_number, group_number):
    data_results = pd.DataFrame(columns=['others_app_size', 'others_app_number',
                                         'others_text_size', 'others_text_number'])


    for web_index in range(web_number):
        print(web_index)
        temp = {'others_app_size': [], 'others_app_number': [],
                'others_text_size': [], 'others_text_number': []}


        for group_index in range(group_number):
            file_name = folder_in + 'group{0}/{1}_{2}.har'.format(group_index, group_index, web_index)
            #flie_name = 'har_files/Japan/without_ad_block/group{0}/{1}_{2}.har'.format(group_index, group_index, web_index)

            try:
                har = HAR(file_name)
            except:
                # if the har file is missing, skip it.
                continue

            stats = har_stats(har=har)

            # append stats data to the temp dict of lists
            temp['others_app_size'].append(stats['others_app_size'])
            temp['others_text_size'].append(stats['others_text_size'])
            temp['others_app_number'].append(stats['others_app_number'])
            temp['others_text_number'].append(stats['others_text_number'])


        # take the median value of all the data and store it in the dataframe
        for item in temp.keys():
            if not temp[item]:
                print(web_index)
            data_results.set_value(web_index, item, np.median(temp[item]))

    return data_results


def get_types(folder_in, web_number, group_number):
    type_list = ['image',
                 'javascript',
                 'css',
                 'html',
                 'xml',
                 'xml',
                 'audio',
                 'video']

    type_set = set([])
    for web_index in range(web_number):
        for group_index in range(group_number):
            file_name = folder_in + 'group{0}/{1}_{2}.har'.format(group_index, group_index, web_index)
            #flie_name = 'har_files/Japan/without_ad_block/group{0}/{1}_{2}.har'.format(group_index, group_index, web_index)

            try:
                har = HAR(file_name)
            except:
                # if the har file is missing, skip it.
                continue

            for entry in har.entries:
                mime_type = entry['response']['content']['mimeType']

                flag = False
                for t in type_list:
                    if t in mime_type:
                        flag = True
                if not flag:
                    type_set.add(mime_type)



    return type_set