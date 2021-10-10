import random
import copy

# TODO: do these go in a config.py module?
HAND_SIZE = 10

SCORES = {
            'A': 1, 
            'B': 3, 
            'C': 3, 
            'D': 2, 
            'E': 1, 
            'F': 4, 
            'G': 2, 
            'H': 4, 
            'I': 1, 
            'J': 8, 
            'K': 5, 
            'L': 1, 
            'M': 3, 
            'N': 1, 
            'O': 1, 
            'P': 3, 
            'Q': 10, 
            'R': 6, 
            'S': 1, 
            'T': 1, 
            'U': 1, 
            'V': 4, 
            'W': 4, 
            'X': 8, 
            'Y': 4, 
            'Z': 10
        }

class Hand:
    """ Class to represent a hand of letters in the Adagrams game."""
    def __init__(self, letter_pool):
        self.letters = self.draw_letters(letter_pool)

    def draw_letters(self, letter_pool):
        """ Return a hand of 10 randomly selected letters for user."""
        letter_bank = []
        letters = []

        # Listify letter_pool for proportionality
        for letter, count in letter_pool.items():
            for i in range(count):
                letter_bank.append(letter)
                # ['A', 'A', 'A', ...'B', 'B',...]

        # Choosing 10 letters from pool 
        letters = random.sample(letter_bank, HAND_SIZE)

        return letters

    def uses_avail_letters(self, word):
        """
        Check that user's input word only contains letters that occur
        in user's hand."""

        # Copy letters list for data integrity
        letters_copy = copy.deepcopy(self.letters)
        
        # Confirm letters in users' word are in hand.
        for letter in word:
            letter.upper()
            if letter in letters_copy:
                letters_copy.remove(letter)
            else:
                return False

        return True

    def score_word(word):
        """Return score of word according to rules of Adagrams game."""
        score = 0

        # Calculate points
        for letter in word:
            score += SCORES[letter]

        # Adagrams awards +8 points for words between 7-10 chars
        if 7 <= len(word) <= 10:
            score += 8

        return score

    def get_highest_word_score(word_list):
        """
        Calculate word with highest score, applying Adagrams tie-breaking 
        logic, and return the winning word in a special data structure."""

        # Score each word, store in words_scores_dict
        words_scores_dict = {}
        for word in word_list:
            words_scores_dict[word] = score_word(word)
        
        # Find highest scores, scores stored in words_scores_dict[values]
        highest_score = max(words_scores_dict.values())
        words_with_highest_scores = [k for k, v in words_scores_dict.items() \
                                    if v == highest_score]

        # Alternate way to obtain words_with_highest_scores
        # words_with_highest_scores = []
        # for word, score in words_scores_dict.items():
        #    if score == highest_score:
        #        word_with_highest_scores.append(word)

        # Max, min functions return first respective value
        longest_word = max(words_with_highest_scores, key=len)
        shortest_word = min(words_with_highest_scores, key=len)

        # A word of length 10 wins outright
        if len(longest_word) == 10:
            return (longest_word, score_word(longest_word))
        # Otherwise the shortest word wins
        else:
            return (shortest_word, score_word(shortest_word))