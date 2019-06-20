6# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
name='Lin Lin'
print('Hello my name is {}'.format(name))
number='12'
print('Hello my name is {x} and my number is {y}'.format(x=name,y=number))

hrs = input("Enter Hours:")
rate= input("Enter Rate:")
Pay=float(hrs)*float(rate)
print('Pay:',Pay)
#Python Data Structure
# '7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
# 'and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# 'You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
fname = input("Enter file name: ")# code3-word.txt
fh = open(fname)
for line in fh:# any variable in fh. such as line. l. m....
    line=line.rstrip()#remove white space line
    print(line.upper())
    
#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:    
    #X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution.
# Use the file name mbox-short.txt as the file name
    
fname = input("Enter file name: ")#mbox-short.txt
fh = open(fname)
spam_confidence=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count=count+1
    line_pos=line.find(':')
    line_num=line[line_pos+1:]
    line_num=float(line_num.lstrip())
    spam_confidence=spam_confidence+line_num
    #print(line)
#print("Done")
print('Average spam confidence:',round(spam_confidence/count,12))#Keep 12 certain digits

#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")#romeo.txt
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()#delete blank/space row in next
    #print(line)
    words=line.split()#first read by line;one line has seperate words; 
    #print(words)
    for word in words:
        if word not in lst:
            lst.append(word)
            #print(lst)
lst.sort()
print(lst)#really important cannot directly use print(lst.sort())

#Open the file mbox-short.txt and read it line by line. 
#When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line 
#(i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#Method1 with If and not
fname = input("Enter file name: ")#mbox-short.txt
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        count=count+1
        line=line.rstrip()
        words=line.split()
        print(words[1])#directly print out the email result
print("There were", count, "lines in the file with From as the first word")
#  Method 2.1 with continue
fname = input("Enter file name: ")#mbox-short.txt
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From"):
        line=line.rstrip()
        words=line.split()
        #count=count+1 #54 lines start both with 'From' and 'From:'
        if len(words)<1: #if words is blank-with nothing, words[0] will be out of range
            continue  #continue means'skip it and returns back to top to do loop
        if words[0]!="From":
            continue
        count=count+1 #27 lines only start with 'From'
        print(words[1])#directly print out the email result
print("There were", count, "lines in the file with From as the first word")
#  Method 2.2 with continue
fname = input("Enter file name: ")#mbox-short.txt
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From"):
        line=line.rstrip()
        if line=='':
            print('Skip Blank')
            continue
        words=line.split()
        #count=count+1 #54 lines start both with 'From' and 'From:'
        if words[0]!="From":
            continue
        count=count+1 #27 lines only start with 'From'
        print(words[1])#directly print out the email result
print("There were", count, "lines in the file with From as the first word")
#  Method 2.3 guardian in a compound statement
fname = input("Enter file name: ")#mbox-short.txt
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From"):
        line=line.rstrip()
        words=line.split()
        #count=count+1 #54 lines start both with 'From' and 'From:'
        if len(words)<3 or words[0]!="From": #sequence is really important-guardian before index[0]
            continue
        count=count+1 #27 lines only start with 'From'
        print(words[1])#directly print out the email result
print("There were", count, "lines in the file with From as the first word")
# Method 3 with the [] as a list inside
fname = input("Enter file name: ")#mbox-short.txt
if len(fname) < 1 : fname = "mbox-short.txt"
lst=list()
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        count=count+1
        line=line.rstrip()
        words=line.split()
        lst.append(words[1])
print(lst)
print("There were", count, "lines in the file with From as the first word")

#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:") # mbox-short.txt
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    if line.startswith("From "):#Even little change can affect lots of things-have added space
        line=line.rstrip()
        words=line.split()
        words=words[1]
        print(words)
        counts[words]=counts.get(words,0)+1
        print(counts.items())

bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)#cwen@iupui.edu 5 add  if line.startswith("From ") or line.startswith("From:"): result is cwen@iupui.edu 10

# Method1-Try in video using clown.txt
fname=input('Enter File: ')
if len(fname)<1: fname='clown.txt'
hand=open(fname)

di=dict()#using collection as index-list use value as index
for lin in hand:
    lin=lin.rstrip()
    #print(lin)
    wds=lin.split()
    #print(wds)
    for w in wds:
        if w in di:
            di[w]=di[w]+1
            print('**Existing**')
        else:
            di[w]=1
            print('**NEW**')
        print(di[w])#print count
print(di)#    print collection-and value
    
# Method2-Try in video using clown.txt
fname=input('Enter File: ')
if len(fname)<1: fname='clown.txt'
hand=open(fname)

