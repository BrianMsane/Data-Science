import inspect
from typing import Callable


class Tool:
    """
    Generic and resuable code for a Tool

    Attributes:
        name(str): Name of the tool.
        description(str): A textual description of what the tool does.
        func (typing.Callable): A function this tool wraps.
        arguments(list): A list of arguments
        outpus(str or list): The return type(s) of the wrapped function
    """

    def __init__(
        self,
        name: str,
        description: str,
        func: Callable,
        arguments: list,
        outputs: str | list,
    ):
        self.name = name
        self.description = description
        self.func = func
        self.arguments = arguments
        self.outputs = outputs

    def to_string(self) -> str:
        """
        Return the string representation of the tool including its \
            name, description, arguments, and outputs
        """

        arg_str = ", ".join(
            [f"{arg_name}: {arg_type}" for arg_name, arg_type in self.arguments]
        )
        return (
            f"Tool name: {self.name},"
            f"Description: {self.description},"
            f"Arguments: {arg_str},"
            f"Outpus: {self.outputs}"
        )

    def __call__(self, *args, **kwargs):
        """
        Invoke teh underlying function with the provided arguments
        """
        return self.func(*args, **kwargs)


def tool(func):
    """
    Decorator that creates a Tool instance from the given function
    """
    signature = inspect.signature(func)  # python 3.13
    arguments = []
    for param in signature.parameters.values():
        annotation_name = (
            param.annotation.__name__
            if hasattr(param.annotation, "__name__")
            else str(param.annotation)
        )
        arguments.append((param.name, annotation_name))

    return_annotation = signature.return_annotation
    if return_annotation is inspect._empty:
        outputs = "No return annotation"
    else:
        outputs = (
            return_annotation.__name__
            if hasattr(return_annotation, "__name__")
            else str(return_annotation)
        )

    return Tool(
        name=func.__name__,
        description=func.__doc__ or "No description provided",
        func=func,
        arguments=arguments,
        outputs=outputs,
    )


def calculator(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


# Two different ways of creating a tool now


@tool
def say_hello(name: str, surname: str):
    return "Hello {}, {}".format(name, surname)


calculator = Tool(
    "calculator",
    "Multiply two numbers",
    calculator,
    [{"a": "int", "b": "int"}],
    "int",
)

print(
    calculator.to_string()
)  # Tool name: calculator, Description: Multiply two numbers, Arguments: a: int, b: int, Output: int

print(
    say_hello.to_string()
)  # Tool name: say_hello, Description: No description provided, Arguments: name: str, surname: str, Output: No return annotation
