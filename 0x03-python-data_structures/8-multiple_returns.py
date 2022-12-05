#!/usr/bin/python3
def multiple_returns(sentence):
    for x in range(len(sentence)):
        if len(sentence) == 0:
            result = (len(sentence), None)
        else:
            result = (len(sentence), sentence[0])
    return result
