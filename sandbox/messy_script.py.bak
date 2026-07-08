# Refactored script.

def my_function(a: int, b: int, c: int) -> int:
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


def another_function(x_val: bool, y_val: bool) -> None:
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
    def __init__(self, name: str, age: int):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        self.name = name
        self.age = age

    def display(self) -> None:
        """
        Displays the name and age of the person.
        """
        print("Name:", self.name, "Age:", self.age)

    def __str__(self) -> str:
        """
        Returns a string representation of the MyClass object.
        """
        return f"MyClass(name='{self.name}', age={self.age})"

    def __repr__(self) -> str:
        """
        Returns a developer-friendly string representation of the MyClass object.
        """
        return self.__str__()


if __name__ == "__main__":
    # Localized variables for my_function
    x = 10
    y = 20
    z = 30

    print(my_function(x, y, z))
    another_function(True, False)

    try:
        obj = MyClass("Alice", 25)
        obj.display()
        print(obj) # Demonstrates __str__
    except ValueError as e:
        print(f"Error creating MyClass object: {e}")

    try:
        # Example of invalid input
        invalid_obj = MyClass("", -5)
    except ValueError as e:
        print(f"Error creating MyClass object: {e}")
