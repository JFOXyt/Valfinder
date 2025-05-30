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
                               ,command=lambda:[pesquisarbundle()]
                               ,bg=gray)
    
    butaosearch.place(x=600,y=320)

    url=requests.get('https://valorant-api.com/v1/bundles')
    response=url.json()

    def pesquisarbundle():

        for label in result_labels:
            label.destroy()

        result_labels.clear()

        entrygets=entry.get().lower()
        entry.delete(0,END)

        if url.status_code==200 and entrygets!='':
            bundellen=len(response['data'])

            for bundles in range(bundellen):
                bundlenames=response['data'][bundles]['displayName'].lower()
                bundlename=bundlenames.find(entrygets)

                if bundlename!=-1:
                    img_bundle=requests.get(response['data'][bundles]['displayIcon2'])
                    img_bundle_vertical=requests.get(response['data'][bundles]['verticalPromoImage'])
                    pode=True
                    break
                else:
                    pode=False       

            if pode!=True:
                tkinter.messagebox.showerror('Error',"Check if you are conected to the wifi or if you entered a bundle name")
            try:
                with open('bundleimg.png','wb') as img:
                    img.write(img_bundle.content)
                with open('bundleimg_vert.png','wb') as img_vert:
                    img_vert.write(img_bundle_vertical.content)
                pode1=True
            except:
                pode1=False

            if pode1==True:

                nomebundle=tkinter.Label(root,text=bundlenames.title()
                                        ,bg=gray
                                        ,font=('Arial',32,'bold'))
                nomebundle.place(x=50,y=400)
                result_labels.append(nomebundle)

                img_p=Image.open('bundleimg.png')
                big=img_p.resize([1200,770])
                img_b=ImageTk.PhotoImage(big)

                img_b_t=tkinter.Label(root,image=img_b
                                    ,bg=gray)
                img_b_t.img_b=img_b
                img_b_t.place(x=720,y=280)
                result_labels.append(img_b_t)

                imgvert_p=Image.open('bundleimg_vert.png')
                big_vert=imgvert_p.resize([400,600])
                imgvert_b=ImageTk.PhotoImage(big_vert)

                imgvert_b_t=tkinter.Label(root,image=imgvert_b
                                          ,bg=gray)
                imgvert_b_t.imgvert_b=imgvert_b
                imgvert_b_t.place(x=50,y=500)
                result_labels.append(imgvert_b_t)

        else:
            tkinter.messagebox.showerror('Error',"Check if you are conected to the wifi or if you entered a bundle name")