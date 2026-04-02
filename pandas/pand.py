import pandas as pd

# 1) What is a DataFrame?
l=['a','b','c']
df=pd.DataFrame({
    'name':['aman','chaman','dhaman'],
    'age':[23,24,25]
    },index=l)
print(df)

# 2) What is a Series?
name=['aman','chaman','dhaman']
s=pd.Series(name,index=l)
print(s)

# 3) How does groupby work?
i=['a','b','c','d']
df=pd.DataFrame({
    'name':['aman','chaman','dhaman','kaman'],
    'age':[23,24,23,23]
},index=i)
gdf=df.groupby('age')
for age,group in gdf:
    print(group)