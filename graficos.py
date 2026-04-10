import matplotlib.pyplot as plt

# Dados atualizados
processos = [1, 2, 4, 8, 12]
tempos = [37.66, 25.74, 17.96, 13.34, 11.25]
t_referencia = tempos[0]

speedup = [t_referencia / t for t in tempos]
eficiencia = [s / p for s, p in zip(speedup, processos)]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

# Gráfico de Tempo
ax1.plot(processos, tempos, marker='o', color='tab:blue', linewidth=2)
ax1.set_title('Tempo de Execução (s)')
ax1.set_xlabel('Nº Processos')
ax1.grid(True, ls='--')

# Gráfico de Speedup
ax2.plot(processos, speedup, marker='o', color='tab:green', linewidth=2, label='Real')
ax2.plot(processos, processos, ls='--', color='gray', label='Ideal')
ax2.set_title('Speedup')
ax2.set_xlabel('Nº Processos')
ax2.legend()
ax2.grid(True, ls='--')

# Gráfico de Eficiência
ax3.plot(processos, eficiencia, marker='o', color='tab:red', linewidth=2)
ax3.set_title('Eficiência (0.0 - 1.0)')
ax3.set_xlabel('Nº Processos')
ax3.set_ylim(0, 1.1)
ax3.grid(True, ls='--')

plt.tight_layout()
plt.show()