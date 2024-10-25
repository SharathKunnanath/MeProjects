import numpy as np

def generate_random_matrix(rows, cols):
    return np.random.randint(1, 51, size=(rows, cols))

def setMatrixForTesting():
    matrix = np.array([[3, 2, 12, 15, 10], 
                       [6, 19, 7, 11, 17], 
                       [8, 5, 12, 32, 21],
                       [3, 20, 2, 9, 7]])
    return matrix

# Example usage
if __name__ == "__main__":
    rows, cols = 4, 4  # You can change the dimensions as needed
    random_matrix = generate_random_matrix(rows, cols)
    print(random_matrix)