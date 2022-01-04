"""
Author: Godwin Chierika Eke
Email: https://mailto:ekegodwinc@gmail.com
Github: https://githubcom/GodwinEke

----------------------------------
Functions of erikwonda
----------------------------------
erikwonda.languages() : returns a list of languages erikwonda knows
erikwonda.help(): returns a list of keywords used when running the program
erikwonda.check (keyword, language): returns a statement verifying if a word is a Russian, Chinese, Japanese, Spanish, or English word.
erikwonda.hello(): strikes up a conversation with user
"""
from datetime import datetime
import sqlite3
from jokes import Jokes, greetings
import time
import requests
from dictionary import Dictionary
from news import News
import os
import license_detector

HAPPY_CONDITION = ["I am fine", "I'm good", "I'm ok", "I am good", "I am ok",
                   "fine", "good", "happy", "lively", "awesome", "elated", 
                   "yeah", 'yes', 'y', 'yup', 'yeh', 'yeah', 'sure']


SAD_CONDITION = ["sad", "lonely", "angry", "not fine",
                 "I am not fine", "I'm  not good", "I'm not ok",
                 "I am not good", "I am not ok", "not good"]


YES = ['yes', 'y', 'yup', 'yeh', 'yeah', 'sure']
NO = ['no', 'nope', 'nah', 'nay']


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def help():
    return f"KEYWORDS\t\t\tFUNCTIONS\n\
{150 * '-'}\n\
about\t\t\t\tReturns the purpose of the assistant and a description of the author.\n\
news\t\t\t\tReturns a list of recent news of different sections (Business, Tech etc.) from The Guardian using The Guardian API.\n\
define\t\t\t\tReturns definitions, synonyms and antonyms of a word using the Free Dictionary API.\n\
help\t\t\t\tReturns a list of command-line arguments to type to implement the functionalitie.s\n\
check\t\t\t\tChecks if user input is a word in English, Chinese, Russian, German, Japanese, French or Spanish.\n\
eligible\t\t\tChecks if user is eligbile for a Full Licence, Provisional License or Learner's Permit in all 54 states of America\n\
hello, howdy, hey\t\tPrompts erikwonda to start a conversation with user.\n\
add_todo\t\t\tAdd events into a TODO list for user\n\
see_todo\t\t\tReturns a list of events added to TODO list"



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def languages() -> list[str]:
    """"
    Returns a list of languages Erikwonda knows
    """
    return ['english', 'russian', 'german', 'chinese', 'french', 'japanese', 'spanish']


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def check(keyword, language):
    """
    Assumes keyword is str,
    Assumes language is str,
    returns True if keyword is a word in the language else False
    """
   
   #get file path [you can choose file path though]
    path = os.environ.get('FILE_PATH')

    connection = sqlite3.connect(f"{path}/databases/{formatted(language)}_words.db")
    cursor = connection.cursor()

    # Check for the word in the specified language
    if language == "english":
        rows = cursor.execute("SELECT * FROM words_en WHERE words = :word", {"word": formatted(language)}).fetchall()

    elif language == "russian":
        rows = cursor.execute("SELECT * FROM words_rus WHERE words = :word", {"word": formatted(language)}).fetchall()

    elif language == "german":
        rows = cursor.execute("SELECT * FROM words_ger WHERE words = :word", {"word":formatted(language)}).fetchall()

    elif language == "chinese":
        rows = cursor.execute("SELECT * FROM words_china WHERE words = :word", {"word": formatted(language)}).fetchall()

    elif language == "french":
        rows = cursor.execute("SELECT * FROM words_fr WHERE words = :word", {"word": formatted(language)}).fetchall()

    elif language == "japanese":
        rows = cursor.execute("SELECT * FROM words_japan WHERE words = :word", {"word": formatted(language)}).fetchall()
    elif language == "spanish":
        rows = cursor.execute("SELECT * FROM words_es WHERE word = :word", {"word": formatted(language)}).fetchall()

   # Close the cursor and connection
    cursor.close()
    connection.close()

    # Ensure a row was gotten
    if len(rows) != 1:
        return False
    else:
        return True


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def error_message():
    """
    Returns an error message
    """
    return "Sorry, I cannot do this at the moment.\n\
Just type [python main.py -k help] on your terminal to know what I can do."


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def default_message():
    """
    Returns a default message
    """
    return "Seems I do not understand since i only speak 0 and 1.\n\
Just in case, if you need any help, just type [python main.py -k KEYWORD] on your terminal."


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def formatted(word) -> str:
    """"
    Assumes word as str,
    Returns the word in lowercase and stripped from whitespaces or trailing spaces.
    """
    return word.strip().lower()


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def loop():
    while True:
        print(Jokes())
        ans = input("Do you want to hear another one? ")

        if ans in YES:
            continue
        else:
            print("Yeah, I think that's enough. If you need me, you know how to get me.")
            break
    time.sleep(1)
    print("Oh, just in case, you can type [python main.py -k KEYWORD] on your terminal to know what I can do.")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def hello():

    """
    Ellicits a conversation with user
    """

    # Greet user and get reply
    answer = input(greetings())
    # if no answer,
    if len(answer) == 0:
        ans = input("Guess you don't want to share. Personal, right?")

        if formatted(ans) in YES:
            ans = ("Don't worry. It will be fine. I can tell you a joke. Should I?")
            if formatted(ans) in YES:
                print(Jokes())
            else:
                print("Okay. But I bet you would have laughed!. Let me know if you need me.\nJust type [python main.py -k help]\
 on your terminal to know what I can do.")

        else:
            return "Well, Ok. Let me know if you need me."

    # if user is happy, greet back and send user back to functions
    elif formatted(answer) in HAPPY_CONDITION:
        print("Lovely!")
        time.sleep(1)
        print("Just in case, you know, you can type [python main.py -k help] on your terminal to know what I can do.")
        time.sleep(1)
        ans = input("Mind if i ask you to hear a joke? ")

        if formatted(ans) in YES:

            #loop jokes
            loop()
        else:
            print("Ok.")

    # if user is sad, try saying a joke until user says no
    elif formatted(answer) in SAD_CONDITION:
        print('Oh...')
        time.sleep(1)
        print("Well, I can say a joke to make you laugh")
        ans = input("Do you want to hear a joke? ")

        # if user says yes,
        if formatted(ans) in YES:
            loop()
        else:
            print('Ouch...')
            time.sleep(2)
            print('Uhm..')
            time.sleep(2)
            print("Well, sorry for what happened! Take care!")

    # if user says something different, repeat default message
    else:
        return default_message()


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def about():
    """
    About Erikwonda and the Author
    """

    return "\nHi, my name is Erikwonda and I am your command-line virtual assistant aimed to have versatile functionalities.\n\
I was built with Python and SQL using SQLite framework, and some of the things I can do are checking if a user's input is a word in six languages,\n\
 define a word for you from the English dictionary, create a TODO list, strike up a conversation, say jokes etc.\n\
More details if you type [-k help] when you use me.\n\
My author is Godwin Chierika Eke, a Computer Engineering major at Morgan State University.\nYou can reach him at https://mailto:ekegodwinc@gmail.com\
to report problems or issues. To pull up request, reach him at https://github.com/GodwinEke\n"


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def define(word_input):
    """"
    Assumes word_input as str,
    Returns the meanings, synonyms, anotnyms, phonetics e.t.c of a word
    """

    # check if word is a valid word
    if not check(word_input, 'english'):
        print("Word is not in the English dictionary. If you are ")

    # get the start of the process
    start = time.time()

    # get word from Free Dictionary API
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{formatted(word_input)}")

    # ensure ststus code was 200
    if response.status_code != 200:
        return None

    # convert to a json file
    contents = response.json()[0]

    # parse the json file
    contents = Dictionary(contents)
    first_letter_cap = word_input[0].upper() + word_input[1:]
    phonetic = contents.get_phonetic()
    origin = contents.origin()

    # get end of process
    end = time.time()

    # print the output
    print(f"Word: {first_letter_cap}")
    print('-------------------------')
    print(f"Phonetic: {phonetic}\nOrigin: {origin}")
    contents.print_phonetics()
    contents.print_meanings()
    print()
    print("-----Results generated in {:.4f} seconds-----\n".format(end-start))


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def news():
    """
    Prints a list of news according to sections
    """
    # get API key
    key = os.environ.get('NYT_API_KEY')

    #start request process
    start = time.time()
    contents = requests.get(f"https://content.guardianapis.com/search?api-key={key}")
    contents = contents.json()

    # parse the json file
    news = News(contents)
    news.get_news()

    end = time.time()
    print("-----Results generated in {:.4f} seconds-----\n".format(end-start))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def eligible():
    return license_detector.main()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_todo():
    """
    Prompts user to input into their TODO list
    prints 'Success' if successfully added
    """
    
    #get file path [you can choose file path though]
    path = os.environ.get('FILE_PATH')
    
    # initialize the connection
    connection = sqlite3.connect(f'{path}/todo/todo.db')
    cursor = connection.cursor()

    # aesthetics on the terminal
    print(f"💪 ADD TODO\n{150 * '-'}\n")

    # inform the user
    print('Just a heads up: you can call up your old TODO lists. But nonetheless...')

    #get the description of 'TODO'
    today = datetime.now()
    description = input('What do you want to add? ')
    cursor.execute('INSERT INTO todo(day, month, year, description) VALUES(?,?,?,?)', (today.day, today.month, today.year, formatted(description)))

    if cursor.rowcount > 0:
        print('Success.')

    ans = input('Would you like to see your TODO list? ')
    if ans in YES:
        see_todo()
    else:
        print('Ok.')

    #save changes, close cursor and connection
    connection.commit()
    cursor.close()
    connection.close()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def see_todo():
    """
    Prompts user to input the day, month, and year of the desired TODO
    prints an iteration of the TODOs on that day
    """

    #user can change the file path to use
    path = os.environ.get('FILE_PATH')

    # initialize the connection
    connection = sqlite3.connect(f'{path}/todo/todo.db')
    cursor = connection.cursor()

    # inform the user
    print('\nNOTE: In case you did not know, you can call up your old TODO lists.\n')

    while True:
        # Ensure user typed in a valid date
        try:
            day = int(input('Day: '))
            if day > 0 and day <= 31:
                break
        except ValueError:
            print('\nInvalid number.\n')

    while True:
        # Ensure user typed in a valid month
        try:
            month = int(input('Month number(M): '))
            if month > 0 and month <= 12:
                break
        except ValueError:
            print('\nInvalid month number.\n')

    while True:
        # Ensure user typed in a valid year
        try:
            year = int(input('Year(YYYY): '))

            #if year is greater than present year, keep looping 
            if year <= datetime.now().year :
                break
        except ValueError:
            print('\nInvalid year.\n')
    
    rows = cursor.execute("SELECT description FROM todo WHERE day = ? AND month = ? AND year = ?", (day, month, year)).fetchall()
    
    #COnfirm there is a TODO in the list
    if len(rows) == 0:
        print("\nThere are no TODOs in your TODO list. Well done!\n")
    
    else:
        # aesthetics on the terminal
        print(f"💪 SEE TODO\n{150 * '-'}\n")

        i = 1
        for row in rows:
            # list and capitalize first letter
            print(f'{i}. ', row[0][0].upper() + row[0][1:])
            i += 1

    #close cursor and connection
    cursor.close()
    connection.close()


 # ------------------------------------------------------------------------------------------------------------------------------------------------------------------       
