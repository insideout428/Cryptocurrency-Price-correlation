import pandas as pd
import numpy as np
import seaborn as sns


data = pd.read_excel("D:/Downloads/Bitcoin Data/Data/Crypto Currency Price Data.xlsx")
correlation = data.corr()
sns.heatmap(correlation, xticklabels= correlation.columns, yticklabels= correlation.columns,
            annot = False)      
