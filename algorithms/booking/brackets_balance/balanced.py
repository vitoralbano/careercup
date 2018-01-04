import re

def balanced(input_value):

	pattern_clean_chars = r'[^][{}()]'

	input_value = re.sub(pattern_clean_chars, '', input_value)
	input_length = len(input_value)

	div_result = divmod(input_length, 2)
	max_opens = 0

	if(div_result[1] != 0):
		return False
	else:
		max_opens = div_result[0]

	count_chars = 0
	count_opens = 0
	
	open_brackets = {
		'{': 0,
		'[': 0,
		'(': 0,
	}

	close_brackets = {
		'}': '{',
		']': '[',
		')': '(',
	}

	for char in input_value:
		count_chars += 1

		if(open_brackets.get(char, False) is not False):
			open_brackets[char] += 1
			count_opens += 1

			if(count_opens > max_opens):
				return False

		elif(close_brackets.get(char, False) is not False):
			open_char = close_brackets[char]
			open_brackets[open_char] -= 1

			if(open_brackets[open_char] < 0):
				return False
		else:
			return False

	return True

print(balanced('(c)((b)[a]'))
print(balanced('[(a)'))
print(balanced('([}{])'))
print(balanced('(1)'))
print(balanced('(1)[2]{3}'))
print(balanced('(foo)([bar]{5})'))