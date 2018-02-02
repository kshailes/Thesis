import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html 
import re
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

# url = 'http://edition.cnn.com/search/?q=clinton%20email%20scandal&size=10&sort=relevance&type=article'  
# r = Render(url)  
# result = r.frame.toHtml()

###########writing to a file

# htmlpage='searchpage1.html'
# f=open(htmlpage,'w')
# f.write(result)
# f.close()


#for i in range(2,11):
url= 'http://edition.cnn.com/search/?q=clinton%20email%20scandal&size=100&page=2&from=10&sort=relevance&type=article'
r=Render(url)
result=r.frame.toHtml()
htmlpage='searchpage'+str(2)+'.html'
f=open(htmlpage,'w')
f.write(result)
f.close()
print 'file written'





#Now using correct Xpath we are fetching URL of archives
# archive_links = tree.xpath('//divass="campaign"]/a/@href')
# print archive_links