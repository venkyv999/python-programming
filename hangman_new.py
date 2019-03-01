# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    TrueCount = 0
    for chr in secret_word:
        for ch in letters_guessed:
            if chr==ch:
                TrueCount+=1
                break
    if TrueCount==len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    ResultString = ''
    flag = False
    for chr in secret_word:
        flag = False
        for ch in letters_guessed:
            if chr==ch:
                ResultString+=chr
                flag = True
        if flag==False:
            ResultString+='_ '
    return ResultString



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ''
    for chr in string.ascii_lowercase:
      if chr not in letters_guessed:
        available_letters+=chr
    return available_letters
  
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    NumberOfGuesses = 6
    NumberOfWarnings = 3
    letters_guessed = []
    AllGuessedLetters = []
    vowels = 'aeiou'
    success = False
    print("----------Welcome to the HANGMAN game!!----------")
    print("\n**In this game you have to guess a word which is",len(secret_word),"letter long.")
    
    while(NumberOfGuesses>0):
        print("You have",NumberOfGuesses,"guesses left !")
        print("You have",NumberOfWarnings,"warnings left !")
        print("Available letters are: ",get_available_letters(AllGuessedLetters))
        letter = input("Enter the guessed letter : ")
        AllGuessedLetters.append(letter)
        ''' Input validation '''
        if not letter.isalpha():
          print("Wrong input, Please enter a alphabate, you lost a warning")
          NumberOfWarnings-=1
          if NumberOfWarnings<=0:
            NumberOfGuesses-=1
            NumberOfWarnings = 3
            print("You have lost 3 warnings and thats why lost one 1 guess, be alert next time")
          print("Result String :",get_guessed_word(secret_word, letters_guessed))
          print("**************************************\n")
          continue
        if letter in letters_guessed:
          print("Wrong input, You have entered a already guessed letter, you lost a warning")
          NumberOfWarnings-=1
          if NumberOfWarnings<=0:
            NumberOfGuesses-=1
            NumberOfWarnings = 3
            print("You have lost 3 warnings and thats why lost one 1 guess, be alert next time")
          print("Result String :",get_guessed_word(secret_word, letters_guessed))
          print("**************************************\n")
          continue
        if letter in secret_word:
          letters_guessed.append(letter)
          if is_word_guessed(secret_word, letters_guessed):
            print("**********Congrats you won the game!!!!**********")
            print("Your score is :",len(letters_guessed)*NumberOfGuesses)
            success = True
            break
          print("**********Good guess**********")
          print("Result String :",get_guessed_word(secret_word, letters_guessed))
          print("**************************************\n")
          continue
        if letter not in secret_word:
          if letter in vowels:
            NumberOfGuesses-=2
            print("Wrong guess, You lost a 2 guess becoz u guessed wrong vowel")
          else:
            NumberOfGuesses-=1
            print("Wrong guess, You lost a guess")
          print("Result String :",get_guessed_word(secret_word, letters_guessed))
          print("**************************************\n")
    if success == False:
      print("You lost better luck next time")


          
    
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    position = 0
    flag = False
    for chr in my_word:
      if chr.isalpha():
        if chr==other_word[position]:
          flag = True
          position+=1
          continue
        else:
          return False
      else:
        position+=1
    return flag



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    flag = False
    for line in wordlist:
      if len(line)==len(my_word):
        if match_with_gaps(my_word, line):
          print(line, end =" ")
          flag = True
    if flag == False:
      print("No matches found")
    print("\n")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    NumberOfGuesses = 6
    NumberOfWarnings = 3
    letters_guessed = []
    AllGuessedLetters = []
    vowels = 'aeiou'
    success = False
    print("----------Welcome to the HANGMAN WITH HINTS game!!----------")
    print("\n**In this game you have to guess a word which is",len(secret_word),"letter long.")
    
    while(NumberOfGuesses>0):
        print("You have",NumberOfGuesses,"guesses left !")
        print("You have",NumberOfWarnings,"warnings left !")
        print("Available letters are: ",get_available_letters(AllGuessedLetters))
        letter = input("Enter the letter (or for hints press * ): ")
        if letter == '*':
          print("Ok. Lets make it easy for you. Following are some hints.\n")
          ResultString = get_guessed_word(secret_word, letters_guessed)
          ResultString = ResultString.replace(' ','')
          show_possible_matches(ResultString)
          continue
        else:
          AllGuessedLetters.append(letter)
        ''' Input validation '''
        if not letter.isalpha():
          print("Wrong input, Please enter a alphabate, you lost a warning")
          NumberOfWarnings-=1
          if NumberOfWarnings<=0:
            NumberOfGuesses-=1
            NumberOfWarnings = 3
            print("You have lost 3 warnings and thats why lost one 1 guess, be alert next time")
          print("Result String :",get_guessed_word(secret_word, letters_guessed))
          print("**************************************\n")
          continue
        if letter in letters_guessed:
          print("Wrong input, You have entered a already guessed letter, you lost a warning")
          NumberOfWarnings-=1
          if NumberOfWarnings<=0:
            NumberOfGuesses-=1
            NumberOfWarnings = 3
            print("You have lost 3 warnings and thats why lost one 1 guess, be alert next time")
          print("Result String :",get_guessed_word(secret_word, letters_guessed))
          print("**************************************\n")
          continue
        if letter in secret_word:
          letters_guessed.append(letter)
          if is_word_guessed(secret_word, letters_guessed):
            print("**********Congrats you won the game!!!!**********")
            print("Your score is :",len(letters_guessed)*NumberOfGuesses)
            success = True
            break
          print("**********Good guess**********")
          print("Result String :",get_guessed_word(secret_word, letters_guessed))
          print("**************************************\n")
          continue
        if letter not in secret_word:
          if letter in vowels:
            NumberOfGuesses-=2
            print("Wrong guess, You lost a 2 guess becoz u guessed wrong vowel")
          else:
            NumberOfGuesses-=1
            print("Wrong guess, You lost a guess")
          print("Result String :",get_guessed_word(secret_word, letters_guessed))
          print("**************************************\n")
    if success == False:
      print("You lost better luck next time")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # print(secret_word)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    print(secret_word)
    hangman_with_hints(secret_word)