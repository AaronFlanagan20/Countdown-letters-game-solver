### Aaron Flanagan
#### G00330035

# Countdown Letters Game Solver
As part of a module, Theory of Algorithms, for my final year I had to write this algorithm to solve the [Countdown letters game][1].
I also had to write a report about the algorithm and compare different methods and the efficiency of each method. This included research into various Python optimisation techniques and how to properly time each method taking into consideration some functions need only be run once but might take a considerate amount of time for I/O, like writing to a file or printing results.

#My Analysis Approach
One common mistake spotted in a lot of different algorithms is storage isn't considered on top of time. It's great if you can write and solve and object comparator algorithm that takes in 10,000 objects and compares them, but how efficient is it when you run out of memory half way through, if you make it that far. An algorithm isn't only defined by how fast it completes or even by its optimality, it's efficiency is also measured by it's ability to adapt. With any algorithm [Combinatorial explosion][6] can become a huge problem. If handed more inputs will it crash or still finish with a decent amount of extra time depending on how large the input is. An example would be the quicksort and mergesort algorithms. Quicksort is faster with smaller arrays but as the input increases mergesort comes out faster. So for this project I made three different analysis', timing, memory and adaptability.

1. I will time each section individually to show the importance of un-importance of each function.

2. I will discuss the memory at the end taking the whole algorithm into account.

3. The adaptability will be seen in the *Update* sections where I changed code and added more and more words to my wordlist.


## Background
The first task was to find a wordlist with a decent amount of words. I got a word list from [Basic English][2] with over 29,000 words in it, which is quite small.
From there I opened a few old reports, assignments and books and pasted a lot of text into the file to increase the word count. I then wrote [parser.py](parser.py) to strip out and separate all the words into a dictionary type format.
Next I was on to actually write the algorithm to sort through the words and return the first nine letter word found that contained all the letters specified.

## Word list
My word list is in the file [wordlist.txt](wordlist.txt) in this repository/gist.
As I explained above I got the original list [meanings.txt](meanings.txt) from [Basic English][1] with over 29,000 words and manually added to it by using old reports and two wordlist files found [here][3]. The final word count comes in at over 105,800 words give or take in the file. 

Update: more words found and added from [Peter Novig][5]. File now has 113,990 words.

## Parser.py
My [parser.py](parser.py) file in this repository does the following:
It loops through the file that was just passed in, [meanings.txt](meanings.txt), and retrieves each word by splitting the spaces between them.
We then apply a regular expression to remove all the characters that are not letters and change them to lowercase.
Once done it checks a Python set to see if it contains the word, if not it's added, else it's ignored.
When the set doesn't contain the word, the word is added to the list and written to [wordlist.txt](wordlist.txt)

### Timing Parser.py
By default the timeit function in Python try's to run the code 1,000,000 times, but since the parser only needs to run once, we define below only run the code once in the print statement. The average time to finish comes in between 6.8 - 7.0 seconds for a file with 110,000 words give or take. When timeit runs it 10 times the average time printed is between 68 - 70 seconds, which divided by 10 still gives 6.8 - 7.0 seconds of an average. But with every language standard I/O comes with a price on the time it takes to complete a function. When we take the print function out the average time to complete the average drops to 67 seconds. Although it's a miniscule amount of time, we must keep in mind that if it was a file with over +300,000 words or we if parsed every English word known to man it would save a lot of time.

### Parser.py code
```python
import re
import timeit

def parse():
	g = open('meanings.txt', 'r')##open 
	f = open('wordlist.txt', 'w')## write

	## This code was written and then adapted from a post on Stackoverflow about checking for duplicate words
	## http://stackoverflow.com/questions/12937798/how-can-i-find-duplicate-lines-in-a-text-file-excluding-case-and-print-them

	##and another page describing how a regular expression pattern works for splitting
	##http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
	seen = set()
	I = 0
	for line in g:
		for a in line.split():##split by spaces
			newString = re.sub(r'[^a-z]', "", a.lower())## sub all non ascii letters and lowercase them
			if newString not in seen and len(newString) > 2:##if not in set and has atleast 2 letters
				seen.add(newString)##add to set
				f.write(newString)##write to file
				f.write("\n")##append line for dictionary format
				i = i + 1

	print("Words in file: ", i)

t = timeit.Timer("parse()", "from __main__ import parse")
print(t.timeit(10))
```

