from random import choices
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

def draw_letters():
    '''
    Returns a letter bank list of 10 letters to user.  
    '''

    letter_bank = {}

    # Randomly select a letter according to its weight in LETTER_POOL
    while len(letter_bank) < 10:
        letter_pool_keys = list(LETTER_POOL.keys())
        weighted_values = list(LETTER_POOL.values())
        # random.choices(population, weights, k) --> returns single letter list
        letter = choices(letter_pool_keys, weighted_values, k=1)
        letter = letter[0]
    
        if letter in letter_bank:
            # Ensure letter does not occur more frequently than in LETTER_POOL 
            if letter_bank[letter] > LETTER_POOL[letter]:
                pass
            else:
                # Increment letter frequency
                letter_bank[letter] = letter_bank.get(letter, 0) + 1
        else:
            # Add letter
            letter_bank[letter] = letter_bank.get(letter, 1)
    #TODO 1. allowing for duplicates. 2. Change k to 10     
    return list(letter_bank.keys())   #TODO -- account for duplicate letters
    
def uses_available_letters(word, letter_bank):
    letter_bank_2 = letter_bank[:]

    for letter in word:
        if letter not in letter_bank_2:
            return False
        else:
            letter_bank_2.remove(letter)
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass