# unieuro-concorrente-202601-atividade5
Testar a solução MPI construindo relatório de avaliação de performance para 2, 4, 8, 12 processos.

# unieuro-concorrente-202601-atividade5
Relatório da atividade de Programação Concorrente e Distribuída 05
**Disciplina:** PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA  
**Aluno(s):** Filipe Ferreira  
**Turma:** 5º semestre de ADS matutino  
**Professor:** Rafael Marconi Ramos  
**Data:** 10/04/2026

---

# 1. Descrição do Problema
O objetivo desta atividade é avaliar o desempenho de uma solução de processamento distribuído utilizando o protocolo **MPI (Message Passing Interface)** através da biblioteca `mpi4py`. O problema consiste em processar o dataset `nlp_features_train.csv` (proveniente do desafio Quora Question Pairs do Kaggle), realizando operações de leitura e análise de dados em larga escala.

* **Algoritmo utilizado:** A versão distribuída utiliza o modelo de passagem de mensagens. O processo mestre (rank 0) coordena a distribuição dos dados ou a leitura paralela, enquanto os processos escravos realizam o processamento computacional das features do dataset. A redução final consolida os resultados de todos os nós.
* **Dataset:** Arquivo `nlp_features_train.csv` (Kaggle - Quora Question Pairs).
* **Objetivo da paralelização:** Comparar a execução serial com a execução distribuída via MPI, medindo o ganho de desempenho (Speedup) e a eficiência conforme o número de processos aumenta (2, 4, 8 e 12 processos).
* **Complexidade:** A complexidade de tempo do algoritmo é $O(n)$, onde $n$ é o número de registros no dataset.

---

# 2. Ambiente Experimental

Os experimentos foram executados no seguinte ambiente:

| Item                        | Descrição |
| --------------------------- | --------- |
| Processador                 | 12th Gen Intel(R) Core(TM) i5-12500 (3.00 GHz) |
| Número de núcleos           | 6 Núcleos Físicos / 12 Threads |
| Memória RAM                 | 16,0 GB |
| Sistema Operacional         | Windows 11 Pro |
| Linguagem utilizada         | Python 3.13.2 |
| Biblioteca MPI              | `mpi4py` e Microsoft MPI (MS-MPI v10) |
| Dataset                     | nlp_features_train.csv |

---

# 3. Metodologia de Testes

Os tempos foram medidos utilizando a função `time.perf_counter()` para garantir precisão de alta resolução.

* **Execução Serial:** `python avaliador.py`
* **Execução Distribuída:** `mpiexec -n <p> python avaliador_mpi.py` (onde $p$ é o número de processos).
* **Cálculo:** Foram realizadas 5 execuções para cada configuração. O tempo registrado descarta a primeira execução (*cold start*) e apresenta a média aritmética das execuções subsequentes.

---

# 4. Resultados Experimentais

Tempos médios de execução obtidos no processamento do dataset Quora:

| Nº Processos | Tempo de Execução (s) |
| ------------ | --------------------- |
| 1 (Serial)   | 23.15s                |
| 2            | 25.74s                |
| 4            | 17.96s                |
| 8            | 13.34s                |
| 12           | 11.25s                |

---

# 5. Cálculo de Speedup e Eficiência

As métricas de desempenho foram calculadas com base nas seguintes fórmulas:

### Speedup
$$S(p) = \frac{T(1)}{T(p)}$$

### Eficiência
$$E(p) = \frac{S(p)}{p}$$

---

# 6. Tabela de Resultados Consolidados

| Processos | Tempo (s) | Speedup ($S_p$) | Eficiência ($E_p$) |
| --------- | --------- | --------------- | ------------------ |
| 1         | 23.15s    | 1.00            | 1.00               |
| 2         | 25.74s    | 0.90            | 0.45               |
| 4         | 17.96s    | 1.29            | 0.32               |
| 8         | 13.34s    | 1.74            | 0.21               |
| 12        | 11.25s    | 2.06            | 0.17               |

---

# 7. Gráfico de Tempo de Execução
![Gráfico Tempo](graficos/tempo_mpi.png)

# 8. Gráfico de Speedup
![Gráfico Speedup](graficos/speedup_mpi.png)

# 9. Gráfico de Eficiência
![Gráfico Eficiência](graficos/eficiencia_mpi.png)

---

# 10. Análise dos Resultados

A análise dos dados revela comportamentos críticos da computação distribuída em ambiente local:

1.  **Overhead de Inicialização (Caso de 2 Processos):** A execução com 2 processos foi mais lenta (**25.74s**) que a serial (**23.15s**). Isso demonstra o custo de inicialização do ambiente MS-MPI e a latência de comunicação entre processos, que superou o ganho da divisão de carga.
2.  **Gargalo de I/O e Comunicação:** Embora o tempo total tenha caído para **11.25s** com 12 processos, o Speedup resultante foi de apenas **2.06x**. Isso indica que o processamento do dataset do Quora é fortemente limitado pela velocidade de leitura do disco e pela transferência dos dados entre os processos MPI.
3.  **Eficiência:** A eficiência caiu drasticamente para **17%** com 12 processos, sugerindo que o aumento de recursos computacionais não se traduz em ganho proporcional devido à contenção de recursos compartilhados (barramento de memória e disco).

---

# 11. Conclusão

O experimento com MPI validou que a paralelização distribuída reduz o tempo de execução, mas introduz um custo de coordenação (*overhead*) superior ao observado na biblioteca `multiprocessing` padrão em cargas menores. 

Para otimizar a performance no dataset `nlp_features_train.csv`, recomenda-se que cada processo MPI realize a leitura de fatias específicas do arquivo (offset) de forma independente, minimizando a comunicação centralizada e maximizando a vazão de dados. O uso de MPI mostra-se mais vantajoso em ambientes de cluster onde a carga computacional por nó justifica o custo da rede.

