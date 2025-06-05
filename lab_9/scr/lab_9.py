import sys

plates =  open("ijones.in", "r")
def indiano(plates):
    with plates as f:
        data = f.read().splitlines()
    
    if not data:
        with plates as f:
            f.write("0")
        return
    
    w, h = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + h):
        grid.append(data[i].strip())
    
    n = h  
    m = w  
    
    dp_prev = [1] * n
    global_sum = [0] * 26  
    
   
    for i in range(n):
        c = grid[i][0]
        idx = ord(c) - ord('a')
        global_sum[idx] += 1
    
    
    
    if m > 1:
        for j in range(1, m):
            dp_curr = [0] * n
            for i in range(n):
                c = grid[i][j]
                c_idx = ord(c) - ord('a')
               
                dp_curr[i] = dp_prev[i]
                
                if grid[i][j-1] == c:
                    dp_curr[i] += global_sum[c_idx] - dp_prev[i]
                else:
                    dp_curr[i] += global_sum[c_idx]
            
            
            for i in range(n):
                c = grid[i][j]
                c_idx = ord(c) - ord('a')
                global_sum[c_idx] += dp_curr[i]
            
            dp_prev = dp_curr
    
   
    if n == 1:
        result = dp_prev[0]
    else:
        result = dp_prev[0] + dp_prev[n-1]
    
    with open("ijones.out", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    indiano(plates)