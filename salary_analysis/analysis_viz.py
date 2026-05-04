import pandas as pd
import matplotlib.pyplot as plt

# carregar dados
import os

path = os.path.join(os.path.dirname(__file__), "employee_salary_dataset.csv")
df = pd.read_csv(path)

# 1. salário por departamento
dept_salary = df.groupby("Department")["Monthly_Salary"].mean()

dept_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.tight_layout()
import os

base_path = os.path.dirname(__file__)

plt.savefig(os.path.join(base_path, "salary_by_department.png"))
plt.show()

# 2. salário por educação
edu_salary = df.groupby("Education_Level")["Monthly_Salary"].mean()

edu_salary.plot(kind="bar")
plt.title("Average Salary by Education Level")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(base_path, "salary_by_education.png"))
plt.show()