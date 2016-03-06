# Aaron Flanagan
# G00330035
# 06/03/2016

# Import random to shuffle a list.
import random as rn
import timeit
import sys
import copy

MAX_LENGTH = 9
# This preprocessing function loads the words list file into a Python list.
def preprocessing():
	contents = []
	with open('wordlist.txt', 'r') as read:
		data = read.read()
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
	while count < 10:## does nine iterations
		while count <= int(x):##while less than users input number
			choice = rn.choice(vowels)##choose a random vowel
			count = count + 1##increment counter
			generatedLetters.append(choice)##add vowel to the list

		count = count + 1##increment counter
		generatedLetters.append(rn.choice(consonents))##add consonent to list

	return generatedLetters
	
  
# This is the function that actually checks the random letters for words.
## adpated from http://loskundos.blogspot.ie/2015/03/countdown-word-game-solver-python.html
def check():
	p = preprocessing()
	letters = generateLetters()
	result = {}	
	for word in p:
		if is_word_possible(word, letters):## returns True if any letter is in word
			length = len(word)
			try:
				copy = result[length]## keeps track of everything in result at that word size
			except KeyError:
				copy = []

			copy.append(word)
			result[length] = copy##re appends result with the new word for that word size	

	##le = max(len(x) for x in result)
	#print(result)
	print(result[sorted(result.keys())[-1]])##prints the longest word/words found if same length

def is_word_possible(word, given_chars):
    wordchars = list(word)
    u_wordchars = copy.deepcopy(given_chars)

    for character in wordchars:## loops each character in the word passed in
    	if character in u_wordchars:## if chars are the same
    		u_wordchars[u_wordchars.index(character)] = ''##set it blank to remember it was checked
    	else:
    		return False##if not return false

    return True

# It does the preprocessing, then creates a random list of letters, and finally runs the solver.
if __name__ == '__main__':
	t = timeit.Timer("check()", "from __main__ import check")
	print(t.timeit(1))
