import pandas as pd
dataset_path = ('gpa.csv')
df = pd.read_csv(dataset_path)

df['Number'] = df['Number'].astype(int)

print(df)