
# תרגיל 1
def if_even_return_the_lowest_number(*args):
    for i in args:
        if i % 2 != 0:
           return "not all the numbers are even"
    return abs(min(args))

print(if_even_return_the_lowest_number(1,2,3,4,5,6,7,8,9,10))
print(if_even_return_the_lowest_number(6,8,-2,-8,10))

# תרגיל 2
def order_list_with_original_index(*args):
    for i in args:
        list = len(i)
    print(list)

order_list_with_original_index("ghsd", "vosdkjdvs")

# תרגיל 3
def the_diff(char1, char2):
    char1 = ord(char1)
    char2 = ord(char2)
    return char1 - char2

print(the_diff("a", "b"))
