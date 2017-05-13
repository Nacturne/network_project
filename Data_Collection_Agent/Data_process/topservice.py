'''
Created on Apr 24, 2017

@author: ash
'''
service_dict ={}

def top200service(nation,number,service_dict):
    dataname = 'Data/'+nation+'/service_list.txt'
    datafile = open(dataname,'r')
    
    for i in range(number):
        line = datafile.readline()
        list = line.split(',')[:-1]
        for web in list:
            if service_dict.has_key(web):
                service_dict[web]+=1
            else:
                service_dict[web]=1
    #print service_dict        
    datafile.close()
    return service_dict

service_dict1 = top200service('AU', 32, service_dict)
#calorigin_fraction('CA',34,10) 
service_dict2 = top200service('CN',30,service_dict1) 
service_dict3 = top200service('GE',71,service_dict2) 
service_dict4 = top200service('India',35,service_dict3) 
service_dict5 = top200service('Japan',30,service_dict4) 
service_dict6 = top200service('Korea',30,service_dict5) 
service_dict7 = top200service('UK',37,service_dict6) 
#calorigin_fraction('Country',299,10)         
service_dict8 = top200service('US_remote',434,service_dict7)
print len(service_dict8)
top200service = sorted(service_dict.items(), key=lambda d: d[1])[2054:2254] 
for item in top200service:
    print item
