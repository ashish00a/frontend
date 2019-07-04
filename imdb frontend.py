#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import re

query=raw_input("Movie Name\n")
keywords=query.split(" ")
q=""
for key in keywords:
	q=q+key+"+"

# print q[0:len(q)-1]

search="http://www.imdb.com/find?ref_=nv_sr_fn&q="+q[0:len(q)-1]+"&s=all"

# print search

page = urllib2.urlopen(search)
soup = BeautifulSoup(page, "lxml")

# soup.prettify("utf-8")
# listedResult=soup.find_all('td', class_="result_text")
# for link in soup.findAll('a'):
#     print link.get('href')
# <tr class="findResult odd"> 
# 	<td class="primary_photo"> 
# 		<a href="/title/tt1023111/?ref_=fn_al_tt_1">
# 			<img src="https://ia.media-imdb.com/images/M/MV5BMTkzNDg3MTIyMF5BMl5BanBnXkFtZTcwOTAwNDc1MQ@@._V1_UX32_CR0,0,32,44_AL_.jpg"/>
# 		</a>
# 	</td>
# 	<td class="result_text">
# 		<a href="/title/tt1023111/?ref_=fn_al_tt_1">
# 			Never Back Down
# 		</a> 
# 		(2008) 
# 	</td>
# </tr>

i=0;
List=[]
for item in soup.find_all('td', class_="result_text"):
	try:
		x=item.find('a', attrs={'href': re.compile("^/title")}).get("href")
		List.append(x)
		# print x
		# l[i]=x
	except Exception as e:
		continue
	else:
		pass
	
# print len(List)
if len(List)>0:
	print str(len(List))+" Entries Found \n"
	if len(List)>3:
		print "Showing the top 3\n"
else:
	print "No Result Found, Try a different keywords"
	exit(0)
print "############################################################"
for l in List:
	i=i+1
	s="http://www.imdb.com"+str(l)
	# print s
	page = urllib2.urlopen(s)
	soup = BeautifulSoup(page, "lxml")
	if soup.title is not None:
		print "\nTitle: " +soup.title.text # title and year
	if soup.find('div', class_="ratingValue") is not None:
		print "IMDB Ratings: " +soup.find('div', class_="ratingValue").text.lstrip()
	
	detail= soup.find('div', class_="title_wrapper")
	# print detail.find('h1').text # year
	if detail.find('div', class_="subtext").find('time') is not None:
		time=detail.find('div', class_="subtext").find('time').text
		print "Duration: "+time.rstrip().lstrip()
	genres=detail.find('div', class_="subtext").find_all('a')
	if len(genres)>0:
		print "Genres:"
		for genre in genres:
			print genre.text
	print "############################################################"
	if i > 2:
		break;
	
