import pyperclip
import pandas as pd
import matplotlib.pyplot as plt


text = pyperclip.paste().lower()   


a=text.count("a")
b=text.count("b")
c=text.count("c")
d=text.count("d")
e=text.count("e")
f=text.count("f")
g=text.count("g")
h=text.count("h")
i=text.count("i")
j=text.count("j")
k=text.count("k")
l=text.count("l")
m=text.count("m")
n=text.count("n")
o=text.count("o")
p=text.count("p")
q=text.count("q")
r=text.count("r")
s=text.count("s")
t=text.count("t")
u=text.count("u")
v=text.count("v")
w=text.count("w")
x=text.count("x")
y=text.count("y")
z=text.count("z")


letters = list("abcdefghijklmnopqrstuvwxyz")
counts = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

df = pd.DataFrame({"letter": letters,"count": counts})


plt.figure(figsize=(12,6))


plt.plot(df["letter"], df["count"], marker="o", label="Line Chart")


plt.bar(df["letter"], df["count"], alpha=0.5, label="Bar Chart")

for x, y in zip(df["letter"], df["count"]):
    plt.text(x, y, str(y), ha='center', va='bottom', fontsize=9, color="red")

plt.title("Letter Frequency")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.legend()
plt.grid(True)

plt.show()
