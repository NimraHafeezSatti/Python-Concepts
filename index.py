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
#args2s
def add(*stuffs):
    sum=0
    stuffs=list(stuffs)
    stuffs[0]=0
    for i in stuffs:
        sum +=i
    return sum


print(add(1,2,3,4,5))
