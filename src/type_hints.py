from typing import Union, Callable
# Any -> Any value
# Union -> mix value types

# Primitive types
string: str = 'abc'
integer: int = 2
boolean: bool = True
float_num: float = 2.4

# Collections
list_type: list = ['aa', 3, 4]
integer_list: list[int] = [2, 3, 4]
mixed_list: list[Union[int, str]] = [2, 'a']


tuple_type: tuple = (2, 2, 2, 2)
specify_tuple: tuple[int, int, int, str] = (
    2, 3, 4, 'a')  # must specify each index

# My Type

myDict = dict[str, Union[str, int, list[int]]]  # Alias

# Dictionary
dict_type: dict = {'key': 'value'}
specify_dict: myDict = {
    'key': 2,
    'potato': 'Ok',
    'banana': [1, 2]
}

# Callable -> receive a function, pass the arguments
#  in a list and second parameter its the return of the function passed


def exec_function(function: Callable[[], None]) -> Callable:
    return function


def say_hi() -> None:
    print('hi')
    return


exec_function(say_hi)()


def exec_sum(function: Callable[[int, int], int]) -> Callable:
    return function


def summ(x: int, y: int) -> int:
    return x + y


result = exec_sum(summ)(10, 15)
print(result)
