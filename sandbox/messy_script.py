# Refactored script.

def calculate_sum(a: int, b: int, c: int) -> int:
    """
    Calculates the sum of three numbers.

    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.

    Returns:
        int: The sum of the three numbers.
    """
    total_sum = a + b + c
    return total_sum


def demonstrate_conditionals_and_iteration(check_x: bool, check_y: bool) -> None:
    """
    Demonstrates conditional logic and list iteration.

    Args:
        check_x (bool): A boolean value to check for condition x.
        check_y (bool): A boolean value to check for condition y.
    """
    if check_x:
        print("x is true")
    if not check_y:
        print("y is false")
    numbers_list = [1, 2, 3, 4, 5]
    for number in numbers_list:
        print(number)


class Person:
    """
    A simple class to represent a person.
    """
    def __init__(self, name: str, age: int):
        """
        Initializes a new Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.

        Raises:
            ValueError: If name is not a non-empty string or age is not a positive integer.
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        self.name = name
        self.age = age

    def display_info(self) -> None:
        """
        Displays the name and age of the person.
        """
        print("Name:", self.name, "Age:", self.age)

    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the Person object.
        """
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self) -> str:
        """
        Returns a developer-friendly string representation of the Person object.
        """
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"


if __name__ == "__main__":
    # Variables for calculate_sum
    num1 = 10
    num2 = 20
    num3 = 30

    print(calculate_sum(num1, num2, num3))
    demonstrate_conditionals_and_iteration(True, False)

    try:
        person_obj = Person("Alice", 25)
        person_obj.display_info()
        print(person_obj)  # Demonstrates __str__
    except ValueError as e:
        print(f"Error creating Person object: {e}")

    try:
        # Example of invalid input
        invalid_person_obj = Person("", -5)
    except ValueError as e:
        print(f"Error creating Person object: {e}")