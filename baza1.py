

#%%
import pandas as pd

#%%

data4=pd.read_csv('title.ratings.tsv',sep='\t')
data7=pd.read_csv('title.akas.tsv',sep='\t')
data7.rename(columns={'titleId': 'tconst'}, inplace=True)
data8=pd.merge(data4,data7,on='tconst',how='left')
del data4
del data7
#%%
data=pd.read_csv('title.basics.tsv',sep='\t')
data4=pd.merge(data8, data,on='tconst')
#%%
del data
del data8
#%%
data3=pd.read_csv('title.principals.tsv',sep='\t')
data4=pd.merge(data4,data3,on='tconst')
del data3

#%%
data=pd.read_csv('title.basics.tsv',sep='\t')
data3=pd.read_csv('title.principals.tsv',sep='\t')
data2=pd.read_csv('name.basics.tsv',sep='\t')
#%%
data2=pd.read_csv('name.basics.tsv',sep='\t')
data2=pd.merge(data4,data2,on='nconst',how='left')
del data4
#%%
data2.to_csv('filmovi.csv')

