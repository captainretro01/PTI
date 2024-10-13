import sys
from tkinter.filedialog import askopenfilename
import time

file = askopenfilename(filetypes=[("Plaintext Images", "*.pti"),("Text Files", "*.txt")])
img = open(file, "r")
lne = img.readline()
dat = lne.split(" ")
txt = dat[2]
w = int(dat[0])
h = int(dat[1])
print("Img Size: ",w,"x",h)
l=int(len(txt))
t=0
for c in range(l):
    if txt[c]=="1":
        print("██",end="")
    else:
        print("  ",end="")
    t=t+1
    if t==w:
        print(""
              "")
        t=0
time.sleep(5)
