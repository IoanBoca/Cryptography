import time


def gcd_euclid(a, b):
    """
    Euclid's algorithm finds the largest number that divides both numbers
    without a remainder, by calling the method recursively with the
    the first number mod the second number and the first number again,
    as the paramenters.
    :param a: first number
    :param b: second number
    :return: the greatest common divisor
    """
    if a == 0:
        return b
    return gcd_euclid(b % a, a)


def gcd_bruteforce(a, b):
    """
    The bruteforce method goes with an index from the smallest of the two numbers
    decrementing it until we find a number that divides both the first and the second
    number with no remainder.
    :param a: first number
    :param b: second number
    :return: the greatest common divisor
    """
    if a == 0 and b == 0:
        return None
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        aux = a
        a = b
        b = aux
    i = a
    while a % i != 0 or b % i != 0:
        i -= 1
    return i


def gcd_dijkstra(a, b):
    """
    Dijkstra's algorithm also known as the method of repeated subtractions
    calls the algorithm recursively using as parameters the subtraction
    of the smaller number from the larger number and then the smaller number
    until the two numbers are equal.
    :param a: first number
    :param b: second number
    :return: the greatest common divisor
    """
    if a == 0 and b == 0:
        return None
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd_dijkstra(a-b, b)
    else:
        return gcd_dijkstra(a, b-a)


start_time = time.time()
print(gcd_euclid(25734, 34312))
print(gcd_euclid(25734, 34312))
print(gcd_euclid(25734, 34312))
print(gcd_euclid(25734, 34312))
print(gcd_euclid(25734, 34312))
print(gcd_euclid(25734, 34312))
print(gcd_euclid(25734, 34312))
print(gcd_euclid(25734, 34312))
print(gcd_euclid(25734, 34312))
print(gcd_euclid(25734, 34312))
time.sleep(1)
end_time = time.time()
print("gcd euclid duration: ", end_time-start_time-1)

start_time = time.time()
print(gcd_bruteforce(25734, 34312))
print(gcd_bruteforce(25734, 34312))
print(gcd_bruteforce(25734, 34312))
print(gcd_bruteforce(25734, 34312))
print(gcd_bruteforce(25734, 34312))
print(gcd_bruteforce(25734, 34312))
print(gcd_bruteforce(25734, 34312))
print(gcd_bruteforce(25734, 34312))
print(gcd_bruteforce(25734, 34312))
print(gcd_bruteforce(25734, 34312))
time.sleep(1)
end_time = time.time()
print("gcd brute force duration: ", end_time-start_time-1)

start_time = time.time()
print(gcd_dijkstra(25734, 34312))
print(gcd_dijkstra(25734, 34312))
print(gcd_dijkstra(25734, 34312))
print(gcd_dijkstra(25734, 34312))
print(gcd_dijkstra(25734, 34312))
print(gcd_dijkstra(25734, 34312))
print(gcd_dijkstra(25734, 34312))
print(gcd_dijkstra(25734, 34312))
print(gcd_dijkstra(25734, 34312))
print(gcd_dijkstra(25734, 34312))
time.sleep(1)
end_time = time.time()
print("gcd dijkstra duration: ", end_time-start_time-1)