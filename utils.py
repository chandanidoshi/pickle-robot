CHAR_NUMBER_MAP = {
	'A': '2', 'B': '2','C': '2',
	'D': '3', 'E': '3','F': '3',
	'G': '4', 'H': '4','I': '4',
	'J': '5', 'K': '5','L': '5',
	'M': '6', 'N': '6','O': '6',
	'P': '7', 'Q': '7','R': '7', 'S': '7',
	'T': '8', 'U': '8','V': '8',
	'W': '9', 'X': '9','Y': '9', 'Z': '9'
}

NUMBER_CHAR_MAP = {
	'2': ['A', 'B', 'C'],
	'3': ['D', 'E', 'F'],
	'4': ['G', 'H', 'I'],
	'5': ['J', 'K', 'L'],
	'6': ['M', 'N', 'O'],
	'7': ['P', 'Q', 'R', 'S'],
	'8': ['T', 'U', 'V'],
	'9': ['W', 'X', 'Y', 'Z']
}

def split_phone_number(phone_number):
	substrings = phone_number.split('-')
	return [substrings[0], substrings[1]], ''.join(substrings[2], substrings[3])


