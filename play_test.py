# def score_word(word):

#     # Create points collectio
#     sample = {
#         1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S'],
#         2: ['D', 'G'],
#         3: ['B', 'C', 'M', 'P'],
#         4: ['F', 'H', 'V', 'W', 'Y'],
#         5: ['K'],
#         8: ['J', 'X'],
#         10: ['Q', 'Z']
#     }

# #     return score
# sample = {
#         ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S'): 1,
#         ('D', 'G'): 2,
#         ('B', 'C', 'M', 'P'): 3,
#         ('F', 'H', 'V', 'W', 'Y'): 4,
#         ('K'): 5,
#         ('J', 'X'): 8,
#         ('Q', 'Z'): 10
#     }

# print(sample[1])




def score_word(word):

    score = 0

    # list of lists
    scores = [
            ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S'], # 1
            ['D', 'G'], # 2
            ['B', 'C', 'M', 'P'], # 3
            ['F', 'H', 'V', 'W', 'Y'], #4
            ['K'], #5
            ['J', 'X'],  #8
            ['Q', 'Z'], #10
    ]

    for letter in word:
        letter = letter.upper()
        if letter in scores[0]:
            score += 1
        elif letter in scores[1]:
            score += 2
        elif letter in scores[2]:
            score += 3
        elif letter in scores[3]:
            score += 4
        elif letter in scores[4]:
            score += 5
        elif letter in scores[5]:
            score += 8
        elif letter in scores[6]:
            score += 10

    if 7 <= len(word) <= 10:
        score += 8

    return score

result = score_word("XXXXXXXXX")
print(result)