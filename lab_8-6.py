"""
Create a Python file named lab_8-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a function count_a(word) that takes in a string word and returns the number of a's in the word. 
The function should count both lowercase (a) and uppercase (A)
_____________________________________________________________________________________

Create a Python file named lab_8-5.py

Write a function factorial(num) that takes in a number num 
and returns the product of all numbers from 1 up to and including num

_______________________________________________________________________________________

Create a Python file named lab_8-6.py

Write a function is_palindrome(word) that takes in a string word 
and returns the true if the word is a palindrome, false otherwise. 

A palindrome is a word that is spelled the same forwards and backwards.



"""

#lab_8-4
def count_a(word):
    # start variable for a
    a_count = 0
    
    
    for char in word:
        # looks for a and A
        if char == 'a' or char == 'A':
                    a_count += 1
    
    # sends back the amount of a found
    return a_count

word_example = "Anagram"
result = count_a(word_example)
print(f"The number of 'a's in '{word_example}' totals to {result}")

#lab_8-5

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
result = factorial(9)
print(result)

#lab_8-6
def is_palindrome(word):
    # makes it lowercase
    lowercase_word = word.lower()
    
    # Reverse the lowercase word using slicing
    reversed_word = lowercase_word[::-1]
    
    # Check if the original and reversed words are the same, if not it returns it as false
    return lowercase_word == reversed_word

word_to_check = "superfluous"
result = is_palindrome(word_to_check)

# Print the result
print(f"The word '{word_to_check}' is a palindrome: {result}")