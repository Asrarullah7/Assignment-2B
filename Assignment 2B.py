import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('college_1.csv')
df2 = pd.read_csv('college_1.csv')
df = pd.concat([df1,df2], ignore_index=True)
df


