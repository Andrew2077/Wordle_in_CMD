
from valid_words_5 import valid_words
import random
import sys

# * choose a random word from the list of valid words
CHOOSEN_WORD = random.choice(valid_words)
#CHOOSEN_WORD = "trunk"
GUESSES_COUNT = 6  # * number of guesses allowed


#* https://pkg.go.dev/github.com/whitedevops/colors
class color:
    PREFIX = '\033'
    BASE = "\033[0m"
    GREY = "\033[90m"
    RED = "\033[31m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[91m"
    Magenta      = "\033[35m"
    PERSISTENT_COLORS = [RED, GREEN]


class GuessWord:
    #* counter for number of attemps
    counter = 1
    #* empty list to store the guesses
    all_guesses = []
    #* alphabet to coloize the important alphabets to help guessing
    alphabet = {
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
    }

    def __init__(self, word_str: str):

        # if  word_str not in valid_words:
        #     print (f"{word_str} not a word !!")

        self.word_str = word_str
        self.word_char = list(word_str)  # * list of chars
        self.post_guess_word_str = ""

    def show_alphabets():
        # list_alphabets = list(wordle.GuessWord.alphabet) #! this will return the keys -- which are not changed in our game
        list_alphabets = list(GuessWord.alphabet.values()) #* values to return the values not keyw 
        for element in list_alphabets:
            print(element, end=" "
                  if list_alphabets[-1] != element 
                  else "\n")
            
    def turn_taken(self):
        GuessWord.counter += 1  # * increment the counter for the whole class

    def is_valid(self):
        # * check if the word is in the list of valid words
        return self.word_str in valid_words

    def check_guess(self):

        for i, char in enumerate(self.word_char):
            if char in set(CHOOSEN_WORD):
                if char == list(CHOOSEN_WORD)[i]:
                    colored_char = (f"{color.GREEN}{char}{color.BASE}")
                    self.edit_alphabets(str(char),str(colored_char))

                else:
                    # print(char, "is yellow")
                    colored_char = (f"{color.YELLOW}{char}{color.BASE}")
                    if color.GREEN not in GuessWord.alphabet.get(char):
                        self.edit_alphabets(str(char),str(colored_char))
                    
                

            else:
                # print(char, "is black")
                colored_char = (f"{color.RED}{char}{color.BASE}")
                self.edit_alphabets(char,colored_char )

            # self.post_guess_word_str += colored_char
            self.post_guess_word_str += "".join(colored_char)
            
            # if is_yellow :
            #     pass
                #self.edit_alphabets(char,colored_char )
            
            # is_green = False
            # is_yellow = False
            # is_red = False
                        
        self.all_guesses.append(self.post_guess_word_str)
        print(self.post_guess_word_str)
    
    def edit_alphabets(self, k, v):
        GuessWord.alphabet[k] = v

    def check_win(self):
        # if self.post_guess_word_str == CHOOSEN_WORD : #! warning
        # * although post_guess_word_str could be the right word
        # * we can't check if it equals the choosen word
        # * cause it's a combination of colored colors  [033[31m p] =! [ p]

        # @ so checking the inserting word rightaway is the correct method

        if self.word_str == CHOOSEN_WORD:
            print(f"{color.Magenta}Congratulation !!! you beat WORLDE{color.BASE}")
            print(f"    you found the correct word {color.BLUE}{CHOOSEN_WORD}{color.BASE} in {color.BLUE}{GuessWord.counter}{color.BASE} guesses :")
            #print(GuessWord.all_guesses) #! will print garbage 
            for element in GuessWord.all_guesses:
                print(element)
            sys.exit(1)

    def check_loss(self):
        if (GuessWord.counter == GUESSES_COUNT+1):
            print(f"{color.RED}YOU USED ALL YOUR GUESSES {color.BASE}")
            print(f"     THE CORRECT WORDS WAS {color.BLUE}{CHOOSEN_WORD}{color.BASE}")
            sys.exit(1)
            
