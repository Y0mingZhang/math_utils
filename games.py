from itertools import permutations, product
from math import isclose
import fileinput

def the_24_game(a,b,c,d):
    ops = list(product((mult, div, add, sub), repeat=3))
    for n0, n1, n2, n3 in set(permutations((a,b,c,d))):
        for op0, op1, op2 in ops:
            res = op0(n0, n1)
            res = op1(res, n2)
            res = op2(res, n3)
            if isclose(res, 24, abs_tol=1e-2): 
                print('Solution exists.')
                print('((({} {} {}) {} {}) {} {})'.format(n0, op_print(op0), n1, op_print(op1), n2, op_print(op2), n3))
                return True
            
            res_L = op0(n0, n1)
            res_R = op2(n2, n3)
            res = op1(res_L, res_R)
            if isclose(res, 24, abs_tol=1e-2):
                print('Solution exists.')
                print('({} {} {}) {} ({} {} {})'.format(n0, op_print(op0), n1, op_print(op1), n2, op_print(op2), n3))
                return True
            
            res = op2(n2, n3)
            res = op1(n1, res)
            res = op0(n0, res)
            if isclose(res, 24, abs_tol=1e-2):
                print('Solution exists.')
                print('({} {} ({} {} ({} {} {})))'.format(n0, op_print(op0), n1, op_print(op1), n2, op_print(op2), n3))
                return True
    print('Solution does not exist.')
    return False

def play_24():
    while 1:
        print('Provide 4 numbers, seperated by a space.')
        for line in fileinput.input():
            try:
                nums = [int(n) for n in line.split()]
                the_24_game(*nums)
            except:
                continue
        


def mult(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return float('inf')
    else:
        return a/b

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def op_print(f):
    if f == mult:
        return '*'
    if f == div:
        return '/'
    if f == add:
        return '+'
    if f == sub:
        return '-'
