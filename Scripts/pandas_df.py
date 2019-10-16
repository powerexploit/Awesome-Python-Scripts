# Python code demonstrate creating a sample dataframe in pandas

# pip3 install pandas
# Importing the pandas library
import pandas as pd 
from numpy import nan

# intialise data of lists. 
data = {'Name':['Smith', 'Sourabh', 'Sahil', 'Jack'], 'Age':[20, 21, 19, 18],'Sports Involvement':['Football','Running','Cricket',nan]} 

# Create DataFrame 
df = pd.DataFrame(data) 

# Print the output. 
print(df) 

