import pandas as pd

# Load data from CSV into a DataFrame
df = pd.read_csv('emps.csv')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove decimal places in the Age column
df['Age'] = df['Age'].astype(int)

# Convert USD salary to EGP (assuming 1 USD = 16 EGP for this example)
df['Salary'] = df['Salary'] * 16

print(f"Average age: {df['Age'].mean()}")
print(f"Median salary: {df['USD Salary'].median()}")
print(f"Ratio of male to female employees: {df[df['Gender'] == 'Male'].shape[0] / df[df['Gender'] == 'Female'].shape[0]}")

# Write new data to a new CSV file
df.to_csv('new_data.csv', index=False)