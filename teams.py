import tkinter
from tkinter import END, messagebox
import requests
from PIL import Image, ImageTk
from teamsregions import regionsshort,regions

def butaoteams(root,img,result_labels,gray,static_labels):
    for label in result_labels + static_labels:
        label.destroy()

    result_labels.clear()
    static_labels.clear()

    entry=tkinter.Entry(root
                        ,font=('Arial',32))
    
    entry.place(x=25,y=325,height=60,width=550)

    teaml=tkinter.Label(root,text='Team'
                        ,bg=gray
                        ,font=('Arial',16,'italic'))
    teaml.place(x=25,y=290)
    static_labels.append(teaml)

    regionl=tkinter.Label(root,text='Region'
                          ,bg=gray
                          ,font=('Arial',16,'italic'))
    regionl.place(x=625,y=290)
    static_labels.append(regionl)

    entryregion=tkinter.Entry(root
                              ,font=('Arial',32))
    entryregion.place(x=625,y=325,height=60,width=550)
    static_labels.append(entryregion)

    image=tkinter.PhotoImage(file=img[4]).subsample(6,6)
    imagesearch=image
    

    butaosearch=tkinter.Button(root,image=imagesearch
                               ,cursor='hand2'
                               ,border=0
                               ,command=lambda:[pesquisarteams()]
                               ,bg=gray)
    
    butaosearch.image=image
    butaosearch.place(x=1200,y=320)
    static_labels.append(butaosearch)

    def fix_url(url):
        if url.startswith("//"):
            return "https:" + url
        return url

    def pesquisarteams():

        for label in result_labels:
            label.destroy()

        getregion=entryregion.get().lower().strip().replace(' ','-')    
        region=entryregion.get().lower().strip().replace(' ','-')
        entryregion.delete(0,END)

        regionsnum=len(regions)

        for regiao in range(regionsnum):

            if regions[regiao].lower()==region.lower():
                region=regionsshort[regiao]
                break
            elif regionsshort[regiao]==region.lower():
                region=regionsshort[regiao]
                break

        erro=False

        
        
        print(region)

        try:
            url=requests.get(f'https://vlrggapi.vercel.app/rankings?region={region}')
            response=url.json()
        except:
            pass

        result_labels.clear()

        entrygets=entry.get().lower().strip()
        entry.delete(0,END)
        

        if url.status_code==200 and entrygets!='' and getregion!='':
            teamslen=len(response['data'])

            logores=[0,0]

            for team in range(teamslen):
                nometeam=response['data'][team]['team'].lower().strip()
                teamentry=nometeam.find(entrygets)

                if teamentry!=-1:
                
                    try:
                    
                        teamlogo=requests.get(fix_url(response['data'][team]['logo']))
                        teamrank=response['data'][team]['rank']
                        country=response['data'][team]['country']
                        record=response['data'][team]['record']
                        earnings=response['data'][team]['earnings']
                        recentmatch=[]

                        partida=response['data'][team]['last_played']
                        recentmatch.append(response['data'][team]['last_played_team'].replace('vs. ',''))
                        recentmatch.append(requests.get(fix_url(response['data'][team]['last_played_team_logo'])))

                        #faz frontend

                        nometeaml=tkinter.Label(root,text=nometeam.title()
                                                ,bg=gray
                                                ,font=('Arial',44,'bold'))
                        nometeaml.place(x=75,y=450)
                        result_labels.append(nometeaml)

                        rankteaml=tkinter.Label(root,text=f'#{teamrank}'
                                                ,bg=gray
                                                ,font=('Arial',44,'bold'))
                        rankteaml.place(x=75,y=550)
                        result_labels.append(rankteaml)

                        countryl=tkinter.Label(root,text=f'Country: {country}'
                                            ,bg=gray
                                            ,font=('Arial',44))
                        countryl.place(x=250,y=550)
                        result_labels.append(countryl)

                        recordl=tkinter.Label(root,text=f'Record (W/L): {record}'
                                            ,bg=gray
                                            ,font=('Arial',36,'bold'))
                        recordl.place(x=75,y=675)
                        result_labels.append(recordl)

                        earningsl=tkinter.Label(root,text=f'Earnings ($):{earnings.replace(",",".")}'
                                                ,bg=gray
                                                ,font=('Arial',36,'bold'))
                        earningsl.place(x=75,y=800)
                        result_labels.append(earningsl)

                        with open('zteamlogo.png','wb') as logoteam:
                            logoteam.write(teamlogo.content)

                        with open('zoponentlogo.png','wb') as logooponent:
                            logooponent.write(recentmatch[1].content)

                        logores=[150,150]

                        teamlogom=Image.open('zteamlogo.png').resize(logores)
                        teamlogom=ImageTk.PhotoImage(teamlogom)

                        teamlogol=tkinter.Label(root,image=teamlogom
                                                ,bg=gray)
                        teamlogol.teamlogom=teamlogom
                        teamlogol.place(x=650,y=400)
                        result_labels.append(teamlogol)

                        teamnamel=tkinter.Label(root,text=nometeam.title()
                                                ,bg=gray
                                                ,font=('Arial',34,'bold'))
                        
                        X=1200

                        if teamnamel.winfo_reqwidth()>=302:
                            X=1150
                            
                        teamnamel.config(wraplength=302)

                        teamnamel.place(x=X,y=440)
                        result_labels.append(teamnamel)

                        logores=[125,125]

                        teamlogom=Image.open('zteamlogo.png').resize(logores)
                        teamlogom=ImageTk.PhotoImage(teamlogom)

                        logoteaml=tkinter.Label(root,image=teamlogom
                                                ,bg=gray)
                        logoteaml.teamlogom=teamlogom
                        logoteaml.place(x=1200,y=550)
                        result_labels.append(logoteaml)

                        oponentnamel=tkinter.Label(root,text=recentmatch[0]
                                                ,bg=gray
                                                ,font=('Arial',34,'bold'))
                        
                        X=1600

                        if oponentnamel.winfo_reqwidth()>=302:
                            X=1550
                            
                        oponentnamel.config(wraplength=302)

                        oponentnamel.place(x=X,y=440)
                        result_labels.append(oponentnamel)

                        oponentlogom=Image.open('zoponentlogo.png').resize(logores)
                        oponentlogom=ImageTk.PhotoImage(oponentlogom)

                        oponentteaml=tkinter.Label(root,image=oponentlogom
                                                ,bg=gray)
                        oponentteaml.oponentlogom=oponentlogom
                        oponentteaml.place(x=1600,y=550)
                        result_labels.append(oponentteaml)

                        partidal=tkinter.Label(root,text=partida
                                            ,bg=gray
                                            ,font=('Arial',24))
                        partidal.place(x=1400,y=600)
                        result_labels.append(partidal)

                        vsl=tkinter.Label(root,text='VS'
                                        ,bg=gray
                                        ,font=('Arial',42))
                        vsl.place(x=1400,y=525)
                        result_labels.append(vsl)

                        erro=False
                        break
                    except:
                        pass
                else:
                    erro=True
                    
                
            if erro:
                messagebox.showerror('ERROR',"Check if you're connected to wifi or if you entered a team/region name")

        else:
            messagebox.showerror('ERROR',"Check if you're connected to wifi or if you entered a team/region name")