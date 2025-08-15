import pandas as pd
import matplotlib.pyplot as plt
file_path = r"C:\MINI PROJECT\PRODIGY\TASK3\test3.csv"
df = pd.read_csv(file_path, sep=None, engine='python', on_bad_lines='skip')
print("First 5 rows of the dataset:")
print(df.head(), "\n")
print("Column names:", df.columns.tolist())
if 'job' in df.columns and 'duration' in df.columns:
    job_duration = df.groupby('job')['duration'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    job_duration.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Job')
    plt.ylabel('Average Duration')
    plt.title('Top 10 Jobs by Average Call Duration')
    plt.tight_layout()
    plt.savefig("top10_jobs_duration.png", dpi=300)
    plt.show()
else:
    print("'job' or 'duration' column not found in dataset.")

