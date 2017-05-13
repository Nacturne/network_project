'''
Created on May 5, 2017

@author: ash
'''


dict ={}

cotlist = [line.rstrip('\r\n') for line in open('nation.txt')]
cotlist = cotlist[0:500]
webslist = [line.rstrip('\r\n') for line in open('add_Top500News.txt')]
index=range(500)
for i in index:
    if dict.has_key(cotlist[i]):
        dict[cotlist[i]].append(webslist[i])
    else:
        dict[cotlist[i]]=[webslist[i]]
for nation in dict.keys():
    print nation
    for web in dict[nation]:
        print web
'''
import dns.name
import dns.message
import dns.query
import dns.resolver
import re

from geoip import geolite2
import win_inet_pton
#match = geolite2.lookup('17.0.0.1')
'''
'''
webslist = [line.rstrip('\r\n') for line in open('Http_Top500News.txt')]
datafile = open('ip_address.txt','w')
list =[i for i in range (500)]
for i in list:
    web = webslist[i]
    web = web.split('/')[0]
    if web.endswith('/'):       
        web = web[:-1]
    domain = dns.name.from_text(web)
    try:                   
        answers = dns.resolver.query(domain, 'A')   
    except:
        datafile.write('\n')
        continue             
    for rdata in answers:
            1
    datafile.write(str(rdata)+'\n')
datafile.close()
'''
'''
iplist = [line.rstrip('\r\n') for line in open('ip_address.txt')]
datafile = open('nation.txt','w')
list =[i for i in range (500)]
for i in list:
    ip = iplist[i]
    match = geolite2.lookup(str(ip))
    #print match
    if match is None:
        print i,ip
        datafile.write('\n')
        continue
    else:
        try:
            print i,match.country
            datafile.write(match.country+'\n')
        except:
            print i,ip
            datafile.write('\n')
            continue
datafile.close()
'''