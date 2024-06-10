from typing import Any


def callLimit(limit: int):
    """
    Decorator that limits the number of times a function can be called.

    Args:
        limit (int): The maximum number of times the decorated function
        can be called.

    Returns:
        function: A new function that wraps the original function, limiting
        its number of calls.

    Usage:
        @callLimit(3)
        def my_function():
            pass
    """
    count = [0]

    def callLimiter(function):

        def limit_function(*args: Any, **kwargs: Any):
            if count[0] < limit:
                count[0] += 1
                return function(*args, **kwargs)
            else:
                print(f"""Error: <function {function.__name__} at
                      {hex(id(function))}> call too many times""")
        return limit_function
    return callLimiter


def main():
    @callLimit(3)  # same as f = callLimit(limit)(function)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
