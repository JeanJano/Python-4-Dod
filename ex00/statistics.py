def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Calculate and print various statistical measures for a list of numbers.

    The function accepts any number of positional arguments, which should be
    numbers.
    It also accepts keyword arguments specifying which statistical measures
    to calculate.
    The possible keyword arguments are "mean", "median", "quartile", "std",
    and "var".

    Args:
        *args: The numbers to calculate statistics for.
        **kwargs: The statistical measures to calculate. The keys should
        be the names of the measures, and the values should be the names of
        the measures.

    Prints:
        The calculated statistical measures. If a measure is specified but
        cannot be calculated
        (for example, if the list of numbers is empty), an error message is
        printed.

    Usage:
        ft_statistics(1, 2, 3, 4, 5, mean="mean", median="median",
        quartile="quartile", std="std", var="var")
    """
    arr = []
    for arg in args:
        if isinstance(arg, (int, float, complex)):
            arr.append(arg)
    arr.sort()

    for key, value in kwargs.items():
        if value == "mean" and arr:
            print(f"mean: {sum(arr) / len(arr)}")
        elif value == "median" and arr:
            print(f"median: {arr[len(arr) // 2]}")
        elif value == "quartile" and arr:
            print(f"""quartile: [{float(arr[len(arr) // 4])},
                  {float(arr[len(arr) // 4 * 3])}]""")
        elif value == "std" and arr:
            mean = sum(arr) / len(arr)
            variance = sum((x - mean) ** 2 for x in arr) / len(arr)
            print(f"std: {variance ** 0.5}")
        elif value == "var" and arr:
            mean = sum(arr) / len(arr)
            variance = sum((x - mean) ** 2 for x in arr) / len(arr)
            print(f"var: {variance}")
        elif arr == [] and (value == 'mean'
                            or value == 'median'
                            or value == 'quartile'
                            or value == 'std'
                            or value == 'var'):
            print("Error")


def main() -> None:
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                  tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std",
                  world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                  ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
