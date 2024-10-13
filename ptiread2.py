import sys
from tkinter.filedialog import askopenfilename
import time
import matplotlib.pyplot as plt
import numpy as np

file = askopenfilename(filetypes=[("Plaintext Images", "*.pti"),("Text Files", "*.txt")])
img = open(file, "r")
lne = img.readline()
dat = lne.split(" ")
txt = dat[2]
w = int(dat[0])
h = int(dat[1])
print("Img Size: ",w,"x",h)
print(w*h," Pixels Total")
s = float(input("Enter pixel size: "))
l=int(len(txt))
x=[]
y=[]
xs=0
ys=h
for c in range(l):
    if txt[c]=="1":
        x.append(xs)
        y.append(ys)
    xs=xs+1
    if xs==w:
        xs=0
        ys=ys-1

xp = np.array(x)
yp = np.array(y)
plt.plot(xp,yp, 'o', ms = s, mec = 'k', mfc = 'k' )
plt.show()
