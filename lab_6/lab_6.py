import heapq

def main():
    try:
        with open('input.txt', 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        
        if len(lines) < 2:
            raise ValueError("Файл має містити принаймні два рядки (N M і клієнти).")
        
        
        try:
            N, M = map(int, lines[0].split())
        except:
            raise ValueError("Перший рядок має містити два числа: N і M.")
        
        
        try:
            clients = list(map(int, lines[1].split()))
            clients = set(clients)
        except:
            raise ValueError("Другий рядок має містити номери клієнтів.")
        
        if len(lines) < 2 + M:
            raise ValueError(f"Очікувалось {M} рядків зі з'єднаннями, але отримано {len(lines) - 2}.")
        
        
        graph = [[] for _ in range(N + 1)]
        for line in lines[2:2+M]:
            try:
                u, v, lat = map(int, line.split())
                if u < 1 or u > N or v < 1 or v > N:
                    raise ValueError(f"Номер вузла повинен бути від 1 до {N}.")
                graph[u].append((v, lat))
                graph[v].append((u, lat))
            except:
                raise ValueError(f"Невірний формат рядка зі з'єднанням: '{line}'")
        
        min_max_latency = float('inf')
        
        for server in range(1, N + 1):
            if server in clients:
                continue
            
            
            dist = [float('inf')] * (N + 1)
            dist[server] = 0
            heap = []
            heapq.heappush(heap, (0, server))
            
            while heap:
                current_dist, u = heapq.heappop(heap)
                if current_dist > dist[u]:
                    continue
                for v, lat in graph[u]:
                    if dist[v] > dist[u] + lat:
                        dist[v] = dist[u] + lat
                        heapq.heappush(heap, (dist[v], v))
            
            
            max_lat = 0
            for client in clients:
                if dist[client] == float('inf'):
                    max_lat = float('inf')
                    break
                max_lat = max(max_lat, dist[client])
            
            if max_lat < min_max_latency:
                min_max_latency = max_lat
        
        if min_max_latency == float('inf'):
            raise ValueError("Немає сервера, який би досягав усіх клієнтів.")
        
        with open('output.txt', 'w') as f:
            f.write(str(min_max_latency))
    
    except Exception as e:
        with open('output.txt', 'w') as f:
            f.write(f"Помилка: {str(e)}")

if __name__ == "__main__":
    main()