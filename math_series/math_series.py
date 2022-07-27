def fibonacci(num):
    """
    if number is 0 return 0
    if number is number is 1 return 1
    if number is 2 return 1
    if number is not 0 or 1 or 2 return fibonacci(n-1) +  fibonacci(n-2)

    """
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def lucas(num):
    """
    if number is 0 return 2
    if number is 1 return 1
    if number is not 0 or 1 return lucas(n-1)+ lucas(n-2)
    """
    if num == 0:
        return 2
    elif num == 1:
        return 1
    else:
        return lucas(num - 1) + lucas(num - 2)


def sum_series(num, x=0, y=1):
    if not x and not y:
        return fibonacci(num)

    elif x == 1 or x == 2 or y == 1 or y == 2:
        return lucas(num)
    else:
        return num + 1
