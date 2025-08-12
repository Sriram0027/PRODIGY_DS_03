import pandas as pd
import matplotlib.pyplot as plt
file_path = r"C:\MINI PROJECT\PRODIGY\TASK3\test3.csv"
try:
    df = pd.read_csv(file_path, sep=None, engine='python', on_bad_lines='skip')
except Exception as e:
    print(f"Error reading CSV: {e}")
    exit()
print("First 5 rows of the dataset:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())
if '2020' not in df.columns:
    print("\nColumn '2020' not found in dataset. Available columns are:")
    print(df.columns.tolist())
    exit()
df = df.dropna(subset=['2020'])
df['2020'] = pd.to_numeric(df['2020'], errors='coerce')
df_sorted = df.sort_values(by='2020', ascending=False)
top_10 = df_sorted.head(10)
plt.figure(figsize=(10, 6))
plt.bar(top_10['Country Name'], top_10['2020'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Country')
plt.ylabel('Value in 2020')
plt.title('Top 10 Countries by 2020 Value')
plt.tight_layout()
plt.show()
