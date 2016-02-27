import re
import timeit

def parse():
	g = open('meanings.txt', 'r')##open 
	f = open('wordlist.txt', 'w')## write

	## This code was written and then adapated from a post on Stackoverflow about checking for duplicate words
	## http://stackoverflow.com/questions/12937798/how-can-i-find-duplicate-lines-in-a-text-file-excluding-case-and-print-them

	##and another page describing how a regular expression pattern works for splitting
	##http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
	seen = set()
	##i = 0
	for line in g:
		for a in line.split():##split by spaces
			newString = re.sub(r'[^a-z]', "", a.lower())## sub all non ascii letters and lowercase them
			if newString not in seen and len(newString) > 3:##if not in set and has atleast 2 letters
				seen.add(newString)##add to set
				f.write(newString)##write to file
				f.write("\n")##append line for dictionary format
				##i = i + 1

	##print("Words in file: ", i)

t = timeit.Timer("parse()", "from __main__ import parse")
print(t.timeit(10))