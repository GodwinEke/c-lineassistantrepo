"""
Author: Godwin Chierika Eke
Email: https://mailto:ekegodwinc@gmail.com
Github: https://githubcom/GodwinEke

get_integer: Assumes prompt as None by default,
             Takes in prompt and converts to string,
             Reads input from user and returns data if data is an integer, 

formatted: Assumes word as str,
           Returns the word in lowercase 
           and stripped from whitespaces or trailing spaces.
"""



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_integer(prompt=None):
    """
    Assumes prompt as None by default,
    Takes in prompt and converts to string,
    Reads input from user and returns data if data is an integer, 
    """
    if prompt is None:
        prompt = 'Number: '
    while True:
        try:
            num = int(input(str(prompt)))
            if type(num) == int:
                return num
        except ValueError:
            print('\nInvalid number\n')
            continue
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def formatted(word) -> str:
    """"
    Assumes word as str,
    Returns the word in lowercase and stripped from whitespaces or trailing spaces.
    """
    return word.strip().lower()


    
