try:
    n=int(input("enter your number="))
    print("number entered is",n)
except ValueError as ex:
    print("exception :",ex)
