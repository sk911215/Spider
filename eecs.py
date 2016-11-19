# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

url = 'http://web.engr.oregonstate.edu/~walkiner/teaching/cs581-fa16/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<h2 id=.*?">(.*?)</h2>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item+'\n'
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason