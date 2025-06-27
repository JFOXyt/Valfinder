import tkinter
from tkinter import END, messagebox
import requests
from PIL import Image, ImageTk
from teamsregions import regionsshort,regions

def butaoplayers(root,img,result_labels,gray,static_labels):
    for label in result_labels + static_labels:
        label.destroy()

    result_labels.clear()
    static_labels.clear()

    entry=tkinter.Entry(root
                        ,font=('Arial',32))
    
    entry.place(x=25,y=325,height=60,width=550)

    playerl=tkinter.Label(root,text='Player'
                        ,bg=gray
                        ,font=('Arial',16,'italic'))
    playerl.place(x=25,y=290)
    static_labels.append(playerl)

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
                               ,command=lambda:[pesquisarplayers()]
                               ,bg=gray)
    
    butaosearch.image=image
    butaosearch.place(x=1200,y=320)
    static_labels.append(butaosearch)

    def pesquisarplayers():

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
            url=requests.get(f'https://vlrggapi.vercel.app/stats?region={region}&timespan=60')
            response=url.json()
        except:
            pass

        result_labels.clear()

        entrygets=entry.get().lower().strip()
        entry.delete(0,END)
        

        if url.status_code==200 and entrygets!='' and getregion!='':
            playerslen=len(response['data']['segments'])
            pode=False

            for player in range(playerslen):
                nomeplayer=response['data']['segments'][player]['player'].lower()
                playerentry=nomeplayer.find(entrygets)

                if playerentry!=-1:

                    org=response['data']['segments'][player]['org']
                    mains=response['data']['segments'][player]['agents']
                    mainslen=len(mains)

                    rounds=response['data']['segments'][player]['rounds_played']
                    rating=response['data']['segments'][player]['rating']
                    hs=response['data']['segments'][player]['headshot_percentage']
                    kpr=response['data']['segments'][player]['kills_per_round']

                    avgdpr=response['data']['segments'][player]['average_damage_per_round']
                    avgcs=response['data']['segments'][player]['average_combat_score']
                    csp=response['data']['segments'][player]['clutch_success_percentage']

                    nameplayerl=tkinter.Label(root,text=nomeplayer.title()
                                              ,font=('Arial',44,'bold')
                                              ,bg=gray)
                    nameplayerl.place(x=75,y=450)
                    result_labels.append(nameplayerl)

                    orgl=tkinter.Label(root,text=f'Team: {org}'
                                       ,font=('Arial',44,'bold')
                                       ,bg=gray)
                    orgl.place(x=550,y=450)
                    result_labels.append(orgl)

                    statsl=tkinter.Label(root,text='Stats: '
                                         ,font=('Arial',44,'bold')
                                         ,bg=gray)
                    statsl.place(x=75,y=575)
                    result_labels.append(statsl)

                    roundsl=tkinter.Label(root,text=f'Rounds played: {rounds}'
                                          ,font=('Arial',32)
                                          ,bg=gray)
                    roundsl.place(x=125,y=675)
                    result_labels.append(roundsl)

                    ratingl=tkinter.Label(root,text=f'Rating: {rating}'
                                          ,font=('Arial',32)
                                          ,bg=gray)
                    ratingl.place(x=125,y=750)
                    result_labels.append(ratingl)

                    hsl=tkinter.Label(root,text=f'Headshot (%): {hs}'
                                      ,font=('Arial',32)
                                      ,bg=gray)
                    hsl.place(x=125,y=825)
                    result_labels.append(hsl)

                    kprl=tkinter.Label(root,text=f'Kill p/ round: {kpr}'
                                       ,font=('Arial',32)
                                       ,bg=gray)
                    kprl.place(x=125,y=900)
                    result_labels.append(kprl)

                    avgdprl=tkinter.Label(root,text=f'Average Damage p/ round: {avgdpr}'
                                          ,font=('Arial',32)
                                          ,bg=gray)
                    avgdprl.place(x=575,y=675)
                    result_labels.append(avgdprl)

                    avgcsl=tkinter.Label(root,text=f'Average Combat Score: {avgcs}'
                                         ,font=('Arial',32)
                                         ,bg=gray)
                    avgcsl.place(x=575,y=750)
                    result_labels.append(avgcsl)

                    cspl=tkinter.Label(root,text=f'Clutch Win Percentage: {csp}'
                                       ,font=('Arial',32)
                                       ,bg=gray)
                    cspl.place(x=575,y=825)
                    result_labels.append(cspl)

                    mainagentl=tkinter.Label(root,text='Main Agent: '
                                             ,font=('Arial',44,'bold')
                                             ,bg=gray)
                    mainagentl.place(x=1325,y=450)
                    result_labels.append(mainagentl) #1375

                    for main in range(mainslen):
                        mainsl=tkinter.Label(root,text=mains[main].title()
                                             ,font=('Arial',42,'bold')
                                             ,bg=gray)
                        mainsl.place(x=1375,y=575+main*125)
                        result_labels.append(mainsl)
                        
                    pode=False
                    break

                else:
                    pode=True

            if pode:
                messagebox.showerror('ERROR',"Check if you're connected to wifi or if you entered a correct region/player name")

        else:
            messagebox.showerror('ERROR',"Check if you're connected to wifi or if you entered a correct region/player name")




