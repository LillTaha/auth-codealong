def divide(numerator, denominator):
    try:
        result = numerator / denominator
        print("The result of", numerator ,"divided by", denominator, "is", result)
    except ZeroDivisionError:
        print("can't divide by zero")
    except TypeError:
        print("wrong type")

divide(12,3)
divide(3,0)
divide("a","b")










# list = [1, 2, 3, 4, 5]
# try:
#     for i in list:
#         print("The value is :" ,list[i])

# except IndexError:
#     print("Error: Index is out of range.")