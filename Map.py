
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
    Matrix = [[0]*H for _ in range(W)]
    
    for i in range(1, Gn+1): # Golden Point position
        gx, gy = map(int, l[i].split())
        Matrix[gx][gy] = 1
    
    for i in range(Gn+1, Gn+Sm+1): # Silver point position
        sx, sy, ssc = map(int, l[i].split())
        Matrix[sx][sy] = (2, ssc)

    tiles = []
    for i in range(Gn+Sm+1, Gn+Sm+Tl+1): #dict of tiles with ID, Cost, Number
        tid, tc, tn = l[i].split()
        tiles.append({'ID': tid, 'Cost': int(tc), 'Number': int(tn)})

    return Matrix,tiles



print(matrix_from_text_file("01-comedy.txt"))