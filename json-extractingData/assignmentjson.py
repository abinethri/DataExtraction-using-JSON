# sample assignment extracting data from json 

import urllib
import json

url = raw_input("Enter a url: ")
if len(url)<1: url = "http://python-data.dr-chuck.net/comments_42.json"

urlhand = urllib.urlopen(url)
print "Retrieving ", url
data = urlhand.read()
print "Retrieved", len(data), 'characters'
#print "type of data:",type(data)
info = json.loads(data)
print "Type of info:",type(info)

summation = 0
for item in info['comments']:
    print "Count:", item['count']
    #print type(item['count'])
    summation = item['count']+ summation  
    
print "Sum Of Comment Counts: ", summation

    

