#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    if not sentence:
        return (len(sentence), None)
    return (len(sentence), first)

