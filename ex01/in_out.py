def square(x: int | float) -> int | float:
    """
    Returns the square of the given number.

    Args:
        x (int | float): The number to square.

    Returns:
        int | float: The square of the number.

    Usage:
        print(square(2))  # Prints 4
        print(square(1.5))  # Prints 2.25
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Returns the number raised to the power of itself.

    Args:
        x (int | float): The number to raise to its own power.

    Returns:
        int | float: The number raised to the power of itself.

    Usage:
        print(pow(2))  # Prints 4
        print(pow(1.5))  # Prints 1.8371173070873836
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a function that applies the given function to its argument,
    and then applies the function to the result each time it's called.

    Args:
        x (int | float): The initial value to apply the function to.
        function (callable): The function to apply.

    Returns:
        function: A function that applies the given function to its argument,
                  and then applies the function to the result each time it's
                  called.

    Usage:
        double = outer(2, lambda x: x * 2)
        print(double())  # Prints 4
        print(double())  # Prints 8
        print(double())  # Prints 16
    """
    count = 1
    result = [x]

    def inner() -> float:
        nonlocal count
        if count > 0:
            result[0] = function(result[0])
        count += 1
        return result[0]
    return inner


def main() -> None:
    my_counter = outer(-3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
