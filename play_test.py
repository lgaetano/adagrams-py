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
    Returns a 10 letter 'hand' for user.
    '''
    # Create a data structure to store drawn letters
    drawn_letters = {
        # 'V': 2, 
        # 'W': 1, 
        # 'X': 1, 
        # 'Y': 1,
        # 'H': 1, 
        # 'Z': 2
    }

    # Loop 10 times to add 10 letters to drawn letters
    # while len(drawn_letters) < 10:
        # Randomly select a letter according to its weight in LETTER_POOL
        # letter =  possibly using random.choices() 
        
    letter = 'H'
        # Make sure specific letter is not drawn too many times by comparing
        #  to values in LETTER_POOL  
        # if drawn_letters[letter] > LETTER_POOL[letter]:
        #     continue
        # else:
        #     drawn_letters[letter] = drawn_letters.get(letter, 0) + 1
    drawn_letters[letter] = drawn_letters.get(letter, 0) + 1
                


    return list(drawn_letters.values())


test_values = draw_letters()
print(test_values)