di=dict()#using collection as index-list use value as index
for lin in hand:
    lin=lin.rstrip()
    #print(lin)
    wds=lin.split()
    #print(wds)
    for w in wds:
        # if the key is not there the count is zero
        oldcount=di.get(w,0)#if word is new and doesn't exist before, set the default value zero
        print(w,'old',oldcount)
        newcount=oldcount+1
        di[w]=newcount#set the certain word in dictionary to a value(how many word appears)
        print(w,'new',newcount)
print(di)#    print collection-and value 
 
# Method3-Try in video using clown.txt
fname=input('Enter File: ')
if len(fname)<1: fname='clown.txt'
hand=open(fname)

di=dict()#using collection as index-list use value as index
for lin in hand:
    lin=lin.rstrip()
    #print(lin)
    wds=lin.split()
    #print(wds)
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w]=di.get(w,0)+1
        #print(w,'new',di[w])
print(di)#    print collection-and value  

# now we want to find the most common word
largest=-1
theword =None
for k,v in di.items():#key and values
    print(k,v)
    if v>largest:
        largest=v
        theword=k# capture/remember the word that was largest
print('Done',theword,largest)
#

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])

#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")#mbox-short.txt
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts={}
for line in handle:
    if line.startswith("From "):
        line=line.rstrip()
        pos=line.find(':')
        hrs=line[pos-2:pos]
        counts[hrs]=counts.get(hrs,0)+1
print(counts)
for (k,v) in sorted(counts.items()):
    print(k,v)
print( sorted( [ (v,k) for k,v in counts.items() ] ) )

#Extension example
#Try in video using clown.txt
fname=input('Enter File: ')
if len(fname)<1: fname='clown.txt'
hand=open(fname)

di=dict()#using collection as index-list use value as index
for lin in hand:
    lin=lin.rstrip()
    #print(lin)
    wds=lin.split()
    #print(wds)
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w]=di.get(w,0)+1
        #print(w,'new',di[w])
print(di)#    print collection-and value  

tmp=list()
for k,v in di.items():
    #print(k,v)
    newt=(v,k)
    tmp.append(newt)
print('Flipped',tmp)#we have a list flipped to a tuple thing

tmp=sorted(tmp,reverse=True)#it is sorted by tuple-v and k-reverse from highest to lowest
print('Sorted',tmp[:5])# no ',' in between

for v,k in tmp[:5]:
    print(k,v)
# https://walletinvestor.com/commodity-forecast/wheat-prediction
    
## Using Python to Access Web Data
#Before you can use regular expressions in your program, 
#you must import the library using “import re”
import re
#
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos=data.find('@')
print(atpos)

sppos=data.find(' ',atpos)#logic there is return default value is atpos, continue to find the space after atpos
print(sppos)

host=data[atpos+1:sppos]
print(host)
# or try
words=data.split()
email=words[1]
pieces=email.split('@')
print(pieces[1])
#or using Regex Version
import re
y=re.findall('@([^ ]*)',data)
print(y)

y=re.findall('^From .*@([^ ]*)',data)
print(y)

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))


x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y=re.findall('\S+?@\S+',x)

## test data set is 'regex_sum_42.txt';real dataset is 'regex_sum_196942.txt'
import re
fname=input('Enter File: ')
if len(fname)<1: fname='regex_sum_42.txt'
hand=open(fname)
count=0
nums=dict()#using collection as index-list use value as index
int_nums=dict()
sum_all=0
for lin in hand:
    lin=lin.rstrip()
    #print(lin)
    #words=lin.split()
    nums=re.findall('[0-9]+',lin)
    print(nums)
    if len(nums):
        for i in range(0,len(nums)):
            #count=count+1
            #print(count) 90
            nums[i]=int(nums[i])
            #print(int_nums)
            sum_nums=sum(filter(lambda i: isinstance(i,int),nums))
        sum_all+=sum_nums#logic
            #nums=str(nums)
print(sum_all)

#
import re
fname=input('Enter File: ')
if len(fname)<1: fname='regex_sum_196942.txt'
hand=open(fname)
count=0
nums=dict()#using collection as index-list use value as index
int_nums=dict()
sum_all=0
for lin in hand:
    lin=lin.rstrip()
    #print(lin)
    #words=lin.split()
    nums=re.findall('[0-9]+',lin)
    print(nums)
    if len(nums):
        for i in range(0,len(nums)):
            #count=count+1
            #print(count) 90
            nums[i]=int(nums[i])
            #print(int_nums)
            sum_nums=sum(filter(lambda i: isinstance(i,int),nums))#add within one line
        sum_all+=sum_nums#logic
            #nums=str(nums)
