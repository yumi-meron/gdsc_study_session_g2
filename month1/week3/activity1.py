"""
for i in range(99):
    print("{:02d}, ".format(i),end = '')
print(str(i+1)) 
"""

print(', '.join(["{:02d}".format(i) for i in range(99)]) + ', 99') 