# Fixed messy script.

x = 10
y = 20
z = 30


def my_function(a, b, c):
    """
    Calculates the sum of three numbers.

    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.

    Returns:
        int: The sum of the three numbers.
    """
    result = a + b + c
    return result


def another_function(x_val, y_val):
    """
    Demonstrates conditional logic and list iteration.

    Args:
        x_val (bool): A boolean value to check.
        y_val (bool): Another boolean value to check.
    """
    if x_val:
        print("x is true")
    if not y_val:
        print("y is false")
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        print(item)


class MyClass:
    """
    A simple class to represent a person.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        """
        Displays the name and age of the person.
        """
        print("Name:", self.name, "Age:", self.age)


print(my_function(x, y, z))
another_function(True, False)
obj = MyClass("Alice", 25)
obj.display()
