import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    return poss_values[int(len(poss_values)/2)]

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if current_val > next_val:
        if user_input == 'l':
            return True
    else:
        if user_input == 'h':
            return True
    return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    if letter in word:
        for i, l in enumerate(word):
            if l == letter:
                board[i] = letter
        print('Well done! \'' + letter + '\' is in the word')
        return True
    else:
        print('Sorry, \'' + letter + '\' is not in the word')
        return False
        
