#!/usr/bin/env python

import sys
from collections import Counter, defaultdict
import timeit
import re


def write_to_file(output_path,data):
    file = open(output_path, 'w+')
    for item in data:
        print>> file, item


def compute(input_path, output_path):

    d = defaultdict(int)

    with open(input_path) as ins:
        for line in ins:
            key = line.split(' ',7)[6]
            value1 = line.rsplit(' ', 1)[1]   #Resource_name
            value2 = line.rsplit('\n', 3)[0]
            value3 = value2.rsplit(' ', 1)[1]  #Size
            if value3 is '-':
                value3=0
            if key not in d:
                d[key] = [0.0,0,0.0]
                d[key][1]=int(value3)   
            d[key][0] += 1  
            d[key][2] = d[key][0]*d[key][1]


    keys = sorted(d, key=lambda key: d[key][2], reverse=True)[:10]


    for itm in range(len(keys)):
        keys[itm] = str(keys[itm]).replace("'", "").replace(' ', '')

    write_to_file(output_path, keys)


def main(argv):
    input_path = argv[1]
    output_path = argv[2]
    
    compute(input_path,output_path)
    


if __name__ == "__main__":
    main(sys.argv)


