dat=""
from PIL import Image
from tkinter import filedialog
file = filedialog.askopenfilename(filetypes=[("Bitmap", "*.bmp")])

img = Image.open(file,"r")
pv=list(img.getdata())
w, h = img.size
dat= str(w)+" "+str(h)+" "
l=len(pv)
print("Steps: ",l)
print("PROCESSING START")
for c in range(l):
    vals=str(pv[c])
    vals=vals[1:-1]
    pixval = vals.split(", ")
    for i in range(len(pixval)):
        pixval[i] = int(pixval[i])
    r=hex(pixval[0])
    g=hex(pixval[1])
    b=hex(pixval[2])
    r=str(r)
    g=str(g)
    b=str(b)
    r=r[2:]
    b=b[2:]
    g=g[2:]
    rgb="#"+r+g+b
    if len(rgb)==4:
        rgb=rgb+"000"
    elif len(rgb)==5:
        rgb=rgb+"00"
    elif len(rgb)==6:
        rgb=rgb+"0"
    
    dat=dat+rgb+" "
    print("Step ",c," of ",l)

pti = filedialog.asksaveasfile(mode='w', filetypes=[("Colour Plaintext Image","*.cpti")], defaultextension=[(".cpti")])  
pti.write(dat)
pti.close()
