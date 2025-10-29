"""
Lesson 5 – Files and Error Handling
Goal: Learn to save data persistently and handle problems gracefully.
"""

import json

# --- Part 1: Writing and Reading Plain Text Files ---
print("Writing to 'notes.txt'...")
with open("notes.txt", "w") as f:
    f.write("This is a test note.\n")
    f.write("Files let your programs remember things!")

print("Reading back from 'notes.txt':")
with open("notes.txt", "r") as f:
    print(f.read())

# --- Part 2: Handling Errors Gracefully ---
print("\nTrying to open a non-existent file:")
try:
    with open("missing.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("⚠️ File not found! Creating a new one instead.")
    with open("missing.txt", "w") as f:
        f.write("This file was just created because it didn't exist.")

# --- Part 3: Saving Dictionaries to JSON ---
inventory = {
    "apples": 5,
    "bananas": 2,
    "pears": 7
}

print("\nSaving inventory to JSON...")
with open("inventory.json", "w") as f:
    json.dump(inventory, f, indent=2)

print("Loading inventory back in:")
try:
    with open("inventory.json", "r") as f:
        data = json.load(f)
    print("Inventory loaded successfully:", data)
except json.JSONDecodeError:
    print("Oops! There was a problem decoding the JSON file.")

# --- Part 4: Practice Challenge ---
"""
CHALLENGE:
1. Ask the user for a list of tasks and save them to 'todo.json'.
2. Next time the program runs, load and display the list first.
3. Use try/except to handle the case where the file doesn't exist yet.
"""