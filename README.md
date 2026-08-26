# 🧠 Raciocínio Algorítmico — PUCPR

Resoluções dos exercícios da disciplina de Raciocínio Algorítmico, do curso de
Tecnologia em Jogos Digitais da PUCPR. Cada arquivo contém o enunciado do
exercício comentado logo acima da solução.

## 📖 Sobre o Projeto

Este repositório documenta minha evolução em lógica de programação com Python,
partindo dos conceitos fundamentais (variáveis, condicionais, laços) até a
aplicação de boas práticas como funções puras, separação de responsabilidades
e type hints. A disciplina é composta por 18 listas de exercícios ao longo do
semestre, então este repositório cresce progressivamente conforme novas listas
são resolvidas.

## 📋 Listas de Exercícios

| # | Lista | Status | Principais conceitos |
| - | ----- | ------ | --------------------- |
| 01 | Problemas Sequenciais I | ✅ | `input()`, conversão de tipos, operadores aritméticos, formatação `.2f` |
| 02 | Problemas Sequenciais II | ✅ | Funções puras, type hints, docstrings, `round`/`ceil` |
| 03 | — | ⬜ | — |
| ... | — | ⬜ | — |
| 18 | — | ⬜ | — |

## 🧩 Padrão de Código

A partir da Lista 02, adotei um padrão consistente: funções puras que apenas
calculam e retornam valores, com um bloco separado responsável por ler o
`input()` e exibir o `print()`. Isso separa a lógica de negócio da entrada e
saída, facilitando testes e reaproveitamento.

## 📚 O Que Aprendi

- Diferença entre `/` (divisão real) e `//` (divisão inteira), e como isso
  evita bugs sutis em cálculos de conversão (tempo, moedas, etc.)
- `input()` sempre retorna string — conversão explícita (`int()`, `float()`)
  é obrigatória antes de qualquer operação numérica
- Separar cálculo (função pura) de exibição (`print()`) deixa o código mais
  fácil de revisar e depurar
- Identificar e corrigir o padrão de bug mais comum nos meus próprios
  exercícios: usar a variável errada em operações de módulo/resto em cascata

## 🛠️ Tecnologias

- Python 3

## 👤 Autor

Gabriel Apolinário — [LinkedIn](https://linkedin.com/in/gabapolinario) · [itch.io](https://gabriel-apolinario.itch.io)
