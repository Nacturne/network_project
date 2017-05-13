'''
Created on May 6, 2017

@author: ash
'''
import os
from HAR import HAR


datafile = open('DaTa/US_remote.txt','w')
nationlist = [line.rstrip('\r\n') for line in open('nation.txt')]
webslist = [line.rstrip('\r\n') for line in open('Data/US.txt')]
for index in range(500):
    if nationlist[index]=='US':       
        datafile.write(webslist[index]+'\n')   
datafile.close()

def clear1(nation,index,number_group):
    for i in range(number_group):
        oriname = 'Country/'+nation+'/without_ad_block/group'+str(i)+'/'+str(i)+'_'+str(index)+'.har'
        desname = 'Country/Drop/'+nation+'_'+str(i)+'_'+str(index)+'.har'
        try:
            os.rename(oriname,desname)
        except:
            continue
        
        
def clear0(nation,number,number_group):
    for i in range(number):
        for j in range(number_group):  
            total_list = []     
            flie_name = 'Country/'+nation+'/without_ad_block/group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
            except:
                continue
            total_list.append(har.total_objects())
            
        total_list.sort()
        
        if len(total_list) == 0:
            clear1(nation, i, number_group)
        elif  total_list[-1] ==0:
            clear1(nation, i, number_group)
 
 
def clear2(nation,index,number_group):
    for i in range(number_group):
        oriname = 'Country/Drop/'+nation+'_'+str(i)+'_'+str(index)+'.har'
        desname = 'Country/'+nation+'/without_ad_block/group'+str(i)+'/'+str(i)+'_'+str(index)+'.har'
        try:
            os.rename(oriname,desname)
        except:
            continue
        
        
def clear3(nation,number,number_group):
    for i in range(number):
        for j in range(number_group):       
            flie_name = 'Country/Drop/'+nation+'_'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
            except:
                continue
            
            if har.total_objects()<>0:
                clear2(nation, i, number_group)

'''
clear3('Japan', 30, 10)
clear3('CA',34,10) 
clear3('CN',30,10) 
clear3('GE',71,10) 
clear3('India',35,10) 
clear3('Japan',30,10) 
clear3('Korea',30,10) 
clear3('UK',37,10) 
clear3('Country',299,10)
clear3('US',500,18)      
'''                 
'''
clear0('Japan', 30, 10)
clear0('CA',34,10) 
clear0('CN',30,10) 
clear0('GE',71,10) 
clear0('India',35,10) 
clear0('Japan',30,10) 
clear0('Korea',30,10) 
clear0('UK',37,10) 
clear0('Country',299,10)
clear0('US',500,18)
    
'''

'''
datafile = open('DaTa/US.txt','w+')
webslist = [line.rstrip('\r\n') for line in open('DaTa/Http_Top500News.txt')]

for index in range(500):
    web = webslist[index]

    if web.endswith('/'):       
        web = web[:-1]
    datafile.write(str(web)+'\n')
    
datafile.close()
'''
'''
import os
for i in range(18):
    for j in range(500):
        oriname = 'Country/US/without_ad_block/group'+str(i)+'/'+str(j)+'.har'
        desname = 'Country/US/without_ad_block/group'+str(i)+'/'+str(i)+'_'+str(j)+'.har'
        print oriname,desname
        try:
            os.rename(oriname,desname)
        except:
            continue
            '''
