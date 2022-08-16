def add(*args):
    result = 0
    for i in args:
        result += i

    return result

print(add(1, 1, 1))
