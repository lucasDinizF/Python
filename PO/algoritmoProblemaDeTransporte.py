# Importando o PuLP
from pulp import *

# Dados do Problema
cds = ['CD1', 'CD2', 'CD3']
lojas = ['LojaA', 'LojaB', 'LojaC', 'LojaD']

# Custos de transporte (em R$)
custos = {
    ('CD1', 'LojaA'): 10, ('CD1', 'LojaB'): 14, ('CD1', 'LojaC'): 18, ('CD1', 'LojaD'): 12,
    ('CD2', 'LojaA'): 12, ('CD2', 'LojaB'): 9,  ('CD2', 'LojaC'): 16, ('CD2', 'LojaD'): 11,
    ('CD3', 'LojaA'): 15, ('CD3', 'LojaB'): 13, ('CD3', 'LojaC'): 12, ('CD3', 'LojaD'): 8
}

# Capacidades dos CDs
capacidades = {'CD1': 500, 'CD2': 600, 'CD3': 350}

# Demandas das lojas
demandas = {'LojaA': 300, 'LojaB': 450, 'LojaC': 400, 'LojaD': 350}

# Criando o Modelo
model = LpProblem("Problema_de_Transporte", LpMinimize)

# Variáveis de decisão: quanto enviar de cada CD para cada loja
x = LpVariable.dicts("x", (cds, lojas), lowBound=0, cat='Integer')

# Função Objetivo: minimizar o custo total de transporte
model += lpSum(x[c][l] * custos[(c, l)] for c in cds for l in lojas)

# Restrições de capacidade dos centros de distribuição
for c in cds:
    model += lpSum(x[c][l] for l in lojas) <= capacidades[c], f"Capacidade_{c}"

# Restrições de demanda das lojas
for l in lojas:
    model += lpSum(x[c][l] for c in cds) >= demandas[l], f"Demanda_{l}"

# Resolver o problema
model.solve()

# Exibir resultados
if LpStatus[model.status] == 'Optimal':
    print("Custo total mínimo (R$):", value(model.objective))
    for c in cds:
        for l in lojas:
            print(f"De {c} para {l}: {x[c][l].varValue:.0f} unidades")
else:
    print("Nenhuma solução ótima encontrada.\n")


print("O problema não possui solução otima, aqui está o resultado do custo")

print("Custo total mínimo (R$):", value(model.objective))
for c in cds:
    for l in lojas:
        print(f"De {c} para {l}: {x[c][l].varValue:.0f} unidades")