## Preprocessing
My script does a lot of preprocessing, which only needs to be run once.
Once the preprocessing is done we can run the game solver again and again without that overhead.
It is done as follows:
It has to read through all the words and append them to a list, while removing all the words with a length greater than 9.
All the words are then returned in a list for the next function to traverse.

```python
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
```

### Timing Preprocessing
The above code only needs to be run once. Once a list of words is generated there is no need to regenerate it every time we check for words for the random letters. So I applied the same principle to this section of code as I did to the [parser.py](parser.py) code above. I ran the snippet of code once and the average came in at 0.07 seconds. When ran 10 times the average came in at .75 seconds. Now notice our code looks like the following:
*Check Update below*
```python
read = open('wordlist.txt', 'r')
data = read.read()
read.close()

contents = []
for i in data.split():
```
The file being read is returned as a string type and then we iterate through the string, which gives us the 0.07 second average when run once. But when I first iterated through the read object like so: ```for i in read:``` the average time came in at .08 seconds. The more efficient approach for preprocessing my list was to iterate over a very large string Data then the TextIOWrapper object read.

The final snippet of code to test just the preprocessing stage:
```python
if __name__ == '__main__':
	t = timeit.Timer("preprocessing()", "from __main__ import preprocessing")
	print(t.timeit(1))
```

*Update*: Over 8000 more words where added to the file so the time to process was increased to    .09 or higher seconds. So I developed a new way to to read and append the file and lowered it back down to anywhere between .082 and .09
Previously it looked like this:
```python
	read = open('wordlist.txt', 'r')
	data = read.read()
	read.close()

	contents = []
	for i in data.split():
		if len(i) <= MAX_LENGTH:
			contents.append(i)

	return contents
```

Now it looks like:
```python
def preprocessing():
	contents = []
	with open('wordlist.txt', 'r') as read:
		data = read.read()
		for i in data.split():
			if len(i) <= MAX_LENGTH:
				contents.append(i)

	return contents
```

## Python script
My script [solver.py](solver.py) is in this repository and it works as follows.
It first does it's preprocessing task as explained above. Next it will call the generateLetters function that returns a list of randomly chosen letters. It will then loop through each word and check if they contain any of the letters, if so it will return true and append the result array with the new word and it's size, else it breaks and loops again.

```python
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
```

Previously it looked like this, it didn't count the weight of each letter or abide by the rules of a minimum of 3 vowels and 4 consonants:
```python
## adapated from http://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
## shows the option of using random choice
def generateLetters():
	vowels = "aeiou"
	consonents = 'bcdfghjklmnpqrstvwxyz'
	generatedLetters = []
	count = 1
	x = input("How many vowels would like? ")
	if int(x) > 9:
		print("You must select les than 9 vowels")
		sys.exit()

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
```
That didn't work too well, so I changed it because the majority of English words contain a vowel or more and you could get a list with no vowels in it. It was also changed because according to the [Countdown letters game][1] game show, letters within each pile are weighted according to their frequency in natural English, and the rules clearly state you must have atleast three vowels and four consonants which I didn't abide by originally. So research was done and [this][4] was found. The author explains the algorithm he wrote, it's efficiency and how each iteration checks the words passed in for the letters generated. 

This is the section where it checks each letter and appends the new words to the results, ending with largest words at the end.

```python
# This is the function that actually checks the random letters for words.
## used from http://loskundos.blogspot.ie/2015/03/countdown-word-game-solver-python.html
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

	#print(max(result[length]))
```

*Update:* loop changed because it is faster to call a method once and iterate over it's contents:
Before change:
```python
	letters = generateLetters()
	result = {}
	for word in preprocessing():
```

