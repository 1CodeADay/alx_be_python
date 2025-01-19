# def file():
#     try:
#         f = input("Enter the name of the file to open: ")
#         if f == "test.txt":
#             print(f.read())
#         else:
#             print(f"File '{f}' not found.")
#     except FileNotFoundError:
#         print(f"File '{f}' not found.")

# file()


class ValueTooHighError(Exception):

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Value too high: {self.number}"


try:
    # take input
    # check if unput > 100
    # raise error
    num = int(input("Enter a number: "))
    if num > 100:
        raise ValueTooHighError(num)
    else :
        print("Number is less than 100")
except ValueTooHighError as e:
    print(e)
except ValueError:
    print("Invalid input.")

ValueTooHighError(num)
