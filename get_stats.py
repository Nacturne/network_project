import pandas as pd

from utils.HAR import HAR

data = pd.DataFrame(columns=['image_size',
                             'javascript_size',
                             'css_size',
                             'html_size',
                             'audio_size',
                             'vedio_size',
                             'total_size',
                             'image_number',
                             'javascript_number',
                             'css_number',
                             'html_number',
                             'audio_number',
                             'vedio_number',
                             'total_number',
                             ])


for web_index in range(500):
    flie_name = 'httpdata_184_343_386/{}.har'.format(web_index)
    try:
        har = HAR(flie_name)
    except:
        continue

    size_dict = {'image': 0,
                'javascript': 0,
                'css': 0,
                'html': 0,
                'audio': 0,
                'vedio': 0}

    number_dict = {'image': 0,
                'javascript': 0,
                'css': 0,
                'html': 0,
                'audio': 0,
                'vedio': 0}

    for entry in har.entries:
        mime_type = entry['response']['content']['mimeType']
        size = entry['response']['bodySize']

        for t in size_dict.keys():
            if t in mime_type:
                size_dict[t] = size_dict[t] + size
                number_dict[t] = number_dict[t] + 1

    total_size = 0
    for t in size_dict.keys():
        data.set_value(web_index, t + '_size',  size_dict[t])
        total_size = total_size + size_dict[t]
    data.set_value(web_index, 'total_size', total_size)


    total_number = 0
    for t in number_dict.keys():
        data.set_value(web_index, t + '_number',  number_dict[t])
        total_number = total_number + number_dict[t]
    data.set_value(web_index, 'total_number', total_number)

data.to_csv('data/stats_new.txt', sep='\t')





'''
content_dict = {'image': [],
                'javascript': [],
                'css': [],
                'html': [],
                'audio': [],
                'vedio': []}


x_coor = []

for web_index in range(500):
    flie_name = 'httpdata2/{}.har'.format(web_index)
    try:
        har = HAR(flie_name)
        x_coor.append(web_index)
    except:
        continue

    temp_dict = {'image': 0,
                'javascript': 0,
                'css': 0,
                'html': 0,
                'audio': 0,
                'vedio': 0}

    for entry in har.entries:
        mime_type = entry['response']['content']['mimeType']
        size = entry['response']['bodySize']

        for t in ['image', 'javascript', 'css', 'html', 'audio', 'vedio']:
            if t in mime_type:
                temp_dict[t] = temp_dict[t] + size

    for t in ['image', 'javascript', 'css', 'html', 'audio', 'vedio']:
        content_dict[t].append(temp_dict[t])




print('-'*50)

print(len(x_coor))
print(len(content_dict['image']))


for t in ['image', 'javascript', 'css', 'html', 'audio', 'vedio']:
    plt.plot(x_coor, content_dict[t], label=t)

plt.legend()
plt.show()
'''
