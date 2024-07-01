# #slicing
# name="bro code"
# first_name=name[:3]
# print(first_name)
#function
# def hello():
#     print("hello!")






# hello()
# hello()
# hello()
#exception
# try:
#     numerator=int(input("divide number by:"))
#     denominator=int(input("divide  number by:"))
#     result=numerator/denominator
# except ZeroDivisionError:
#      print("idiot!you can't divide it by zero!")

# except Exception:
#     print("something went wrong!")
# except ValueError:
#      print("you entered invalid input! please enter a number.")
# else:
#     print(result)
# finally:
#     print("This is always executed.")
#stringformat
# a
#args
def add(*stuffs):
    result=0
    for stuff in stuffs:
        result+=stuff
    return result
print(add(1,4,5,2,4,4,5))