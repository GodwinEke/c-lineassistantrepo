""" 
Author: Godwin Chierika Eke
Email: https://mailto:ekegodwinc@gmail.com
Github: https://www.github.com/GodwinEke

 +================================================================+
 |     ___   __   .             __                                |
 |    |___| |__|  |  |/ | /\ | |  | |\ |  ___|  /\                |
 |    |___  |\    |  |\ |/  \| |__| | \| |___| /  \               |
 +================================================================+
"""

import sys
import functions as wonda
from auxilliary import formatted
from keywords import Action


# get the various functionalities
KEYWORDS = Action.returnKeywords()

# ------------------------------------------------------------------------------------------------------------------------------------------------------
def main(args):
    # Ensure a case if there are no keywords is solved
    if len(args) <= 1:
        sys.exit('\nHello, please specify what you want me to do.\nYou can see what I do if you type [python erikwonda.py help]. Thank you :)\n')
        

    if len(args) > 2:
        sys.exit("\nHey, there. Sorry, I can do one action at a time: python erikwonda.py [KEYWORD]. Type 'help' to know what I can do.\n")
        
    #Prompt user with a help message
    if formatted(args[1]) == Action.HELP:
        print('\n', wonda.help(), '\n')

    
    elif formatted(args[1]) == Action.CHECK:
        word = input("Word: ")
        language = input("Language: ")

        # Ensure language is in the languages wonda knows
        if formatted(language) not in wonda.languages():
            print("\nSorry, I do not know this language yet.\n Type [help] to know the languages I can check.\n")
            sys.exit(1)

        else:
            # if wonda does not know it, print error message exit
            if not wonda.check(word, formatted(language)):
                print("\nSorry, please check your spelling or the language specified.\nIf you are certain that this is the correct spelling, I would suggest\
heading to [https://google.com/search] to check.\n")
                sys.exit(1)
            else:
                print(f"\n{word} is a word in the {language} dictionary. You can confirm at [https://google.com/search?q={word}] but I am certain it is there.\n")
            

    elif formatted(args[1]) in Action.HELLO:
        wonda.hello()

    elif formatted(args[1]) == Action.DEFINE:
        word = input("Word: ")
        wonda.define(word)

    elif formatted(args[1]) == Action.ABOUT:
        print(wonda.about())

    elif formatted(args[1]) == Action.ELIGIBLE:
        return wonda.eligible()

    elif formatted(args[1]) == Action.NEWS:
        return wonda.news()

    elif formatted(args[1]) == Action.ADD_TODO:
        return wonda.add_todo()

    elif formatted(args[1]) == Action.SEE_TODO:
        return wonda.see_todo()
    
    elif formatted(args[1]) == Action.REMOVE_TODO:
        return wonda.remove_todo()
    
    elif formatted(args[1]) == Action.WEATHER:
        return wonda.weather()
    
    else:
        print('\n', wonda.error_message(), '\n')
        sys.exit(1)
    

if __name__ == '__main__':
    main(sys.argv)
