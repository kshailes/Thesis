import re

f=open('searchpage2.html','rU')
result=f.read()


#pat= '\<div\sclass\=\"cnn\-search\_\_result\-body\"\>(.*?)\<\/div\>'


pat='\<span\>(.*?)\<\/span\>'


match = re.findall(pat, result,flags= re.DOTALL) #flag is used for multiline data.if single line flag=0

dates=[]
for m in match:
	dates.append(m)

#print dates

pat= '\<div\sclass\=\"cnn\-search\_\_result\-body\"\>(.*?)\<\/div\>'

match = re.findall(pat, result,flags= re.DOTALL) #flag is used for multiline data.if single line flag=0


i=1

for m in match:
	#print m
	filename='emailscandals/doc'+str(i+10)+'.txt'
	f=open(filename,'w')
	f.write(dates[i-1])
	f.write(m)
	f.close()
	i=i+1

