import ortools.linear_solver.pywraplp as otlp

# Criar o solver
solver = otlp.Solver('MisturaRacao', otlp.Solver.GLOP_LINEAR_PROGRAMMING)

# Variáveis de decisão: quantidade (em kg) de cada ingrediente na mistura
milho = solver.NumVar(0, solver.infinity(), 'Milho')
soja = solver.NumVar(0, solver.infinity(), 'Soja')
farinha = solver.NumVar(0, solver.infinity(), 'Farinha_de_Carne')

# Restrição: proteína (mínimo 220g)
solver.Add(80 * milho + 250 * soja + 300 * farinha >= 220)

# Restrição: gordura (mínimo 60g)
solver.Add(35 * milho + 30 * soja + 150 * farinha >= 60)

# Restrição: fibras (mínimo 50g)
solver.Add(70 * milho + 48 * soja + 40 * farinha >= 50)

# Restrição: total de ingredientes = 1kg
solver.Add(milho + soja + farinha == 1)

# Função objetivo: minimizar o custo (R$/kg)
solver.Minimize(2.00 * milho + 3.50 * soja + 4.20 * farinha)

# Resolver o problema
result_status = solver.Solve()

# Exibir os resultados
if result_status == otlp.Solver.OPTIMAL:
  print('Resultado Ótimo Encontrado:')
  print(f'Milho: {milho.solution_value():.4f} kg')
  print(f'Soja: {soja.solution_value():.4f} kg')
  print(f'Farinha de Carne: {farinha.solution_value():.4f} kg')
  print(f'Custo Total (R$): {solver.Objective().Value():.2f}')
else:
  print('Solução não encontrada.')
