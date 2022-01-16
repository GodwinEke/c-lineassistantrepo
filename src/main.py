# Author: Godwin Chierika Eke
# Email: https://mailto:ekegodwinc@gmail.com
# Github: https://www.github.com/GodwinEke

#--------------------------------------
# |\  /|  /\  | |\ |   |] \/          |
# | \/ | /  \ | | \| . |  ||          |
#--------------------------------------



import sys
import argparse
import erikwonda
from functions import formatted


KEYWORDS = ["about", "hello", "hey", 
            "howdy", "help","check", 
            "add_todo","see_todo", 
            "remove_todo", "translate",
            "define", "news", "eligible"]


# get keywords from command line
parser = argparse.ArgumentParser()
parser.add_argument('-k', '--keyword', required=True, default='help',
        help='Keyword Required.\nUsage: python main.py [-h] -k KEYWORD\n Type [-k help] for more details')

# store the argument in a dictionary
args= vars(parser.parse_args())


# ------------------------------------------------------------------------------------------------------------------------------------------------------
def main():

    #Ensure keyword is in keywords
    if args["keyword"] not in KEYWORDS:
        print('\n', erikwonda.error_message(), '\n')
        sys.exit(1)

    #Prompt user with a help message
    elif args["keyword"] == "help":
        print ('\n', erikwonda.help(), '\n')

    
    elif args["keyword"] == "check":
        word = input("What word do you want to check? ")
        language = input("What language? ")

        # Ensure language is in the languages erikwonda knows
        if formatted(language) not in erikwonda.languages():
            print("\nSorry, I do not know this language yet.\n Type [-k help] to know the languages I can check.\n")
            sys.exit(1)
        else:
            # if erikwond does not know it, print error message exit
            if not erikwonda.check(word, formatted(language)):
                print("\nSorry, please check your spelling or the language specified.\nIf you are certain that this is the correct spelling, I would suggest\
                       heading to [https://google.com/search] to check.\n")
                sys.exit(1)
            else:
                print(f"\n{word} is a word in the {language} dictionary. You can confirm at [https://google.com/search?q={word}] but I am certain it is there.\n")
            

    elif args["keyword"] == "hey" or args["keyword"] == "hello" or args["keyword"] == "howdy":
        erikwonda.hello()

    elif args["keyword"] == "define":
        word = input("Word: ")
        erikwonda.define(word)

    elif args["keyword"] == "about":
        print(erikwonda.about())

    elif args["keyword"] == "eligible":
        return erikwonda.eligible()

    elif args["keyword"] == "news":
        return erikwonda.news()

    elif args["keyword"] == 'add_todo':
        return erikwonda.add_todo()

    elif args["keyword"] == 'see_todo':
        return erikwonda.see_todo()
    
    elif args["keyword"] == 'remove_todo':
        return erikwonda.remove_todo()
    



if __name__ == '__main__':
    main()
