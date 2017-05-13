'''
Created on May 8, 2017

@author: ash
'''

from HAR import HAR
import dns.resolver



def calserver_number(nation,number,number_group):
    #fliename = 'Country/'+nation+'/without_ad_block/group'+str(i)+'/'+str(i)+'_'+str(j)+'.har'
    dataname = 'Data/'+nation+'/server_number.txt'
    datafile = open(dataname,'w')
    for i in range(number):
        sernumberlist = []
        for j in range(number_group):       
            flie_name = 'Country/'+nation+'/without_ad_block/group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
            except:
                continue
            #print har.server_number()
            sernumberlist.append(har.server_number())
        sernumberlist.sort()
        #print sernumberlist
        half = len(sernumberlist)//2
        if len(sernumberlist)<>0:
            sernum = (sernumberlist[half] + sernumberlist[~half])/2
            datafile.write(str(sernum)+'\n')
    datafile.close()
      


    
def calservice_number(nation,number,number_group):
    #fliename = 'Country/'+nation+'/without_ad_block/group'+str(i)+'/'+str(i)+'_'+str(j)+'.har'
    dataname = 'Data/'+nation+'/service_number.txt'
    datafile = open(dataname,'w')
    for i in range(number):
        print nation,i
        sernumberlist = []
        for j in range(number_group):       
            flie_name = 'Country/'+nation+'/without_ad_block/group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
            except:
                continue
            #print har.server_number()
            sernumberlist.append(har.service_number())
        sernumberlist.sort()
        #print sernumberlist
        half = len(sernumberlist)//2
        if len(sernumberlist)<>0:
            sernum = (sernumberlist[half] + sernumberlist[~half])/2
            datafile.write(str(sernum)+'\n')
    datafile.close()
#calservice_number('Country',299,10)         
#calservice_number('Japan',30,10)   

def calservice_list(nation,number,number_group):
    #fliename = 'Country/'+nation+'/without_ad_block/group'+str(i)+'/'+str(i)+'_'+str(j)+'.har'
    dataname = 'Data/'+nation+'/service_list.txt'
    datafile = open(dataname,'w')
    for i in range(number):
        print nation,i
        for j in range(number_group):       
            flie_name = 'Country/'+nation+'/without_ad_block/group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
            except:
                continue
            #print har.server_number()
            sernumberlist=har.service_list()
            if len(sernumberlist)!=0:
                for service in sernumberlist:
                    datafile.write(str(service)+',') 
                datafile.write('\n')
                break
    datafile.close()
#calservice_number('Country',299,10)         
#calservice_number('Japan',30,10) 

def calorigin_fraction(nation,number,number_group):
    
    weblist = [line.rstrip('\r\n') for line in open('DaTa/'+nation+'.txt')]
    dataname = 'Data/'+nation+'/origin_fraction.txt'
    datafile = open(dataname,'w')
    
    for i in range(number):  
        oridomain = weblist[i].split('/')[0]
        if nation=='GE' and i ==10:
            continue
        if nation=='Korea' and i ==23:
            continue
        if nation=='CN' and i ==26:
            continue
        try:                   
            answer = dns.resolver.query(oridomain, 'NS')   
        except:
            continue 
        oriNS = []       
        for rdata in answer:  
            oriNS.append(str(rdata));
        print nation,i
        originbyte = []
        originobject = []
        origintime = []
        for j in range(number_group):      
            #print j 
            flie_name = 'Country/'+nation+'/without_ad_block/group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
            except:
                continue
                        
            #print har.server_number()
            if har.total_byte()!=0 and har.total_time()!=0 and har.total_objects()!=0:
                (bbyte,oobject,ttime) =har.nonori_fraction(weblist[i],oriNS)
                originbyte.append(bbyte)
                originobject.append(oobject)
                origintime.append(ttime)
        originbyte.sort()
        originobject.sort()
        origintime.sort()
        #print originbyte
        half = len(originbyte)//2
        if len(originbyte)<>0:
            byte = (originbyte[half] + originbyte[~half])/2
            objects = (originobject[half] + originobject[~half])/2
            time = (origintime[half] + origintime[~half])/2                   
            datafile.write(str(i)+','+str(byte)+','+str(objects)+','+str(time)+'\n')
    datafile.close()
#calorigin_fraction('Country',299,10) 

     
def calorigin_content(nation,number,number_group):
    
    weblist = [line.rstrip('\r\n') for line in open('DaTa/'+nation+'.txt')]
    dataname = 'Data/'+nation+'/origin_content.txt'
    datafile = open(dataname,'w')
    
    for i in range(number):  
        if nation=='GE' and i ==10:
            continue
        if nation=='Korea' and i ==23:
            continue
        if nation=='CN' and i ==26:
            continue
        oridomain = weblist[i].split('/')[0]
        try:                   
            answer = dns.resolver.query(oridomain, 'NS')   
        except:
            continue 
        oriNS = []       
        for rdata in answer:  
            oriNS.append(str(rdata));
        print nation,i

        for j in range(number_group):      
            #print j 
            flie_name = 'Country/'+nation+'/without_ad_block/group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
            except:
                continue
                                    #print har.server_number()
            if har.total_byte()!=0 and har.total_time()!=0 and har.total_objects()!=0:
                contentdict = har.nonori_content(weblist[i],oriNS)
                totalcontent = 0
                for key in contentdict:
                    totalcontent+=contentdict[key]
                print contentdict   
                if totalcontent ==0:
                    continue
                datafile.write(str(i)+',')
                for key in contentdict:
                    datafile.write(str("{0:.4f}".format(float(contentdict[key])/totalcontent))+',')    
                
                datafile.write('\n')
                break
        
    datafile.close()

