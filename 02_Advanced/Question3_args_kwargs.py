# My wrong solution
def get_args_and_kwargs(*args, **kwargs):
    if len(args) >= 4:
        return True

    if "num" in kwargs and type(kwargs['num']) is int and kwargs['num'] >= 5:
        return True

    return False

# print(get_args_and_kwargs("a", [2], 3, num=4))
# print(get_args_and_kwargs("a", [2], 3, num=6))
# print(get_args_and_kwargs("a", [2], 3, num=6, x=True))
# print(get_args_and_kwargs(2, 3, a=1, b=2, num="6"))
print(get_args_and_kwargs(2, 3, a=1, b=2, number="7"))


# Tim solution
def get_args_and_kwargs(*args, **kwargs):
    number_of_args = len(args) + len(kwargs)
    num = kwargs.get("num", 0)

    if not isinstance(num, int) and not isinstance(num, float):
        return False

    return number_of_args >= 4 and num > 5