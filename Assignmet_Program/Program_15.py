# TO convert temperatures to and from celsius, Fahrenheit
temp=input("Enter the temperatures in celsius or fahrenheit: ")
d=int(temp[:-1])
i=temp[-1]
if i.upper()=="C":
    r=int(round((d*9)/5+32))
    h="Fahreheit"
elif i.upper()=="F":
    r=int(round(d-32)*(5/9))
    h="Celsius"
print(f"The temperatures in {h} is {r} degress")
