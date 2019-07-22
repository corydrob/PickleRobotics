keypad={'2':['A','B','C'],
	'3':['D','E','F'],
	'4':['G','H','I'],
	'5':['J','K','L'],
	'6':['M','N','O'],
	'7':['P','Q','R','S'],
	'8':['T','U','V'],
	'9':['W','X','Y','Z']}

reverse_keypad={}
for number,letters in keypad.items():
	for char in letters:
		reverse_keypad[char]=number

#print('keypad: \n', keypad)
#print('reverse lookup: \n',reverse_keypad)

'''
After I wrote parse_fragments I realized that this does not work 
because i made the bad assumption that words would be number-
separated

'''
def parse_fragments(s):
	'''
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
