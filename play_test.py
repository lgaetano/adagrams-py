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
    Returns a list of 10 letters to user.  
    '''

    letter_bank = {
        'X': 7,
        'Y': 2, 
        'Z': 1        
    }

    # Randomly select a letter according to its weight in LETTER_POOL
    # while len(letter_bank) < 10:
        # letter_pool_keys = list(LETTER_POOL.keys())
        # weighted_values = list(LETTER_POOL.values())
        # # random.choices(population, weights, k) --> returns single letter list
        # letter = choices(letter_pool_keys, weighted_values, k=1)
        # letter = letter[0]
    
        # if letter in letter_bank:
        #     # Ensure letter does not occur more frequently than in LETTER_POOL 
        #     if letter_bank[letter] > LETTER_POOL[letter]:
        #         pass
        #     else:
        #         # Increment letter frequency
        #         letter_bank[letter] = letter_bank.get(letter, 0) + 1
        # else:
        #     # Add letter
        #     letter_bank[letter] = letter_bank.get(letter, 1)
    
    
    # Create list to display letters by frequency
    letter_bank_list = []
    for letter, freq in letter_bank.items():
        for i in range(freq):
            letter_bank_list.append(letter)

    return letter_bank_list

    # return list(letter_bank.keys())
    



test_values = draw_letters()
print(test_values)