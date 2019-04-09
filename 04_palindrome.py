"""
10 min

A palindrome is a word that reads the same backward or forward.

Write a function that checks if a given word is a palindrome. Character case should be ignored.

For example, is_palindrome("Deleveled") should return True as character case
should be ignored, resulting in "deleveled", which is a palindrome since it
reads the same backward and forward.


    def is_palindrome(word):
        return None

    print(is_palindrome('Deleveled'))
"""


def is_palindrome(word):
    word = word.lower()
    half = len(word) // 2
    m = len(word) % 2
    return word[:half] == word[:half+m-1:-1]


print(is_palindrome('Deleveled'))
