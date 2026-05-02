try:
    n1,n2=eval(input("enter two numbers seperated with a comma ="))
    res=n1/n2
    print(res)
except ZeroDivisionError:
    print("Division by zero")
except SyntaxError:
    print("comma is missing")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this program will execute")