def calredirection(nation,number,number_group):
    dataname = 'Data/'+nation+'/redirect.txt'
    #datafile = open(dataname,'w')
    
    for i in range(number):
        #print i
        timelist = []
        fractionlist =[]
        for j in range(number_group):       
            flie_name = 'Country/'+nation+'/without_ad_block/group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
                redi_time,redi_frac = har.redirection() 
            except:
                continue
            #print har.server_number()
            timelist.append(redi_time)
            fractionlist.append(redi_frac)
        timelist.sort()
        fractionlist.sort()
        #print sernumberlist
        
        if len(timelist)<>0:
            half = len(timelist)//2
            ttime= (timelist[half] + timelist[~half])/2
            ffrac= (fractionlist[half] + fractionlist[~half])/2
            #datafile.write(str(i)+','+str(ttime)+','+str(ffrac)+'\n')
    print 'Done'
    #datafile.close()

def calredirection_check(nation,number,number_group):
    #dataname = 'Data/'+nation+'/redirect.txt'
    #datafile = open(dataname,'w')
    
    for i in range(number):
        #print i
        timelist = []
        fractionlist =[]
        for j in range(number_group):       
            flie_name = 'Country/'+nation+'/without_ad_block/group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
                har.redirection_check() 
            except:
                continue
            #print har.server_number()
            
        
        '''
        timelist.sort()
        fractionlist.sort()
        #print sernumberlist
        
        if len(timelist)<>0:
            half = len(timelist)//2
            ttime= (timelist[half] + timelist[~half])/2
            ffrac= (fractionlist[half] + fractionlist[~half])/2
            #datafile.write(str(i)+','+str(ttime)+','+str(ffrac)+'\n')
        '''
    print 'Done'
    #datafile.close()

def calredirection_code(nation,number,number_group):
    dataname = 'Data/'+nation+'/redirect_code.txt'
    datafile = open(dataname,'w')
    
    for i in range(number):
        #print i
        redirect_code_list = {'301':[],'302':[],'303':[],'307':[]}
        for j in range(number_group):       
            flie_name = 'Country/'+nation+'/without_ad_block/group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
                redirect_dict = har.redirection_code() 
            except:
                continue
            #print har.server_number()
            for key in redirect_dict:
                redirect_code_list[key].append(redirect_dict[key])
                
        for key in redirect_code_list:
            redirect_code_list[key].sort()
        #print sernumberlist
        
        if len(redirect_code_list['301'])<>0:
            half = len(redirect_code_list['301'])//2
            datafile.write(str(i)+',')
            #ttime= (timelist[half] + timelist[~half])/2
            for key in redirect_code_list:
                fraction = (redirect_code_list[key][half] + redirect_code_list[key][~half])/2
                datafile.write(str(fraction)+',')
            datafile.write('\n')
    print 'Done'
    datafile.close()

def calredirection_type(nation,number,number_group):
    dataname = 'Data/'+nation+'/redirect_type.txt'
    datafile = open(dataname,'w')
    
    for i in range(number):
        #print i
        redirect_type_list = {'www':[],'https':[],'port':[],'geo':[],'inside':[],'cdn':[],'others':[]}
        for j in range(number_group):       
            flie_name = 'Country/'+nation+'/without_ad_block/group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
                redirect_dict = har.redirection_type() 
            except:
                continue
            #print har.server_number()
            
            for key in redirect_dict:
                redirect_type_list[key].append(redirect_dict[key])
        print redirect_type_list        
        for key in redirect_type_list:
            redirect_type_list[key].sort()
        #print sernumberlist
        
        if len(redirect_type_list['port'])<>0:
            half = len(redirect_type_list['port'])//2
            datafile.write(str(i)+',')
            #ttime= (timelist[half] + timelist[~half])/2
            for key in redirect_type_list:
                fraction = (redirect_type_list[key][half] + redirect_type_list[key][~half])/2
                datafile.write(str(fraction)+',')
            datafile.write('\n')
    print 'Done'
    datafile.close()

#calserver_number('US',500,18) 
#calservice_number('US',500,18) 

