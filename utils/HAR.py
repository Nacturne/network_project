import json
from datetime import datetime
import re
import dns.resolver
import dns.name


class HAR(object):
    def __init__(self, file_name):
        with open(file_name) as data_file:
            log = json.load(data_file)['log']
        self.comment = log['comment']
        self.entries = log['entries']
        self.version = log['version']
        self.pages = log['pages']
        self.creator = log['creator']

    def loadtime(self):
        starttime = datetime.strptime(str(self.pages[0]['startedDateTime'][0:23]), "%Y-%m-%dT%H:%M:%S.%f")
        endtime = datetime.strptime(str(self.entries[-1]['startedDateTime'][0:23]), "%Y-%m-%dT%H:%M:%S.%f")
        durtime = endtime - starttime
        return durtime.seconds + durtime.microseconds / 1000000.0 + self.entries[-1]['time'] / 1000.0


    # what's servernubmer and service number -------------------------------------------------------------
    def server_number(self):
        server_ip_list = []
        for entry in self.entries:
            status = str(entry['response']['status'])
            if status == '400' or status == '0':
                continue
            try:
                ip = entry['serverIPAddress']
            except:
                continue
            if ip not in server_ip_list:
                server_ip_list.append(ip)
        return len(server_ip_list)

    def service_number(self):
        service_ns_list = []
        server_name_list = []
        service_name_list = []
        pattern = re.compile(r'^\d*.\d*.\d*.\d*$')

        for entry in self.entries:
            status = str(entry['response']['status'])
            if status == '400' or status == '0':
                continue
            try:
                url = str(entry['request']['url'])
            except:
                continue

            temp = url.split('//')[1].split('/')[0].split(':')[0].split('.')
            if len(temp) == 4:
                string = temp[0] + '.' + temp[1] + '.' + temp[2] + '.' + temp[3]
                if pattern.match(string):
                    top2domain = temp
                    service_name_list.append(top2domain)
                    continue

            if (temp[-1] == 'cn' or temp[-1] == 'au' or temp[-1] == 'cn') and len(temp) > 2:
                top2domain = temp[-3] + '.' + temp[-2]
            else:
                top2domain = temp[-2] + '.' + temp[-1]

            if top2domain not in server_name_list:
                server_name_list.append(top2domain)
                domain = dns.name.from_text(top2domain)
                try:
                    answers = dns.resolver.query(domain, 'NS')
                except:
                    service_name_list.append(top2domain)
                    continue
                nslist = []
                for rdata in answers:
                    nslist.append(str(rdata))
                nslist.sort()

                if nslist not in service_ns_list:
                    service_ns_list.append(nslist)
                    service_name_list.append(top2domain)

        return len(service_name_list)
