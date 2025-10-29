#task 1 - enter fulll name and print it on new line
'''print("Write full name here:")
phrase = input("")
for i in range(len(phrase)):
    print(phrase[i])'''

#task 2 - printing multiples of numbers
'''num = int(input("Enter number between 1 and 10:"))
result=num
while result < 101:
    print(result)
    result = result + num'''

#task 3 - password problems
'''password = "truksrcul"
userPassword = input("Enter password:")
wrongs = 0
while userPassword != password:
    print("Wrong password")
    userPassword = input("Try Again:")
    wrongs += 1
print("It took you " + str(wrongs) + " times")'''

#task 4 - summing perfect squares
total=0
i=1
while i*i < 101:
    total = total + i*i
    i += 1
print(str(total))
