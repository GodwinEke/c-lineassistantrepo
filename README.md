# **Erikwonda** :technologist:
----------------------------------------------------------------------------------------------------------------
This is Erikwonda, a command-line virtual assistant  for programmers aimed to have versatile functionalities done on the terminal 
without having to browse everything on the Internet. With the tap of a key, Erikwonda is being built to bring the 
Internet to the terminal (and not to replace it though). Erikwonda was built with APIs such as [The Guardian API](https://open-platform.theguardian.com/) and [The Free Dictionary API](https://dictionaryapi.dev/) 

## Features
- Verifies if a word is an actual English, Russian, Chinese, German, Spanish or French word from SQL databases having **[274k+ - 1.6M+]** 
words
- Defines any English word with all its meanings, pronunciations, synonyms and antonyms in the dictionary.
- Gives users a list of recent news of different sections (Business, Technology, World News etc.) from The Guardian using The Guardian API.
- *Verifies if a person is eligible for a Full License, Provisional License, or a Learner's Permit from all 50 states of America.
- **Strikes up a conversation with a user.
- Prints out jokes, commonly referred to as Dad **Jokes**.
- User can add or remove events in their TODO lists. If not deleted (that is, crossed out realistically), users can always pull up their TODO
lists as specified

# Usage
--------------------------------------------------------------------------------------------------------------------
To use Erikwonda, go to your command terminal. This README will assume you are already in the file directory in your terminal.
In order to use Erikwonda, a keyword will be needed as shown below:
```
python erikwonda.py [KEYWORD]
```
where ```[KEYWORD]``` returns the desired feature. 
To see all commands, type in:
```
python main.py help
```
and you will see a list of functions as outlined below:
```
KEYWORDS                       FUNCTIONS
-------------------------------------------------------------------------------------------------------------------------------------
about                           Returns the purpose of the assistant and a description of the author.
news                            Returns a list of recent news of different sections (Business, Tech etc.) from The Guardian using The Guardian API.
define                          Returns definitions, synonyms and antonyms of a word using the Free Dictionary API.
help                            Returns a list of command-line arguments to type to implement the functionalitie.s
check                           Checks if user input is a word in English, Chinese, Russian, German, Japanese, French or Spanish.
eligible                        Checks if user is eligbile for a Full Licence, Provisional License or Learner's Permit in all 54 states of America
hello, howdy, hey               Prompts erikwonda to start a conversation with user.
add_todo                        Add events into a TODO list for user
see_todo                        Returns a list of events added to TODO list
remove_todo                     Allows user to remove events from TODO list.
```
# Configurations
----------------------------------------------------------------------------------------------------------------------------------
To use the ```news``` keyword, user must retrieve an ```apikey``` from [The Guardian](https://open-platform.theguardian.com/) and add to your ```ENVIRONMENT_VARIABLE```
If you are using PowerShell, type on the terminal:
```$env:GUARDIAN_APIKEY = api_key```
If you are using Bash or Linux, type on the shell:
```export GUARDIAN_APIKEY = api_key```

In addition, copy the directory (```file_path```) of where the folder is located and add to the ```ENVIRONMENT_VARIABLE```:
If you are using PowerShell, type on the terminal:
```$env:FILE_PATH = file_path```
If you are using Bash or Linux, type on the shell:
```export FILE_PATH = file_path```


# Walkthrough
Here is a walkthrough of Erikwonda:
![Walkthrough](https://github.com/GodwinEke/c-lineassistantrepo/blob/master/gif/walkthrough.gif)

GIF created by[Convertio](https://convertio.co/mp4-gif/)

# Future Improvements
- Implement more functionalities
- Leverage the use of APIs to make it more sophisticated
- Improve aesthetics

# Notes
- *Data used for the license detector was gotten from [The Word Population Review](https://worldpopulationreview.com/state-rankings/driving-age-by-state)
- **Erikwonda is currently under active development

# Credits
Please refer to [CREDITS.md](https://github.com/GodwinEke/c-lineassistantrepo/blob/master/data/wordstxt/CREDITS.md) to see the people that made this project
possible

# Report Issues
If you have any problems or issues or suggestions, you are most welcomed :handshake:
