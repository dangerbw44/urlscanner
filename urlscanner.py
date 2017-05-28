#!/usr/bin/python


__author__ = "Danger"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2017/05/27 15:38:17 $"
__copyright__ = "Copyright (c) 2017 Danger"
__license__ = "Python"

from sgmllib import SGMLParser
import sys

if len(sys.argv) != 2:
	print "\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++"
	print "\nURL Scanner By Danger\n            "
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++"
	print "\nUse : python urlscanner.py <site>            "
	print "Exemplo: python urlscanner.py http://www.google.com          "
	print "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++"
	sys.exit(1)



class URLLister(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.urls = []

	def start_a(self, attrs):
		href = [v for k, v in attrs if k=='href']
		if href:
			self.urls.extend(href)

if __name__ == "__main__":

	import urllib
	print "\n##########################################################"
	print "# 							 #"
	print "#	     URL Scanner By Danger		         #"
	print "#		BlueWare			         #"
	print "# 							 #"
	print "##########################################################\n"
	link = sys.argv[1]
	try:
		usock = urllib.urlopen(link)
		parser = URLLister()
		parser.feed(usock.read())
		parser.close()
		usock.close()
		for url in parser.urls: print url
	except: 
		print "Nao conseguimos scannear " + sys.argv[1] + " !"
		print "Voce tem de meter um http:// antes do nome!"
