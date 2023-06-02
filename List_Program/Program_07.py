# To check if an element exists in the list or not
# using count()

test_list= [10,14,67,34,7,34,864]
print("checking if 14 exists in list")

#number of times element exists in list
exist_count = test_list.count(14)

#checking if it is more than than 0
if exist_count > 0:
    print("yes,14 exists in list")
else:
    print("No ,15 does not exists in list")
