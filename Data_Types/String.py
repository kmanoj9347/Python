String1 ='Welcome to the world'
print("String withu use of single quotes: ")
print(String1)

String1 ="I am Manoj"
print("\nString with the use of double quotes: ")
print(String1)

String1 ='''\nString with triple Quotes'''
print(String1)
print()

String1 ='''k
        Manoj
        kumar'''
print("\nCreating a multiline string: ")
print(String1)

#Access character of string
print("Acessing of characters:")
print(String1[0])
print(String1[12])
print(String1[-8])

#Reversing of string
print("Reversing of string:")
print(String1[::-1])
#using reversed and join function
print("Reversing string using revered function")
String1 ="".join(reversed(String1))
print(String1)

#updating a character of the string
#1
String1 ="ManojKumar"
list1 =list(String1)
list1[2]='p'
String2=''.join(list1)
print("\nUpdating character atv2nd Index: ")
print(String2)
#2
String2 = String1[0:1]+'p'+String1[5:]
print(String2)

#Escape Sequencing of String
#1
String1 = 'I\'m "Manoj"'
print("\nEscaping Single Quotes: ")
print(String1)
#2
String1 = "I'm \"Manoj\""
print("\nEscaping Double Quotes: ")
print(String1)
#3
String1 = "Hi\tHello"
print("\nTab: ")
print(String1)

