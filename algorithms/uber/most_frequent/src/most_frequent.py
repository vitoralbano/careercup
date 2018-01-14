from collections import Iterable

def get_most_frequent(input_list):
	max_sequence = 0
	most_frequent = None
	numbers_frequence = {}

	if(not isinstance(input_list, Iterable)):
		return most_frequent

	for n in input_list:
		if(numbers_frequence.get(n, False) is not False):
			numbers_frequence[n] += 1
		else:
			numbers_frequence[n] = 1

		if(numbers_frequence[n] > max_sequence):
			max_sequence = numbers_frequence[n]
			most_frequent = [n]
		elif(numbers_frequence[n] is max_sequence):
			most_frequent.append(n)

	return most_frequent


print(get_most_frequent([0,1,2,3,4,4,4]))
print(get_most_frequent([5,5,5,7,7,7,8,9]))
print(get_most_frequent([0]))
