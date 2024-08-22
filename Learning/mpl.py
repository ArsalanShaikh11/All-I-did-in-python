#try differend types of graph by your own 
import matplotlib.pyplot as mp
import numpy as n

x=n.array([1,2,3,4])
y=n.array([5,6,7,8])
mp.title("GRAPH")
mp.xlabel("X")
mp.ylabel("Y")
mp.plot(x,y)
mp.show()

mp.bar(x,height=y,color="g") 
mp.show()

lm=["a","b","c","d"]
exp=[0,0,0.1,0]
mp.pie(x,labels=lm,explode=exp)
mp.legend()
mp.show()

# subplot
mp.subplot(1,2,1)
mp.plot(x,y,marker="*")    

x1=n.array([1,2,3,4])
y1=n.array([5,6,7,8])
mp.subplot(1,2,2)
mp.plot(x1,y1)
mp.show()


# histograph
# scatererd grpgh