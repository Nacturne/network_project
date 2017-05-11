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
webslist = [line.rstrip('\r\n') for line in open('add_Top500News.txt')]
startval = 0# sys.argv[1]
endval = 500# sys.argv[2]
list =[i for i in range (int(startval),int(endval))]
#shuffle(list)
'''
try:
    os.state('httpdata1/')
except:
    os.makedirs('httpdata1/')
'''

log = open('httpdata22/testlog','a+')

server = Server("browsermob-proxy-2.1.4/bin/browsermob-proxy")
server.start()

for i in list:
    if i%2 == 0:
        time.sleep(20)
   

    proxy = server.create_proxy()
    print i+1, str(webslist[i])
    log.write(str(i+1)+str(webslist[i])+'\n')    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
    
    driver = webdriver.Chrome(chrome_options = chrome_options)
    driver.set_page_load_timeout(60)
    proxy.new_har()
    
    web = webslist[i]

    try:
        driver.get(web)
    except:
        print "Error"
        log.write('Error\n')
        driver.quit()
        continue
    else:
        proxy.har
        filename='httpdata22/'+str(i)+'.har'
    
        out_f = open(filename, 'w')
        json.dump(proxy.har, out_f)
        out_f.close()            
        driver.quit()

server.stop()    
display.stop()  
log.close()
