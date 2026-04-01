# 1) What is list comprehension?
result=['even' if i%2==0 else 'odd' for i in range(10)]
print(result)

# 2) What is dictionary comprehension?
result={ i:'even' if i%2==0 else 'odd' for i in range(10)}
print(result)

# 3) What is map(), filter(), reduce()?
l=[1,2,3,4,5]
result=list(map(lambda i:i*i if i%2==0 else i,l))
print(result)
res=list(filter(lambda i:i%2==0,l))
print(res)
from functools import reduce
re=reduce(lambda i,j:i+j,l)
print(re)