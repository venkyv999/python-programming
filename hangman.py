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
guessed_list = []
number_of_guesses = 6
count_warnings = 0

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    let_pos = []
    flag = 0
    if letters_guessed.isalpha():
      for i in range(0,len(secret_word)):
          if letters_guessed==secret_word[i]:
            let_pos.append(i)
            flag = 1
      if flag==1:
        return let_pos
      elif flag==0:
        return False      
    else:
      print("incorrect input, enter a letter!")
      count_warnings =+ 1
      if count_warnings>=3:
        number_of_guesses -=1
        print("You lost one guess!!")
        count_warnings = 0           
          
    # return False
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_str = ''
    pos = is_word_guessed(secret_word,letters_guessed)
    if pos == False:
      print("Wrong guess")
      print(res_string)
      print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
      get_available_letters(letters_guessed)
      return False
    else:
      my_word_str+=letters_guessed
      for pos_i in range(0,len(pos)):
          q = pos[pos_i]
          res_string[q] = letters_guessed
      print(res_string)
      show_possible_matches(res_string,pos)
      print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
      get_available_letters(letters_guessed)
      i = int(0)
      count = int(0)
      for char in secret_word:
        if res_string[i] == char:
          count+=1
          i+=1
      if count == len(secret_word):
        print("Congratulations!!! You won!!") 
        return 2
      return True
    # elif pos<0:
    #   return False
    

    
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = string.ascii_lowercase
    
    i = 0
    guessed_list.append(letters_guessed)
    for i in range(len(guessed_list)):
      l = guessed_list[i]
      letters = letters.replace(l,"")
      
    print("Available letters are: ",letters)
    print("\n")
    

# def hangman(secret_word):
#     '''
#     secret_word: string, the secret word to guess.
    
#     Starts up an interactive game of Hangman.
    
#     * At the start of the game, let the user know how many 
#       letters the secret_word contains and how many guesses s/he starts with.
      
#     * The user should start with 6 guesses

#     * Before each round, you should display to the user how many guesses
#       s/he has left and the letters that the user has not yet guessed.
    
#     * Ask the user to supply one guess per round. Remember to make
#       sure that the user puts in a letter!
    
#     * The user should receive feedback immediately after each guess 
#       about whether their guess appears in the computer's word.

#     * After each guess, you should display to the user the 
#       partially guessed word so far.
    
#     Follows the other limitations detailed in the problem write-up.
#     '''
#     # FILL IN YOUR CODE HERE AND DELETE "pass"
    
#     number_of_guesses = 6
#     while number_of_guesses>=1:
#       r =  get_guessed_word(secret_word,input("Enter letter :  "))
      
#       if r == False:
#         number_of_guesses-=1
#         print("You have ",number_of_guesses," guesses left!!")
#         print("\n")
#       if r == 2:
#         break

#     if number_of_guesses<=0:
#       print("Sorry you ran out of guesses, you lost")
#       print("The secret word was: ",secret_word)

       
        
    



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word,pos):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    wlist = []
    
    pos_match.extend(pos)
    print(pos_match)
    my_word_str = ''.join(map(str, my_word))
    print(my_word_str)
    for line in wordlist:
      if len(line)==len(secret_word):
        flag = 0
        for pos_i in range(0,len(pos_match)):
          q = pos_match[pos_i]
          if line[q] == secret_word[q]:
            flag += 1
          
        if flag == len(pos_match):
          wlist.append(line)

    print(wlist)




def hangman_with_hints(secret_word,number_of_guesses):
  
  while number_of_guesses>=1:
      r =  get_guessed_word(secret_word,input("Enter letter :  "))
      
      if r == False:
        number_of_guesses-=1
        print("You have ",number_of_guesses," guesses left!!")
        print("\n")
      if r == 2:
        break

  if number_of_guesses<=0:
    print("Sorry you ran out of guesses, you lost")
    print("The secret word was: ",secret_word)
      
  

  



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    # res_string = []
    # secret_word = choose_word(wordlist)
    # print("guess the secret word which is ",len(secret_word),"letter long")
    # for n in range(0,len(secret_word)):
    #   res_string.append('_')
    # print(res_string)
    # hangman(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    res_string = []
    pos_match = []
  
    secret_word = choose_word(wordlist)
    print(secret_word)
    print("guess the secret word which is ",len(secret_word),"letter long")
    for n in range(0,len(secret_word)):
      res_string.append('_')
    print(res_string)
    hangman_with_hints(secret_word,number_of_guesses)