station = input().split()
N, K, M = map(int, station)
def min_stations_to_travel(N, K, M):
    if K < M:
        return min(M-K-1, N-M+K-1)
    else:
        return min(K-M-1, N-K+M-1)

print(min_stations_to_travel(N, K, M))
