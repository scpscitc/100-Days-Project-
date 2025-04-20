import random
words=["mouse", "horse", "camel"]
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
randon_word = random.choice(words)
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
        print(lose)
    if "_" not in display:
        game_over = True
        print("You win")
        print(win)
