def greeting(name):
    print(f"Hello, {name}")
greeting(input("Enter name "))

def summ(a,b):
    return a+b
a,b = map(int,input("Enter Two Numbers").split())
print(summ(a,b))

inputs = input("Enter any amount of inputs ").split()
def print_args(*args):
    for arg in args:
        print(arg)
print_args(*inputs)

lst = list(map(int, input("enter any amount of numbers: ").split()))
def average(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ / len(args)
print(average(*lst))
