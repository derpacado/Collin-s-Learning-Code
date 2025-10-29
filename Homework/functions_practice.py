'''Complete the following functions/conditionals/loops practice problems. 
Once you have done your best on each, try out the nested loops Bonus problem from last homework'''

# Write a function that takes in a parameter called `prompt`, gets user input using that prompt, then returns the first letter of whatever the user entered
def get_prompt_response(prompt):
    phrase = input(prompt) 
    return phrase[0]
'''print(get_prompt_response("Type here: "))'''
# Write a function that takes in 3 numbers and returns whichever number is biggest between the 3 of them 

#print("Find biggest number")
import random
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)
def find_biggest(num1, num2, num3):
    print(num1, num2, num3)
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
'''print(find_biggest(num1, num2, num3))'''

# Write a function that takes in 2 words and returns the longer word
def find_long_word():
    print("Find longest word!")
    word1 = (input("Input first word: "))
    word2 = (input("Input second word: "))
    if len(word1) > len(word2):
        print(str(word1))
    else:
        print(str(word2))
'''find_long_word()'''

# Write a function that takes in a number n, and then prints the numbers from 1 to n, but...
    # if n is a multiple of 3, it prints "Fizz"
    # if a multiple of 5, prints "Buzz"
    # if multiple of both, prints "FizzBuzz"
def fizzbuzz(n):
    for i in range(1, n + 1, 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
#fizzbuzz(36)
# Write a function that takes in a number and returns its factorial
def find_factorial(num):
    total = 1
    i = 1
    while i <= num:
        total = total*i
        i += 1
    return(total)
#print(find_factorial(6))

# Write a function that takes in a string and a letter and returns how many times that letter appears in the string
def  letter_count(write, let):
    count = 0
    for i in write:
        if i == let:
            count += 1
    print("There are " + str(count) + " " + str(let) + "'s in " + str(write) + ".")
    return(count)
letter_count("mississippi", "s")