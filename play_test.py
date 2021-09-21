LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

from random import choices

def draw_letters():
    '''
    Returns a 10 letter 'hand' for player.
    '''
    users_letters = {
        'V': 2, 
        'W': 1, 
        'X': 1, 
        'Y': 1,
        'H': 1, 
        'Z': 2
    }

    while len(users_letters) < 11:
        # letter = Randomly select a letter, ossibly using random.choices() 
        # if too many of that letter
        if users_letters[letter] > LETTER_POOL[letter]:
            continue
        else:
            users_letters[letter] = users_letters.get(letter, 0) + 1
                
        
    #


    return list(letters.values())


test_values = draw_letters()
print(test_values)