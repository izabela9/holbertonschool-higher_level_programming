#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    if len(sentence) == 0:
        return (len(sentence), None)
    return (len(sentence), first)


sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
