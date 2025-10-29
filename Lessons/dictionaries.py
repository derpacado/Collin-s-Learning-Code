"""
Lesson 4 – Dictionaries
Goal: Learn how to store, access, modify, and iterate through key-value data.
"""

# --- Part 1: Creating and Accessing Dictionaries ---
'''student = {
    "name": "Collin",
    "age": 15,
    "favorite_language": "Python"
}

print("Accessing values:")
print("Name:", student["name"])
print("Favorite language:", student["favorite_language"])
print()

# --- Part 2: Adding, Updating, and Deleting ---
student["age"] = 18  # update
student["grade"] = "12th"  # add
del student["favorite_language"]  # delete

print("Modified dictionary:", student)
print()

# --- Part 3: Iterating Over Dictionaries ---
print("Iterating through keys:")
for key in student:
    print(key, "->", student[key])

print("\nIterating through key-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# --- Part 4: Nested Dictionaries and Lists ---
class_roster = {
    "Collin": {"age": 16, "score": 92},
    "Mia": {"age": 15, "score": 88},
    "Ethan": {"age": 16, "score": 95}
}

print("\nClass roster:")
for name, info in class_roster.items():
    print(f"{name} - Age: {info['age']}, Score: {info['score']}")'''

# --- Part 5: Practice – Flashcard Quiz ---
print("\n=== Flashcard Quiz ===")

flashcards = {
    "What is the color of the sky?" : "blue",
    "What is the color of the sand?" : "yellow",
    "What is the color of the dirt?" : "brown",
    "What is the color of my shirt?" : "gray"
}
answers=[]
total=0
for key in flashcards:
    print(key)
    a=input()
    answers.append(a)
    if a == flashcards[key]:
        total+= 1
print(f"You got   {total}  /  {len(flashcards)}   correct.")