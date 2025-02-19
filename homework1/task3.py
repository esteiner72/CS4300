def task3_1(n):
    if n % 2 == 0:
        return "n is even"
    elif n % 2 == 1:
        return "n is odd"
    else:
        return "n is 0"

def task3_2():
    # Since we only want the first 10 prime numbers, and not n prime numbers, we can hard-code!
    return {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

def task3_3():
    sum = 0
    n = 1
    while (n <= 100):
        sum = sum + n
        n = n + 1
    return sum