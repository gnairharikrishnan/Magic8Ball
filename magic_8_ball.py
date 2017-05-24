#!/usr/bin/env python

import sys
import random

loop_variable=True

while loop_variable:
	ques = raw_input("Ask the magic 8 ball a question: ")
	ans=random.randint(1,8);
	if ques =="":
		sys.exit()
	elif ans == 1:
		print "Life is Strange sometimes"
	elif ans == 2:
		print "Everything is not as it seems"
	elif ans == 3:
		print "Do not complicate things in life"
	elif ans == 4:
		print "Some times things are exactly as it is and thats ok"
	elif ans == 5:
		print "What you are searching for is you"
	elif ans == 6:
		print "If I could answer that I wouldnt be talking to you on a montior"
	elif ans == 7:
		print "Thank you for that question, but its answer is beyond my humble capabilities"
	elif ans == 8:
		print "Thats it!! I give up!!"
