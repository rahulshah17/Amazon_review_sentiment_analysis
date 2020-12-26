import json
import pandas as pd
import numpy as np
import time
start_time=time.time()
df=pd.read_json('a.json',lines=True)
dataset={"Name":df["reviewerName"],"Review":df["reviewText"],"Rating":df["overall"]}
dataset=pd.DataFrame(data=dataset)

dataset["Name"]=dataset["Name"].replace(np.nan," ",regex=True)
dataset["Review"]=dataset["Review"].replace(np.nan," ",regex=True)
dataset["Rating"]=dataset["Rating"].replace(np.nan," ",regex=True)

dataset = dataset[dataset["Rating"] != '3']
#dataset["Output"]=dataset["Rating"].apply(lambda rating:+1 if str(rating) >'3' else -1)
dataset["Output"]=dataset["Rating"].apply(lambda val:1 if val >3 else (-1 if val<3 else 0))
print(dataset)

from sklearn.model_selection import train_test_split
x=pd.DataFrame(dataset,columns=["Review"])
y=pd.DataFrame(dataset,columns=["Output"])
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=17)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(token_pattern=r'\b\w+\b')
training = cv.fit_transform(x_train["Review"].values.astype(str))
testing = cv.transform(x_test["Review"].values.astype(str))

from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression()
regressor.fit(training, y_train.values.ravel())
acc = regressor.score(testing, y_test)
print("Accuracy is:",acc*100)

n=dataset["Name"].tolist()
p=dataset["Output"].tolist()
from collections import Counter
cnt = Counter()
for word in n:
    cnt[word] += 1
l=dict(cnt.most_common(5))
alpha=list(l.keys())[0]
count=0
for m,i in enumerate(n):
    if(i==alpha):
            if(p[m]>0):
                count=count+1
print("The Global Promoter is:",alpha,"With highest number of positive reviews =",count)
print("Code Execution Time is: %s seconds " % (time.time() - start_time))

            