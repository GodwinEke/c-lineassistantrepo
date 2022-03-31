class Action:
    ABOUT = 'about'
    ADD_TODO = 'add_todo'
    CHECK  = 'check'
    DEFINE = 'define'
    ELIGIBLE = 'eligible'
    HELLO = ['hello', 'hey', 'howdy', 'hola', "What's up?"]
    HELP = 'help'
    NEWS = 'news'
    REMOVE_TODO = 'remove_todo'
    SEE_TODO = 'see_todo'
    TRANSLATE = 'translate'
    WEATHER = 'weather'

    def returnKeywords() -> list:
        actions = [Action.ABOUT, Action.HELP,
                   Action.CHECK, Action.ADD_TODO, Action.SEE_TODO,
                   Action.REMOVE_TODO, Action.TRANSLATE, Action.DEFINE,
                   Action.NEWS, Action.ELIGIBLE,
                   Action.WEATHER
                   ] + Action.HELLO
        return actions
    
class Answers:
    YES = ['yes', 'y', 'yup', 'yeh', 'yeah', 'sure']
    NO = ['no', 'n',  'nope', 'nah', 'nay']
    HAPPY_CONDITION = ["I am fine", "I'm good", "I'm ok",
                       "I am good", "I am ok", "fine",
                       "good", "happy", "lively", "awesome",
                       "elated", "yeah", 'yes', 'y', 'yup',
                       'yeh', 'yeah', 'sure'
                       ]
    SAD_CONDITION = ["sad", "lonely", "angry", "not fine",
                    "I am not fine", "I'm  not good", "I'm not ok",
                    "I am not good", "I am not ok", "not good"
                    ]
