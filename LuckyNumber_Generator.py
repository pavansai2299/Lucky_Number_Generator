import random
playAgain='y'
while playAgain=='y' or playAgain=='Y':
	def validateInput():
    		inputGuess = raw_input("Enter your 4 letters e.g. XXXX:")

    		while True:
			if len(inputGuess) != 4:
	       		    inputGuess = raw_input("Hint:\n	Enter exactly 4 letters.\nEnter your 4 letters e.g. XXXX:")
	       		else:
			    wordList = list( inputGuess.upper() )

			    invalidLetters = False
			    for letter in wordList:
			        if letter not in ['P','A','V','S','U']:
			            invalidLetters = True 
			    	    break	
			    if invalidLetters == True:
			        inputGuess = raw_input("Hint:\n	Enter your guess in letters, 'P, A, V, S, U' only.\nEnter your 4 letters e.g. XXXX:") 

			    else:
			        return wordList

	code = []
	guess = []
	sequence=['P','A','V','S','U']
	length=5
	for i in range(4):
		randomLetter=random.choice(sequence)
		code.append(randomLetter)
		for j in range(length):
			if randomLetter==sequence[j]:
				del sequence[j]
				length-=1
				break
				
	#print ("").join(code)
	print "Guess my sequence of four letters, in the correct order."
	print "Possible letters are P, A, V, S, U.\nHint:\n	There are no repetitions in letters."
	
	guessesRemaining = 5
	while guessesRemaining > 0:
	    correctPosition = 0
	    correctLetter = 0
	    guess =validateInput()
	    tempGuess = list(guess)
	    tempCode = list(code)
	
	    for i in range(4):
		if guess[i] == code[i]:
		    correctPosition += 1
		    tempGuess[i] = "X"
		    tempCode[i] = "X"

	    for j in range(4):
		if tempGuess[j] in tempCode and tempGuess[j] != "X":
		    correctLetter += 1

	    if correctPosition > 0:
		print "Your status:\n	You had",correctPosition,"correct letters in the correct place."
	    if correctLetter > 0:
		print "	You had",correctLetter,"correct letters in the wrong place."
	    if correctPosition == 0 and correctLetter == 0:
		print "Your status:\nNo correct letters"
            
	    if correctPosition == 4:
		print "You have guessed the correct sequence in",6-guessesRemaining,"chances, congratulations!"
		break
	    guessesRemaining -= 1  
	    print "Number of remaining chances: %d" %(guessesRemaining)

	if(guessesRemaining==0):
		print "Your total score : 0"
		print "The correct sequence is %s" %( ("").join(code))
		print "Better luck next time"
	elif(guessesRemaining<=5 and guessesRemaining>=1):
		print "Your total score : %d" %(guessesRemaining*20)
	print "Do you want to play again: \nEnter ('Y' or 'y') to play again.\nEnter ('N' or 'n') to quit. "
	playAgain=raw_input()
print "Thanks for playing."
