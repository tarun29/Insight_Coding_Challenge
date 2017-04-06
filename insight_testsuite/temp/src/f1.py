#!/usr/bin/env python

import sys
from collections import Counter, defaultdict


def write_to_file(output_path,data):
	## Writing to File
	file = open(output_path, 'w+')
	for k, v in data.most_common(10):
	    print>> file, '%s,%i' % (k, v)

def compute(input_path, output_path):
	d = defaultdict(int)
	with open(input_path) as ins:       ##   TEST Log
	    for line in ins:
	        key = line.split(' ', 1)[0]
	        d[key] += 1

	d1 = Counter(d)
	d1.most_common()

	write_to_file(output_path, d1)
	


def main(argv):
	input_path = argv[1]
	output_path = argv[2]
	
	compute(input_path,output_path)
	
if __name__ == "__main__":
    main(sys.argv)
