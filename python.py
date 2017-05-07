import json
import numpy as np
import re
from  urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.error
import urllib
import datetime
import time
import random
import os 

getdir = r'G:/text/downlond5'
pages = set()
pageUrl = 28

def getlinks(pageUrl):
	global pages
	pageUrl = str(pageUrl)
	url = 'http://jandan.net/ooxx/page-' + pageUrl + '#comments'
	#html = urlopen(url) 

	lista = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'),
			('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'),
			('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'),
			('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'),
			('User-Agent','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'),
			('User-Agent','Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'),
			('User-Agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'),
			('User-Agent','Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5')]
	headers = lista[random.randint(0,7)]
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	html = opener.open(url)
	bsobjpg = BeautifulSoup(html,'lxml')
	for link in bsobjpg.find('ol',{'class':'commentlist'}).findAll('img',src=re.compile('^(//wx[1-9].sinaimg.cn)')):
		if link.attrs['src'] not in pages:
			imglink = link.attrs['src']
			print(imglink)
			pages.add(imglink)
			sock =urlopen('http:'+imglink)
			dataimg = sock.read(10000000)
			#urllib.request.urlretrieve(url+imglink,getdir + '/' + '%s.jpg' % str(random.randint(1,10000)))
			filename = getdir + '/' + str(random.randint(1,10000)) + '.jpg'
			f = open(filename,'wb')
			f.write(dataimg)
			f.close()
			time.sleep(1)
	print('the page:' + pageUrl)
	print(type(pageUrl))
	print(pageUrl+ ' pages is over ')
	pageUrl = int(pageUrl)
	print(type(pageUrl))
	try:
		if pageUrl>1:
			pageUrl = pageUrl-1
			getlinks(pageUrl)
	except:
		pass
	finally:
		print('you have got all of the girl img')

getlinks(pageUrl)
