import wordification_helper as help
from nltk.corpus import words as word_list
import time
 
def numbers_to_words(number_string):
	if len(number_string)==10:
		print('10 digit number. Assuming that this is a US number with country-code missing.'
			)
	elif len(number_string)!=11:
		print("This does not appear to be a US phone number.")
		return None
	
	pass


def words_to_numbers(wordification):
	
	if len(wordification)==10:
		print('Phone number seems to lack a country code. Is this intentional?')
	elif len(wordification) !=11:
		return('Error: Length wrong. Are you sure this wordification started as an American phone number')
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
	start=time.time()
	print('turning word list into set for speed')
	words=set(word_list.words())
	#nltk word list includes every English letter as an entry. 
	#so I'm deleting all but I and A
	for char in help.junk_letters:
		words.discard(char)
	
	end=time.time()
	print('word list imported. it took ', (end-start))
	possibilities=['']
	wordifications = []
	
	if len(number_string)==10:
		print('10 digit number. Assuming that this is a US number with country-code missing.'
			)
	elif len(number_string)!=11:
		print("This does not appear to be a US phone number.")
		return None
	
	print('Now we\'re populating the possibilities list')
	start=time.time()
	for char in number_string:
		temp=[]
		print(char)
		print(possibilities)
		if char not in help.keypad.keys():
			for p in possibilities:
				temp.append(p+char)
				print(p)
			possibilities.extend(temp)
			print(possibilities)
				#print(p," should've been for 0 and 1")
		else:
			for p in possibilities:
				#print(p,"should've been for letter substitutions.")
	
				for letter in help.keypad[char]:
					temp.append(p+letter)	
			possibilities.extend(temp)
	print(possibilities)
	print('generated possibilities, above.')
	end=time.time()
	print('possibilities took ', (end-start))
	print('finally, plucking wordifications from possibilities')
	start=time.time()
	for p in possibilities:
		if len(p)>9:
			#in our list of possible wordifications,, find each one's letter sequences
			frags=help.parse_fragments(p) 
			word_status=[(w in words) for w in frags]
			if all(word_status):
				wordifications.append(p)
	end=time.time()
	print('word verification took ',(end-start))
	
	return wordifications
