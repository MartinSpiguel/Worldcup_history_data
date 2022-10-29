import pandas as pd

##########################Cleaning data completly and getting it ready for use########################

#Loading data
data = pd.read_csv('data.csv', encoding='latin-1')

#Creating data frame
df = pd.DataFrame(data)
print(df.tail())