def calredirection_times(nation,number,number_group):
    dataname = 'Data/'+nation+'/redirect_times.txt'
    datafile = open(dataname,'w')
    redirect_type_list = {'www':0,'https':0,'port':0,'geo':0,'inside':0,'cdn':0,'others':0}
    
    for i in range(number):
        redirect_type_flag_list = {'www':True,'https':True,'port':True,'geo':True,'inside':True,'cdn':True,'others':True}
        #print i       
        for j in range(number_group):       
            flie_name = 'Country/'+nation+'/without_ad_block/group'+str(j)+'/'+str(j)+'_'+str(i)+'.har'
            #print flie_name
            try:
                har = HAR(flie_name)
                redirect_dict = har.redirection_type() 
            except:
                continue
            #print har.server_number()
            
            for key in redirect_dict:
                if redirect_dict[key]>0:
                    redirect_type_flag_list[key]=False
            #print redirect_dict        
        for key in redirect_type_flag_list:
            if redirect_type_flag_list[key]==False:
                redirect_type_list[key]+=1
        print redirect_type_list
        

    for key in redirect_type_list:
        datafile.write(str(redirect_type_list[key])+',')
    datafile.write('\n')
    print 'Done'
    datafile.close()

'''        
calserver_number('AU',32,10)       
calserver_number('CA',34,10) 
calserver_number('CN',30,10) 
calserver_number('GE',71,10) 
calserver_number('India',35,10) 
calserver_number('Japan',30,10) 
calserver_number('Korea',30,10) 
calserver_number('UK',37,10) 
calserver_number('Country',299,10)
calserver_number('US',500,18)  
'''           

'''
calservice_number('AU',32,10)        
calservice_number('CA',34,10) 
calservice_number('CN',30,10) 
calservice_number('GE',71,10) 
calservice_number('India',35,10) 
calservice_number('Japan',30,10) 
calservice_number('Korea',30,10) 
calservice_number('UK',37,10) 
#calservice_number('Country',299,10)         
calservice_number('US',500,18)       
'''
#calorigin_content('AU', 32, 10)
calservice_number('US',434,10) 
'''
#calorigin_fraction('AU', 32, 10)
#calorigin_fraction('CA',34,10) 
calorigin_fraction('CN',30,10) 
calorigin_fraction('GE',71,10) 
calorigin_fraction('India',35,10) 
calorigin_fraction('Japan',30,10) 
calorigin_fraction('Korea',30,10) 
calorigin_fraction('UK',37,10) 
#calorigin_fraction('Country',299,10)         
calorigin_fraction('US_remote',434,10)  
  
calorigin_content('Country',299,10)

calorigin_content('AU', 32, 10)
calorigin_content('CA',34,10) 
calorigin_content('CN',30,10) 
calorigin_content('GE',71,10) 
calorigin_content('India',35,10) 
calorigin_content('Japan',30,10) 
calorigin_content('Korea',30,10) 
calorigin_content('UK',37,10) 
#calorigin_byte('Country',299,10)         
calorigin_content('US_remote',434,10)  
'''
'''     
calredirection('AU', 32, 10)
calredirection('CA',34,10) 
calredirection('CN',30,10) 
calredirection('GE',71,10) 
calredirection('India',35,10) 
calredirection('Japan',30,10) 
calredirection('Korea',30,10) 
calredirection('UK',37,10) 
#calredirection('Country',299,10)         
#calredirection('US',500,10)
calredirection('US_remote',434,10)
'''
'''
calredirection_code('AU', 32, 10)
calredirection_code('CA',34,10) 
calredirection_code('CN',30,10) 
calredirection_code('GE',71,10) 
calredirection_code('India',35,10) 
calredirection_code('Japan',30,10) 
calredirection_code('Korea',30,10) 
calredirection_code('UK',37,10) 
#calredirection('Country',299,10)         
#calredirection('US',500,10)
calredirection_code('US_remote',434,10)
'''    

#calredirection_type('AU', 32, 10)
'''
calredirection_type('CA',34,10) 
calredirection_type('CN',30,10) 
calredirection_type('GE',71,10) 
calredirection_type('India',35,10) 
calredirection_type('Japan',30,10) 
calredirection_type('Korea',30,10) 
calredirection_type('UK',37,10) 
#calredirection('Country',299,10)         
#calredirection('US',500,10)
calredirection_type('US_remote',434,10)


'''
'''
calredirection_times('AU', 32, 10)
calredirection_times('CA',34,10) 
calredirection_times('CN',30,10) 
calredirection_times('GE',71,10) 
calredirection_times('India',35,10) 
calredirection_times('Japan',30,10) 
calredirection_times('Korea',30,10) 
calredirection_times('UK',37,10) 
#calredirection('Country',299,10)         
#calredirection('US',500,10)
calredirection_times('US_remote',434,10)
'''

#calservice_list('AU', 32, 10)
#calservice_list('CA',34,10) 
#calservice_list('CN',30,10) 
#calservice_list('GE',71,10) 
#calservice_list('India',35,10) 
#calservice_list('Japan',30,10) 
#calservice_list('Korea',30,10) 
#calservice_list('UK',37,10) 
#calredirection('Country',299,10)         
#calredirection('US',500,10)
#calservice_list('US_remote',434,10)
