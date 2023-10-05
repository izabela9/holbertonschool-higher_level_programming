#!/usr/bin/python3
def roman_to_int(roman_string):
    r_str = roman_string
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if type(r_str) is not str or r_str is None:
        return 0
    res = 0
    for i in range(len(r_str)):
        if i + 1 < len(r_str) and roman[r_str[i]] < roman[r_str[i + 1]]:
            res -= roman[r_str[i]]
        else:
            res += roman[r_str[i]]

    return res
