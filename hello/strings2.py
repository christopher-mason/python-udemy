#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw

number = "9,223,372,036,854,775,807"
print(number[1::4])
number2 = "9,223;372:036 854,775;807"
print(number2[1::4])
seperators = number2[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number2).split()
print([int(val) for val in values])


'''
print(parrot[0:6]) # Norweg... Up tp but not including position 6
print(parrot[-14:-8])
print(parrot[-4:-2]) # Bl
print(parrot[-4:12])
'''

'''
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9]) # start value defaults to start of sepuence, so up to but not including 9
print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])
print(parrot[:])

letters = "abcdefghijklmnopqrstuvwxyz"
'''


#print(parrot)

#print(parrot[3])
#print(parrot[4])
#print(parrot[9])
#print(parrot[3])
#print(parrot[6])
#print(parrot[8])

#print()

#print(parrot[-11])
#print(parrot[-10])
#print(parrot[-5])
#print(parrot[-11])
#print(parrot[-8])
#print(parrot[-6])