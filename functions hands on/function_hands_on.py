def all_sum(a, b, c):
    return a + b + c


print(all_sum(2, 4, 6))


def multiply_them_all(a, b, c):
    return a * b * c


print(multiply_them_all(6, 5, 4))


def average(a, b, c):
    return (a + b + c) / 3


print(average(5, 4, 5))
# print(average((5), (4), (5)))

""" stretch goal 1 do the same thing above, but as a lambda expression """


#def add_alot(a, b, c): return a + b + c

def number(x, y, z): return x + y + z


print(number(2, 4, 6))


def muliply_alot(a, b, c): return a * b * c


print(muliply_alot(10, 20, 30))


def average_it_all(a, b, c): return (a + b + c) / 3


print(average_it_all(2, 4, 6))

""" STRETCH GOAL 2"""


list_1 = [4, 5, 6, 7, 8, 9, 10]
list_2 = [1, 2, 4, 5, 6, 7, 8]
list_3 = [4, 6, 9, 9, 7, 2, 2]

list_a = sum(list_1)
list_b = sum(list_2)
list_c = sum(list_3)

list_fuck_your_ass = list_a + list_b + list_c

print((list_fuck_your_ass) / 3)
