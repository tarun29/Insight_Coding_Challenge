# Insight_Coding_Challenge
Coding Challenge - March 2017: 
The python files implementing each individual Feature are placed in the src directory. 


Feature 1: 
Apart from the implementation, I also considered using a probablistic method for this which would sample the data  say 100 data lines at random positions. Based on that, we can estimate the 90 percentile of the traffic host address on a website. However, even though it will be a faster implementation, it may not always give the right answer. 

Feature 3: 
Due to a little misunderstanding of Feature 3, I also ended up implementing the Busiest 60 minute period starting from only the time stamps in the data file. That implementation was later also used in implementing feature 3, and is the "countreq" function. 

It relies on an algorithm similar to binary search for finding the 60-minute count, starting at any index and the corresponding data in the data log file. I search for the transition that occurs at from the element before the 60 minute period, and the one after. I found this approach to be much better than looping through the data set to find the index of the element after the 60 minute period. 


