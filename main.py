#STRING
#a = "Adarsh"
'''
print(a[-1:-6])
Start index = -1 → 'h'
Stop index = -6 → before 'A'
Step is +1 by default.

With a positive step, Python moves left to right. Since the start (-1) is already to the right of the stop (-6), 
it can't move forward to reach it, so 
result is an empty string

a[start:stop] → step is +1 (left → right)
a[start:stop:-1] → step is -1 (right → left)
'''
#print(a[-1:-7:-1]) 
#print(a[::-1])



'''
a = input("Enter the Word :- ")
b = a[::-1]
print(a[0:len(a)] == b)
'''


'''
a = input("Enter The Word :- ")
print(a.count("a"))
print(a.count("e"))
print(a.count("i"))
print(a.count("o"))
print(a.count("u"))
'''

'''
a = input("Enter Anything You Want :- ")
print(a.replace(" ", ""))
'''

a = input("Enter The Word :- ")
print(a)
#b = a.replace("a,i,e,o,u", "*")
print(a.replace("a","*"))


#a = input("Enter the Word :- ")
