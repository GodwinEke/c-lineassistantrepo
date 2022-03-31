"""
Author: Godwin Chierika Eke
The purpose of the dicitonary is to parse JSON files from the Free Dictionary API

-------------------------------------------------------------
FUNCTIONS

get_word(): returns the word that is being searched
get_phonetic(): returns the phonetic of the word
print_phonetics(): prints the phonetics related to the world. Number of phonetics is not definite, returns None
origin: returns the origin of the word
print_meanings(): prints the meanings of the word, returns None
-------------------------------------------------------------------


"""
class Dictionary:
    def __init__(self, content):
        self.content = content[0][0]
    
    # get the value of the 'word' key
    def get_word(self):
        """
        Returns the word from JSON file
        """
        # Ensure the word is avaialble 
        try:
            self.content['word']
        except KeyError:
            return 'Not available'
        return self.content['word']

    # get the value of the 'phonetic' key
    def get_phonetic(self):
        """
        Returns the value of the 'phonetic' key
        """
        # Ensure phonetic is available
        try:
            self.content['phonetic']
        except KeyError:
            return 'Not available'
        return self.content["phonetic"]
    
    # get the key-value pairs of the phonetics list
    def print_phonetics(self):
        """"
        Prints the list of phonetics with its text and audio pronunciation
        """
        # Ensure phonetics are available
        try:
            self.content['phonetics'][0]
        except IndexError:
            return

        for word in self.content['phonetics'][0]:
            print(f"{word}: {self.content['phonetics'][0][word]}")
    
    # get the value of the 'origin' key
    def origin(self):
        """
        Returns origin of the word if present
        """
        # Ensure origin is available
        try:
            self.content['origin']
        except KeyError:
            return 'Not available'
        return self.content['origin']

    def print_meanings(self):
        """
        Prints all the meanings of the word with synonyms, and antonyms
        """
        num_definitions = self.content['meanings'][0]
        for meaning in num_definitions:

            # if word is a definition, iterate the meaning, antonyms and synonyms
            if meaning == 'definitions' and type(num_definitions[meaning]) == list:
                counter = 1

                #Traverse through the number of definitions
                for definition in num_definitions[meaning]:

                    if definition.get('definition'):
                        print('\n', counter, definition['definition'])
                    
                    # confirm there is an example section
                    if definition.get('example'):
                        # if there is no antonym 
                        if len(definition['example']) != 0:
                            print('\tExample:', definition['example'])
                        else:
                            print('\tExamples: None')
                    counter += 1
            else:
                print(f"{meaning}: {self.content['meanings'][0][meaning]}")
        
        # print the source 
        print('\nSource(s):', self.content['sourceUrls'])