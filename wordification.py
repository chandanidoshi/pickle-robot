from utils import *

def number_to_words(number):
	pass

def words_to_number(s):
	number_in_words = clean_input(s)
	if not is_valid_phone_number(number_in_words):
		return 'Provide valid US phone number'
	number = ''
	for c in number_in_words:
		if c.isalpha():
			number += CHAR_NUMBER_MAP[c]
		else:
			number += c
	return format_number(number)


