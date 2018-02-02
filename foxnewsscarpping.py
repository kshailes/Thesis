import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html 
import re

import time
#Take this class for granted.Just use result of rendering.


class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

all_links=[]

# for i in range(10):
url = "http://www.foxnews.com/search-results/search?q=clinton%20email%20scandal&ss=fn&type=story&start=60"
r = Render(url)  
result = r.frame.toHtml()
formatted_result = str(result.toAscii())
tree = html.fromstring(formatted_result)
links=tree.xpath('//a[@ng-bind="article.title"]/@href')
print links
all_links.extend(links)
	#time.sleep(5)
	
###########writing to a file
print "file"
htmlpage='foxnewslinks.txt'
f=open(htmlpage,'a')
for l in all_links:
	f.write(l)
	f.write("\n")
f.close()
print "done"
#Now using correct Xpath we are fetching URL of archives



#Next build lxml tree from formatted_result


#Now using correct Xpath we are fetching URL of archives
#archive_links = tree.xpath('//divass="campaign"]/a/@href')
#print archive_links




#<a ng-bind="article.title" ng-href="http://www.foxnews.com/opinion/2017/09/05/michael-goodwin-case-for-special-counsel-to-investigate-hillary-clinton.html" class="ng-binding" href="http://#www.foxnews.com/opinion/2017/09/05/michael-goodwin-case-for-special-counsel-to-investigate-hillary-clinton.html">Michael Goodwin: The case for a special counsel to investigate Hillary Clinton</a>

#attribute::lang

#//a[@class='specified_string']/@href
