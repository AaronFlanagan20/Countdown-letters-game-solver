import re

g = open('meanings.txt', 'r')##open 
f = open('wordlist.txt', 'w')## write

## This code was adapated from a post on Stackoverflow
## about checking for duplicate words
## http://stackoverflow.com/questions/12937798/how-can-i-find-duplicate-lines-in-a-text-file-excluding-case-and-print-them

##and another page describing how a regular expression pattern for splitting
##http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
seen = set()
i = 0
for line in g:
	for a in line.split():
		newString = re.sub(r'[^a-z]', "", a.lower())
		if newString not in seen and len(newString) > 2:
			seen.add(newString)
			f.write(newString)
			f.write("\n")
			i = i + 1

print("Words in file: ", i)