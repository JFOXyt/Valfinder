import tkinter
from tkinter import END
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

def butaoagentes(root,img,result_labels,gray,static_labels):

    for label in result_labels + static_labels:
        label.destroy()

    result_labels.clear()
    static_labels.clear()

    entry=tkinter.Entry(root
                        ,font=('Arial',32))
    
    entry.place(x=25,y=325,height=60,width=550)

    image=tkinter.PhotoImage(file=img[4]).subsample(6,6)
    imagesearch=image

    butaosearch=tkinter.Button(root,image=imagesearch
                               ,cursor='hand2'
                               ,border=0
                               ,command=lambda:[butaosearch()]
                               ,bg=gray)
    
    butaosearch.image=image
    
    butaosearch.place(x=600,y=320)
    static_labels.append(butaosearch)

    url=requests.get('https://valorant-api.com/v1/agents')
    response=url.json()

    def butaosearch():
        found=False

        for label in result_labels:
            label.destroy()
        result_labels.clear()

        entryget=entry.get().lower().strip()
        entry.delete(0,END)

        if url.status_code==200 and entryget!='':
            lenagent=len(response['data'])
            print(lenagent)

            for i in range(lenagent):
                pegarnomeagente=response['data'][i]['displayName'].lower().strip()
                isplayable=response['data'][i]['isPlayableCharacter']
                temoun=entryget.find(pegarnomeagente)

                if temoun!=-1 and isplayable:
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

                        dimensoes=52

                        abilityiconp=Image.open(img[6]).resize([dimensoes,dimensoes])
                        abilityiconp=ImageTk.PhotoImage(abilityiconp)

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
                    
                    agentimagep=Image.open(img[0])
                    agentimagep=agentimagep.resize((agentimagep.width//3,agentimagep.height//3))
                    agentimage=ImageTk.PhotoImage(agentimagep)

                    agentimaget=tkinter.Label(root,image=agentimage,bg=gray)
                    agentimaget.agentimage=agentimage
                    agentimaget.place(x=-160,y=395)
                    result_labels.append(agentimaget)


                    nomeagentet=tkinter.Label(root,text=nomeagente.title()
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
                    found=True

                    break
            if not found:
                messagebox.showerror('Error',"Check if you are conected to the wifi or if you entered an agent name")

        else:
            messagebox.showerror('Error',"Check if you are conected to the wifi or if you entered an agent name")
