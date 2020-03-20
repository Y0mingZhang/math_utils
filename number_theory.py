class Polynomial:
    def __init__(self, coeffs):
        if not coeffs:
            coeffs = [0]
        self.coeffs = coeffs
    def derivative(self):
        deriv_coeffs = [i * self.coeffs[i] for i in range(1, len(self.coeffs), 1)]
        return Polynomial(deriv_coeffs)
    def eval(self, val):
        res = 0
        for power, coeff in enumerate(self.coeffs):
            res += coeff * (val**power)
        return res
    def __repr__(self):
        str_repr = ["{}x^{}".format(coeff, i) if i != 0 else "{}".format(coeff) for \
            i, coeff in enumerate(self.coeffs) if coeff != 0]
        return " + ".join(str_repr)

def poly_solver(poly, modulus):
    res = []
    for x in range(modulus):
        if poly.eval(x) % modulus == 0:
            res.append(x)
    return res

def inv(x, modulus):
    for i in range(1, modulus):
        if x*i % modulus == 1:
            return i


def prime_factorization(x):
    base = 2
    primes = []
    while x != 1:
        if x % base == 0:
            x //= base
            primes.append(base)
        else:
            base += 1
    return primes

def sieve_of_eratosthenes(n):
    sieve = [True for _ in range(n+1)]
    i = 2
    while i < len(sieve):
        if sieve[i]:
            for j in range(i*2, len(sieve), i):
                sieve[j] = False
        i += 1
    
    return [i for i in range(2, len(sieve)) if sieve[i]]


def primes(n):
    return sieve_of_eratosthenes(n)

def order(n, modulus):
    return min([i for i in range(1, modulus) if (n ** i) % modulus == 1])

def print_orders(modulus):
    print('n\tord(n)')
    for i in range(1, modulus):
        print('{}\t{}'.format(i, order(i, modulus)))

def print_prim_root_powers(prim_root, modulus):
    print("i\t{}^i".format(prim_root))
    for i in range(1, modulus):
        print('{}\t{}'.format(i, prim_root**i % modulus))
    

def primitive_roots(modulus):
    return [i for i in range(1, modulus) if order(i, modulus) == modulus-1]
