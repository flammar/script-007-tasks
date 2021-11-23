"""This is demo module.

It contains a lof useful functions.
Here you can find a class `MyClass`.
"""


class MyClass:
    @staticmethod
    def sum(a: int, b: int) -> int:
        """Sum the values of two numbers.

        Args:
            a (int): number 1
            b (int): number 2

        Returns:
            This is a description of what is returned.

        Raises:
            KeyError: Raises an exception.
        """
        return a + b


print(dir(MyClass.sum))
print("__annotations__:", MyClass.sum.__annotations__)
print("__doc__:", MyClass.sum.__doc__)
print("call:", MyClass.sum(1, 2))
print("call:", MyClass.sum("bug", "bug"))
print("call:", MyClass.sum(1, "bug"))
