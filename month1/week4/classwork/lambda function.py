x,y = map(int,input("Enter Two Numbers").split())
sum_func = lambda x,y : x+y
print(sum_func(x,y))

sqr_func = lambda x: x**2
print(sqr_func(x))

even_func = lambda y: y%2==0
print(even_func(y))

lst = list(map(int,input().split()))
evens = filter(lambda x: x%2==0, lst)
print(evens)

doubled = map(lambda x: x*2, lst)
print(doubled)

