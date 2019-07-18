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