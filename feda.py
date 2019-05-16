import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def initialize():
    plt.style.use('bmh')

def count_null(df):
    table = pd.DataFrame()
    
    report = df.isnull().sum(axis = 0)[df.isnull().sum(axis = 0) != 0].sort_values(ascending=False)
    
    table['Column'] = list(report.index)
    table['Count'] = list(report.values)
    
    print(table.to_string())
    
def distribution(df, target):
    plt.figure(figsize=(9, 8))
    sns.distplot(df[target], color='g', bins=100, hist_kws={'alpha': 0.4})
    
def list_types(df):
    return list(set(df.dtypes.tolist()))

def list_columns_by_type(df):
    types = list_types(df)
    
    for type_ in types:
        print(' - ' + str(type_))
        print(list(df.select_dtypes(include=[type_]).columns))

#initialize()
#
#df = pd.read_csv('/home/caiocarneloz/Dropbox/BCC/DataScience/Kaggle/house_prices/train.csv')
#
#count_null(df)
#distribution(df,'SalePrice')
#list_types(df)
#list_columns_by_type(df)