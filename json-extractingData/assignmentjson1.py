#extracting data from json 
#actual assignment

import urllib
import json
 
while True:
    print "Enter a url or print 'done' at user prompt to exit"
    url = raw_input("Enter a url: ")
  
    if len(url)<1: url = "http://python-data.dr-chuck.net/comments_350984.json"
    
    if url == 'done': break 
    
    print "Retrieving", url
    urlhand = urllib.urlopen(url)
    data = urlhand.read()
    #print "type of data:",type(data)
    print "Retrieved", len(data), 'characters'
    info = json.loads(data)
    #print "Type of info:",type(info)
    
    summation = 0
    for item in info['comments']:
        print "Count:", item['count']
        #print type(item['count'])
        summation = item['count']+ summation  
    
    print "Sum Of Comment Counts: ", summation
    
