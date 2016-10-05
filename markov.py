from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as open_file:
        open_file = open_file.read()
        return open_file

# input_path = "green-eggs.txt"
# input_text = open_and_read_file(input_path)

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    # split the inputted text_string at the spaces and lines
    text_string = text_string.split()
    #create an empty dictionary called chains
    chains = {}
    # for each index in the range of text_string up to the 3nd to last character
    for index in range(len(text_string) - 2):
        # create a key that is a tuple made up of text_string
        # at current index and text_string at next index
        two_word_key = text_string[index], text_string[index + 1]
        # create a value to later assign to two_word_key that is
        # equal to the text_string at the next next index
        new_value = text_string[index + 2]
        # if already exists a key of current two_word_key value in
        # dictionary, perform following steps:
        if chains.get(two_word_key):
            # append new_value to existing value list for this key
            chains[two_word_key].append(new_value)
        # if there does not already exist a key of current two_word_key value in
        # dictionary, assign key:value to two_word_key(tuple):third word(value)
        else:
            chains[two_word_key] = [new_value]

    # printing instead of returning for now, for testing
    # print chains
    return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    import random
    
    # text = ""
    # list_of_words = []
    # your code goes here
    # while True:
    random_key = random.choice(chains.keys())
    random_key_values = chains[random_key]
    third_word = random.choice(random_key_values)
    temp_list = [random_key[0], random_key[1], third_word]
    # for item in temp_list

    # while True:


    text = " ".join(temp_list)
    print text
    # return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

# print random_text
