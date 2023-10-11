
import pandas as pd

# Example DataFrame
df = pd.read_excel('C:\\Users\\homa.behmardi\\Downloads\\es_L2600_c2.xlsx')

# Remove rows with any null (NaN) values
df_cleaned = df.dropna()



# Save the cleaned DataFrame to a new Excel file
df_cleaned.to_excel('esnew.xlsx', index=False)