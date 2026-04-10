import matplotlib.pyplot as plt
import os

# Cria a pasta 'graficos' caso ela não exista
os.makedirs('graficos', exist_ok=True)

# Dados atualizados
processos = [1, 2, 4, 8, 12]
tempos = [37.66, 25.74, 17.96, 13.34, 11.25]
t_referencia = tempos[0]

speedup = [t_referencia / t for t in tempos]
eficiencia = [s / p for s, p in zip(speedup, processos)]

# --- GRÁFICO 1: TEMPO DE EXECUÇÃO ---
plt.figure(figsize=(8, 5))
plt.plot(processos, tempos, marker='o', color='tab:blue', linewidth=2)
plt.title('Tempo de Execução (s)')
plt.xlabel('Número de Processos')
plt.ylabel('Tempo (Segundos)')
plt.xticks(processos)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('graficos/tempo_mpi.png')
plt.close() # Fecha a figura para não sobrepor a próxima

# --- GRÁFICO 2: SPEEDUP ---
plt.figure(figsize=(8, 5))
plt.plot(processos, speedup, marker='o', color='tab:green', linewidth=2, label='Speedup Real')
plt.plot(processos, processos, linestyle='--', color='gray', label='Speedup Ideal (Linear)')
plt.title('Speedup')
plt.xlabel('Número de Processos')
plt.ylabel('Aceleração (x)')
plt.xticks(processos)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('graficos/speedup_mpi.png')
plt.close()

# --- GRÁFICO 3: EFICIÊNCIA ---
plt.figure(figsize=(8, 5))
plt.plot(processos, eficiencia, marker='o', color='tab:red', linewidth=2)
plt.title('Eficiência')
plt.xlabel('Número de Processos')
plt.ylabel('Eficiência (0.0 até 1.0)')
plt.xticks(processos)
plt.ylim(0, 1.1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('graficos/eficiencia_mpi.png')
plt.close()

print("Gráficos gerados com sucesso na pasta 'graficos'!")