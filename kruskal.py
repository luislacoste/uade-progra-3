def kruskal(grafo):
    F = set()
    ListaAristas = obtenerAristas(grafo)
    ordenarAristas(ListaAristas)
    for v in grafo['vertices']:
        crearConjunto(v)
    for u, v in ListaAristas:
        if conjunto(u) != conjunto(v):
            F.add((u, v))
            unir(conjunto(u), conjunto(v))
            
    return F
