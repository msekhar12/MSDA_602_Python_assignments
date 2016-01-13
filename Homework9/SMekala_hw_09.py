import pandas as pd
from pandas import Series,DataFrame
import math
import os
import csv
import re
import sys

def clear_scr():
    '''Clears the screen
    '''
#To accommodate all Operating systems, I am using 2 commands
    try:
        unused_var = os.system('clear')
        unused_var = os.system('cls')
    except:
        pass

def read_file():
    '''Reads the supplied file, and returns a DataFrame'''
    clear_scr()

    s = raw_input("\nEnter File location. To quit, press ENTER on blank input\n ==>")    

    while True:
        if s == '':
            print '\n\nGood Bye'
            sys.exit()
        
        try:
            file_reader = csv.reader(open(s),delimiter = ' ', quoting = csv.QUOTE_NONE)
        except:
            print "\nThe given file location is incorrect. Enter file's location (complete path) again or EXIT to quit\n"
            s = raw_input("==>")
            continue
        else:
            break

    origin = list()
    day = list()
    hour = list()
    minute = list()
    second = list()
    req_type = list()
    url = list()
    retcode = list()
    bytes_transferred = list()
    
    for line in file_reader:
        origin.append(line[0])

        dt = re.match(r'(.*):(.*):(.*):(.*)',re.sub(r'\[|\]','',line[1]))
        day.append(dt.group(1))
        hour.append(dt.group(2))
        minute.append(dt.group(3))
        second.append(dt.group(4))

        req = re.sub(r'\"| *','',line[2])
        req_type.append(req)
        if line[-1] == '-':
            bytes_transferred.append(long(0))
        else:
            bytes_transferred.append(long(line[-1]))


        retcode.append(int(line[-2]))
        l = len(line)
        u = re.sub(r'\"','',line[3])
        if (l > 7):
            #(l - 3), to avoid HTTP/1.0 text
            ul = line[4:(l-3)]
            ul = " ".join(ul)
            url.append(u +" "+ ul)
        else:
            url.append(u)
        
    df = DataFrame()
    

    df['origin'] = origin
    df['day'] = day
    df['hour'] = hour
    df['minute'] = minute
    df['second'] = second
    df['req_type'] = req_type
    df['url'] = url
    df['retcode'] = retcode
    df['bytes_transferred'] = bytes_transferred
    return (df)


if __name__ == '__main__':

    #Read the file first!!
    HTTP_DF =  read_file()

    
    l = Series((HTTP_DF['origin']))
    l = l.value_counts()

    clear_scr()
    
    print "\n"
    print "Questions"
    print "---------"
    print "Question:1."
    print "-----------"
    print "Which hostname or IP address made the most requests?"
    print "Answer:"
    print "-------"
    print "The MAXIMUM number of requests were made by '%s'.\nFrom this address, a total of %d requests were made" % (l.idxmax(),l.max())
    print "\n"

    l = HTTP_DF.groupby(['origin'])['bytes_transferred'].sum()
    print "Question:2."
    print "-----------"
    print "Which hostname or IP address received the most total bytes from the server?  How many bytes did it receive?"
    print "Answer:"
    print "-------"
    print "The MAXIMUM number of bytes were received by '%s'. This address has received a total of %d bytes." % (l.idxmax(), l.max())
    print "\n"
    

    l = Series((HTTP_DF['hour']))
    l = l.value_counts()

    print "Question:3."
    print "-----------"
    print "During what hour was the server the busiest in terms of requests?"
    print "Answer:"
    print "-------"
    print "The MAXIMUM number of requests were made in the hour '%s'.\nIn this hour, a total of %d requests were made" % (l.idxmax(),l.max())

    l = HTTP_DF[HTTP_DF['url'].str.contains('.gif',case=False)]['url']
    l = l.value_counts()
    print "\n"
  
    print "Question:4."
    print "-----------"
    print "Which .gif image was downloaded the most during the day?"
    print "Answer:"
    print "-------"
    print "The MAXIMUM number of downloads were made for the image '%s'.\nThis image was downloaded %d times" % (l.idxmax(),l.max())    

    l = HTTP_DF[HTTP_DF['retcode'] != 200]['retcode']
    
    print "\n"
    print "Question:5."
    print "-----------"
    print "What HTTP reply codes were sent other than 200?"
    print "Answer:"
    print "-------"
    print "The following return codes (other than 200) wrere sent:"
    print l.unique()
