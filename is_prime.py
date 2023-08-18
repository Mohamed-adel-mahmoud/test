def is_prime(num):
    if num < 2:
        print(False)
    for x in range(2, num):
        if num % x == 0:
            return False
        else:
            return True


list_of_numbers = [2, 3, 4, 5, 6, 7, 8, 9]

print(list(map(is_prime, list_of_numbers)))
