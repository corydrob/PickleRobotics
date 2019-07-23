from mercurial.templater import word
from Cython.Runtime.refnanny import result
from re import search
keypad={'2':['A','B','C'],
	'3':['D','E','F'],
	'4':['G','H','I'],
	'5':['J','K','L'],
	'6':['M','N','O'],
	'7':['P','Q','R','S'],
	'8':['T','U','V'],
	'9':['W','X','Y','Z']}
junk_letters={'B','C','D','E','F',
			'G','H','J','K','L','M',
			'N','O','P','Q','R','S'
			'T','U','V','W','X','Y','Z'}

reverse_keypad={}
for number,letters in keypad.items():
	for char in letters:
		reverse_keypad[char]=number

#print('keypad: \n', keypad)
#print('reverse lookup: \n',reverse_keypad)


def scan_word(s,word_list):
	'''
	takes a string and scans it for words off a given word list
	returns 1 if all letters found within the word form non-overlapping segments
	of valid words from the word-list
	returns 0 if there are no letters in the list, or if there are any segments
	of gibberish.
	'''
	#output_words=[]
	result=1			
	search_term=''
	word_positions=[]		#for finding wordifications with multiple short non-overlapping words
	word_start=0
	word_end=0
	
	chunks=split_word_chunks(s)
	for chunk in chunks:
		if chunk in word_list:
			continue
		else:
			
		
	return result
	
	
	
	for i in range(len(s)):
		if s[i].isalpha():
			if !word_start:
				word_start=i
			word_end=i+1
			search_term+=s[i]
			if search_term in word_list:
				word_positions.append((word_start,word_end)
		elif s[i].isdigit():
			word_end=i
			while len(search_term):
				search_term=search_term[1:]
				if search_term in word_list:
					word_positions.append((word_start,word_end))
		else:
			print("You seem to have left punctuation in this input.")
				
	#below: previous phrasing 		
	'''			
	for char in s:
		if char.isdigit():
			while len(search_term):
				search_term=search_term[1:]
				if word 
			continue
		elif char.isalpha():
			word_search+=char
			if search_term in word_list:
				output_words.append(search_term)
	'
	return result
	'''

'''
After I wrote parse_fragments I realized that this does not work 
because i made the bad assumption that words would be number-
separated. function left here for posterity.

'''
def parse_fragments(s):
	'''
	DEPRECATED:
	scan_word is now my preferred function for evaluating wordifications.
	
	Takes a string, s, of letters and numbers and returns a list of 
	letter-chunks.
	does NOT consult a dictionary to see if they are real words
	'''
	
	frags=[]		#list of letter fragments to be returned. 
	chunk=''		#current run of letters in string not interrupted by number
	
	for char in s: 
		if char.isalpha():
			chunk+=char
		else:
			frags.append(chunk)
			chunk=''
	if len(chunk)>0:
		frags.append(chunk)
	return frags
