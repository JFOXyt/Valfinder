import tkinter,requests,glob
import tkinter.messagebox
from tkinter import messagebox,END
from tkinter.messagebox import showerror
from PIL import Image,ImageTk
import agentes,skins,bundles,buddies

root=tkinter.Tk()

altura=1080
largura=1920

gray='#d1d1d1'

root.geometry(f'{str(largura)}x{str(altura)}')
root.resizable(False,False)
root.title('Valorant Finder')
root.config(bg=gray)

img=glob.glob('*.png')
print(img)

result_labels=[]

def clearentrys():
    for label in result_labels:
        label.destroy()

    result_labels.clear()

valred='#FF4655'
valblack='#0F0D19'

frame=tkinter.Frame(root
                    ,bg=valred
                    ,width=largura,height=100)

frame.place(x=0,y=0,height=280)

imageframep=Image.open(img[7]).resize((370,200))
imageframe=ImageTk.PhotoImage(imageframep)

imageframelabel=tkinter.Label(root,image=imageframe,bg=valred)
imageframelabel.imageframe=imageframe
imageframelabel.place(x=25,y=30)

labelframe=tkinter.Label(root,text='Finder'
                         ,fg=valblack,bg=valred
                         ,font=('Arial',42,'bold'))

labelframe.place(x=300,y=80)


widthbutons=largura/7

butaoagents=tkinter.Button(root,text='Agents'
                           ,bg=valred,fg=valblack
                           ,font=('Arial',22,'bold')
                           ,border=0
                           ,command=lambda:[clearentrys(),agentes.butaoagentes(root,img,result_labels,gray)])

butaoagents.place(x=0,y=200,width=widthbutons,height=80)


butaoskins=tkinter.Button(root,text='Skins'
                          ,bg=valred,fg=valblack
                          ,font=('Arial',22,'bold')
                          ,border=0
                          ,command=lambda:[clearentrys(),skins.butaoskins(root,img,result_labels,gray)])

butaoskins.place(x=widthbutons,y=200,width=widthbutons,height=80)


butaobundls=tkinter.Button(root,text='Bundles'
                            ,bg=valred,fg=valblack
                            ,font=('Arial',22,'bold')
                            ,border=0
                            ,command=lambda:[clearentrys(),bundles.butaobundles(root,img,result_labels,gray)])

butaobundls.place(x=widthbutons*2,y=200,width=widthbutons,height=80)



butaobudis=tkinter.Button(root,text='Buddies'
                           ,bg=valred,fg=valblack
                           ,font=('Arial',22,'bold')
                           ,border=0
                           ,command=lambda:[clearentrys(),buddies   .butaobuddies(root,img,result_labels,gray)])

butaobudis.place(x=widthbutons*3,y=200,width=widthbutons,height=80)


butaomas=tkinter.Button(root,text='Maps'
                         ,bg=valred,fg=valblack
                         ,font=('Arial',22,'bold')
                         ,border=0)

butaomas.place(x=widthbutons*4,y=200,width=widthbutons,height=80)


butaospras=tkinter.Button(root,text='Sprays'
                           ,bg=valred,fg=valblack
                           ,font=('Arial',22,'bold')
                           ,border=0)

butaospras.place(x=widthbutons*5,y=200,width=widthbutons,height=80)


butaocars=tkinter.Button(root,text='Cards'
                          ,bg=valred,fg=valblack
                          ,font=('Arial',22,'bold')
                          ,border=0)

butaocars.place(x=widthbutons*6,y=200,width=widthbutons,height=80)

root.mainloop()