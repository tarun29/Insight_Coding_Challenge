#!/usr/bin/env python

# importing the necessary module
import sys
#Feature 4

import time
import re
import linecache
from collections import defaultdict
d = defaultdict(int)

onetime=0
beingchecked=0


loggedtimestamps = []


def write_to_file(output_path, data):
     ####Write to a File
    file = open(output_path, 'w+')
    for item in data:
        print>> file, item
    ############################

def compute(input_path, output_path):
    globalupdatetime = 0
    
    with open(input_path) as ins:
        for line in ins:
            
            checkiflogin =  line.rsplit(' ', 5)[1][1:]  #Checks if a login has been attempted
            if checkiflogin=="POST":
                httpreplycode = line.rsplit(' ', 2)[1]  # Http Reply code
                timestamp1 = re.findall(r'\d{2}[-/]\w{3}[-/]\d{4}:\d{2}:\d{2}:\d{2}', line)
                pattern = '%d/%b/%Y:%H:%M:%S'
                newtime = int(time.mktime(time.strptime(timestamp1[0], pattern)))  # Timestamp
                if (newtime-globalupdatetime)>300:
                    beingchecked = 0


                if httpreplycode=="200" and (beingchecked==0):
                   print
                else:


                    hostname = line.split(' ', 1)[0]  # Host name


                    if hostname not in d:
                        d[hostname] = [0, 0, 0, 0,
                                       0]  # 5 values are: Count, newtime, FirstOccurencetime(foc), unblock time, http reply code

                    d[hostname][1] = newtime
                    d[hostname][4] = httpreplycode


                    if (d[hostname][1] > d[hostname][3]) or (d[hostname][3] == 0):
                        if (d[hostname][
                                2] == 0):  
                            d[hostname][2] = d[hostname][1]

                        if (d[hostname][1] - d[hostname][2]) > 20:  
                            d[hostname][0] = 1  
                            d[hostname][2] = d[hostname][1]  

                        else:
                            d[hostname][0] += 1
                            if d[hostname][0] == 3:
                                beingchecked=1 
                                d[hostname][3] = d[hostname][
                                                     1] + 300 
                                globalupdatetime = d[hostname][3] 
                                d[hostname][0] = 0


                    else:
                        loggedtimestamps.append(line)


    for itm in range(len(loggedtimestamps)):
        loggedtimestamps[itm] = str(loggedtimestamps[itm]).replace("\n", "")

    write_to_file(output_path, loggedtimestamps)


def main(argv):
    input_path = argv[1]
    output_path = argv[2]
    
    compute(input_path,output_path)
    

if __name__ == "__main__":
    main(sys.argv)


