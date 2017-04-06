#!/usr/bin/env bash

echo "Feature 1"
python ./src/f1.py ./log_input/log.txt ./log_output/hosts.txt 
echo "Feature 1 COMPLETE "

echo "Feature 2"
python ./src/f2.py ./log_input/log.txt ./log_output/resources.txt 
echo "Feature 2 COMPLETE "

echo "Feature 3"
python ./src/f3.py ./log_input/log.txt ./log_output/hours.txt 
echo "Feature 3 COMPLETE "

echo "Feature 4"
python ./src/f4.py ./log_input/log.txt ./log_output/blocked.txt
echo "Feature 4 COMPLETE "

