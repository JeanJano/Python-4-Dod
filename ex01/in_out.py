def square(x: int | float) -> int | float:
    return x * x


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
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
