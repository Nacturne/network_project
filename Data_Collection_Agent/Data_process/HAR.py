'''
Created on Apr 23, 2017

@author: ash
'''
import json
from datetime import datetime
import re
import dns.resolver
import dns.name
from werkzeug import redirect

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
        starttime = datetime.strptime(str(self.pages[0]['startedDateTime'][0:23]),"%Y-%m-%dT%H:%M:%S.%f")
        endtime = datetime.strptime(str(self.entries[-1]['startedDateTime'][0:23]),"%Y-%m-%dT%H:%M:%S.%f")
        durtime = endtime - starttime 
        return durtime.seconds + durtime.microseconds/1000000.0 + self.entries[-1]['time']/1000.0 

    def total_objects(self):
        objects = 0
        for entry in self.entries:           
            status = str(entry['response']['status'])
            if status <> '200':
                continue   
            #print status
            objects +=1
        return objects
    
    def total_time(self):
        time = 0
        for entry in self.entries:           
            status = str(entry['response']['status'])
            if status <> '200':
                continue   
            #print status
            time += entry['time']
        return time
    
    def total_byte(self):
        byte = 0
        for entry in self.entries:           
            status = str(entry['response']['status'])
            if status <> '200':
                continue   
            #print status
            byte += entry['response']['bodySize']
        return byte
    
    def redirection(self):
        total_number = 0
        total_time = 0
        redirect_number = 0
        redirect_time = 0
        
        for entry in self.entries:
            
            status = str(entry['response']['status'])
            if status <> '400' and status <> '0':
                total_number +=  1   
                total_time += entry['time']
                #status_list = ['300','302']
                if status[0] =='3' and status!='304' and status!='305':
                #if status =='303' or status =='307':
                    #print status
                    '''
                    print  status,entry['request']['url'].split('//')[1].split('/')[0]
                    print entry['response']['redirectURL'].split('//')[1].split('/')[0]
                    print entry['request']['url']
                    print entry['response']['redirectURL']
                    '''
                    redirect_number +=  1   
                    redirect_time += entry['time']
                    
        return float(redirect_number)/total_number,float(redirect_time)/total_time  
    
    def redirection_check(self):
        total_number = 0
        total_time = 0

        
        for entry in self.entries:
            
            status = str(entry['response']['status'])
            if status <> '400' and status <> '0':
                total_number +=  1   
                total_time += entry['time']
                #status_list = ['300','302']
                if status[0] =='3' and status!='304' and status!='305':
                    nationlist =  ['cn','au','kr','it','de','ca','fr','in','jp','uk']
                #if status =='301':# or status =='307':
                    if entry['response']['httpVersion']=="HTTP/1.1":
                        
                        version1 = entry['request']['url'].split('//')[0]
                        version2 = entry['response']['redirectURL'].split('//')[0]
                        server1 = entry['request']['url'].split('//')[1].split('/')[0]
                        server2 = entry['response']['redirectURL'].split('//')[1].split('/')[0]
                        subserver1 = entry['request']['url'].split('//')[1].split('/')[1]
                        subserver2 = entry['response']['redirectURL'].split('//')[1].split('/')[1]
                        #if version1==version2  and server1!=server2 and (server1 not in server2):
                        if version1==version2  and server1!=server2 and 'cdn' not in server1 and 'cdn' in server2:
                            #if subserver1 not in nationlist and subserver2 in nationlist :
                            print status,entry['response']['httpVersion']
                            print server1
                            print server2
                            print entry['request']['url']
                            print entry['response']['redirectURL']
                        
                                        
    
    def redirection_code(self):
        redirectdict = {'301':0,'302':0,'303':0,'307':0,} 
        
        for entry in self.entries:
            
            status = str(entry['response']['status'])
            if status <> '400' and status <> '0':
                #status_list = ['300','302']
                if status[0] =='3' and status!='304' and status!='305':
                    #if entry['response']['httpVersion']=="HTTP/1.0":
                    redirectdict[status]+=1
                #if status =='304' or status =='305':
                    #print status
                    '''
                    print  status,entry['request']['url'].split('//')[1].split('/')[0]
                    print entry['response']['redirectURL'].split('//')[1].split('/')[0]
                    print entry['request']['url']
                    print entry['response']['redirectURL']
                    '''
                        
        total = 0
        for key in redirectdict:
            total +=redirectdict[key]
        for key in redirectdict:
            redirectdict[key] = redirectdict[key]/float(total)
                       
        return redirectdict    
    
    def redirection_type(self):
        redirectdict = {'www':0,'https':0,'port':0,'geo':0,'inside':0,'cdn':0,'others':0} 
        
        for entry in self.entries:
            
            status = str(entry['response']['status'])
            if status <> '400' and status <> '0':
                #status_list = ['300','302']
                if status[0] =='3' and status!='304' and status!='305':
                    version1 = entry['request']['url'].split('//')[0]
                    version2 = entry['response']['redirectURL'].split('//')[0]
                    server1 = entry['request']['url'].split('//')[1].split('/')[0]
                    server2 = entry['response']['redirectURL'].split('//')[1].split('/')[0]
                    subserver1 = entry['request']['url'].split('//')[1].split('/')[1]
                    subserver2 = entry['response']['redirectURL'].split('//')[1].split('/')[1]
                    nationlist =  ['cn','au','kr','it','de','ca','fr','in','jp','uk']       
                    if version1!=version2 and server1==server2:
                        redirectdict['https']+=1
                    elif version1==version2  and server1!=server2 and server1 in server2:
                        if  'www' not in server1 and 'www' in server2:
                            redirectdict['www']+=1
                        elif server1[-1]!=server2[-1]:
                            if ':' not in server2[len(server1)-1:-1]:
                                redirectdict['geo']+=1
                            else:
                                redirectdict['port']+=1                           
                    elif version1==version2  and server1!=server2 and 'cdn' not in entry['request']['url'] and 'cdn' in entry['response']['redirectURL']:
                            redirectdict['cdn']+=1                               
                    elif version1==version2  and server1==server2:
                        if subserver1 not in nationlist and subserver2 in nationlist :
                            redirectdict['geo']+=1
                        else:
                            redirectdict['inside']+=1
                    else:
                        redirectdict['others']+=0
                        
        total = 0
        for key in redirectdict:
            total +=redirectdict[key]
        for key in redirectdict:
            redirectdict[key] = redirectdict[key]/float(total)
                       
        return redirectdict      
    
    def server_number(self):
        server_domain_list = []
        for entry in self.entries:
            status = str(entry['response']['status'])
            
            if status <> '200':
                continue   
            #print status
            url = entry['request']['url']   
            #print url
            full_domain_name = url.split('//')[1].split('/')[0]  
            #print full_domain_name   
            if full_domain_name not in server_domain_list:
                server_domain_list.append(full_domain_name)
        return len(server_domain_list)
    
    def service_list(self):
        service_ns_list =[]
        server_name_list =[]
        service_name_list =[]
        pattern=re.compile(r'^\d*.\d*.\d*.\d*$')
    
        for entry in self.entries:
            status = str(entry['response']['status'])
            if status <>'200':
                continue            
            try:
                url = str(entry['request']['url'])
            except:
                continue
            
            temp = url.split('//')[1].split('/')[0].split(':')[0].split('.')
            if len(temp)==4:
                string =  temp[0]+'.'+temp[1]+'.'+temp[2]+'.'+temp[3]
                if pattern.match(string):
                        top2domain = temp
                        service_name_list.append(top2domain)
                        continue
            nationlist = ['cn','au','kr','it','de','ca','fr','in','jp','uk']       
            if (temp[-1] in nationlist ) and len(temp)>2:
                top2domain = temp[-3]+'.'+temp[-2]+'.'+temp[-1]
            else:
                top2domain = temp[-2]+'.'+temp[-1]
                
            if top2domain not in server_name_list:
                server_name_list.append(top2domain)               
                domain = dns.name.from_text(top2domain)
                try:                   
                    answers = dns.resolver.query(domain, 'NS')   
                except:
                    service_name_list.append(top2domain)
                    continue             
                nslist =[]            
                for rdata in answers:  
                    nslist.append(str(rdata));
                nslist.sort()   
                             
                if nslist not in service_ns_list:
                    service_ns_list.append(nslist)
                    service_name_list.append(top2domain)
        
        return  service_name_list
                 
    def service_number(self):
        service_ns_list =[]
        server_name_list =[]
        service_name_list =[]
        pattern=re.compile(r'^\d*.\d*.\d*.\d*$')
    
        for entry in self.entries:
            status = str(entry['response']['status'])
            if status <>'200':
                continue            
            try:
                url = str(entry['request']['url'])
            except:
                continue
            
            temp = url.split('//')[1].split('/')[0].split(':')[0].split('.')
            if len(temp)==4:
                string =  temp[0]+'.'+temp[1]+'.'+temp[2]+'.'+temp[3]
                if pattern.match(string):
                        top2domain = temp
                        service_name_list.append(top2domain)
                        continue
            nationlist = ['cn','au','kr','it','de','ca','fr','in','jp','uk']       
            if (temp[-1] in nationlist ) and len(temp)>2:
                top2domain = temp[-3]+'.'+temp[-2]+'.'+temp[-1]
            else:
                top2domain = temp[-2]+'.'+temp[-1]
                
            if top2domain not in server_name_list:
                server_name_list.append(top2domain)               
                domain = dns.name.from_text(top2domain)
                try:                   
                    answers = dns.resolver.query(domain, 'NS')   
                except:
                    service_name_list.append(top2domain)
                    continue             
                nslist =[]            
                for rdata in answers:  
                    nslist.append(str(rdata));
                nslist.sort()   
                             
                if nslist not in service_ns_list:
                    service_ns_list.append(nslist)
                    service_name_list.append(top2domain)
        
        return  len(service_name_list)
        
    def nonori_fraction(self,oridomain,oriNS):     
        servicelist = []
        pattern = re.compile(r'^\d*.\d*.\d*.\d*$')
        nonori_byte = 0
        nonori_object = 0
        nonori_time = 0
        #print self.total_byte(),self.total_objects(),self.total_time()
        oridomain = oridomain.lower().split('/')[0]
        for entry in self.entries:
            
            status = str(entry['response']['status'])
            if status <>'200':
                continue            
            try:
                url = str(entry['request']['url'])
            except:
                continue
            
            temp = url.split('//')[1].split('/')[0].split(':')[0].split('.')
            if len(temp)==4:
                string =  temp[0]+'.'+temp[1]+'.'+temp[2]+'.'+temp[3]
                if pattern.match(string):
                        top2domain = temp
                        continue
            nationlist = ['cn','au','kr','it','de','ca','fr','in','jp','uk']       
            if (temp[-1] in nationlist ) and len(temp)>2:
                top2domain = temp[-3]+'.'+temp[-2]+'.'+temp[-1]
            else:
                top2domain = temp[-2]+'.'+temp[-1]
            
            #print '1',oridomain,top2domain 
            
            if oridomain ==top2domain:
                continue  
            
            if top2domain in servicelist: 
                nonori_byte += entry['response']['bodySize']
                nonori_object +=1
                nonori_time += entry['time']
            
            else: 
            
                domain = dns.name.from_text(top2domain)
                try:                   
                    answers = dns.resolver.query(domain, 'NS')   
                except:
                    continue           
                NS = []
    
                for rdata in answers:  
                    NS.append(str(rdata));
                if NS <> oriNS:
                    nonori_byte += entry['response']['bodySize']
                    nonori_object +=1
                    nonori_time += entry['time']
                    servicelist.append(top2domain)
                    #print nonori_byte,nonori_object,nonori_time
 
        return  float(nonori_byte)/self.total_byte(),float(nonori_object)/self.total_objects(),float(nonori_time)/self.total_time()
    
    def nonori_content(self,oridomain,oriNS):     
        servicelist = []
        pattern = re.compile(r'^\d*.\d*.\d*.\d*$')
        nonori_number = {'image': 0,
                        'javascript':0,
                        'css': 0,
                        'html': 0,
                        'audio': 0,
                        'vedio': 0,
                        'xml':0,
                        'text':0,
                        'application':0}
        #print self.total_byte(),self.total_objects(),self.total_time()
        oridomain = oridomain.lower().split('/')[0]
        
        for entry in self.entries:            
            status = str(entry['response']['status'])
            if status <>'200':
                continue            
            try:
                url = str(entry['request']['url'])
            except:
                continue
            
            temp = url.split('//')[1].split('/')[0].split(':')[0].split('.')
            if len(temp)==4:
                string =  temp[0]+'.'+temp[1]+'.'+temp[2]+'.'+temp[3]
                if pattern.match(string):
                        top2domain = temp
                        continue
            nationlist = ['cn','au','kr','it','de','ca','fr','in','jp','uk']       
            if (temp[-1] in nationlist ) and len(temp)>2:
                top2domain = temp[-3]+'.'+temp[-2]+'.'+temp[-1]
            else:
                top2domain = temp[-2]+'.'+temp[-1]
            
            #print '1',oridomain,top2domain 
            
            if oridomain ==top2domain:
                continue  
            
            if top2domain in servicelist: 
                mimetype = entry['response']['content']['mimeType']
                #print mimetype
                if mimetype !='':
                    #print 'notype' 
                    maintype = mimetype.split('/')[0]
                    if maintype =='image' or maintype =='audio' or maintype == 'vedio':
                        nonori_number [maintype] +=1
                    else:
                        try:
                            subtype = mimetype.split('/')[1].split(';')[0]
                        except:
                            continue
                        subtype = mimetype.split('/')[1].split(';')[0]
                        if subtype =='javascript' or subtype == 'css' or subtype == 'html' or subtype == 'xml':  
                            nonori_number[subtype] +=1
                        elif maintype =='application' or maintype =='text':
                            nonori_number [maintype] +=1
                #print nonori_number
            
            else: 
                domain = dns.name.from_text(top2domain)
                try:                   
                    answers = dns.resolver.query(domain, 'NS')   
                except:
                    continue           
                NS = []
    
                for rdata in answers:  
                    NS.append(str(rdata));
                if NS <> oriNS:
                    
                    mimetype = entry['response']['content']['mimeType']
                    if mimetype !='':
                        #print mimetype#print 'notype' 
                        maintype = mimetype.split('/')[0]
                        if maintype =='image' or maintype =='audio' or maintype == 'vedio':
                            nonori_number [maintype] +=1
                        else:
                            try:
                                subtype = mimetype.split('/')[1].split(';')[0]
                            except:
                                continue
                            if subtype =='javascript' or subtype == 'css' or subtype == 'html' or subtype == 'xml':  
                                nonori_number[subtype] +=1
                            elif maintype =='application' or maintype =='text':
                                nonori_number [maintype] +=1
                    servicelist.append(top2domain)
                    #print nonori_number
                    #print nonori_byte,nonori_object,nonori_time
                
                    
        return  nonori_number
                    