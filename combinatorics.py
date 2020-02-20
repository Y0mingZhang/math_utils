
def CatalanNumber(n):
    memo = []
    memo.append(1)
    for i in range(1,n+1):
        res = 0
        for j in range(0, i):
            res += memo[j]*memo[i-j-1]
        memo.append(res)
    return memo[n]

def lattice_path_with_diagonal_step(n):
    """ Also known as the Schroder number """
    memo = [[0 for _ in range(n+1)] for _ in range(n+1)]
    memo[0][0] = 1
    def lattice_path_with_diagonal_step_aux(x, y):
        if x < 0 or y < 0 or y > x:
            return 0
        if memo[x][y] == 0:
            memo[x][y] = lattice_path_with_diagonal_step_aux(x-1,y-1) +\
                        lattice_path_with_diagonal_step_aux(x-1,y) +\
                        lattice_path_with_diagonal_step_aux(x, y-1)
        return memo[x][y]
    return lattice_path_with_diagonal_step_aux(n,n)

