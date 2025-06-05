from collections import deque

def read_input(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        
        start = tuple(map(int, lines[0].replace(' ', '').split(',')))
        end = tuple(map(int, lines[1].replace(' ', '').split(',')))
        
        
        rows, cols = map(int, lines[2].replace(' ', '').split(','))
        
        
        matrix = []
        for line in lines[3:]:
            
            cleaned_line = line.strip('[]').replace(',', ' ').split()
            row = list(map(int, cleaned_line))
            matrix.append(row)
            
            
            if len(row) != cols:
                raise ValueError(f"Рядок матриці має {len(row)} стовпців, очікувалось {cols}")

        
        if len(matrix) != rows:
            raise ValueError(f"Матриця має {len(matrix)} рядків, очікувалось {rows}")

        return start, end, rows, cols, matrix

    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        raise

way = []
def shortest_path(matrix, start, end, rows, cols):
    
    if (start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols or
        end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols):
        return -1

    
    if matrix[start[0]][start[1]] == 0 or matrix[end[0]][end[1]] == 0:
        return -1

    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True

    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, dist = queue.popleft()
        
        
        if (x, y) == end:
            return dist

        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            
            if (0 <= nx < rows and 0 <= ny < cols and 
                not visited[nx][ny] and matrix[nx][ny] == 1):
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
                way.append((nx, ny))


    
    return -1

def write_output(file_path, result):
    with open(file_path, 'w') as f:
        f.write(str(result) if result is not None else "-1")
        f.write(str(way))


if __name__ == "__main__":
    
    input_path = r'C:\Users\Somk0\Desktop\projectsXD\lab_5\input.txt'
    output_path = r'C:\Users\Somk0\Desktop\projectsXD\lab_5\output.txt'
        
    start, end, rows, cols, matrix = read_input(input_path)
        
        
    result = shortest_path(matrix, start, end, rows, cols)
        
        
    write_output(output_path, result)
    