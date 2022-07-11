import os
from valid_words_5 import valid_words
import wordle

os.system("cls") if os.name == "nt" else os.system("clear")

begin_message = """
'##:::::'##::'#######::'########::'########::'##:::::::'########:
 ##:'##: ##:'##.... ##: ##.... ##: ##.... ##: ##::::::: ##.....::
 ##: ##: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##::::::: ##:::::::
 ##: ##: ##: ##:::: ##: ########:: ##:::: ##: ##::::::: ######:::
 ##: ##: ##: ##:::: ##: ##.. ##::: ##:::: ##: ##::::::: ##...::::
 ##: ##: ##: ##:::: ##: ##::. ##:: ##:::: ##: ##::::::: ##:::::::
. ###. ###::. #######:: ##:::. ##: ########:: ########: ########:


        YOU HAVE 6 GUESSES TO GUESS A WORD OF 5 LETTERS

:...::...::::.......:::..:::::..::........:::........::........::
"""
begin_message = begin_message.replace(
    "#", f"{wordle.color.RED}#{wordle.color.BASE}")
begin_message = begin_message.replace(
    ":", f"{wordle.color.BLUE}:{wordle.color.BASE}")
begin_message = begin_message.replace(
    ".", f"{wordle.color.BLUE}.{wordle.color.BASE}")
begin_message = begin_message.replace(
    "'", f"{wordle.color.BLUE}'{wordle.color.BASE}")
begin_message = begin_message.replace(
    "        YOU HAVE 6 GUESSES TO GUESS A WORD OF 5 LETTERS", f"{wordle.color.RED}        YOU HAVE 6 GUESSES TO GUESS A WORD OF 5 LETTERS{wordle.color.BASE}")


print(begin_message)


# print(len(valid_words))

if __name__ == '__main__':  # * if this is the main file

    with open("firstgame/cheat.txt", "w")as f:
        f.write(wordle.CHOOSEN_WORD)

       
    list_alphabets = list(wordle.GuessWord.alphabet.values())
    for element in list_alphabets:
            print(element, end=" " if list_alphabets[-1] != element else "\n")
            
    while True:
        guess = wordle.GuessWord(
            word_str=input(f'GUESS {wordle.GuessWord.counter}: ')  # * get a word from the user
        
        )
        



        if guess.is_valid():  
            guess.check_guess()
            guess.show_alphabets()
            guess.check_win()
            guess.turn_taken()
            guess.check_loss()
            # print(guess.counter) #* will always print 2
            # print(wordle.GuessWord.counter)

        else:
            incorrect_suggestion = guess.word_str
            print(
                f" {wordle.color.RED}!!! WARNING : [ {incorrect_suggestion} ] is not a word !!{wordle.color.BASE}")
