import random
die = random.SystemRandom() # a single dice
def single_test(n,a):

    exp = n-1
    while not exp & 1:
        exp >>= 1

    if pow(a,exp, n) == 1:
        return True

    while exp < n - 1:
        if pow(a, exp, n) == n-1:
            return True

        exp <<=  1
    #bitwise left shift operator: the binary number is appended with 0s at the end, which is equal to multiplying by two

    return False

def miller_rabin(n, k=40):
    for i in range(k):
        a = die.randrange(2, n-1)
        if not single_test(n,a):
            return False

    return True

def gen_prime(bits):
    while True:
        # Guarantees it's a odd
        a = (die.randrange(1 << bits -1, 1 << bits) << 1) +1 # << 1 equals to multiplying by two
        if miller_rabin(a):
            return a

gen_prime(10)