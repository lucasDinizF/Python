from pulp import *

# Definição dos nós
nos = ['S', 'A', 'B', 'C', 'D']
no_origem = 'S'
no_destino = 'D'

# Arestas existentes e suas capacidades
arestas = [
    ('S', 'A'), ('S', 'B'),
    ('A', 'C'),
    ('B', 'C'), ('B', 'D'),
    ('C', 'D')
]

capacidades = {
    ('S', 'A'): 10,
    ('S', 'B'): 15,
    ('A', 'C'): 10,
    ('B', 'C'): 5,
    ('B', 'D'): 10,
    ('C', 'D'): 10
}

# Variáveis de decisão (fluxo pelas arestas)
x = LpVariable.dicts("x", arestas, lowBound=0, cat='Continuous')

# Criar o modelo
model = LpProblem("Problema_Fluxo_Maximo", LpMaximize)

# Função objetivo: maximizar o fluxo que sai da fonte S
model += lpSum(x[a] for a in arestas if a[0] == no_origem)

# Restrições de conservação de fluxo (tudo que chega = tudo que sai, exceto origem e destino)
for no in nos:
    if no != no_origem and no != no_destino:
        model += (
                lpSum(x[a] for a in arestas if a[0] == no) ==
                lpSum(x[a] for a in arestas if a[1] == no)
        )

# Restrições de capacidade
for a in arestas:
    model += x[a] <= capacidades[a]

# Resolver
model.solve()

# Exibir resultado
print("Status:", LpStatus[model.status])
print("Fluxo máximo possível (litros/hora):", value(model.objective))
print("Fluxos por aresta:")
for a in arestas:
    print(f"{a[0]} → {a[1]} : {value(x[a])} l/h")
