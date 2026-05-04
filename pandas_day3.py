import pandas as pd

df = pd.read_csv("employee_salary_dataset.csv")

#print(df.head())

#print("\nColunas:")
#print(df.columns)

#print("\nInformação geral:")
#print(df.info())

#print("\nEstatísticas:")
#print(df.describe())

#print(df["Monthly_Salary"].mean())

##print("\nSalário máximo:")
#print(df["Monthly_Salary"].max())

#print("\nSalário mínimo:")
#print(df["Monthly_Salary"].min())

#print("\nDiferença entre salário máximo e mínimo:")
#print(df["Monthly_Salary"].max() - df["Monthly_Salary"].min())

#salario_max = df["Monthly_Salary"].max()
#salario_min = df["Monthly_Salary"].min()
#diferenca = salario_max - salario_min

#print(diferenca)

print(df.groupby("Department")["Monthly_Salary"].mean())

print(df.groupby("Gender")["Monthly_Salary"].mean())

print(df.groupby("Department")["Age"].mean())


print(df.groupby("Department")["Monthly_Salary"].mean())

salario_max = df["Monthly_Salary"].max()
salario_min = df["Monthly_Salary"].min()
diferenca = salario_max - salario_min
print(diferenca)

print(df.groupby("Department")["Gender"].value_counts())

print(df.groupby("Department")["Education_Level"].value_counts())

#“O departamento de Marketing apresenta salários médios mais elevados (~96k) comparado com Finance (~67k). 
#Esta diferença pode estar associada a maior experiência média e, possivelmente, a níveis de educação mais elevados,
#embora não seja possível estabelecer uma relação causal direta com os dados disponíveis.”

print(df.groupby("Experience_Years")["Monthly_Salary"].mean())

#“O número de anos de experiência não está diretamente ligado a salários médios mais altos de forma linear,
#uma vez que existem flutuações significativas ao longo dos anos. Embora se observe um aumento inicial até 
#cerca dos 8–9 anos de experiência, os salários diminuem posteriormente em vários pontos, indicando que outros 
#fatores além da experiência influenciam o salário.”

#Versão ainda melhor:

#“Apesar de existir um aumento inicial nos salários com mais anos de experiência, a relação não é consistente 
#ao longo do dataset. As flutuações observadas podem dever-se ao baixo número de observações em alguns níveis 
#de experiência e à influência de outros fatores como departamento ou função.”

print(df.groupby("Experience_Years").size())

print(df.groupby(["Department", "Experience_Years"])["Monthly_Salary"].mean())

df_filtered = df[df["Department"].isin(["Marketing", "Finance"])]

print(df_filtered.groupby(["Department", "Experience_Years"])["Monthly_Salary"].mean())

print(df_filtered.groupby("Department")["Experience_Years"].mean())
print(df_filtered.groupby("Department")["Monthly_Salary"].mean())

print(df.groupby("Education_Level")["Monthly_Salary"].mean())

print(df.groupby("Education_Level").size())