def dijkstra(G, origen):
    dist = []
    prev = []
    Q = inicializarColaPrioridad(G, origen)
    for v in vertices(G):
        dist[v] = float('inf')
        prev[v] = None
        Q.insertar(v, dist[v])
        
    dist[origen] = 0
    Q.agregar(origen, dist[origen])
    while not Q.vacia():
        u = extraerMinimo(Q)
        Q.eliminar(u)
        for v in adyacentes(u):
            alt = dist[u] + peso(u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                Q.editar(v, dist[v])
                
    return dist, prev