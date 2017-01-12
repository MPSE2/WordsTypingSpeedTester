import sys
import os
import math
import msvcrt
import re
import time
from colorama import init
from colorama import Fore, Back, Style

#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL

init()

UNTYPED_TEXT_STYLE = Fore.CYAN + Back.BLUE + Style.BRIGHT
TYPING_TEXT_STYLE = Fore.WHITE + Back.CYAN + Style.BRIGHT
CORRECTLY_TYPED_TEXT_STYLE = Fore.WHITE + Back.GREEN + Style.BRIGHT
BADLY_TYPED_TEXT_STYLE = Fore.MAGENTA + Back.RED + Style.BRIGHT

if __name__ == '__main__':
	theText = "Hi there this is some text itsy bitsy bla yada yada\
			   only words this okay you get it now cockroach bla environment\
			   bla again haha just laughing doing your further skills\
			   butter spinach then there faster than this tell me now\
			   piglet hamster asparagus crazy computer science is cool\
			   homer kratos creative gladiator cause he is glad to kill you\
			   idiotical power struggle instant action team speak guru preferences\
			   god before hand condominium inside out and about greetings\
			   bible present stuff nothingness space time after\
			   dose operating systems windows sucks hahaha linux rocks\
			   or does it really herbs and others miscellaneous indoor\
			   mock the fuck hehehe not again come on moron stay back\
			   go get your rack bitch please stop playing games turn on\
			   the radio let us listen to rock fm grab your fucking guitar\
			   here we go dropping plates on your ass hahaha stop right there\n"
	
	theText = theText.replace("\t", " ")
	theText = theText.replace("\n", " ")
	splitText = re.split(' ', theText)
	splitText = [a for a in splitText if a != '']

	currentIndex = 0
	initialized = False

	typedWordsStack = [(a, UNTYPED_TEXT_STYLE) for a in splitText]
	typedWords = []
	currentTypeIndex = 0
	crtWord = ''

	crtTime = 0.0
	prevTime = 0.0
	startTime = time.time()
	timeout = 9999999999

	lastScore = ''
	numCorrect = 0
	numWrong = 0
	while True:
		if not initialized:
			os.system('cls')
			print(Fore.CYAN + Back.BLUE + Style.BRIGHT + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t Press [ENTER] to START.\n"+ Back.RED + "\t\t\t\t\t Press  [ESC] to ..." + Fore.WHITE + Back.GREEN +"EXIT" + Fore.CYAN + Back.BLUE + Style.BRIGHT)
			print(lastScore)
			ch = msvcrt.getch()
			if ord(ch) == 13:
				currentIndex = 0
				typedWordsStack = [(a, UNTYPED_TEXT_STYLE) for a in splitText]
				typedWords = []
				currentTypeIndex = 0
				crtWord = ''
				initialized = True
				startTime = time.time()
				timeout = 60.0
				crtTime = 0.0
				prevTime = 0.0
				numCorrect = 0
				numWrong = 0
			elif ord(ch) == 27:
				break
		else:
			shownText = Style.RESET_ALL + '                         WORDS\' TYPING SPEED TEST                              ' 
			shownText += '\n_________________________________________________________________________________\n\n\t' + Fore.CYAN + Back.BLUE + Style.BRIGHT
			count = 0
			for (tex, col) in typedWordsStack:
				count = count + 1
				shownText = shownText + col + tex + ' '
				if count % 15 == 0:
					shownText = shownText + '\n\t'
			shownText += '\n'

			numCorrect = 0
			numWrong = 0
			for (tex, col) in typedWordsStack:
				if col == TYPING_TEXT_STYLE or col == UNTYPED_TEXT_STYLE:
					break
				elif col == CORRECTLY_TYPED_TEXT_STYLE:
					numCorrect = numCorrect + 1
				else:
					numWrong = numWrong + 1

			shownText += CORRECTLY_TYPED_TEXT_STYLE + 'Correct Words: [{}]\t\t\t\t\t'.format(numCorrect) + Style.RESET_ALL + 'Press [ENTER] to RESTART.\n'
			shownText += BADLY_TYPED_TEXT_STYLE + '  Wrong Words: [{}]\t\t\t\t\t'.format(numWrong) + Style.RESET_ALL + 'Press   [ESC] to EXIT.' + Fore.CYAN + Back.BLUE + Style.BRIGHT + '\n'
			shownText += '{}\n'.format(60 - int(crtTime))
			shownText += '_________________________________________________________________________________\n\n\n'
			count = 0
			typedText = ''
			for a in typedWords:
				typedText = typedText + a + ' '
				count = count + 1
				if count % 10 == 0:
					typedText = typedText + '\n'
			
			shownText = shownText + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + typedText + Fore.CYAN + Back.BLUE + Style.BRIGHT + crtWord
			if updateScreen:
				os.system('cls')
				print(shownText)	
		crtTime = time.time() - startTime
		if math.floor(prevTime) < math.floor(crtTime):
			updateScreen = True
		else:
			updateScreen = False
		prevTime = crtTime
		if msvcrt.kbhit():
			updateScreen = True
			ch = msvcrt.getch()
			if ch == ' ':
				# print("YOU Pressed SPACE")
				if crtWord != '':
					if crtWord.lower() == typedWordsStack[currentIndex][0].lower():
						typedWordsStack[currentIndex] = (typedWordsStack[currentIndex][0], CORRECTLY_TYPED_TEXT_STYLE)
					else:
						typedWordsStack[currentIndex]= (typedWordsStack[currentIndex][0], BADLY_TYPED_TEXT_STYLE)
					typedWords = typedWords + [crtWord]
					crtWord = ''
					currentIndex = currentIndex + 1
			elif ord(ch) == 13:
				currentIndex = 0
				typedWordsStack = [(a, UNTYPED_TEXT_STYLE) for a in splitText]
				typedWords = []
				currentTypeIndex = 0
				crtWord = ''
				initialized = True
				startTime = time.time()
				timeout = 60.0
				crtTime = 0.0
				prevTime = 0.0
				numCorrect = 0
				numWrong = 0
			elif ord(ch) == 27:
				break
			elif ord(ch) == 8:
				if crtWord == '':
					typedWordsStack[currentIndex] = (typedWordsStack[currentIndex][0], UNTYPED_TEXT_STYLE)
					currentIndex = currentIndex - 1
					if currentIndex < 0:
						currentIndex = 0
						crtWord = ''
						typedWords = []
						typedWordsStack = [(a, UNTYPED_TEXT_STYLE) for a in splitText]
						typedWordsStack[0] = (typedWordsStack[0][0], TYPING_TEXT_STYLE)
					else:
						crtWord = typedWords[currentIndex]
						typedWords = typedWords[0:len(typedWords) - 1]
				else:
					crtWord = crtWord[0:len(crtWord) - 1]

			elif ord(ch) >= 97 and ord(ch) <= 122 or ord(ch) >= 65 and ord(ch) <= 90:
				crtWord = crtWord + ch
			if crtWord.lower() == typedWordsStack[currentIndex][0][0:len(crtWord)].lower():
				typedWordsStack[currentIndex] = (typedWordsStack[currentIndex][0], TYPING_TEXT_STYLE)
			else:
				typedWordsStack[currentIndex] = (typedWordsStack[currentIndex][0], BADLY_TYPED_TEXT_STYLE)
  		elif crtTime > timeout:
			initialized = False
			lastScore = 'You typed {} correct words in one minute!\nYou also misspelled {} words...'.format(numCorrect, numWrong)
		
