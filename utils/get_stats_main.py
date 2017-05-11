import numpy as np
import pandas as pd

from utils.HAR import HAR


def har_stats(har):
    size_dict = {'image': 0,
                 'javascript': 0,
                 'css': 0,
                 'html': 0,
                 'xml': 0,
                 'audio': 0,
                 'video': 0}

    number_dict = {'image': 0,
                   'javascript': 0,
                   'css': 0,
                   'html': 0,
                   'xml': 0,
                   'audio': 0,
                   'video': 0}

    for entry in har.entries:
        mime_type = entry['response']['content']['mimeType']
        size = entry['response']['bodySize']

        for t in size_dict.keys():
            if t in mime_type:
                size_dict[t] = size_dict[t] + size
                number_dict[t] = number_dict[t] + 1


    return {'size_dict': size_dict,
            'number_dict': number_dict,
            'load_time': har.loadtime(),
            'server_number': har.server_number(),
            'service_number': har.service_number()}



def get_stats_main(folder_in, web_number, group_number):
    data_results = pd.DataFrame(columns=['image_size',
                                         'javascript_size',
                                         'css_size',
                                         'html_size',
                                         'xml_size',
                                         'audio_size',
                                         'video_size',
                                         'image_number',
                                         'javascript_number',
                                         'css_number',
                                         'html_number',
                                         'xml_number',
                                         'audio_number',
                                         'video_number',
                                         'load_time',
                                         'load_time_std',
                                         'server_number',
                                         'service_number'])


    for web_index in range(web_number):
        print(web_index)
        temp = {'image_size': [],
                 'javascript_size': [],
                 'css_size': [],
                 'html_size': [],
                'xml_size': [],
                 'audio_size': [],
                 'video_size': [],
                 'image_number': [],
                 'javascript_number': [],
                 'css_number': [],
                 'html_number': [],
                'xml_number': [],
                 'audio_number': [],
                 'video_number': [],
                 'load_time': [],
                 'server_number': [],
                 'service_number': []
                }


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
            temp['load_time'].append(stats['load_time'])
            temp['server_number'].append(stats['server_number'])
            temp['service_number'].append(stats['service_number'])

            for mime_type in stats['size_dict'].keys():
                temp['{}_size'.format(mime_type)].append(stats['size_dict'][mime_type])

            for mime_type in stats['number_dict'].keys():
                temp['{}_number'.format(mime_type)].append(stats['number_dict'][mime_type])

        # take the median value of all the data and store it in the dataframe
        for item in temp.keys():
            if not temp[item]:
                print(web_index)
            data_results.set_value(web_index, item, np.median(temp[item]))

        # store the standard deviation of load time
        data_results.set_value(web_index, 'load_time_std', np.std(temp['load_time']))

    data_results['total_number'] = data_results['image_number'] + data_results['javascript_number'] + \
                                 data_results['css_number'] + data_results['html_number'] + \
                                 data_results['xml_number'] + data_results['audio_number'] + data_results['video_number']

    data_results['total_size'] = data_results['image_size'] + data_results['javascript_size'] + \
                                 data_results['css_size'] + data_results['html_size'] + \
                                 data_results['xml_size'] + data_results['audio_size'] + data_results['video_size']
    return data_results

