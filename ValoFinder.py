import tkinter,requests,glob
import tkinter.messagebox
from tkinter import messagebox,END
from tkinter.messagebox import showerror
from PIL import Image,ImageTk

root=tkinter.Tk()

altura=root.winfo_screenheight()
largura=root.winfo_screenwidth()

gray='#d1d1d1'

root.geometry(f'{str(largura)}x{str(altura)}')
root.resizable(False,False)
root.title('Valorant Finder')
root.config(bg=gray)

img=glob.glob('*.png')
print(img)

result_labels=[]

def clearentrys():
    result_labels.clear()

def butaoagentes():
    for label in result_labels:
        label.destroy()

    result_labels.clear()


    entry=tkinter.Entry(root
                        ,font=('Arial',32))
    
    entry.place(x=25,y=300,height=60,width=550)

    image=tkinter.PhotoImage(file=img[2]).subsample(6,6)
    imagesearch=image

    butaosearch=tkinter.Button(root,image=imagesearch
                               ,cursor='hand2'
                               ,border=0
                               ,command=lambda:[butaosearch()]
                               ,bg=gray)
    
    imagesearch.image=image
    
    butaosearch.place(x=600,y=295)

    url=requests.get('https://valorant-api.com/v1/agents')
    response=url.json()

    def butaosearch():

        for label in result_labels:
            label.destroy()
        result_labels.clear()

        entryget=entry.get().lower().capitalize()
        entry.delete(0,END)

        if url.status_code==200 and entryget!='':
            lenagent=len(response['data'])

            for i in range(lenagent):
                pegarnomeagente=response['data'][i]['displayName']
                isplayable=response['data'][i]['isPlayableCharacter']

                if entryget==pegarnomeagente and isplayable:
                    nomeagente=entryget
                    description=response['data'][i]['description']

                    imageagent=requests.get(response['data'][i]['fullPortrait'])

                    with open('agentimage.png','wb') as ai:
                        ai.write(imageagent.content)
                    
                    role=response['data'][i]['role']['displayName']
                    roledescription=response['data'][i]['role']['description']
                    roleagent=requests.get(response['data'][i]['role']['displayIcon'])

                    with open('agentrole.png','wb') as ar:
                        ar.write(roleagent.content)

                    abilitylen=len(response['data'][i]['abilities'])

                    for a in range(abilitylen):
                        try:
                            abilityicon=requests.get(response['data'][i]['abilities'][a]['displayIcon'])
                            abilityname=response['data'][i]['abilities'][a]['displayName']
                            abilitydescription=response['data'][i]['abilities'][a]['description']

                            with open('iconability.png','wb') as ib:
                                ib.write(abilityicon.content)

                            abilitynamet=tkinter.Label(root,text=abilityname
                                                       ,bg=gray
                                                       ,font=('Arial',24,'bold'))
                            
                            abilitynamet.place(x=1000,y=430+150*a)
                            result_labels.append(abilitynamet)

                            abilityicondimension=Image.open(img[3])
                            dimensao=abilityicondimension.width

                            if dimensao==1024:
                                dimensoes=13
                            elif dimensao==128:
                                dimensoes=2

                            abilityiconp=tkinter.PhotoImage(file=img[3]).subsample(dimensoes,dimensoes)

                            abilityiconpt=tkinter.Label(root,image=abilityiconp
                                                        ,bg=gray)
                            
                            abilityiconpt.abilityiconp=abilityiconp
                            abilityiconpt.place(x=900,y=430+150*a)
                            result_labels.append(abilityiconpt)

                            abilitydescriptiont=tkinter.Label(root,text=abilitydescription
                                                              ,wraplength=850
                                                              ,bg=gray
                                                              ,font=('Arial',14))
                            
                            abilitydescriptiont.place(x=1000,y=480+150*a)
                            result_labels.append(abilitydescriptiont)

                        except:
                            pass
                    
                    agentimagep=Image.open(img[0])
                    agentimagep=agentimagep.resize((agentimagep.width//3,agentimagep.height//3))
                    agentimage=ImageTk.PhotoImage(agentimagep)

                    agentimaget=tkinter.Label(root,image=agentimage,bg=gray)
                    agentimaget.agentimage=agentimage
                    agentimaget.place(x=-160,y=395)
                    result_labels.append(agentimaget)


                    nomeagentet=tkinter.Label(root,text=nomeagente
                                              ,font=('Arial',44,'bold')
                                              ,bg=gray)
                    
                    nomeagentet.place(x=325,y=396)
                    result_labels.append(nomeagentet)

                    descriptiont=tkinter.Label(root,text=description
                                               ,font=('Arial',18)
                                               ,bg=gray
                                               ,wraplength=370)
                    
                    descriptiont.place(x=375,y=500)
                    result_labels.append(descriptiont)

                    agentrole=tkinter.PhotoImage(file=img[1]).subsample(2,2)
                    agentrolet=tkinter.Label(root,image=agentrole
                                             ,bg=gray)
                    
                    agentrolet.agentrole=agentrole
                    agentrolet.place(x=325,y=750)
                    result_labels.append(agentrolet)

                    rolet=tkinter.Label(root,text=role
                                        ,bg=gray
                                        ,font=('Arial',32,'bold'))
                    
                    rolet.place(x=400,y=765)
                    result_labels.append(rolet)

                    roledescriptiont=tkinter.Label(root,text=roledescription
                                                   ,bg=gray
                                                   ,wraplength=370
                                                   ,font=('Arial',18))
                    
                    roledescriptiont.place(x=350,y=855)
                    result_labels.append(roledescriptiont)

                    abilitiest=tkinter.Label(root,text='Abilities'
                                             ,bg=gray
                                             ,font=('Arial',44,'bold'))
                    
                    abilitiest.place(x=950,y=300)
                    result_labels.append(abilitiest)
                    

        else:
            tkinter.messagebox.showerror('Error',"Check if you are conected to the wifi or if you entered an agent name")

def butaoskins():
    for label in result_labels:
            label.destroy()

    result_labels.clear()

    entry=tkinter.Entry(root
                        ,font=('Arial',32))
    
    entry.place(x=25,y=300,height=60,width=550)

    image=tkinter.PhotoImage(file=img[2]).subsample(6,6)
    imagesearch=image
    imagesearch.image=image

    butaosearch=tkinter.Button(root,image=imagesearch
                               ,cursor='hand2'
                               ,border=0
                               ,command=lambda:[butaosearch()]
                               ,bg=gray)
    
    butaosearch.place(x=600,y=295)

    url=requests.get('https://valorant-api.com/v1/weapons')
    response=url.json()

    def butaosearch():
        for label in result_labels:
            label.destroy()
        result_labels.clear()

        entryget=entry.get().lower().capitalize()
        entry.delete(0,END)

        if url.status_code==200 and entryget!='':

            #tem de ter um for a pegar em todos os tipos de armas e dps pega na terminaçao da entryget o nome da arma tp odin e dps entra na parte das odins e etc
            pass
        
        else:
            tkinter.messagebox.showerror('Error',"Check if you are conected to the wifi or if you entered a gun skin")



valred='#FF4655'
valblack='#0F0D19'

frame=tkinter.Frame(root
                    ,bg=valred
                    ,width=largura,height=100)

frame.place(x=0,y=0,height=280)

imageframep=Image.open(img[4]).resize((370,200))
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
                           ,command=lambda:[butaoagentes(),clearentrys()])

butaoagents.place(x=0,y=200,width=widthbutons,height=80)


butaoskis=tkinter.Button(root,text='Skins'
                          ,bg=valred,fg=valblack
                          ,font=('Arial',22,'bold')
                          ,border=0
                          ,command=lambda:[butaoskins(),clearentrys()])

butaoskis.place(x=widthbutons,y=200,width=widthbutons,height=80)


butaobundls=tkinter.Button(root,text='Bundles'
                            ,bg=valred,fg=valblack
                            ,font=('Arial',22,'bold')
                            ,border=0)

butaobundls.place(x=widthbutons*2,y=200,width=widthbutons,height=80)



butaobudis=tkinter.Button(root,text='Buddies'
                           ,bg=valred,fg=valblack
                           ,font=('Arial',22,'bold')
                           ,border=0)

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