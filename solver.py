# Aaron Flanagan
# G00330035
# 17/03/2016

# Import random to shuffle a list.
import random as rn

MAX_LENGTH = 9
# This preprocessing function loads the words list file into a Python list.
def preprocessing():
	read = open('wordlist.txt', 'r')
	data = read.read()
	read.close()

	contents = []
	for i in data.split():
		if len(i) <= MAX_LENGTH:
			contents.append(i)

	return contents
  
# This is the function that actually checks the random letters for words.
def check(letters):
  while (letters):
    letters.pop()
  return []


# This function is just a wrapper that shows how my script works.
# It does the preprocessing, then creates a random list of letters, and finally runs the solver.
