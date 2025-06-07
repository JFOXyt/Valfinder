import tkinter
from tkinter import END, messagebox
import requests
from PIL import Image, ImageTk

def butaobundles(root,img,result_labels,gray):
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
                               ,command=lambda:[pesquisarmapa()]
                               ,bg=gray)
    
    butaosearch.place(x=600,y=320)

    url=requests.get('https://valorant-api.com/v1/bundles')
    response=url.json()

    def pesquisarmapa():
        for label in result_labels:
            label.destroy()

        result_labels.clear()

        entrygets=entry.get().lower()
        entry.delete(0,END)

        if url.status_code==200 and entrygets!='':
            mapslen=len(response['data'])

            for mapas in range(mapslen):
                nomemapa=response['data'][mapas]['displayName']
                mapaentry=nomemapa.find(entrygets)

                if mapaentry!=-1:
                    tacticalDescription=response['data'][mapas]['tacticalDescription']
                    coordinates=response['data'][mapas]['coordinates']
                    displayIcon=response['data'][mapas]['displayIcon']
                    listViewIconTall=response['data'][mapas]['listViewIconTall']
                    listasuperregion=[]
                    listaregion=[]

                    calloutlen=len(response['data'][mapas]['callouts'])

                    for call in range(calloutlen):
                        listasuperregion.append(response['data'][mapas]['callout'][call]['superRegionName'])
                        listaregion.append(response['data'][mapas]['callout'][call]['RegionName'])

                    break
            
            
                    