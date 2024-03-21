import pprint



def read_text_file_line_by_line(file_path):
    l = []
    with open(file_path, 'r') as file:
        for line in file:
            l.append(line.strip())
    return l

def matrix_from_text_file(file_path):
    l = read_text_file_line_by_line(file_path)
    l1 = l[0].split()
    W,H,Gn,Sm,Tl = int(l1[0]),int(l1[1]),int(l1[2]),int(l1[3]),int(l1[4])
    Matrix = [[0]*W for _ in range(H)]
    golden_point = []
    silver_point = []
    tiles = []
    
    for i in range(1, Gn+1): # Golden Point position
        gx, gy = map(int, l[i].split())
        Matrix[gy][gx] = 1
        golden_point.append({'x': gx, 'y': gy})

    
    for i in range(Gn+1, Gn+Sm+1): # Silver point position
        sx, sy, ssc = map(int, l[i].split())
        Matrix[sy][sx] = (2, ssc)
        silver_point.append({'x': sx, 'y': sy, 'ssc': ssc})

    for i in range(Gn+Sm+1, Gn+Sm+Tl+1): #dict of tiles with ID, Cost, Number
        tid, tc, tn = l[i].split()
        tiles.append({'ID': tid, 'Cost': int(tc), 'Number': int(tn)})

    return Matrix,golden_point,silver_point,tiles

# print(matrix_from_text_file("00-trailer.txt"))

def little_chuncks(p1, p2, Matrix):
    x1, y1 = p1
    x2, y2 = p2

    # Determine the top-left and bottom-right corners
    top_left = min(y1, y2), min(x1, x2)
    bottom_right = max(y1, y2), max(x1, x2)

    # Slice the matrix
    sub_matrix = [row[top_left[1]:bottom_right[1]+1] for row in Matrix[top_left[0]:bottom_right[0]+1]]

    return sub_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)

Matrix, tiles = matrix_from_text_file('00-trailer.txt')
chunk1 = little_chuncks((2,4), (6,6), Matrix)

print_matrix(Matrix)
print_matrix(chunk1)

def is_valid_move(matrix, visited, x, y):
    # Check if the move is within the bounds of the matrix and the cell is not visited
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and not visited[x][y]

def dfs(matrix, visited, x, y, dest_x, dest_y, path, paths):
    # Mark the current cell as visited and add it to the current path
    visited[x][y] = True
    path.append((x, y))
    
    # If the destination is reached, add the current path to the list of paths
    if x == dest_x and y == dest_y:
        paths.append(path[:])
    else:
        # Explore all valid adjacent cells
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(matrix, visited, new_x, new_y):
                dfs(matrix, visited, new_x, new_y, dest_x, dest_y, path, paths)
    
    # Backtrack: mark the current cell as unvisited and remove it from the current path
    visited[x][y] = False
    path.pop()

def find_traversals(matrix, start, end):
    traversals = []
    rows, cols = len(matrix), len(matrix[0])
    start_x, start_y = start
    end_x, end_y = end
    
    visited = [[False] * cols for _ in range(rows)]
    path = []
    dfs(matrix, visited, start_x, start_y, end_x, end_y, path, traversals)
    return traversals

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
start_point = (0, 0)
end_point = (0, 1)

all_traversals = find_traversals(matrix, start_point, end_point)
for i, traversal in enumerate(all_traversals):
    print(f"Traversal {i + 1}: {traversal}")


