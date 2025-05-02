import random
animals = ["mouse", "horse", "camel", "tiger", "lion", "cow", "dog", "cat"]
birds = ["sparrow", "eagle", "parrot", "pigeon", "owl", "duck", "peacock", "swan", "flamingo",
              "woodpecker", "crow", "hawk", "penguin", "ostrich", "canary", "crane", "robin",
              "seagull", "falcon", "kingfisher"]
fruits = ["apple", "banana", "mango", "grape", "orange", "papaya", "pear", "peach", "kiwi", "melon"]
countries = ["brazil", "canada", "france", "germany", "india", "japan", "mexico", "nepal", "spain", "turkey"]
colors = ["red", "blue", "green", "yellow", "purple", "orange", "black", "white", "pink", "brown"]
professions = ["doctor", "teacher", "engineer", "pilot", "nurse", "chef", "artist", "lawyer", "farmer", "singer"]

words= animals + birds + fruits + countries + colors + professions

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
win = ''' __     __          __          ___       _  
 \ \   / /          \ \        / (_)     | | 
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | | 
   \   / _ \| | | |   \ \/  \/ / | | '_ \| | 
    | | (_) | |_| |    \  /\  /  | | | | |_| 
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_) '''
lose= ''' __     __           _                    _ 
 \ \   / /          | |                  | |
  \ \_/ /__  _   _  | |     ___  ___  ___| |
   \   / _ \| | | | | |    / _ \/ __|/ _ \ |
    | | (_) | |_| | | |___| (_) \__ \  __/_|
    |_|\___/ \__,_| |______\___/|___/\___(_)
                                            '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("Welcome to hangman")
print(logo)
print(stages[6])
randon_word = random.choice(words)
#************************
if randon_word in animals:
    print("It might be an animal uk!")
elif randon_word in birds:
    print("It might be a bird uk!")
elif randon_word in fruits:
    print("It might be a fruit uk!")
elif randon_word in countries:
    print("It might be a country uk!")
elif randon_word in professions:
    print("It might be a profession uk!")
elif randon_word in colors:
    print("It might be a color uk!")
#*****************************
print("_"*len(randon_word))
game_over = False
correct_letters = []
life = len(stages)-1
while not game_over:
    display = ""
    guessed = input("guess a letter:").lower()
    for the_letter in randon_word:
        if the_letter == guessed:
            display = display + the_letter
            correct_letters.append(the_letter)
        elif the_letter in correct_letters:
            display += the_letter
        else:
            display = display + "_"
    if guessed not in randon_word:
        life = life -1
    print(stages[life])
    print(display)
    print(f"Lifes left {life}")
    if life == 0:
        game_over = True
        print("You lose the game!")
        print(f"Huh! the word was '{randon_word}'")
        print(lose)
    if "_" not in display:
        game_over = True
        print("You win")
        print(win)
