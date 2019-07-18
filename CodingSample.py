import wordification_helper as help
from nltk.corpus import words as word_list

#currently treating country code as mandatory. 
#May change mind on that later.
def numbers_to_words(number_string):
	
	pass


def words_to_numbers(wordification):
	
	if len(wordification)==10:
		print('Phone number seems to lack a country code. Is this intentional?')
	elif len(wordification) !=11:
		return('Error: Length wrong. Try with a fresh number')
	output=''
	for i in wordification:
		print('here')
		if i.isalpha():
			print('isalpha')
			if i in help.reverse_keypad.keys():
				output+=help.reverse_keypad[i]
			else:
				
				output+=i
		elif i.isdigit():
			output+=i

	return output

def all_wordifications(number_string):
	''' 
	For a given US phone number, return all possible combinations of numbers and English words that can be formed by
		via typing on a standard phone.:
		1=n/a; 2=ABC; 3=DEF
		4=GHI; 5=JKL; 6=MNO
		7=PQRS;8=TUV; 9=WXYZ
		0=N/A
	inputs: 
		number_string: a string of a US phone number

	'''
	words=set(word_list.words())
	wordifications = []
	
	if len(number_string)==10:
		print('10 digit number. Assuming that this is a US number with country-code missing.'
			)
	elif len(number_string)!=11:
		print("This does not appear to be a US phone number.")
		return None
	
	
	
	for i in number_string:
		if i not in help.keypad.keys():
			ouptut+=i
		else:
	
	return wordifications
