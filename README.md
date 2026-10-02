# Python: Aulas e Exercícios de PCP (2025)

Registro das aulas, listas de exercícios, checkpoints e desafios da matéria de **PCP (Python)** que cursei em 2025 na FIAP, na turma **1CCPW**, com o **Prof. Alexandre Russi**.

O professor deixava o material no repositório dele para a turma acompanhar as aulas. Como esse repositório não está mais disponível, guardei aqui o que fiz ao longo do ano para não perder o registro. Foi uma matéria muito boa e um professor que fez diferença. Obrigado, professor! 🙌

## Estrutura

| Pasta | Conteúdo |
|---|---|
| [`aulas/`](aulas) | Primeiras aulas: variáveis, `input`/`print`, operadores aritméticos e relacionais. Inclui a resolução feita pelo professor de um dos desafios. |
| [`exercicios/`](exercicios) | Exercícios de fixação (tempo de viagem, área do círculo, compras, conversão de temperatura) e geradores de números aleatórios e pseudoaleatórios. |
| [`checkpoints/`](checkpoints) | Checkpoints 1 e 2: conversão de moedas, centena/dezena/unidade, idade em dias, frete de carga, tipos de triângulo, cálculo de salário e simulador de empréstimo. |
| [`orcamento-micro-reformas/`](orcamento-micro-reformas) | Calculadora de orçamento para micro-reformas (piso, pintura, revestimento, ar-condicionado, elétrica e manutenção), com as versões do módulo de ar-condicionado. |
| [`global-solution/`](global-solution) | Global Solution: CLI para registrar e buscar relatos de desastres naturais, validando a distância com a fórmula de Haversine (três versões). |
| [`challenge-sprint3/`](challenge-sprint3) | Challenge Sprint 3: análise estatística (distribuição normal) e regressão linear com pandas, SciPy e scikit-learn. |

## Como rodar

A maioria dos arquivos usa só a biblioteca padrão do Python:

```bash
python "checkpoints/pcp_checkpoint2_ex04.py"
```

O Challenge Sprint 3 precisa de algumas bibliotecas extras e da planilha `base_dados_goodwe_ficticia.xlsx` (que não está neste repositório):

```bash
pip install pandas numpy scipy matplotlib scikit-learn openpyxl
```

## Observação

O código está do jeito que foi escrito durante o curso, sem retoques, justamente para servir de registro da evolução ao longo do ano.
