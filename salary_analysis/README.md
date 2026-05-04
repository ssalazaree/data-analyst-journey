# 📊 Salary Analysis

## 🎯 Objective
The goal of this project is to analyze what factors influence employee salaries using a dataset.

---

## 📁 Dataset
The dataset includes:
- Department
- Experience Years
- Education Level
- Age
- Gender
- Monthly Salary

---

## ❓ Questions
- Which department pays the highest salaries?
- Does experience influence salary?
- Does education level impact salary?

---

## 🔍 Analysis

### 1. Salary by Department

Code used:
df.groupby("Department")["Monthly_Salary"].mean()

Insight:
Marketing has the highest average salary (~96k), while Finance has the lowest (~67k), showing a clear difference between departments.

---

### 2. Experience vs Salary

Code used:
df.groupby("Experience_Years")["Monthly_Salary"].mean()

Insight:
There is no consistent relationship between experience and salary. While salaries sometimes increase with experience, there are strong fluctuations.

---

### 3. Education vs Salary

Code used:
df.groupby("Education_Level")["Monthly_Salary"].mean()

Insight:
Education level does not strongly predict salary. Master's degree holders have the highest average, but PhD salaries are not the highest.

---

## 🧠 Key Insights

- Department is the strongest factor influencing salary
- Experience has an inconsistent effect
- Education alone is not a reliable predictor

---

## ⚠️ Limitations

- Small dataset (~50 entries)
- No job role or seniority data
- Possible imbalance between groups