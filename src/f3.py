#!/usr/bin/env python

# importing the necessary module
import sys


from collections import defaultdict
import linecache
import time
import re


lasttime = 0
samecount = 0
targetoutside = 0
add1 = 0
countdict = defaultdict(int)


def timeatline(linenumber, input_path):
    line1 = linecache.getline(input_path, linenumber)
    timestring = re.findall(r'\d{2}[-/]\w{3}[-/]\d{4}:\d{2}:\d{2}:\d{2}', line1)
    pattern = '%d/%b/%Y:%H:%M:%S'
    timeatline1 = int(time.mktime(time.strptime(timestring[0], pattern)))

    return timeatline1


def countreq(k,timeatline,target, input_path): #Function for defined elements on the list of timestamps.
    targetoutside = 0
    countdict = defaultdict(int)
    line1 = linecache.getline(input_path, k)
    timestring = re.findall(r'\d{2}[-/]\w{3}[-/]\d{4}:\d{2}:\d{2}:\d{2}', line1)
    pattern = '%d/%b/%Y:%H:%M:%S'
    newtime = int(time.mktime(time.strptime(timestring[0], pattern)))


    lenfile = sum(1 for line in open(input_path))
    middle = (lenfile - k) / 2 + k
    lenfile2 = lenfile
    start = k
    add1 = 0
    i=0
    lasttime = 0
    if(k==1):
        lasttime=0
    else:
        lasttime = timeatline(k-1, input_path)

    samecount = 0
    k2 = k

    if(newtime==lasttime):
        for k2 in reversed(range(1,k+1)):
            if timeatline(k2,input_path)==timeatline(k2-1,input_path):
                samecount += 1
            else:
                k = k2
                break
            k2 -=1

    for i in range(lenfile+1):

        if (timeatline(middle,input_path) <= target):
            start = middle

            middle = (lenfile2 - middle) / 2 + start

        elif (timeatline(middle,input_path) > target):
            lenfile2 = middle
            
            middle = (lenfile2 - start) / 2 + start


        if (middle) == lenfile:
            countdict[newtime] = middle - k + 1
            finalval = middle - k + 1
            break

        if ((target >= timeatline(lenfile,input_path)) and middle == lenfile - 1):
            targetoutside = 1
            add1 = 1


        if (((timeatline(middle,input_path) <= target) and (timeatline(middle + 1,input_path) > target)) or targetoutside == 1):


            finalval = middle - k + 1 + add1
            countdict[newtime] = middle - k + 1 + add1
            add1 = 0
            targetoutside = 0

            break

    


    return finalval


def findnextelement(timevalue,timeatline,input_path):   #The function finds the next element which is in the file
    n=0
    lenfil = sum(1 for line in open(input_path))
    for n in range(1,lenfil+1):
        if timeatline(n,input_path)==timevalue:
            break
        if timeatline(n,input_path)>timevalue:
            break
    return n



def write_to_file(output_path, data):
    ####Writing to a File
    file = open(output_path, 'w+')
    for item in data:
        print>> file, item
    

    
def compute(input_path, output_path):
    next= 0
    newtime = timeatline(1,input_path)
    lenfile = sum(1 for line in open(input_path))

    while newtime<timeatline(lenfile,input_path):
        next = findnextelement(newtime,timeatline, input_path)

        target = newtime + 3600
        count = countreq(next,timeatline,target,input_path)
        countdict[newtime] = count

        newtime += 1


    keys = sorted(countdict, key=lambda key: countdict[key], reverse=True)[:10]
    values = [countdict[key] for key in keys]

    ranked = []
    for i1 in range(len(keys)):
        ranked.append(time.strftime("%d/%b/%Y:%H:%M:%S", time.gmtime(keys[i1]-18000)))

    for i in range(len(ranked)):
        ranked[i]=ranked[i]+" -0400"+","+str(values[i])

    write_to_file(output_path,ranked)
    

def main(argv):
    input_path = argv[1]
    output_path = argv[2]
    
    compute(input_path,output_path)
    

if __name__ == "__main__":
    main(sys.argv)




