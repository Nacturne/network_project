'''
Created on Apr 3, 2017

@author: alex
'''

from browsermobproxy import Server
from selenium import webdriver
from pyvirtualdisplay import Display
import json
import time
from random import shuffle
import os
import sys

display = Display(visible=0,size=(800,600))
display.start()
webslist = [line.rstrip('\r\n') for line in open('tools/Http_Top500News.txt')]

list =range(100)
#shuffle(list)

'''
try:
    os.state('httpdata1/')
except:
    os.makedirs('httpdata1/')
'''

log = open('tools/httpdata19/testlog','w+')
server = Server("browsermob-proxy-2.1.4/bin/browsermob-proxy")
server.start()

for i in list:
    '''
    if i%2 == 0:
    	time.sleep(60)
    '''
   
    profile  = webdriver.FirefoxProfile()

    proxy = server.create_proxy({'port':9911})
    print i+1, str(webslist[i])
    log.write(str(i+1)+str(webslist[i])+'\n')
    profile.add_extension('adblocker_ultimate-2.26-an+fx.xpi')
    #profile.set_preference("extensions.adblock_ultimate.currentVersion", "2.26")
    profile.set_proxy(proxy.selenium_proxy())
    profile.accept_untrusted_certs = True
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.set_page_load_timeout(50)
    proxy.new_har()
    
    web = webslist[i]
    if web.find('Http') == -1:        
        web = 'http://'+ web
    if web.endswith('/'):       
        web = web[:-1]

    try:
        driver.get(web)
    except:
        print "Error"
        log.write('Error\n')
        server.stop()
        driver.quit()

        continue
    else:
        #print(proxy.har)
        filename='tools/httpdata19/'+str(i)+'.har'

        out_f = open(filename, 'w')
        json.dump(proxy.har, out_f)
        out_f.close()

        driver.quit()

server.stop()
display.stop()  
log.close()
