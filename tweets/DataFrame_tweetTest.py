import pandas as pd
from tabulate import tabulate

df = pd.read_csv('tweetsManual.csv', sep=';')
print(tabulate(df, headers='keys', tablefmt='psql'))
