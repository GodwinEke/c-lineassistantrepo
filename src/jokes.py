import random

def Jokes():
    """"
    Returns a random joke from list
    """
    
    jokes = [
"\nI said to the Gym instructor “Can you teach me to do the splits?” He said, “How flexible are you?”\n\
I said, “I can’t make Tuesdays.” :)\n",

"\nWhy was the math teacher late to work?\n\
She took the rhombus. :)\n",

"\nWhy can't you trust an atom?\n Because they make up everything. :)\n",

"\nI'm afraid for the calendar.\n Its days are numbered. :)\n",

"\nWhat kind of car runs on leaves?\n An autumn-mobile! :)\n",

"\nI only know 25 letters of the alphabet.\n I don't know y. :)\n",

"\nWhat did Tennessee?\n The same thing as Arkansas. :)\n"

"\nWhy is Peter Pan always flying?\n\
Because he Neverlands. :)\n"

"\nWant to hear a joke about construction?\n\
I’m still working on it. :)\n",

"\nBefore the invention of the wheel…\n\
everything was a drag! :)\n",

"\nWhat are the biggest enemies of caterpillars?\n\
Dogerpillers. :) ",

"\nWhy don't eggs tell jokes?\n\
They'd crack each other up. :)\n",

"\nI don't trust stairs.\n\
They're always up to something. :)\n",

"\nTo whoever stole my copy of Microsoft Office, I will find you.\n\
You have my Word! :)\n",

"\nTwo goldfish are in a tank.\n\
One says to the other, “Do you know how to drive this thing? :)\n",

"\nHow do moths swim?\n\
Using the butterfly stroke. :)\n",

"\nWhat does a cow use to do math?\n\
A cow-culator. :)\n",

"\nWhich is faster, hot or cold?\n\
Hot, because you can catch a cold. :)\n",

"\nMy boss told me to have a good day,\n\
so I went home! (please, don't do this. You will be fired).\n",

"\nRIP boiled water—you will be mist. :)\n",

"\nMy hotel tried to charge me ten dollars extra for air conditioning.\n\
That wasn't cool. :)\n",

"\nAn apple a day keeps the doctor away.\n\
At least it does if you throw it hard enough. :)\n",

"\nI have a joke about chemistry,\n\
but I don't think it will get a reaction :)\n",

"\nWho invented the round table?\n\
Sir Cumference. :)\n/",

"\nWhat do you call a belt made out of watches?\n\
A waist of time.\n",

"\nWhat kind of shoes do ninjas wear?\n\
Sneakers!\n",

"\nIf a child refuses to nap, are they guilty of resisting a rest? :)\n",

"\nWhy do trees seem suspicious on sunny days?\n\
They just seem a little shady!\n",

"\nWhy can't a nose be 12 inches long?\n\
Because then it'd be a foot.\n",

"\nDid you hear about the guy who invented the knock-knock joke?\n\
He won the 'no-bell' prize.\n",

"\nWhat does a baby computer call his father?\n\
Data. :)\n",

"\nWhat’s a computer’s favorite snack?\n\
Microchips! :)\n",

"\nWhat kind of bird is always getting hurt?\n\
The owl. :)\n"

"\nWhy did the computer always play “Someone Like You?”\n\
It was a Dell :)\n",

"\nWhy do smartphones ring?\n\
Because they can’t talk.🥲🥲\n",

"\nWhy don’t phones ever go hungry?\n\
They have plenty of apps to choose from. :)\n",

"\nWhere do math teachers go on vacation?" "Times Square.\n",

"\nMountains aren't just funny.\nThey're hill areas :)\n",

"\nI'm not a big fan of stairs.\n\
They're always up to something. :)\n",

"\nWhy do ghosts love elevators?\n\
Because it lifts their spirits. :)\n",

"\nIf two vegans get in a fight, is it still considered a beef? 🤔🤔\n",

"\nWhy couldn’t the computer buy a new pair of jeans?\n\
It had spent all its cache :)\n",

"\nWhat do you call an elephant that doesn't matter?\n\
An irrelephant. :)\n"

"\nWhy are skeletons so calm?\n\
Because nothing gets under their skin. :)\n",

"\nWhy didn't the astronaut come home to his wife?\n\
He needed his space. ☄️\n",

"\nWhat do you get from a pampered cow?\n\
Spoiled milk! :)\n"
] 

    value = random.randint(0, len(jokes) - 1)     
    return jokes[value]

def greetings():

    """
    Returns a random greeting from list
    """
    greetings = ["Hello, how are you? ", "Hi, how are you?",
                "Hi, lovely day, right? How are you? ",
                "Ah, my friend! How are you? ",
                "Hey fella, You good? ", "Hey, my old friend, how are you? ",
                "Well look who remembered me, how have you been? "]

    pick = random.randint(0, len(greetings) - 1)
    return greetings[pick]

