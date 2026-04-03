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
    
# 4) What is aggregation?
print(df['age'].agg(sum))
print(df.groupby('age').agg('count'))

# 5) How do you handle missing values?
dff=pd.DataFrame({
    'name':['a',None,'c'],
    'salary':[1000,2000,3000],
    'age':[23,20,24]
})
dff[dff.isna()]='b'
print(dff)

# 6) How do you join two DataFrames?
mergeDf=df.merge(dff,'left','age')
print(mergeDf)                      # Merge work column basis
joinedDf=df.join(dff,'age','left',lsuffix='x',rsuffix='y')  # Join work index basis
print(joinedDf)

# 7) What is concat?
print(pd.concat([df, dff]))

# 8) What is indexing?
print(df.loc['a'])
print(df.iloc[0])

# 9) what is vectorization?
print(df['age'] + 1)

# 10) Why is Pandas slow for large data?
# Single cpu, work on RAM, GIL issue and more....