from ProblemMatrices import generate_random_matrix, setMatrixForTesting

class MCPIterative:

    def SolveMCPIter(matrix):

        n = matrix.shape[0]
        m = matrix.shape[1]

        cost = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(0, n):
            for j in range(0, m):
                if i == 0 and j == 0: # Start case
                    cost[i][j] = matrix[i][j]
                elif i == 0: #first row case
                    cost[i][j] = matrix[i][j] + cost[i][j-1]
                elif j == 0: #first column case
                    cost[i][j] = matrix[i][j] + cost[i-1][j]
                else:
                    cost[i][j] = matrix[i][j] + min(cost[i-1][j], cost[i][j-1])

        return cost[n-1][m-1]
    
#matrix = setMatrixForTesting()
matrix = generate_random_matrix(4,4)
print(matrix)
print(MCPIterative.SolveMCPIter(matrix))
