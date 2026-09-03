# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Definição da URL do conjunto de dados
url = "https://raw.githubusercontent.com/microsoft/DataStoriesSamples/master/samples/FraudDetectionOnADL/Data/transactions.csv"

# Carregamento do conjunto de dados
print("Carregando dados de transações...")
df = pd.read_csv(url)

# Exibição das primeiras linhas do DataFrame
print("Colunas do DataFrame:", df.columns.tolist())
display(df.head())

# Seleção das colunas relevantes para análise
features = ["amount", "accountID", "device", "merchant", "transactionType", "isFraud"]

# Filtragem do DataFrame para manter apenas as colunas relevantes
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"Colunas numéricas: {numeric_cols}")

# Preenchendo valores ausentes com 0
X = df[numeric_cols].fillna(0)

# Treinamento do modelo Isolation Forest para detecção de anomalias
print("Treinando o modelo Isolation Forest para detecção de anomalias...")
model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
df['anomaly'] = model.fit_predict(X)

# Classificação das transações como "Anomaly" ou "Normal" com base na previsão do modelo
df["is_anomaly"] = df["anomaly"].apply(lambda x: "Anomaly" if x == -1 else "Normal")

# Exibição do número de anomalias detectadas e das primeiras amostras
anomalias = df[df["is_anomaly"] == "Anomaly"]
print(f"Número de anomalias detectadas: {len(anomalias)}")
print(f"Exibindo as primeiras anomalias detectadas:")

# Exibição das primeiras amostras de anomalias detectadas
print("Amostras de anomalias detectadas:")
display(anomalias.head())