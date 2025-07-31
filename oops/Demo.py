a = 7
b = 0
c = 0

try:
    print("File open")
    b  = int(input("Enter a number"))
    c = a / b

except ValueError:
    print("number only")
except ZeroDivisionError:
    print("0 can't be devide")
except Exception:
    print("Some unknown error")
else:
    print(c)
finally:
    print("File close")


print("BUY")