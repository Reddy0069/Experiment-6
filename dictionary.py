
staff = {
    "Name": "Rahul",
    "Age": 21,
    "Post": "Python Developer",
    "Salary": 70000
}

# Code 1: Accessing dictionary elements
print("Dictionary:", staff)

print("Employee Name:", staff["Name"])
print("Employee Age:", staff["Age"])
print("Employee Post:", staff["Post"])
print("Salary:", staff["Salary"])


# Code 2: Adding, updating and deleting elements
staff["ID"] = "25BCAR0141"
print("After Adding:", staff)

staff["Age"] = 20
print("After Updating Age:", staff)

del staff["Salary"]
print("After Deleting Salary:", staff)


# Code 3: Character frequency
text = input("\nEnter a string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

print("Character Frequency:")

for ch, count in freq.items():
    print(ch, ":", count)


# Code 4: Dictionary methods
print("\nKeys:")
print(staff.keys())

print("Values:")
print(staff.values())

print("Items:")
print(staff.items())

print("Name:", staff.get("Name"))
print("Marks:", staff.get("Marks", "Not Available"))

staff.update({"Age": 20, "Marks": 9})

print("After Updating Dictionary:")
print(staff)

