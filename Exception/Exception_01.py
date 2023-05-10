#To handle simple runtime error

a = [1,2,3]
try:
    print("Second element = %d "%(a[1]))
    print("Fourth elements = %d"%(a[3]))

except:
    print("An error occurred")