## Timing the algorithm
I needed to time the algorithm to test how efficient it worked. The check() method was the main component to be tested, but it also carries the burden of 2 other methods to complete during it, generateLetters() at the start and preprocessing during it's checking.
We already discussed the preprocessing section above and it's average time is 0.07. I needed to time the letters generation aswell in the same manner as above and that came in at 0.9 on average when the user had to input how many vowels they wanted, and 2.5 average when there was no input needed. So far we have 0.97 average on the check method and no checks have been done.

The average time for the check method to complete and return all the results, including the overhead from the other two methods is about 3.1 - 3.5 seconds.

*Update:* As described above more words have been added and the processing stage has been changed, with this in mind I ran the scripting 2 times, timing the method 10 times each. The first came in at 2.7 seconds everytime it runs. I then took out the user input for vowels and ran it again and the average droped to 2.6 seconds.

## Step through
When the check() method runs it calls the preprocessing method that opens the file, and appends all words to a list that are less than nine characters in length. 

It will then call the generateLetters method. This method takes user input and if the input is invalid cuts it shut's down. Once a valid argument is selected it then randomly generates 3 - 5 vowels and the remainder consonants and does a total of ten increments while appending a list and returns the list once finished.

After that the algorithm begins it's loop. It iterates through the processed list and calls the iswordpossible function every iteration passing in the letters and current word. this method splits the letters and words and compares all ten letters to each letter in the word individually. If the word contains any letters the result is True and the loop continues.

Finally the length of the word is stored, and a copy is taken of the dict_list(result) and the length of the word and the word itself are appended the copy, result then takes a copy of the copy object. This is done because if there is any errors along the way the copy object will be set null and we don't lose any of the words in our list. Once the loop finishs the last longest word is printed to the screen.


#Memory
Memory won't be a big issue for my algoritm, but on the topic of algorithm's it is always worth will doing some checking.

First of all I used a file [meanings.txt](meanings.txt) that contained 29,000 words and I added to it. This file is only used in the preprocessing stage. I read in my file to an object 'read'. It's size comes in at 216 bytes, which is taken from opening a 13,094 kilobyte file. I then split the words in read by the white spaces and store them in data. Data consists of one word lines for over 113,000 rows. It's size is 1101988 bytes, which is 1.1 megabytes approximately. Data is appending to the contents list and then made null. Contents size is similar in which it's size its 651,352 bytes / 1024 is 65 kilobytes. This is then returned to the check function.

The generateLetters function is a small function and returns a list of 10 letters at the size of 136 bytes.

The check function uses our contents list to append its own dict object with words in it that contain the letters we generate. A python dict object is 288 bytes in size but even when a list of maybe 20 words or more are appended. It doesn't change in size.

Object size's are returned for Python >2.6 in bytes using
```python
try:
		print(sys.getsizeof(result))
	except AttributeError:
		print("sys.getsizeof exists in Python ")
```

## Results
All the steps above are executed within 2 - 3 seconds. Reading over 113,000 lines of words, generating 10 random letters, looping over every word, comparing it to a list of ten letters and then copying it and appending it to an results dict object, it will them complete the same cycle again for over 113,000 words in my list. But I only timed the algorithm and gave a step by step synopsis. I went and done updates in areas that mostly needed to be optimised, like the preprocessing stage, which could be considered a very important part to the overall completion and run-time of the algorithm. Example my list contains 100,000+ words and completes its processing in just under a second. The Oxford English dictionary contains 350,000+ words. That means if I passed in that list my processing stage triples and a half in the time to complete, 3.5 seconds. In my Analysis I explain above why it was important to optimise. I didn't try optimise the generateLetters function though because I wasn't concerned with it's running time, only the running time of the comparisons. The letters time will always run the same because it can never get any bigger this is only 26 possible letters of which can be chosen. Countdown also states that it randomises letters based on their use in the English language, meaning not all of them are used and some may appear more than others.

## References
[1]: https://en.wikipedia.org/wiki/Countdown_(game_show)
[2]: http://www.basic-english.org/down/download.html
[3]: http://www.curlewcommunications.co.uk/wordlist.html
[4]: http://loskundos.blogspot.ie/2015/03/countdown-word-game-solver-python.html
[5]: http://norvig.com/big.txt
[6]: https://en.wikipedia.org/wiki/Combinatorial_explosion