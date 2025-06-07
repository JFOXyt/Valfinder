import tkinter
from tkinter import END, messagebox
import requests
from PIL import Image, ImageTk

def butaobuddies(root,img,result_labels,gray):
    for label in result_labels:
        label.destroy()

    result_labels.clear()

    entry=tkinter.Entry(root
                        ,font=('Arial',32))
    
    entry.place(x=25,y=325,height=60,width=550)

    image=tkinter.PhotoImage(file=img[4]).subsample(6,6)
    imagesearch=image
    imagesearch.image=image

    butaosearch=tkinter.Button(root,image=imagesearch
                               ,cursor='hand2'
                               ,border=0
                               ,command=lambda:[searchbuddies()]
                               ,bg=gray)
    
    butaosearch.place(x=600,y=320)

    url=requests.get('https://valorant-api.com/v1/buddies')
    response=url.json()

    def searchbuddies():
        for label in result_labels:
            label.destroy()

        result_labels.clear()

        entrygets=entry.get().lower()
        entry.delete(0,END)

        if url.status_code==200 and entrygets!='':
            budielen=len(response['data'])

            for budie in range(budielen):
                budienames=response['data'][budie]['displayName'].lower()
                budiename=budienames.find(entrygets)

                if budiename!=-1:
                    displayicon=requests.get(response['data'][budie]['displayIcon'])
                    print(response['data'][budie]['displayIcon'])
                    pode=True
                    break
                else:
                    pode=False

            if pode!=True:
                tkinter.messagebox.showerror('Error',"Check if you are conected to the wifi or if you entered a bundle name")

            try:
                with open('zdisplayicon_buddie.png','wb') as iconbud:
                    iconbud.write(displayicon.content)

                pode1=True
            except:
                pode1=False

            if pode1:
                
                nomebuddie=tkinter.Label(root,text=budienames.title()
                                         ,bg=gray
                                         ,font=('Arial',44,'bold'))
                nomebuddie.place(x=75,y=450)
                result_labels.append(nomebuddie)

                imgb=Image.open('zdisplayicon_buddie.png')
                imgbu=imgb.resize([300,300])
                imgbud=ImageTk.PhotoImage(imgbu)
                imgbudie=tkinter.Label(root,image=imgbud
                                       ,bg=gray)
                imgbudie.imgbud=imgbud
                imgbudie.place(x=100,y=650)
                result_labels.append(imgbudie)

