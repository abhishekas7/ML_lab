
import matplotlib.pyplot as py
import plotly.express as px
from bokeh.plotting import figure,output_file,show
import seaborn as sns

x=[1,2,3]
y=[4,7,8]
py.plot(x,y)
py.title("first graph")
py.xlabel("x-axis")
py.ylabel("y-axis")
py.show()

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.show()

graph=figure(title="Bokeh")
u=[1,2,3]
v=[5,4,3]
graph.line(u,v)
show(graph)

data = sns.load_dataset("iris")
sns.lineplot(x="sepal_length", y="sepal_width", data=data)
py.title('Title using Matplotlib Function')
py.show()