#Start learning about data structures below!

'''
DATA STRUCTURES
A data structure is a way of organizing and storing data so that it can be accessed and modified in our programs. 
In Python, some of the most commonly used data structures are 
    - lists
    - tuples
    - sets
    - dictionaries
We will go over each of these data structures and provide examples of how to use them.


USING LOOPS WITH DATA STRUCTURES
Since data structures hold multiple items, we often use loops to iterate over them.
We can always use a "for each" loop to go through each item in a data structure.
For example, if we have a list of numbers and we want to print each number, we can use a for loop like this:

numbers = [1, 2, 3, 4, 5]
for number in numbers:
print(number)

This will loop through each number in the list and print it to the console. See more examples below.
'''


# LISTS:
# Lists are ordered collections of items that can be modified. They are defined using square brackets []
'''my_list = [1, 2, 3, 'four', 'five']

# We can access items in a list using their index (starting from 0)
first_item = my_list[0]
print("First item in the list:", first_item) # Output: 1

# We can modify items in a list by assigning a new value to a specific index
my_list[1] = 'two'
print("Modified list:", my_list) # Output: [1, 'two', 3, 'four', 'five']

# We can add items to a list using the append() method
my_list.append('six')
print("List after appending an item:", my_list) # Output: [1, 'two', 3, 'four', 'five', 'six']

# We can remove items from a list using the remove() method
my_list.remove(3)
print("List after removing an item:", my_list) # Output: [1, 'two', 'four', 'five', 'six']

# Finally, we can loop through a list using a for loop
print("Looping through the list:")
for item in my_list:
    print(item, end=', ') # Output: 1, two, four, five, six,
print() # for a new line'''


'''----------------------------------------------------------------'''
# PRACTICE PROBLEMS WITH LISTS:
# 1. Create a list of your favorite fruits and print each fruit using a loop.
fruits = ['banana', 'apple', 'raspberry']
print(fruits)
# 2. Add a new fruit to your list and print the updated list.
fruits.append("mango")
for item in fruits:
    print(item)

# 3. Remove a fruit from your list and print the updated list.
fruits.remove('apple')
print(fruits)

# 4. Modify a fruit in your list and print the updated list.
fruits[1] = "blueberries"
print(fruits)

# 5. Print the number of fruits in your list. (Hint: use the len() function, just like with strings)
print(len(fruits))



'''That's all for now! Next time, we will cover tuples, sets, and dictionaries. :)'''
