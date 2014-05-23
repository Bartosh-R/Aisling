

import urllib2
import re
import string



class Extractor:

	page_source = ""
	forbidden = [".*?<.>.*?"]
	words = []
	#page_source.decode("utf-8")

	def __init__(self, word):
		response = urllib2.urlopen("http://pl.bab.la/slownik/angielski-polski/"+word)
		self.page_source = response.read();
		self.words = []

		self.define("icon-chevron-right","fb-like-wrapper")
		self.extract("class=\"muted-link\">.*?</a")
		 

	def extract(self, p):
		pattern1 = re.compile(p)
		prefix = p.index(".*?")
		postfix = (len(p)-(prefix+3))

		result = re.findall(pattern1, self.page_source)

		for item in result:
			napis = item[prefix:-postfix]
			#napis = self.odkoduj(napis)
			if self.check(napis) == False:
				self.words.append(napis)


	def check(self,tekst):
		for x in self.forbidden:
			pattern = re.compile(x)
			match = pattern.search(tekst)
			if match != None:
				return True
			else: 
				return False


	def define(self,start, stop):
		try:
			begin = self.page_source.index(start)
			end = len(self.page_source)-self.page_source.index(stop)
			self.page_source = self.page_source[begin:-end]
		except ValueError:
			return 0


	def odkoduj(self,tekst):
		polskie = {"\xc4\x84":"A","\xc4\x86":"C",
		"\xc4\x98":"E","\xc5\x81":"L","\xc5\x83":"N","\xc3\x93":"O",
		"\xc5\x9a":"S","\xc5\xb9":"Z","\xc5\xbb":"Z","\xc4\x85":"a",
		"\xc4\x87":"c","\xc4\x99":"e","\xc5\x82":"l","\xc5\x84":"n",
		"\xc3\xB3":"o","\xc5\x9b":"s","\xc5\xba":"z","\xc5\xbc":"z"}
		for x in polskie.keys():
			tekst = string.replace(tekst,x,polskie[x])
		return tekst


#ext = Extractor("cake")
#print ext.words