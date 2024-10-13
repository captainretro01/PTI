dat=""
from PIL import Image
from tkinter import filedialog
file = filedialog.askopenfilename(filetypes=[("Bitmap", "*.bmp")])
img = Image.open(file,"r")
pv=list(img.getdata())
w, h = img.size
dat= str(w)+" "+str(h)+" "
l=len(pv)
print("Total Parts/step: ",l)
print("PROCESSING START")
for c in range(l):
    if pv[c]==0:
        pv[c]=1
    if pv[c]==255:
        pv[c]=0
    print("Step 1 of 2, Part ",c," of ",l)
for c in range(l):
    dat= dat+str(pv[c])
    print("Step 2 of 2, Part: ",c," of ",l)
print("PROCESSING DONE")
pti = filedialog.asksaveasfile(mode='w', filetypes=[("Plaintext Image","*.pti")], defaultextension=[(".pti")])
pti.write(dat)
pti.close()

