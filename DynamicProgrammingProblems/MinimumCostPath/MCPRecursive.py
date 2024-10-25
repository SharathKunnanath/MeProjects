from ProblemMatrices import generate_random_matrix, setMatrixForTesting

class MCPRecursive:
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.dict = {}
        self.n = matrix.shape[0] - 1
        self.m = matrix.shape[1] - 1

    def getMinCostPath(self, n, m):
        
        #recurrence relation is f([n][m]) = [n][m] + MIN(f[n-1][m], f[n][m-1])
        
        if n < 0 or m < 0:
            return float('inf')
        elif n == 0 and m == 0:
            return self.matrix[n][m]
        elif (n, m) in self.dict:
            return self.dict[(n, m)]
        else:
            left = self.getMinCostPath(n-1, m)
            down = self.getMinCostPath(n, m-1)
            self.dict[(n,m)] = self.matrix[n][m] + min(left, down)
            return self.dict[(n,m)]
        
matrix = setMatrixForTesting()
#matrix = generate_random_matrix(4, 4)
print(matrix)
x = MCPRecursive(matrix)
print(x.getMinCostPath(x.n, x.m))