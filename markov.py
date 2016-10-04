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
    text_string = text_string.split()
    chains = {}
    for index in range(len(text_string) - 2):
        two_word_key = text_string[index], text_string[index + 1]
        new_value = text_string[index + 2]
        if chains.get(two_word_key) != None:
            existing_value_list = chains.get(two_word_key)
            existing_value_list.append(new_value)
            chains[two_word_key] = existing_value_list
        elif chains.get(two_word_key) == None:
            chains[two_word_key] = [new_value]
    print chains


    # return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
