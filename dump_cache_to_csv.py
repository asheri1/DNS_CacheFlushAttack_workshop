import lmdb
import pandas as pd
import os

# Path to your LMDB file (assuming it's in the same directory as the script)
current_dir = os.path.dirname(os.path.abspath(__file__))
lmdb_path = os.path.join(current_dir, 'cache.lmdb')

# Open the LMDB environment
env = lmdb.open(lmdb_path, readonly=True)

# Initialize an empty list to store the data
data = []

# Read the data from the LMDB file
with env.begin() as txn:
    cursor = txn.cursor()
    for key, value in cursor:
        # Decode key (assuming keys are strings)
        decoded_key = key.decode('utf-8', errors='ignore')
        # Convert value to a hexadecimal string or handle it as binary
        hex_value = value.hex()
        data.append((decoded_key, hex_value))

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data, columns=['Key', 'Value'])

# Write the DataFrame to a CSV file with escape character
df.to_csv('output.csv', index=False, escapechar='\\')

# Write the DataFrame to an Excel file
# df.to_excel('output.xlsx', index=False)

print("Data has been successfully exported to 'output.csv'")
