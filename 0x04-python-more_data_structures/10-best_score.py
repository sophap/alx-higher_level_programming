#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = None
    maxscore = float('-inf')
    for key, value in a_dictionary.items():
        if value > maxscore:
            maxscore = value
            max = key
    return max
