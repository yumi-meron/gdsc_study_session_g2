char = input("Enter a character: ")
if char in ['a','e','i', 'o','u']:
    print("vowels are not allowed in the input.")
elif len(char)>1:
    print("The length of the character should be one.")
else:
    for i in range(1,10,2):
        s = char * i
        print(s)