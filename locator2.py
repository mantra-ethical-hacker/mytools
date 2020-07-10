import os 
import urllib2
import json

while True:
       ip = input(" Enter the target IP : ")
       url = "http://ip-api.com/json/"
       response = urllib2.urlopen(url + ip) 
       data = response.read()
       values = json.loads(data)
       
       print(" IP " + values['query'])
       print(" City " + values['city'])
       print(" ISP " + values['isp'])
       print(" Country " + values['counrty'])
       print(" Region " + values['region'])
       print(" Time Zone " + values['timezone'])
       
       break
       