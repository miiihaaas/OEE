#Random Odd and Even Numbers

from random import randint
###################
### sequencing  ###
###################
def random_odd_sequencing(a, b):
    min_odd = a // 2
    max_odd = b // 2 - 1
    rndm_odd = randint(min_odd, max_odd) * 2 +1
    return rndm_odd


def random_even_sequencing(a, b):
    min_even = a // 2
    max_even = b // 2 - 1
    rndm_even = randint(min_even, max_even) * 2
    return rndm_even

##############################
### iteration - while loop ###
##############################

def random_odd_iteration(a, b):
    number = randint(a, b)
    while number % 2 == 0:
        number = randint(a, b)
    return number

def random_even_iteration(a, b):
    number = randint(a, b)
    while number % 2 == 1:
        number = randint(a, b)
    return number


###########################
### selection - if blok ###
###########################

def random_odd_selection(a, b):
    number = randint(a, b)
    if number % 2 == 0:
        number += 1
    return number

def random_even_selection(a, b):
    number = randint(a, b)
    if number % 2 == 1:
        number += 1
    return number


###################################

def random_prime_number(a, b):
    number = randint(a,b)
    count = 3

    while count > 2:
        count = 0
        number = randint(a,b)
        for i in range(number):
            if number % (i+1) == 0:
                count += 1
    return number


prime_number = random_prime_number(1, 100)
odd_number = random_odd_selection(1, 100)
even_number = random_even_selection(0,100)
# odd_number = random_odd(0,100)
# even_number = random_even(0,100)
print(f"nasumični neparan broj: {odd_number}")
print(f"nasumični paran broj: {even_number}")
print(f"nasumični prime broj: {prime_number}")
