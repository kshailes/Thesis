import re
import urllib2
import urllib
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

f=open('foxnewslinks.txt','rU')
#result=f.read()


#pat= '\<div\sclass\=\"cnn\-search\_\_result\-body\"\>(.*?)\<\/div\>'
# pat = '\<div\sclass\=\"article\-text\"\>(.*?)\<p\>(.*?)\<\/p\>'
# result = 'http://www.foxnews.com/transcript/2016/07/06/lawmakers-not-finished-with-hillary-clinton-email-scandal.html'
# # i = 1
# data = urllib.urlopen(result).read()
# # match = re.findall(pat, data.read(),flags= re.DOTALL)
# # for m in match:
# # 	print m

# soup= BeautifulSoup(data)
# letters= soup.find_all("div", class_="article-text")
# d= letters[0].find_all("p")
# for l in d:
# 	print l.get_text()

i=1
for line in f:
	data = urllib.urlopen(line).read()
	soup= BeautifulSoup(data)
	#letters= soup.find("div", class_="article-text")
	d= soup.find_all("p")
	allp=""
	for l in d:
		allp=allp+l.get_text()	
	filename='mission/foxemailscandals/doc'+str(i+10)+'.txt'
	f=open(filename,'w')
	f.write(allp)
	f.close()
	i=i+1

# pat='\<span\>(.*?)\<\/span\>'


# match = re.findall(pat, result,flags= re.DOTALL) #flag is used for multiline data.if single line flag=0

# dates=[]
# for m in match:
# 	dates.append(m)

# #print dates

# pat= '\<p\>(.*?)\<\/div\>'

# match = re.findall(pat, result,flags= re.DOTALL) #flag is used for multiline data.if single line flag=0


# i=1

# for m in match:
# 	#print m
# 	filename='mission/foxemailscandals/doc'+str(i+10)+'.txt'
# 	f=open(filename,'w')
# 	f.write(dates[i-1])
# 	f.write(m)
# 	f.close()
# 	i=i+1

