from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn import metrics
from  sklearn.model_selection import train_test_split

iris=datasets.load_iris()
a=iris.data
b=iris.target

x_train,x_test,y_train,y_test=train_test_split(a,b,test_size=3,random_state=42)

model=GaussianNB()
model.fit(x_train,y_train)

prediction=model.predict(x_test)
print(prediction)

print(metrics.accuracy_score(y_test,prediction)*100)

