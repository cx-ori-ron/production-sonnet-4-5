import pandas as pd

df = pd.DataFrame()

expr = input("Enter your query expression: ")
result = df.query(expr, engine='python')
