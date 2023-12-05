user = input("Enter a word: ")
if user == user[::-1]:
    print(f"The word {user} is palindrome.")
else:
    print(f"The word {user} is not palindrome,\n Because {user[::-1]} is not equal to {user}.")