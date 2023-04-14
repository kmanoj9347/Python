#count the number of alphabets in the string 
#and print the alphabets.
string ='Manoj Kumar'
count =0

#Initialising new strings
newstring1=""
newstring2=""

#Interating the string and checking for alphabets
#Incrementing the counter if an alphabet is found
#Finaaly printing the count
for a in string:
    if (a.isalpha()) == True:
        count+=1
        newstring1 +=a
print(count)
print(newstring1)
 
string ='MAnoj123'
count =0
for a in string:
    if (a.isalpha()) == True:
        count+=1
        newstring2+=a
print(count)
print(newstring2)
   

