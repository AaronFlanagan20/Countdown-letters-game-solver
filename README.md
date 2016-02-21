### Aaron Flanagan
#### G00330035

# Countdown Letters Game Solver
As part of a module, Theory of Algorithms, for my final year I had to write this algorithm to solve the [Countdown letters game][1].
I also had to write a report about the algorithm and compare different methods and the efficiency of each method. This included research into various Python optimization techniques and how to properly time each method taking into consideration some functions need only be run once but might take a considerate amount of time for I/O, like writing to a file or printing results.

## Background
The first task was to find a wordlist with a decent amount of words. I got a word list from [Basic English][2] with over 29,000 words in it, which is quite small.
From there I opened a few old reports, assignments and books and pasted a lot of text into the file to increase the word count. I then wrote [parser.py](parser.py) to strip out and seperate all the words into a dictionary type format.
Next I was on to actually write the algorithm to sort through the words and return the first nine letter word found that contained all the letters specified.

## Word list
My word list is in the file [wordlist.txt](wordlist.txt) in this repository/gist.
As I explained above I got the original list [meanings.txt](meanings.txt) from [Basic English][1] with over 29,000 words and manually added to it by using old reports and two wordlist files found [here][3]. The final word count comes in at over 105,800 words give or take in the file. 

## Parser.py
My [parser.py](parser.py) file in this repository does the following:
It loops through the file that was just passed in, [meanings.txt](meanings.txt), and retrieves each word by splitting the spaces between them.
We then apply a regular expression to remove all the characters that are not letters and change them to lowercase.
Once done it checks a Python set to see if it contains the word, if not it's added, else it's ignored.
When the set doesn't contain the word, the word is added to the list and written to [wordlist.txt](wordlist.txt)

### Timing Parser.py
By default the timeit function in Python trys to run the code 1,000,000 times, but since the parser only needs to run once, we define below only run the code once in the print statement. The average time to finish comes in between 6.8 - 7.0 seconds for a file with 110,000 words give or take. When timeit runs it 10 times the average time printed is between 68 - 70 seconds, which divided by 10 still gives 6.8 - 7.0 seconds of an average. But with every language standard I/O comes with a price on the time it takes to complete a function. When we take the print function out the average time to complete the average drops to 67 seconds. Although it's a miniscule amount of time, we must keep in mind that if it was a file with over +300,000 words or we if parsed every English word known to man it would save a lot of time.

### Parser.py code
```python
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
	i = 0
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
	read = open('wordlist.txt', 'r')
	data = read.read()
	read.close()

	contents = []
	for i in data.split():
		if len(i) <= MAX_LENGTH:
			contents.append(i)

	return contents
```

## Python script
My script [solver.py](solver.py) is in this repository and it works as follows.
It first allows a user to input their own choice of letters or uses letters provided:

```python
import random
print(random.shuffle("My code is cool."))
```

Previously it looks like this:
```python
# Note that the following snippet of code was adapted from
# the Stack Overflow post available here: http://www.so.com/post/123
import nothing
```
That didn't work too well, so I changed it.

## Efficiency
Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.

## References
[1]: https://en.wikipedia.org/wiki/Countdown_(game_show)
[2]: http://www.basic-english.org/down/download.html
[3]: http://www.curlewcommunications.co.uk/wordlist.html