import sys
from tkinter.filedialog import askopenfilename
import time
import matplotlib.pyplot as plt
import numpy as np

file = askopenfilename(filetypes=[("Colour Plaintext Images", "*.cpti"),("Text Files", "*.txt")])
img = open(file, "r")
lne = img.readline()
dat = lne.split(" ")

w = int(dat[0])
h = int(dat[1])
print("Img Size: ",w,"x",h)
print(w*h," Pixels Total")
s = float(input("Enter pixel size: "))
l=int(w*h)

x=0
y=h
d=2
for c in range(l):
    
    
    rgb = dat[d]
    if rgb =="#000000":
        rgb="k"
    if len(rgb)==4:
        rgb=rgb+"000"
    elif len(rgb) == 5:
        rgb=rgb+"00"
    elif len(rgb) == 6:
        rgb=rgb+"0"
    
    x=np.array(x)
    y=np.array(y)
    plt.plot(x,y, 'o', ms = s, mec = str(rgb), mfc = str(rgb)  )
    x=x+1
    if x==w:
        y=y-1
        x=0
    print("Reading ",c," of ",l)
    d=d+1


plt.show()
