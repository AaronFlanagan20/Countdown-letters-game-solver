# Aaron Flanagan
# G00330035
# 17/03/2016

# Import random to shuffle a list.
import random as rn
import timeit
import sys

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
## changed to allow the fact that each pile must be weigthed according to their frequency in natural English

def generateLetters():
	generatedLetters = []
	vowels = "eeeeeeeeeeeeaaaaaaaaaiiiiiiiiioooooooouuuu"
	consonents = 'nnnnnnrrrrrrttttttllllssssddddgggbbccmmppffhhvvwwyykjxqz'
	x = input("How many vowels would you like? ")
	if int(x) < 3 or int(x) > 5:
		print("You must select between 3 and 5 vowels")
		sys.exit()
	
	count = 1
	while count < 10:
		while count <= int(x):
			if count == 9:
				break;
			choice = rn.choice(vowels)
			count = count + 1
			generatedLetters.append(choice)

		count = count + 1
		generatedLetters.append(rn.choice(consonents))

	return generatedLetters
	
  
# This is the function that actually checks the random letters for words.
def check():
	result = {}
	letters = generateLetters()
	
	

# It does the preprocessing, then creates a random list of letters, and finally runs the solver.
if __name__ == '__main__':
	##t = timeit.Timer("preprocessing()", "from __main__ import preprocessing")
	##print(t.timeit(1))
	check()