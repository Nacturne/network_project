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

display = Display(visible=0,size=(800,600))
display.start()
webslist = [line.rstrip('\r\n') for line in open('add_Top500News.txt')]
#shuffle(list)

server = Server("browsermob-proxy-2.1.4/bin/browsermob-proxy")
server.start()
 
for i in range(0,500):
   
    profile  = webdriver.FirefoxProfile()
    proxy = server.create_proxy()
    print i+1, str(webslist[i])
    
    profile.add_extension('adblocker_ultimate-2.26.xpi')
    #profile.set_preference("extensions.adblock_ultimate.currentVersion", "2.26")
    profile.set_proxy(proxy.selenium_proxy())
   #profile.accept_untrusted_certs = True
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.set_page_load_timeout(30)
    proxy.new_har()

    try:
        driver.get(web)
    except:
        print "Error"
        
        server.stop()
        driver.quit()
        continue
    else:
        proxy.har
    	tliveime.sleep(20) 
        filename='ad_fx_httpdata6/'+str(i)+'.har'
    
        out_f = open(filename, 'w')
        json.dump(proxy.har, out_f)
        out_f.close()
    
        driver.quit()
    

server.stop()
display.stop()  