def remove_todo():
    """
    Prompts user to input the day, month, and year of the desired TODO
    COnfirms from user for deletion
    Prints 'Success' if successfully deleted
    """

    path = os.environ.get('FILE_PATH')

    # initialize the connection
    connection = sqlite3.connect(f'{path}/todo/todo.db')
    cursor = connection.cursor()

    print('\n⚠️  Note: This feature removes TODO list of today only⚠️\n')
    
    # Prompt user to describe the TODO in one word
    ans = input('Can you describe the TODO in one word (y/n)? ')
    if ans in YES:
        keyword = input('One-word description: ')
        rows = cursor.execute('SELECT description FROM todo WHERE description LIKE :keyword', {'keyword':f'%{keyword}%'}).fetchall()

        if len(rows) == 0:
            print('\nSorry, no such TODO with that keyword :(\nTry again.')

        else:
            # print all TODOs with keyword
            print(f"\nHere is a list of TODOs with description '{keyword}'")
            i = 1
            for row in rows:
                print(f'{i}. {row[0]}')

            # Ensure user typed in a valid year
            while True:
                try:
                    num = int(input('\nWhich index number: '))
                    if num > 0:
                        break
                except ValueError:
                    print('\nInvalid index number.\n')

            # confirm from user it needs to be deleted
            confirm = ''
            while confirm not in YES and confirm not in NO:
                confirm = input('Are you sure? [y/n]: ')
            
            # if user is sure
            if confirm in YES:

                executed = cursor.execute('DELETE FROM todo WHERE description LIKE :description', {'description': f"%{rows[num - 1][0]}%"}).fetchall()

                # save the database
                connection.commit()
                if len(executed) == 0:
                    print('Success!')
            else:
                print('TODO not deleted')

            # Prompt user if he wants to see the TODO list
            ans = input('Would you like to see your TODO list? ')
            if ans in YES:
                see_todo()
            else:
                print('Ok.')

    else:
        print('Sorry, to prevent clearing other TODOs, I will need the main keyword of the TODO')