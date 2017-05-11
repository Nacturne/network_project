import pandas as pd

from utils.HAR import HAR

'''
code_set = set([])

for web_index in range(500):
    for folder in os.listdir('har_files'):
        flie_name = 'har_files/{0}/{1}.har'.format(folder, web_index)
        try:
            har = HAR(flie_name)
        except:
            # if the har file is missing, skip it.
            continue

        for entry in har.entries:
            red_url = entry['response']['redirectURL']

            if len(red_url) == 0:
                continue

            status_code = entry['response']['status']

'''

def get_red_stats(har):
    results = {'time_300': 0, 'count_300': 0,
               'time_301': 0, 'count_301': 0,
               'time_302': 0, 'count_302': 0,
               'time_303': 0, 'count_303': 0,
               'time_307': 0, 'count_307': 0,
               'time_308': 0, 'count_308': 0}

    for entry in har.entries:
        red_url = entry['response']['redirectURL']

        if len(red_url) == 0:
            continue
        status_code = entry['response']['status']
        time = entry['time']

        results['time_{}'.format(status_code)] = results['time_{}'.format(status_code)] + (time/1000.0)
        results['count_{}'.format(status_code)] = results['count_{}'.format(status_code)] + 1

    return results


data = pd.DataFrame(columns=['time_300', 'count_300',
                             'time_301', 'count_301',
                             'time_302', 'count_302',
                             'time_303', 'count_303',
                             'time_307', 'count_307',
                             'time_308', 'count_308',
                             'red_time_total', 'red_count_total'])

for web_index in range(500):
    flie_name = 'har_files/httpdata1/{}.har'.format(web_index)
    try:
        har = HAR(flie_name)
    except:
        # if the har file is missing, skip it.
        continue

    red_stats = get_red_stats(har)

    for item in red_stats.keys():
        data.set_value(web_index, item, red_stats[item])

    data['red_time_total'] = data['time_300'] + data['time_301'] + \
                             data['time_302'] + data['time_303'] + \
                             data['time_307'] + data['time_308']

    data['red_count_total'] = data['count_300'] + data['count_301'] + \
                              data['count_302'] + data['count_303'] + \
                              data['count_307'] + data['count_308']


data.to_csv('data/red_stats.txt', sep='\t')

