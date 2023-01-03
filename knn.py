from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

irisData=load_iris()
a=irisData.data
b=irisData.target
x_train,x_test,y_train,y_test=train_test_split(a,b,test_size=3,random_state=42)

model=KNeighborsClassifier(n_neighbors=9)
model.fit(x_train,y_train)

prediction=model.predict(x_test)
print(prediction)

acc=metrics.accuracy_score(y_test,prediction)
print(acc)