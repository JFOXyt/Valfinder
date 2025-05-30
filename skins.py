import tkinter
from tkinter import END, messagebox
import requests
from PIL import Image, ImageTk
import statsguns

def butaoskins(root,img,result_labels,gray):

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
                               ,command=lambda:butaosearch()
                               ,bg=gray)
    
    butaosearch.place(x=600,y=320)

    ordem=tkinter.Label(root,text='Ordem: Nome Skin/Arma'
                        ,font=('Arial',16,'italic')
                        ,bg=gray)
    
    ordem.place(x=25,y=290)
    result_labels.append(ordem)

    url=requests.get('https://valorant-api.com/v1/weapons')
    response=url.json()

    def imagevariant(chromas_url,v):
        rendervariant=chromas_url[v]['fullRender']
        if rendervariant!=None:

            fullrendervariant=requests.get(chromas_url[v]['fullRender'])
            with open('variant_szin.png','wb') as variant:
                variant.write(fullrendervariant.content)

            fullrendervariant_pil=Image.open('variant_szin.png')
            bigg=fullrendervariant_pil.resize([800,231])
            fullrendervariant_img=ImageTk.PhotoImage(bigg)
            
            fullrendervariant_t=tkinter.Label(root,image=fullrendervariant_img
                                            ,bg=gray)
            fullrendervariant_t.fullrendervariant_img=fullrendervariant_img
            fullrendervariant_t.place(x=1000,y=600)
            result_labels.append(fullrendervariant_t)
        else:
            noexist=tkinter.Label(root,text="Doesn't exist")
            noexist.place(x=1000,y=550)     
            result_labels.append(noexist)       

    def butaosearch():
        entrygets=entry.get().lower()
        entry.delete(0,END)

        for label in result_labels:
                label.destroy()

        result_labels.clear()

        ordem=tkinter.Label(root,text='Ordem: Nome Skin/Arma'
                        ,font=('Arial',16,'italic')
                        ,bg=gray)
    
        ordem.place(x=25,y=290)
        result_labels.append(ordem)

        if url.status_code==200 and entrygets!='':

            guntypes=len(response['data'])

            #tem de ter um for a pegar em todos os tipos de armas e dps pega na terminaçao da entryget o nome da arma tp odin e dps entra na parte das odins e etc

            print(entrygets)

            for guntype in range(guntypes):
                nomesarmas=response['data'][guntype]['displayName'].lower()
                nomearma=entrygets.find(nomesarmas)

                if nomearma!=-1:
                    idarma=guntype
                    print(idarma)
                    break
                else:
                    idarma=404

            if idarma!=404:
                skinnum=len(response['data'][idarma]['skins'])
            else:
                skinnum=0
                tkinter.messagebox.showerror('Error',"Check if you are conected to the wifi or if you entered a gun skin")

            for skintype in range(skinnum):
                nomeskins=response['data'][guntype]['skins'][skintype]['displayName'].lower()
                nomeskin=entrygets.find(nomeskins)

                if nomeskin!=-1:
                    idskin=skintype
                    print(idskin,'nice')
                    break
                else:
                    idskin=404
            print(idskin,'bolas')

            if idskin!=404:
                pass
            else:
                tkinter.messagebox.showerror('Error',"Check if you are conected to the wifi or if you entered a gun skin")

            # meter for pa pegaras cenas necessarias 
            print(idskin)
            chromas_url=response['data'][idarma]['skins'][idskin]['chromas']
            variantes_qnt=len(response['data'][idarma]['skins'][idskin]['chromas'])

            lista_variantes=[]

            for variantes in range(variantes_qnt):
                swatch=chromas_url[variantes]['swatch']
                if swatch!=None:
                    swatch=requests.get(chromas_url[variantes]['swatch'])

                    with open('variante_swatch.png','wb') as swatchs:
                        swatchs.write(swatch.content)

                    swatch_img=tkinter.PhotoImage(file=img[8]).subsample(2,2)
                    swatch_t=tkinter.Button(root,image=swatch_img
                                        ,bg=gray
                                        ,cursor='hand2'
                                        ,border=0
                                        ,command=lambda v=variantes:[imagevariant(chromas_url,v)])
                    
                    swatch_t.swatch_img=swatch_img
                    swatch_t.place(x=1050+variantes*70,y=450)
                    result_labels.append(swatch_t)               

                nome_armat=tkinter.Label(root,text=nomesarmas
                                        ,font=('Arial',44,'bold')
                                        ,bg=gray)

            if swatch==None:
                noexist=tkinter.Label(root,text="Doesn't has variants"
                                      ,bg=gray
                                      ,font=('Arial',44,'bold'))
                noexist.place(x=1050,y=450)
                result_labels.append(noexist)
            
            nome_armat.place(x=50,y=396)
            result_labels.append(nome_armat)

            skinurl=requests.get(chromas_url[0]['fullRender'])

            category=response['data'][idarma]['category'].find('Sidearm')

            if category!=-1:
                subit=2
                y_stat=350

            else:
                subit=1
                y_stat=200

            with open("fullrender.png","wb") as fullrender:
                fullrender.write(skinurl.content)

            fullrenderopen=tkinter.PhotoImage(file="fullrender.png").subsample(subit,subit)

            fullrenderl=tkinter.Label(root,image=fullrenderopen,bg=gray)
            fullrenderl.fullrenderopen=fullrenderopen
            fullrenderl.place(x=300,y=415)
            result_labels.append(fullrenderl)

            nomeskin=tkinter.Label(root,text=nomeskins
                                   ,bg=gray
                                   ,font=('Arial',24,'bold'))
            
            nomeskin.place(x=400,y=565)
            result_labels.append(nomeskin)

            stats=statsguns.stats(response,idarma)

            n_listastats=len(stats[0])

            statpode=True

            for stat in range(n_listastats):
                if stats[1][stat]!= 'range End Meters' and statpode:
                    statt=tkinter.Label(root,text=f'{stats[1][stat].capitalize()}: {round(stats[0][stat],2)}'
                                        ,font=('Arial',18)
                                        ,bg=gray)
                    
                    statt.place(x=50,y=500+stat*50)
                    result_labels.append(statt)

                else:
                    statt=tkinter.Label(root,text=f'{stats[1][stat].capitalize()}: {round(stats[0][stat],2)}'
                                        ,font=('Arial',18)
                                        ,bg=gray)

                    statt.place(x=410,y=y_stat+stat*50)
                    result_labels.append(statt)
                    statpode=False

            variantes_t=tkinter.Label(root,text='Variantes'
                                     ,bg=gray
                                     ,font=('Arial',44,'bold'))
            variantes_t.place(x=1000,y=350)
            result_labels.append(variantes_t)



        else:
            tkinter.messagebox.showerror('Error',"Check if you are conected to the wifi or if you entered a gun skin")