import pandas as pd

df = pd.read_csv("employee_salary_dataset.csv")

print(df.head())

print("\nColunas:")
print(df.columns)

print("\nInformação geral:")
print(df.info())

print("\nEstatísticas:")
print(df.describe())

print(df["Monthly_Salary"].mean())

print("\nSalário máximo:")
print(df["Monthly_Salary"].max())

print("\nSalário mínimo:")
print(df["Monthly_Salary"].min())

print("\nDiferença entre salário máximo e mínimo:")
print(df["Monthly_Salary"].max() - df["Monthly_Salary"].min())

salario_max = df["Monthly_Salary"].max()
salario_min = df["Monthly_Salary"].min()
diferenca = salario_max - salario_min

print(diferenca)

df.groupby("Department")["Monthly_Salary"].mean()
print(df.groupby("Department")["Monthly_Salary"].mean())

print(df.groupby("Gender")["Monthly_Salary"].mean())

print(df.groupby("Department")["Age"].mean())