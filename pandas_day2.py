import pandas as pd

# carregar dados de um ficheiro real
df = pd.read_csv("data.csv")

print("DATA:")
print(df)

print("\nIdade média:")
print(df["idade"].mean())

print("\nMaior salário:")
print(df["salario"].max())

print("\nPessoa com maior salário:")
print(df[df["salario"] == df["salario"].max()])

print("\nSalario médio:")
print(df["salario"].mean())

print("\nIdade mínima:")
print(df["idade"].min())

print("\nOrdenar por Salário:")
print(df.sort_values("salario", ascending=False))