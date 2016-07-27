"""
for x in range(10):
    print(x)
   
for x in range(5, 10):
    print(x)

for x in range(5, 10, 2):
    print(x)
"""    
auto = [5, 4, 3, 2, 22, 19]

"""
for x in auto:
    print(x)

for x in auto[:4]:
    print(x)

for x in auto[:4]:
    if x == 4:
        print("Found a 4!")

#Result - Found a 4!
#Because no condition was specified for x != 4 I guess the program just didn't do anything during that iteration



for x in auto[:4]:
    if x == 4:
        print("Found a 4!")
    else:
        print("No fours here!")

Results:
        No fours here!
        Found a 4!
        No fours here!
        No fours here!

#Only possible within Function: return 4 in auto[:4]

#Equivalent:
for x in range(10):
    print(x)

for x in range(0, 10):
    print(x)

for x in range(0, 10, 1):
    print(x)
"""
