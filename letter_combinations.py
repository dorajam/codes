"""
Given a string containing digits from 2-9 inclusive, return all possible 
letter combinations that the number could represent. 
A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

e.g
for "23" -> ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Notes:
1. Although the above answer is in lexicographical order, your answer could be in any order you want.

July 2018, Dora Jambor
"""

def get_res(letter_combos):
    res = []
    if len(letter_combos) == 1:
        return list(letter_combos[0])

    first = letter_combos[0]
    rest = letter_combos[1:]
    for c in first:
        for element in get_res(rest):
            res.append(c + element)
    return res

def main(digits):
    digit_list = [int(num) - 2 for num in digits]
    alphabet = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    letter_combos = [alphabet[num] for num in digit_list]
    
    return get_res(letter_combos)
