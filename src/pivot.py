def copy(A: list):
    B = [0 for i in range(len(A))]
    for i in range(len(A)):
        if type(A[i]) == list:
            B[i] = copy(A[i])
        else:
            B[i] = A[i]
    return B

def addition(A: list, i: int, j: int, nb: float):
    for k in range(len(A)):
        A[i][k] += A[j][k] * nb

def invertion(A: list, i, j):
    A[i], A[j] = A[j], A[i]

def produit(A: list, b: list):
    x = [0 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(b)):
            x[i] += A[i][j] * b[j]
    return x

def print_matrix(A: list):
    print("[")
    for i in range(len(A)):
        print("", A[i])
    print("]")

def pivot(A: list, b: list):
    """ Résout A*x = b avec A une matrice de dimension nxn et b un vecteur de dimension n """

    Ac = copy(A)
    bc = copy(b)

    # Vérification des dimensions
    n,m = len(A), len(A[0])
    if n != m:
        raise("Matrix is not squared")
    if len(b) != n:
        raise("A and b dimensions don't match")
    x = [0 for i in range(n)]

    # Descente du pivot de Gauss
    for j in range(n):
        # Sélection de la ligne de pivot
        i = j
        a = A[i][j]
        while a == 0:
            i += 1
            if i == n:
                raise("System can't be solved")
            else:
                a = A[i][j]
        invertion(A, j, i)
        
        # Action du pivot sur les lignes en dessous
        for i in range(j+1, n):
            nb = - A[i][j] / A[j][j]
            addition(A, i, j, - A[i][j] / A[j][j])
            b[i] += nb * b[j]
        
    # Remonté du pivot de Gauss
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            b[i] += -A[i][j] * b[j]
        b[i] /= A[i][i]
    
    # Résultats
    print("A = ")
    print_matrix(Ac)
    print("b =", bc)
    print("x =", b)
    print("A*x =", produit(Ac, b))

    return b

def main():
    # A = [
    #     [1, 2],
    #     [2, 3]
    # ]
    # b = [1, 1]
    
    n = 10
    A = [[(i + j + 1)%n for j in range(n)] for i in range(n)]
    b = [1 for i in range(n)]
    x = [2/90 for i in range(n)]
    print("A*x =", produit(A, x))
    pivot(A, b)

if __name__=="__main__":
    main()