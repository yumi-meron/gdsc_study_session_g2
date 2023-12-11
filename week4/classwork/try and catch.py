def sum(x,y):
    try:
        int(x) + int(y)
    except ValueError:
        print("Invalid input value")
    else:
        print(x+y)
x,y=map(int, input("enter two numbers").split())
print(sum(x,y))
'''def divide(x,y):
    try:
        x/y
    except ZeroDivisionError:
        print("you are trying to divide by zero")
    else:
        print(x/y)
x=int(input())
y=int(input())
print(divide(x,y))'''