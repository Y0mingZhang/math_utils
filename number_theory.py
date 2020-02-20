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
            i, coeff in enumerate(self.coeffs)]
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

def root_of_unity(n, p):
    if n >= 1:
        poly = Polynomial([-1] + [0] * (n-1) + [1])
    else:
        poly = Polynomial([0])
    return poly_solver(poly, p)

