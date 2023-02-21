from functools import reduce


def double_comp(lst):
    return [x*2 for x in lst]


def double_recur(lst):
    if len(lst) == 1:
        return [lst[0]*2]
    return [lst[0] * 2] + double_recur(lst[1:])


def double_high_helper(x):
    return x*2


def double_high(lst, func):
    return list(map(func, lst))


print(double_comp([1, 2, 3]))
print(double_recur([1, 2, 3]))
print(double_high([1, 2, 3], double_high_helper))


def flatten_comp(lst):
    return [x for y in lst for x in y]


def flatten_recur(lst):
    if len(lst) == 0:
        return []
    return lst[0] + flatten_recur(lst[1:])


def flatten_high(lst):
    return reduce(lambda cur, ele: cur + ele, lst, [])


print(flatten_comp([[1, 2, 3], [3, 4, 5]]))
print(flatten_recur([[1, 2, 3], [3, 4, 5]]))
print(flatten_high([[1, 2, 3], [3, 4, 5]]))


def double(num):
    return num * 2


def increase(num):
    return num + 1


def square(num):
    return num ** 2


def compose(f, g):
    return lambda x: g(f(x))


def compose_high(*func):
    if len(func) <= 1:
        raise TypeError()
    return reduce(compose, func, lambda x: x)


def compose_recur(*func):
    if len(func) == 0:
        return lambda x: x
    return compose(func[0], compose_recur(*func[1:]))


double_square = compose_high(double, square)
increase_square = compose_recur(increase, square)
print(double_square(5))
print(increase_square(5))
