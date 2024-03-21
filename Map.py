def read_text_file_line_by_line(file_path):
    l = []
    with open(file_path, 'r') as file:
        for line in file:
            l.append(line.strip())
    return l

