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
    letter_bank = {}
    # Loop 10 times to add 10 letters to drawn letters
    
        # Randomly select a letter according to its weight in LETTER_POOL
        # letter =  possibly using random.choices() 
    while len(letter_bank) < 10:
        letter_pool_keys = list(LETTER_POOL.keys())
        weights = list(LETTER_POOL.values())
        letter = choices(letter_pool_keys, weights, k=1)
        letter = letter[0]
    
        if letter in letter_bank:    
            if letter_bank[letter] > LETTER_POOL[letter]:
                pass
            else:
                letter_bank[letter] = letter_bank.get(letter, 0) + 1
        else:
            letter_bank[letter] = letter_bank.get(letter, 0) + 1
        #drawn_letters[letter] = drawn_letters.get(letter, 0) + 1
                
    return list(letter_bank.keys())
    
def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass