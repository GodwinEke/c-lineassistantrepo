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
erikwonda.hello(): strikes up a conversation with user...
"""

import sqlite3
import time
import asyncio
import os
import license_detector
import json
from weather import Weather
from keywords import Answers
from auxilliary import *
from jokes import *
from datetime import datetime
from news import News
from dictionary import Dictionary


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def help():
    return f"KEYWORDS\t\t\tFUNCTIONS\n\
{150 * '-'}\n\
about\t\t\t\tReturns the purpose of the assistant and a description of the author.\n\
news\t\t\t\tReturns a list of recent news of different sections (Business, Tech etc.) from The Guardian using The Guardian API.\n\
define\t\t\t\tReturns definitions, synonyms and antonyms of a word using the Free Dictionary API.\n\
help\t\t\t\tReturns a list of command-line arguments to type to implement the functionalitie.s\n\
check\t\t\t\tChecks if user input is a word in English, Chinese, Russian, German, Japanese, French or Spanish.\n\
eligible\t\t\tChecks if user is eligbile for a Full Licence, Provisional License or Learner's Permit in all 54 states of America.\n\
hello, howdy, hey\t\tPrompts erikwonda to start a conversation with user.\n\
add_todo\t\t\tAdd events into a TODO list for user.\n\
see_todo\t\t\tReturns a list of events added to TODO list.\n\
remove_todo\t\t\tAllows user to remove events from TODO list.\n\
weather\t\t\t\tReturns the weather for the user's city of residence"


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def languages()-> list:
    """"
    Returns a list of languages Erikwonda knows
    """
    return ['english', 'russian', 'german', 'chinese', 'french', 'japanese', 'spanish']


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def check(keyword:str, language:str)->bool:
    """
    Assumes keyword is str,
    Assumes language is str,
    returns True if keyword is a word in the language else False
    """
   
    connection = sqlite3.connect(f"../data/databases/{formatted(language)}_words.db")
    cursor = connection.cursor()

    # Check for the word in the specified language
    if language == "english":
        rows = cursor.execute("SELECT * FROM words_en WHERE words = :word", {"word": formatted(keyword)}).fetchall()

    elif language == "russian":
        rows = cursor.execute("SELECT * FROM words_rus WHERE words = :word", {"word": formatted(keyword)}).fetchall()

    elif language == "german":
        rows = cursor.execute("SELECT * FROM words_ger WHERE words = :word", {"word":formatted(keyword)}).fetchall()

    elif language == "chinese":
        rows = cursor.execute("SELECT * FROM words_china WHERE words = :word", {"word": formatted(keyword)}).fetchall()

    elif language == "french":
        rows = cursor.execute("SELECT * FROM words_fr WHERE words = :word", {"word": formatted(keyword)}).fetchall()

    elif language == "japanese":
        rows = cursor.execute("SELECT * FROM words_japan WHERE words = :word", {"word": formatted(keyword)}).fetchall()
    elif language == "spanish":
        rows = cursor.execute("SELECT * FROM words_es WHERE words = :word", {"word": formatted(keyword)}).fetchall()

   # Close the cursor and connection
    cursor.close()
    connection.close()

    # Ensure a row was gotten
    if len(rows) != 1:
        return False
    else:
        return True


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def error_message()->str:
    """
    Returns an error message
    """
    return "Sorry, I cannot do this at the moment.\n\
Just type [python erikwonda.py help] on your terminal to know what I can do."


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def default_message()->str:
    """
    Returns a default message
    """
    return "Seems I do not understand since i only speak 0 and 1.\n\
Just in case, if you need any help, just type 'python main.py [KEYWORD]' on your terminal."


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def loop():
    while True:
        print(Jokes())
        ans = input("Do you want to hear another one? ")

        if ans in Answers.YES:
            continue
        else:
            print("Yeah, I think that's enough. If you need me, you know how to get me.")
            break
    time.sleep(1)
    print("Oh, just in case, you can type [python main.py -k KEYWORD] on your terminal to know what I can do.")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def hello()->str:

    """
    Ellicits a conversation with user
    """

    # Greet user and get reply
    answer = input(greetings())
    # if no answer,
    if len(answer) == 0:
        ans = input("Guess you don't want to share. Personal, right?")

        if formatted(ans) in Answers.YES:
            ans = ("Don't worry. It will be fine. I can tell you a joke. Should I?")
            if formatted(ans) in Answers.YES:
                print(Jokes())
            else:
                print("Okay. But I bet you would have laughed!. Let me know if you need me.\nJust type 'python main.py help'\
 on your terminal to know what I can do.")

        else:
            return "Well, Ok. Let me know if you need me."

    # if user is happy, greet back and send user back to functions
    elif formatted(answer) in Answers.HAPPY_CONDITION:
        print("Lovely!")
        time.sleep(1)
        print("Just in case, you know, you can type 'python main.py help' on your terminal to know what I can do.")
        time.sleep(1)
        ans = input("Mind if i ask you to hear a joke? ")

        if formatted(ans) in Answers.YES:

            #loop jokes
            loop()
        else:
            print("Ok.")

    # if user is sad, try saying a joke until user says no
    elif formatted(answer) in Answers.SAD_CONDITION:
        print('Oh...')
        time.sleep(1)
        print("Well, I can say a joke to make you laugh")
        ans = input("Do you want to hear a joke? ")

        # if user says yes,
        if formatted(ans) in Answers.YES:
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
def about()->str:
    """
    About Erikwonda and the Author
    """

    return "\nHello, I am Erikwonda and I am your command-line virtual assistant aimed to have versatile functionalities.\n\
Some of the things I can do are checking if a user's input is a word in six languages,define a word for you from the English\
dictionary, create a TODO list, strike up a conversation, say jokes etc.\n\
More details if you type [help] in the terminal.\n\n\
My creator is Godwin Chierika Eke, a Computer Engineering major at Morgan State University.\nYou can reach him at https://mailto:ekegodwinc@gmail.com\
 to report problems or issues. To pull up any request, please do at https://github.com/GodwinEke\n"


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def define(word_input:str):
    """"
    Assumes word_input as str,
    Returns the meanings, synonyms, anotnyms, phonetics e.t.c of a word
    """

    # check if word is a valid word
    if not check(word_input, 'english'):
        print(f"\nThe word is not in the English dictionary. If you are sure it is a valid word, click the link:\
 https://google.com/search?q={word_input}\n")
        return

    # get the start of the process
    start = time.time()

    # get word from Free Dictionary API
    url = [f"https://api.dictionaryapi.dev/api/v2/entries/en/{formatted(word_input)}"]
    response = asyncio.get_event_loop().run_until_complete(requests(url))

    if type(response[0]) == dict and response[0].get('title'):
        print('\nI cannot give you the definition you seek.  If you still want to check for the word, click(or copy) the link:\
 https://google.com/search?q={word_input}\n')
        return
    

    # parse the json file
    contents = Dictionary(response)
    phonetic = contents.get_phonetic()
    origin = contents.origin()

    # get end of process
    end = time.time()

    # print the output
    print('-------------------------')
    print(f"Phonetic: {phonetic}\nOrigin: {origin}")
    contents.print_phonetics()
    contents.print_meanings()
    print()
    print("-----Results generated in {:.4f} seconds-----\n".format(end - start))


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def news():
    """
    Prints a list of news according to sections
    """
    # get API key
    if not os.environ['GUARDIAN_APIKEY']:
        raise RuntimeError("GUARDIAN_API_KEY has not been set.")
    key = os.environ['GUARDIAN_APIKEY']

    #start request process
    start = time.time()
    urls = [f"https://content.guardianapis.com/search?api-key={key}"]
    contents = asyncio.get_event_loop().run_until_complete(requests(urls))

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
    
    # initialize the connection
    connection = sqlite3.connect(f"../data/todo/todo.db")
    cursor = connection.cursor()

    # aesthetics on the terminal
    print(f"💪 ADD TODO\n{150 * '-'}\n")

    # inform the user
    print('Just a heads up: you can call up your old TODO lists. But nonetheless...')

    #get the description of 'TODO'
    today = datetime.now()
    
    # Allow user to add as many entries as desired
    while True:
        description = input('What do you want to add? ')
        cursor.execute('INSERT INTO todo(day, month, year, description) VALUES(?,?,?,?)', (today.day, today.month, today.year, formatted(description)))
        
        if cursor.rowcount > 0:
            print('Success.')
        
        # save changes here before asking user to add another entry
        connection.commit()

        ans = input('Anything else? (y/n): ')
        if ans in Answers.YES:
            continue
        else:
            break

    
    ans = input('Would you like to see your TODO list? ')
    if ans in Answers.YES:
        see_todo()
    else:
        print('Ok.')

    # close cursor and connection
    cursor.close()
    connection.close()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def see_todo():
    """
    Prompts user to input the day, month, and year of the desired TODO
    prints an iteration of the TODOs on that day
    """

    # initialize the connection
    connection = sqlite3.connect(f"../data/todo/todo.db")
    cursor = connection.cursor()

    # inform the user
    print('\nNOTE: In case you did not know, you can call up your old TODO lists.')
    print(150 * '-')
    
    ans = ''
    while ans not in Answers.YES and ans not in Answers.NO:
        ans = input('Do you want to see your TODO list of today? (y/n):  ')
    
    # check is user wants 
    if ans in Answers.NO:
        day = month = year = 0

        # Ensure user typed in a valid date
        while day <= 1 or day > 31:
            day = get_integer('Day: ')
        
        # Ensure user typed in a valid month
        while month < 1 or month > 12:
            month = get_integer('Month: ')

        # Ensure user typed in a valid year
        while year < 1800 or year > datetime.now().year:
            year = get_integer('Year(YYYY): ')
        
        rows = cursor.execute("SELECT description FROM todo WHERE day = ? AND month = ? AND year = ?", (day, month, year)).fetchall()

    else:
        day, month, year = (datetime.now().day, datetime.now().month, datetime.now().year)
        rows = cursor.execute("SELECT description FROM todo WHERE day = ? AND month = ? AND year = ?", (day, month, year)).fetchall()  
    
    # Confirm there is a TODO in the list
    if len(rows) == 0:
        print("\nThere are no TODOs in your TODO list for that day. Well done!\n")
    
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

    # initialize the connection
    connection = sqlite3.connect(f"../data/todo/todo.db")
    cursor = connection.cursor()

    print('\n⚠️  Note: This feature removes TODO list of today only⚠️\n')
    
    # Prompt user to describe the TODO in one word
    ans = input('Can you describe the TODO in one word (y/n)? ')
    if ans in Answers.YES:
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
                i += 1

            # Ensure user typed in a valid year
            num = 0
            while num < 1 or num > len(rows):
                num = get_integer('\nIndex number: ')

            # confirm from user it needs to be deleted
            confirm = ''
            while confirm not in Answers.YES and confirm not in Answers.NO:
                confirm = input('Are you sure? [y/n]: ')
            
            # if user is sure
            if confirm in Answers.YES:

                executed = cursor.execute('DELETE FROM todo WHERE description LIKE :description', {'description': f"%{rows[num - 1][0]}%"}).fetchall()

                # save the database
                connection.commit()
                if len(executed) == 0:
                    print('Success!')
            else:
                print('TODO not deleted')

            # Prompt user if he wants to see the TODO list
            ans = input('Would you like to see your TODO list? ')
            if ans in Answers.YES:
                see_todo()
            else:
                print('Ok.')

    else:
        print('\nSorry, to prevent clearing other TODOs, I will need the main keyword of the TODO.\n')


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------       
def weather():

    #check if key has been set
    if not os.environ["WEATHER_API_KEY"]:
        raise RuntimeError('WEATHER_API_KEY not set')
    key = os.environ["WEATHER_API_KEY"]

    json_file = open(f"../data/data.json", "r+")
    data = json.load(json_file)

    urls = []
    if not data["data"].get("location"):
        print("\nTo tell you the weather, I will need to know your city of residence.")
        ans = input("Are you comfortable sharing your city with me (y/n)? ")

        if ans in Answers.YES:
            print("Thank you.")

            # make sure the user gives a correct input
            while True:
                city = input("City: ")
                if len(city) != 0:
                    break

                # confirm that is the user's city'
                city_ans = input("Are you sure that is the correct spelling? ")
                if city in Answers.YES:
                    break
                else:
                    continue

        elif ans in Answers.NO:
            print("\nI get it. You do not trust me yet. But when you do, just use the keyword 'weather' to ask me for the weather\n")
        else:
            print("\n Sorry but I do not understand your answer. Please try again.")

        # save the city for future actions
        data["data"]["location"] = city
        json_file.seek(0)
        json.dump(data, json_file, indent=4)

    else:
        city = data["data"]["location"]

    urls.append(f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no")
        

    results = asyncio.get_event_loop().run_until_complete(requests(urls, key))
    if results[0].get("error") is not None:
        print("Please confirm the spelling of your city is correct")

        # if not correct, remove from JSON file
        del data["data"]["location"]
        json_file.seek(0)
        json.dump(data, json_file, indent=4)

        return

    result = Weather(results)
    result.print_info()
    json_file.close()