import ortools.linear_solver.pywraplp as otlp

# Criar solver para problema de Inteira Mista
solver = otlp.Solver('Marcenaria', otlp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# Variáveis de decisão: quantidade de mesas e cadeiras (inteiras)
mesa = solver.IntVar(0, solver.infinity(), 'Mesa')
cadeira = solver.IntVar(0, solver.infinity(), 'Cadeira')

# Restrição de madeira (m²)
solver.Add(2 * mesa + 3 * cadeira <= 14)

# Restrição de mão de obra (horas)
solver.Add(2 * mesa + 1 * cadeira <= 10)

# Função objetivo: maximizar o lucro
solver.Maximize(40 * mesa + 10 * cadeira)

# Resolver o problema
result_status = solver.Solve()

# Exibir resultados
if result_status == otlp.Solver.OPTIMAL:
    print('Resultado Ótimo Encontrado:')
    print(f'Mesas: {mesa.solution_value():.0f}')
    print(f'Cadeiras: {cadeira.solution_value():.0f}')
    print(f'Lucro Total (R$): {solver.Objective().Value():.2f}')
else:
    print('Solução não encontrada.')
