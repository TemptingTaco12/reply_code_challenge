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
    
    for i in range(1, Gn+1): # Golden Point position
        gx, gy = map(int, l[i].split())
        Matrix[gy][gx] = 1
    
    for i in range(Gn+1, Gn+Sm+1): # Silver point position
        sx, sy, ssc = map(int, l[i].split())
        Matrix[sy][sx] = (2, ssc)

    tiles = []
    for i in range(Gn+Sm+1, Gn+Sm+Tl+1): #dict of tiles with ID, Cost, Number
        tid, tc, tn = l[i].split()
        tiles.append({'ID': tid, 'Cost': int(tc), 'Number': int(tn)})

    return Matrix,tiles


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