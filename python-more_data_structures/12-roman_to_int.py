#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif not isinstance(roman_string, str):
        return 0

    result = 0
    num = 0
    roman = {"M": 1000,
             "D": 500,
             "C": 100,
             "L": 50,
             "X": 10,
             "V": 5,
             "I": 1}

    for letter in roman_string:
        if roman[letter] > num:
            result -= num
            num = roman[letter] - num
        else:
            num = roman[letter]
        result += num

    return result
