import re
import pygtrie as trie


LETTER_TO_NUMBER_MAP = {
	'A': '2', 'B': '2','C': '2',
	'D': '3', 'E': '3','F': '3',
	'G': '4', 'H': '4','I': '4',
	'J': '5', 'K': '5','L': '5',
	'M': '6', 'N': '6','O': '6',
	'P': '7', 'Q': '7','R': '7', 'S': '7',
	'T': '8', 'U': '8','V': '8',
	'W': '9', 'X': '9','Y': '9', 'Z': '9'
}

NUMBER_TO_LETTERS_MAP = {
	'2': ['A', 'B', 'C'],
	'3': ['D', 'E', 'F'],
	'4': ['G', 'H', 'I'],
	'5': ['J', 'K', 'L'],
	'6': ['M', 'N', 'O'],
	'7': ['P', 'Q', 'R', 'S'],
	'8': ['T', 'U', 'V'],
	'9': ['W', 'X', 'Y', 'Z']
}

def clean_input(phone_number):
	return re.sub('[^0-9A-Z]', '', phone_number.upper())


def is_valid_phone_number(phone_number):
	if len(phone_number) == 10 or len(phone_number) == 11:
		return True
	return False


def format_number(number):
	prefix = number[0] + '-' if len(number) == 11 else ''
	number = number[1:] if len(number) == 11 else number
	return "{}{}-{}-{}".format(prefix, number[:3], number[3:6], number[6:])


def build_dictionary_trie(list_of_words):
	dictionary_trie = trie.Trie()
	with open('dictionary.txt', 'r') as f:	# http://www.mieliestronk.com/corncob_caps.txt
		for word in f:
			if len(word) > 2 and len(word) < 10:
				dictionary_trie[word] = True
	return dictionary_trie





