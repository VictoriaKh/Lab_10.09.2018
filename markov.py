"""Generate Markov text from text files."""

from random import choice
import sys
file_name = sys.argv[1]
words_list = []


def open_and_read_file(file_path):

	"""Take file path as string; return text as string.

	Takes a string that is a file path, opens the file, and turns
	the file's contents as one string of text.
	"""

	with open (file_name) as file:
		for line in file:
			#why can't we just call line.rstrip() without setting it equal to itself?
			line = line.rstrip()
			word = line.split(" ")
			global words_list
			words_list = words_list + word
			#alternative to line 19
			#words_list.extend(word)

	words_list.append(None)

	return words_list	


# open_and_read_file(file_name)

    # your code goes here


    # return "Contents of your file as one long string"


def make_chains(lst):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}

    for x in range(len(words_list) - 2):
    	key = (words_list[x], words_list[x+1])
    	if key not in chains:
    		chains[key] = []
    	# for i in words_list:
    	# 	if i == words_list[x + 1]:
    	chains[key].append(words_list[x + 2])

    # for key in chains.items():
    # 	print('{}: {}'.format(key[0], key[1]))



    return chains












def make_text(chains):
#     """Return text from chains."""
    key = choice(list(chains))
    #x_string = '{} {}'.format(x[0], x[1])
    word = choice(chains[key])

    words = []

    while word is not None:
    	
    	key = (key[1], word)
    	
    	words.append(word)
    	
    	word = choice(chains[key])

    return " ".join(words)


# input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(file_name)

# # Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

print(random_text)
