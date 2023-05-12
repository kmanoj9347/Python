class Error(Exception):
    pass
class zerodivision(Error):
    pass
try:
    i_num = int(input("Enter a number: "))
    if i_num == 0:
        raise zerodivision
except zerodivision:
    print("Input value is zero,try again!")
    print()