from pulp import *

# Definição dos nós
nos = ['A', 'B', 'C', 'D', 'E']
no_origem = 'A'
no_destino = 'E'

# Grafo (arestas possíveis)
arestas = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'D'),
    ('D', 'E')
]

# Custos (distâncias)
custos = {
    ('A', 'B'): 5,
    ('A', 'C'): 10,
    ('B', 'D'): 3,
    ('B', 'E'): 9,
    ('C', 'D'): 1,
    ('D', 'E'): 2
}

# Variáveis de decisão
x = LpVariable.dicts("x", arestas, cat="Binary")

# Criar o modelo
model = LpProblem("Problema_Menor_Caminho", LpMinimize)

# Função objetivo: minimizar distância total
model += lpSum(x[a] * custos[a] for a in arestas)

# Restrições de fluxo
for no in nos:
    saida = lpSum(x[a] for a in arestas if a[0] == no)
    chegada = lpSum(x[a] for a in arestas if a[1] == no)

    if no == no_origem:
        model += saida == 1
    elif no == no_destino:
        model += chegada == 1
    else:
        model += saida - chegada == 0

# Resolver
model.solve()

# Exibir resultado
print("Status:", LpStatus[model.status])
print("Custo total mínimo (km):", value(model.objective))
print("Caminho percorrido:")

for a in arestas:
    if value(x[a]) == 1:
        print(f"{a[0]} → {a[1]}")
