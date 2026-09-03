<div align="center">

# 🔍 DIO Fraud Scan

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)]()
[![Machine Learning](https://img.shields.io/badge/ML-Isolation%20Forest-orange)]()

*Um script analítico para detecção de anomalias e fraudes em transações financeiras utilizando Machine Learning.*

</div>

## 📝 Projeto
Este repositório contém uma implementação prática de **Detecção de Fraudes com Aprendizado de Máquina**. O objetivo é extrair dados de transações financeiras, pré-processar as variáveis numéricas e aplicar o algoritmo *Isolation Forest* para identificar comportamentos anômalos e transações suspeitas de forma automatizada.

## 🛠 Funcionalidades
- **Extract & Load:** Carregamento remoto de um conjunto de dados de transações estruturado via URL.
- **Transform & Preprocess:** Seleção automatizada de colunas numéricas e tratamento de valores ausentes.
- **Machine Learning (Isolation Forest):** Treinamento de modelo não supervisionado para detecção de anomalias com base em contaminação estimada.
- **Análise de Resultados:** Classificação e exibição de transações categorizadas como "Anomaly" ou "Normal".

## 🚀 Como executar
1. Clone o repositório.
2. Certifique-se de ter o Python e as bibliotecas necessárias instaladas (`pandas`, `numpy`, `scikit-learn`, `seaborn`, `matplotlib`).
3. Execute o script principal:
   ```bash
   python main.py
   ```
