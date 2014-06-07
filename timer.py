#!/usr/bin/env python
import time, random, urllib2, color, sys


# run = raw_input("Start? > ")
# mins = 0

# urllib2.urlopen('http://maxiskao.herokuapp.com')
# urllib2.urlopen('glance-it.herokuapp.com')
# Only run if the user types in "start"

# This is saying "while we have not reached 20 minutes running"

if __name__ == '__main__':

	url = sys.argv[1]
	if not url.startswith('http'): url = 'http://'+url

	while True:
		urllib2.urlopen(url).read()
		sec = random.random()*1000 + random.random()*60 + 3.14*random.random()
		print 'wait for', color.render(str(sec), 'g'), 'seconds to access', color.render(url, 'y'), 'again'
		time.sleep(sec)