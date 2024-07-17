import pandas as pd
import matplotlib as plt
import seaborn as sns

df_2018 = pd.read_csv("Dataset IT Salary Survey EU 2018-2020/IT Salary Survey EU 2018.csv")
df_2019 = pd.read_csv("Dataset IT Salary Survey EU 2018-2020/IT Salary Survey EU 2019.csv")
df_2020 = pd.read_csv("Dataset IT Salary Survey EU 2018-2020/IT Salary Survey EU 2020.csv")

print(df_2018)
print(df_2019)
print(df_2020)