print(sum_all)

#OTHER METHODS
import re
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

#An HTTP Request in Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close()


## Parsing Web Pages
##python urllinks.py 
#Enter - http://www.dr-chuck.com/page1.htm
#http://www.dr-chuck.com/page2.htm

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
#
print(ord('i'))

##
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    
############ Sum
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')# http://py4e-data.dr-chuck.net/comments_42.html; http://py4e-data.dr-chuck.net/comments_196944.html
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
sum_tags=0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    sum_tags+=int(tag.contents[0])
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    print('Sum:',sum_tags)
###########
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')#http://py4e-data.dr-chuck.net/known_by_Fikret.html; http://py4e-data.dr-chuck.net/known_by_Marcous.html 
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

#####################
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')#http://py4e-data.dr-chuck.net/known_by_Fikret.html; http://py4e-data.dr-chuck.net/known_by_Marcous.html 
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

for tag in tags:
    print(tag.get('href', None))
## my  Retrieve all of the anchor tags
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count=input('Enter a count-')
count=int(count)
position=input('Enter a position-')
position=int(position)
url_1 = input('Enter - ')#http://py4e-data.dr-chuck.net/known_by_Fikret.html; http://py4e-data.dr-chuck.net/known_by_Marcous.html 
for i in range(count):
    if i==0:
        url=url_1
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        print('Retrieving i:',i,url_1)
    else:
        url=tags[position-1].get('href', None)
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        print('Retrieving i:',i,tags[position-1].get('href', None))
###
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
n=1
url = input('Enter - ')
count= int(input('Enter count'))+1
pos=int(input('Enter position'))
new=url

while n<count:
    if new == url:
        html = urllib.request.urlopen(url, context=ctx).read()
        print('Retrieving', url)
    html = urllib.request.urlopen(new, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    my_tags=tags[pos-1]
    new=my_tags.get('href', None)
    print('Retrieving' , new)
    n=n+1

## http://py4e-data.dr-chuck.net/comments_42.xml; http://py4e-data.dr-chuck.net/comments_196946.xml
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
    
## My http://py4e-data.dr-chuck.net/comments_42.xml; http://py4e-data.dr-chuck.net/comments_196946.xml
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input(' Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum_all=0

for i in range(len(counts)):
    sum_all+=int(counts[i].text) #direct write count.text can get integer
print(len(counts),sum_all)
    

### Method 2 http://py4e-data.dr-chuck.net/comments_42.xml; http://py4e-data.dr-chuck.net/comments_196946.xml
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input(' Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
results = tree.findall('.//count')
iterations = 0
total = 0

#Loop all items in the list
for item in results:
    iterations = iterations + 1
    #Gets the text value from the tag count
    total = total + int(item.text)    
print("Count:",iterations)
print("Sum:",total)
##
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
##
## My Sum with JSON
##  http://py4e-data.dr-chuck.net/comments_42.json; http://py4e-data.dr-chuck.net/comments_196947.json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input(' Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print(data)
print('Retrieved', len(data), 'characters')
print(data.decode())
count_all=0

info = json.loads(data.decode())#can also be original (data)
print('User count:', len(info))
for item in info['comments']:
    #print(item['count'])
    count_all+=int(item['count'])
print(len(info['comments']),count_all)

##My- JSON API- South Federal University; Malayer Azad University
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        #print(data)
        continue
    place_id=js['results'][0]['place_id']
    print('place_id',place_id)

##Other method
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
address = input('Enter location: ')
#address = "South Federal University"
#address = "University of Chicago"

url = serviceurl + urllib.parse.urlencode({'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
try:
   js = json.loads(data)
   print("Place id",js["results"][0]["place_id"])
except:
    js = None  
    print('==== Failure To Retrieve ====')

######## mbox.txt
import sqlite3

conn = sqlite3.connect('new_emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    repieces=email.split('@')
    org=repieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
#sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

table='SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(table):
    print(str(row[0]), row[1])

cur.close()

#######My-fix
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('new_trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;


CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
DELETE FROM Artist;
DELETE FROM Genre;
DELETE FROM Album;
DELETE FROM Track
''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue
    if ( lookup(entry, 'Genre') is None ) : continue#

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry,'Genre')

    if name is None or artist is None or album is None : 
        continue

    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ? )''', 
        ( name, album_id, length, rating, count ) )

    conn.commit()

##################
import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    user = entry[0];
    course = entry[1];
    role=entry[2];

    print((user,course,role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( user, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (user, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( course, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (course, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id,role) VALUES ( ?, ? ,?)''',
        ( user_id, course_id,role ) )

    conn.commit()



