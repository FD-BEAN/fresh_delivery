import pandas as pd
from sspipe import px, p

print(pd.DataFrame([[1,2,3,4], [5,6,7,8]], columns=['a','b','c','d']) | px.drop('a',axis=1))