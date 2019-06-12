import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def initialize():
    plt.style.use('bmh')
    print(' - Fast Exploratory Data Analysis REPORT (FEDA)')

def count_null(df):
    print('\n\n - Null Counting')
    table = pd.DataFrame()

    report = df.isnull().sum(axis = 0)[df.isnull().sum(axis = 0) != 0].sort_values(ascending=False)

    table['Feature'] = list(report.index)
    table['Count'] = list(report.values)

    print(table.to_string())

def distribution(df, target):
    print('\n\n - Distribution')
    
    plt.figure(figsize=(9, 8))
    sns.distplot(df[target], color='g', bins=100, hist_kws={'alpha': 0.4})

def list_types(df):
    print('\n\n - Type List')
    
    types = list(set(df.dtypes.tolist()))

    for type_ in types:
        print(' - '+str(type_))

def list_columns_by_type(df):
    print('\n\n - Columns by Type')
    
    types = list(set(df.dtypes.tolist()))

    for type_ in types:
        print(' - ' + str(type_))
        print(list(df.select_dtypes(include=[type_]).columns))

def list_feature_corr(df, target):
    print('\n\n - Feature Correlation')
    
    table = pd.DataFrame()

    df_corr = abs(df.corr()[target][:-1])
    report = df_corr.sort_values(ascending=False)

    table['Feature'] = list(report.index)
    table['Correlation'] = list(report.values)

    print(table.to_string())

def report(df, target):
    initialize()
    count_null(df)
    distribution(df,target)
    list_types(df)
    list_columns_by_type(df)
    list_feature_corr(df,target)

df = pd.read_csv('path/train.csv')
report(df, 'SalePrice')
