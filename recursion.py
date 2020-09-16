# def say_hello(name):
#     print('Hello, {}'.format(name))
#     say_hello(name)


# say_hello('Infinity')

# def countdown(num):
#     # base case
#     if num == 0:
#         print('Blast off!')
#         return

#     # recursive step
#     print(num)
#     countdown(num - 1)


# countdown(10)

# handles edge case for negative number

# def countdown(num):
#   # base case
#     if num == 0:
#         print('Blast off!')
#         return
#     elif num < 0:
#         print('Please add a positive number and try again')
#         return
#   # recursive step

#     print(num)
#     countdown(num - 1)


# countdown(100)
# countdown(-10)

numbers = [1, 2, 3, 4, 5]


def add_number(array, result=0):
    num = array.pop()
    result += num
    if len(array) == 0:
        return result
    return add_number(array, result)


print(add_number(numbers))

# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def alphabet(letters):
#     sing = abc.pop(0)
#     print(sing)
#     if len(letters):
#         alphabet(letters)
#     else:
#         print('Now I know my abc\'s, next time won\'t you sing with me')
#         return
# alphabet(abc)
