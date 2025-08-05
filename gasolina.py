
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('gasolina.csv')

# Create the plot
sns.lineplot(x='dia', y='venda', data=df)

# Save the plot as a PNG file
plt.savefig('gasolina.png')
