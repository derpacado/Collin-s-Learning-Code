#function for printing out numbers to ten and sum
def print10():
    total = 0
    for i in range(1, 11):
        print(str(i))
        total+= i
    return total

#function for printing out word
def print_word(word):
    for i in range (len(word)):
        print(word[i])
print(print10())