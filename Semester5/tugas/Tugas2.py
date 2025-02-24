import heapq

def dijkstra(graph, start):
    # Inisialisasi jarak ke semua node sebagai tak hingga, kecuali titik awal
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (jarak, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati node jika jaraknya sudah optimal
        if current_distance > distances[current_node]:
            continue

        # Periksa tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak lebih pendek, perbarui
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Contoh penggunaan
graph = {
    'kost': {'Rumah': 13.10, 'kampus': 4.40},  # Jarak dalam kilometer
    'fakultas': {'kost': 0.0, 'kampus': 2.20, 'fakultas': 4.50},
    'kampus': {'kost': 4.4, 'fakultas': 2.20, 'Rumah': 13.10},
    'Rumah': {'Rumah': 4.50, 'kampus': 13.10}
}

start_node = 'kost'
result = dijkstra(graph, start_node)

# Menampilkan hasil dalam format kilometer
print(f"Jarak terpendek dari {start_node}:")
for node, distance in result.items():
    print(f"- Ke {node}: {distance:.2f} km")