'''
import os
def Nrename(number,nation,index):
    for i in range(10):
        for j in range(number):
            oriname = 'Country/'+nation+'/without_ad_block/group'+str(i)+'/'+str(i)+'_'+str(j)+'.har'
            desname = 'Country/Country/without_ad_block/group'+str(i)+'/'+str(i)+'_'+str(j+index)+'.har'
            #print oriname,desname
            try:
                os.rename(oriname,desname)
                
            except:
                continue
=
Nrename(37, 'UK', 0)
Nrename(71, 'GE', 37)
Nrename(34, 'CA', 37+71)
Nrename(32, 'AU', 37+71+34)
Nrename(35, 'India', 37+71+34+32)
Nrename(30, 'Japan', 37+71+34+32+35)
Nrename(30, 'Korea', 37+71+34+32+35+30)

Nrename(30, 'CN', 37+71+34+32+35+30+30)
            

datafile = open('US.txt','w+')
weblist = [line.rstrip('\r\n') for line in open('add_Top500News.txt')]
nationlist = [line.rstrip('\r\n') for line in open('nation.txt')]
for i in range(500):
    if nationlist[i]=='US':
        datafile.write(weblist[i]+'\n')

datafile.close()


from HAR import HAR

import os

#list=[0,1,2,4,6,7,9,10,12,13,16,17,18,19,21,24,26,28]
for j in range(10):
    for i in range(434):
        oriname = 'US/without_ad_block/'+'group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
        
        try:
            har = HAR(oriname)
        except:
            continue
        
        if har.loadtime()>35:
            desname = 'US/drop/'+str(j)+'ad_'+str(i)+'.har'
            print i,j   
            os.rename(oriname,desname)
        


def nationloadtime(Nation_number,Nation,ONindex): 
    datafile = open('ad_Japan_loadtime.txt','a')
    index = range(Nation_number)   
    for j in index:
        loadtime1_list=[]
        loadtime2_list=[]
        for i in range(10):    
            file1_name = 'Country/'+Nation+'/without_ad_block/group'+str(i)+'/'+str(i)+'_'+str(j)+'.har'
            #print file1_name
            try:
                har1 = HAR(file1_name)        
            except:
                continue
            
            loadtime1 = har1.loadtime()
            loadtime1_list.append(loadtime1)
    
        for i in range(5):   
            if i<3:
                t=i
            else: 
                t=i-3
            file2_name = 'Country/ON_fx_httpdata/group'+str(i)+'/'+str(t)+'_'+str(j+ONindex)+'.har'
            try:
                har2 = HAR(file2_name)
            except:
                continue
            
            loadtime2 = har2.loadtime()
            loadtime2_list.append(loadtime2)
            
        loadtime1_list.sort()
        loadtime2_list.sort()
        #print loadtime1_list
        if len(loadtime1_list)>0 and len(loadtime2_list)>0:
            avg_loadtime1 = loadtime1_list[len(loadtime1_list)/2]
            avg_loadtime2 = loadtime2_list[len(loadtime2_list)/2]
            print j,avg_loadtime1,avg_loadtime2
            datafile.write(str(avg_loadtime1)+','+str(avg_loadtime2)+'\n')
            
    datafile.close()
print('-'*50)

nationloadtime(37, 'UK', 0)
nationloadtime(71, 'GE', 37)
nationloadtime(34, 'CA', 37+71)
nationloadtime(32, 'AU', 37+71+34)
nationloadtime(35, 'India', 37+71+34+32)
nationloadtime(30, 'Japan', 37+71+34+32+35)
        
'''
'''
import os

nationlist = [line.rstrip('\r\n') for line in open('nation.txt')]
USlist=[]
for i in range(500):
    if nationlist[i]=='US':
        USlist.append(i)
print len(USlist),USlist

for j in range(19):
    for i in range(434):
        oriname = 'httpdata/'+'group'+str(j)+'/'+str(USlist[i])+'.har'
        desname = 'httpdata/'+'group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
        try:
            os.rename(oriname,desname)
        except:
            continue
'''
'''
datafile = open('add_Top500News.txt','w+')
webslist = [line.rstrip('\r\n') for line in open('Http_Top500News.txt')]

for index in range(500):
    web = webslist[index]
    if web.find('Http') == -1:        
        web = 'http://'+ web
    if web.endswith('/'):       
        web = web[:-1]
    datafile.write(str(web)+'\n')
    
datafile.close()
'''