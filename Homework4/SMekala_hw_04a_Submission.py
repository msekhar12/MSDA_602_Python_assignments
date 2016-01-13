#The user is prompted to enter a URL. He can choose NOT to enter any URL by pressing ENTER on blank input, and by default a wikipedia page is parsed
#Reading a wikipedia.com page, on the topic Peafowl bird (by default)

#Make sure that you copy the alchemyAPI key to the directory, where you stored this file, and executing this program

#Importing the required packages:

import bs4
import urllib2
import re

from alchemyapi import AlchemyAPI
import json

alchemyapi = AlchemyAPI()

#We will be reading content of a wikipedia page on peafowl (peacock bird)

text_extracted = ''

while True:
  try:
     print "\n\nEnter the URL to parse.".center(50," ")
     print "        ** Press ENTER for default. By default the following URL is parsed:"
     print "           https://en.wikipedia.org/wiki/Peafowl (a topic on peacocks)"
     url = raw_input("\nEnter the URL or Press ENTER for default URL==>")

     if url == '': url = "https://en.wikipedia.org/wiki/Peafowl"
     page = urllib2.urlopen(url)
  except:
     print "\n\nIncorrect URL / Connection problem"
  else:
     break


soup = bs4.BeautifulSoup(page.read())
page.close()

#All the text data is conained in between <p> and </p> tags

paragraphs = soup.findAll('p')

#Using regular expressions, replacing the text between []
#Finally the modified text is collected to a string variable

for p in paragraphs:
    s = re.sub(r"\[.*\]","", p.text.encode("utf-8"))
    #text_extracted = text_extracted + p.text.encode("utf-8")
    text_extracted = text_extracted + s


#The following 3 commented lines can be used for debugging, to check what is contained in the text_extracted variable, by directing its contents to a file named "para_txt" file
#paragraphs_txt = open("para_txt.txt","w")
#paragraphs_txt.write(text_extracted)
#paragraphs_txt.close()


demo_text = text_extracted

#The following lines of code was given in example.py of alchemyapi module. Modifying this further for our requirement ...

print '\n\n'
print "URL Source: " + url


print '\n\nProcessed the following text'
print '--------- --- --------- ----\n\n'
print demo_text +'\n\n'


print '\n'

print '############################################'.center(80," ")
print '#              Top 10 Keywords             #'.center(80," ")
print '############################################'.center(80," ")


response = alchemyapi.keywords('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':

    print '\n'
    print "="*80
    print "Keyword".center(50," ") + "Relevance".center(10," ") + "Sentiment".center(10," ") + "Score".center(10," ")
    print "="*80
    i = 0
    for keyword in response['keywords']:
        i += 1
        if i > 10: break
        if 'score' in keyword['sentiment']:
           print keyword['text'].encode('utf-8').center(50, " ") + str(keyword['relevance']).center(10, " ") + str(keyword['sentiment']['type']).center(10, " ")+str(keyword['sentiment']['score']).center(10," ")
        else:
           print keyword['text'].encode('utf-8').center(50, " ") + str(keyword['relevance']).center(10, " ") + str(keyword['sentiment']['type']).center(10, " ")+"------".center(10," ")
    print "="*80
         
        
        #print 'text: ' + keyword['text'].encode('utf-8')
        
        #print 'relevance: ' + keyword['relevance']
        #print 'sentiment: ' + keyword['sentiment']['type']
        #if 'score' in keyword['sentiment']:
        #    print 'sentiment score: ' + keyword['sentiment']['score']
        #print '\n'
else:
    print 'Error in keyword extaction call: ' + response['statusInfo']

