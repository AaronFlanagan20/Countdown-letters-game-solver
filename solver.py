# Aaron Flanagan
# G00330035
# 17/03/2016

# Import random to shuffle a list.
import random as rn
import timeit

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

## adapated from http://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
## shows the option of using random choice
def generateLetters():
	vowels = "aeiouy"
	consonents = 'bcdfghjklmnpqrstvwxz'
	generatedLetters = []
	count = 1
	x = input("How many vowels would like? ")
	while count < 10:
		while count <= int(x):
			choice = rn.choice(vowels)
			count = count + 1
			generatedLetters.append(choice)

		count = count + 1
		generatedLetters.append(rn.choice(consonents))

	return generatedLetters
	
  
# This is the function that actually checks the random letters for words.
def check(letters):

  while (letters):
    letters.pop()
  return []

# It does the preprocessing, then creates a random list of letters, and finally runs the solver.
if __name__ == '__main__':
	##t = timeit.Timer("preprocessing()", "from __main__ import preprocessing")
	##print(t.timeit(1))
	print(generateLetters())