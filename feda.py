import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('bmh')

def count_null(df):
    columns = df.isnull().sum(axis = 0).sort_values(ascending=False)
    columns = columns[columns != 0]
    
    print(columns.to_string())
    

def distribuition(df, target):
    plt.figure(figsize=(9, 8))
    sns.distplot(df[target], color='g', bins=100, hist_kws={'alpha': 0.4})