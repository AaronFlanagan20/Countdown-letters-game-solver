### Aaron Flanagan
#### G00330035

# Countdown Letters Game Solver
As part of a module, Theory of Algorithms, for my final year I had to write this algorithm to solve the [Countdown letters game][1].
I also had to right a report about the algorithm and compare different methods and efficiency of each task, all below.

## Background
The first task was to find a wordlist with a decent amount of words. I got a word list from [Basic English][2] with over 29,000 words in it, which is quite small.
From there I opened a few old reports, assignments and books and pasted a lot of text into the file to increase the word count. I then wrote [parser.py](parser.py) to strip out and seperate all the words into a dictionary type format.
Next I was on to actually write the algorithm to sort through the words and return the first nine letter word found that contained all the letters specified.

## Word list
My word list is in the file [wordlist.txt](wordlist.txt) in this repository/gist.
As I explained above I got the original list [meanings.txt](meanings.txt) from [Basic English][1] with over 29,000 words and manually added to it by using old reports and two wordlist files found [here][3]. The final word count comes in at over 105,800 words give or take in the file. 

## Python script
My script [solver.py](solver.py) is in this repository and it works as follows.

First it has some preprocessing to do. It has to read through all the words and appends them to a list, while removing all the words with a length greater than 9.

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
The most important section then follows. It first allows a user to input their own choice of letters or uses letters provided:

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

## Preprocessing
My script does a lot of preprocessing, which only needs to be run once.
Once the preprocessing is done we can run the game solver again and again without that overhead.

## Efficiency
Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.


## References
[1]: https://en.wikipedia.org/wiki/Countdown_(game_show)
[2]: http://www.basic-english.org/down/download.html
[3]: http://www.curlewcommunications.co.uk/wordlist.html