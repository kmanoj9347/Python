def  Square():
    i =1
    #An infinite loop to generate squares
    while True:
        yield i*i
        i +=1
for num in Square():
    if num > 100:
        break
    print(num)