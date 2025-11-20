phonebook = {
    "Alice": "09123456789",
    "Bob": "09987654321",
    "Charlie": "09223334444"
}

print("Alice's number is: " + phonebook["Alice"])
for name, number in phonebook.items():
    print(name + ": " + number)
