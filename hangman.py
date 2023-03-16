def printhanger(tries):
	if tries==5:
		print('+-----+')
		print('|')
		print('|')
		print('|')
		print (tries,'tries left')
	elif tries==4:
		print('+-----+')
		print('|     o')
		print('|')
		print('|')
		print (tries,'tries left')
	elif tries==3:
		print('+-----+')
		print('|     o')
		print('|   --+')
		print('|')
		print (tries,'tries left')
	elif tries==2:
		print('+-----+')
		print('|     o')
		print('|   --+--')
		print('|')
		print (tries,'tries left')
	elif tries==1:
		print('+-----+')
		print('|     o')
		print('|   --+--')
		print('|    /')
		print (tries,'tries left')
	elif tries==0:
		print('+-----+')
		print('|     o')
		print('|   --+--')
		print('|    / \\')

		
play_again = 'p'
while play_again == 'p' or play_again == 'P':
	wordstxt = open('words.txt','r')
	words0 = wordstxt.readlines()
	words = list()
	for i in range (0,len(words0)):
		words.append(words0[i][:-1])
	print('Welcome to KREMALA!!!')
	x = input('Type g<Enter> or G<Enter> if word will be given by another player: ')
	import os	
	clear = lambda : os.system('tput reset')
	clear()
	if x == 'g' or x == 'G':
		z = False
		while z == False:		
			word_1 = input('Player don\'t look! 2nd Player,type in word, must be in English and at least 3 letters long : ')			
			word_1=word_1.lower()		
			y = list(word_1)
			clear = lambda : os.system('tput reset')
			clear()
			if 3 <= len(y):
				if word_1 not in words:
					print('Give a word of the list!!!!')
				else:
					z = True
					x = 'r'
			else:
				print('Give a word in English and at least 3 letters long !!!!')
	else:
		import random
		l = list()
		for i in range(3,21):
				l.append(str(i))
		z = False
		while z == False:
			type0 = input('Type r<Enter> or R<Enter> for word of random length, else give length of random word (between 3 and 20) : ')
			if type0 == 'r' or type0 == 'R':
				word_1 = random.choice(words)
				z = True	
			elif type0 in l:
				word_1 = random.choice(words)
				k = int(type0)
				p = list(word_1)
				while len(p) != k:
					word_1 = random.choice(words)
					p = list(word_1) 
				z = True
			else:
				z = False	
	word = word_1.upper()
	t = list(word)
	hidden_word = list(word)
	for i in range(len(t)):
		hidden_word[i] ='-'
	letters0 = list()
	print('The word has ' , len(t) , ' letters.')
	tries = 5
	printhanger(tries)
	d = ''.join(hidden_word)
	print(d)
	j = False
	while j == False and tries > 0:
		print('chosen letter',letters0)
		letter1 = input('Guess letter : ')
		b = letter1.upper()
		f = list()
		#for i in range(1,10):
		#	f.append('')
		while len(b) != 1 or b in '1234567890':
			letter1 = input('Guess letter : ')
			b = letter1.upper()
		if b in t:
			if b not in letters0:
				letters0.append(b)
			for i in range(0,len(word)):
				if t[i] == b:
					hidden_word[i] = b

		else:
			if b in letters0:
				print('You\'ve chosen this letter already')
			else:
				if b not in letters0:
					letters0.append(b)
				tries -= 1
		printhanger(tries)
		q = ''.join(hidden_word)
		print(q)
		if '-' not in hidden_word:
			j = True
			print('Congratulations! You\'ve found word ',word,'!!!')
	if tries == 0:
		print('Sorry! You lost! The word was',word)			
	play_again = input('Type P<Enter> or p<Enter> to play again:')	
