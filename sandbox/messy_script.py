#Fixed messy script.

x = 10
y = 20
z = 30


def my_function(a, b, c):
    result = a + b + c
    return result


def another_function(x_val, y_val):
    if x_val:
        print("x is true")
    if not y_val:
        print("y is false")
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        print(item)


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name, "Age:", self.age)


my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_function(x, y, z))
another_function(True, False)
obj = MyClass("Alice", 25)
obj.display()
