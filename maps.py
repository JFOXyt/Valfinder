import tkinter,folium,os,re,webbrowser
from tkinter import END, messagebox
import requests
from PIL import Image, ImageTk

def butaomaps(root,img,result_labels,gray,static_labels):
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
                               ,command=lambda:[pesquisarmapa()]
                               ,bg=gray)
    
    butaosearch.image=image
    
    butaosearch.place(x=600,y=320)

    static_labels.append(butaosearch)

    url=requests.get('https://valorant-api.com/v1/maps')
    response=url.json()

    def pesquisarmapa():
        for label in result_labels:
            label.destroy()

        result_labels.clear()

        entrygets=entry.get().lower().strip()
        entry.delete(0,END)

        if url.status_code==200 and entrygets!='':
            mapslen=len(response['data'])

            for mapas in range(mapslen):
                nomemapa=response['data'][mapas]['displayName'].lower().strip()
                mapaentry=nomemapa.find(entrygets)


                if mapaentry!=-1:
                    tacticalDescription=response['data'][mapas]['tacticalDescription']
                    coordinates=response['data'][mapas]['coordinates']
                    displayIcon=requests.get(response['data'][mapas]['displayIcon'])
                    listViewIconTall=requests.get(response['data'][mapas]['listViewIconTall'])
                    listaregion=[]

                    try:
                        calloutlen=len(response['data'][mapas]['callouts'])
                    except:
                        calloutlen=0

                    for call in range(calloutlen):
                        listaregion.append([response['data'][mapas]['callouts'][call]['superRegionName'],response['data'][mapas]['callouts'][call]['regionName']])

                    print(coordinates)

                    def parse_coordinates(coord_str):

                        coord_str = coord_str.replace('′', "'").replace('″', '"')

                        coord_str = re.sub(r"(\d+)\s*°\s*(\d+)\s*'[^NSWE]*([NSWE])", lambda m: f"{m.group(1)}°{m.group(2)}'{m.group(3)}", coord_str)

                        if ',' in coord_str:
                            parts = coord_str.split(',')
                        else:
                            parts = coord_str.split(maxsplit=1)
                        
                        if len(parts) < 2:
                            raise ValueError("Invalid coordinate format")

                        lat_raw = parts[0].strip()
                        lon_raw = parts[1].strip()

                        def extract(coord):

                            pattern = r"(\d+)°(\d+)'[A-Z]*([NSWE])"
                            match = re.match(pattern, coord)
                            if not match:
                                raise ValueError(f"Invalid part: {coord}")
                            deg = int(match.group(1))
                            minutes = int(match.group(2))
                            direction = match.group(3)

                            decimal = deg + minutes / 60
                            if direction in ['S', 'W']:
                                decimal *= -1
                            return decimal

                        lat = extract(lat_raw)
                        lon = extract(lon_raw)

                        return lat, lon
                                        
                    
                    def mapa():
                        map_center = parse_coordinates(coordinates)
                        m = folium.Map(location=map_center, zoom_start=13)

                        map_file = "map.html"
                        m.save(map_file)

                        file_url = f"file://{os.path.abspath(map_file)}"
                        webbrowser.open(file_url)

                    nomemapal=tkinter.Label(root,text=nomemapa.title()
                                            ,bg=gray
                                            ,font=('Arial',44,'bold'))
                    nomemapal.place(x=75,y=450)
                    result_labels.append(nomemapal)

                    try:
                        tacticalDescription=tacticalDescription.replace('Sites','')
                    except:
                        pass

                    sitesl=tkinter.Label(root,text='Sites: {}'.format(tacticalDescription)
                                         ,bg=gray
                                         ,font=('Arial',32,'bold'))
                    sitesl.place(x=350,y=465)
                    result_labels.append(sitesl)

                    with open('vert_site.png','wb') as vert_site :
                        vert_site.write(listViewIconTall.content)

                    
                    vert_sitep=Image.open('vert_site.png')

                    heigtvert=vert_sitep.height
                    widthvert=vert_sitep.width

                    if heigtvert==1020:
                        resizevert=2
                    elif heigtvert==748:
                        resizevert=1.5
                    else:
                        print('Theres more image sizes')
                        resizevert=1

                    vert_site_resized=vert_sitep.resize((300,500),Image.LANCZOS)
                    vert_siteph=ImageTk.PhotoImage(vert_site_resized)

                    vert_sitel=tkinter.Label(root,image=vert_siteph
                                             ,bg=gray)
                    vert_sitel.vert_siteph=vert_siteph
                    vert_sitel.place(x=75,y=525)
                    result_labels.append(vert_sitel)

                    erro=False

                    regionnum=len(listaregion)
                    a=30
                    mid=30
                    b=30
                    c=30

                    al=tkinter.Label(root,text='A :'
                                     ,bg=gray
                                     ,font=('Arial',26,'bold'))
                    al.place(x=500,y=545)
                    result_labels.append(al)

                    midl=tkinter.Label(root,text='Mid :'
                                       ,bg=gray
                                       ,font=('Arial',26,'bold'))
                    midl.place(x=625,y=545)
                    result_labels.append(midl)

                    bl=tkinter.Label(root,text='B :'
                                     ,bg=gray
                                     ,font=('Arial',26,'bold'))
                    bl.place(x=750,y=545)
                    result_labels.append(bl)

                    cl=tkinter.Label(root,text='C :'
                                     ,bg=gray
                                     ,font=('Arial',26,'bold'))
                    cl.place(x=875,y=545)
                    result_labels.append(cl)

                    for site in range(regionnum):
                        if listaregion[site][0]=='A':
                            region=tkinter.Label(root,text=listaregion[site][1]
                                                  ,bg=gray
                                                  ,font=('Arial',18))
                            region.place(x=500,y=575+a)
                            result_labels.append(region)
                            a+=30
                        if listaregion[site][0]=='Mid':
                            region=tkinter.Label(root,text=listaregion[site][1]
                                                    ,bg=gray
                                                    ,font=('Arial',18))
                            region.place(x=625,y=575+mid)
                            result_labels.append(region)
                            mid+=30
                        if listaregion[site][0]=='B':
                            region=tkinter.Label(root,text=listaregion[site][1]
                                                 ,bg=gray
                                                 ,font=('Arial',18))
                            region.place(x=750,y=575+b)
                            result_labels.append(region)
                            b+=30
                        if listaregion[site][0]=='C':
                            region=tkinter.Label(root,text=listaregion[site][1]
                                                 ,bg=gray
                                                 ,font=('Arial',18))
                            region.place(x=875,y=575+c)
                            result_labels.append(region)
                            c+=30

                    with open('zdisplayicon_map.png','wb') as mapicon:
                        mapicon.write(displayIcon.content)

                    mapiconp=ImageTk.PhotoImage(Image.open('zdisplayicon_map.png').resize([800,700]))

                    mapiconl=tkinter.Label(root,image=mapiconp
                                           ,bg=gray)
                    mapiconl.mapiconp=mapiconp
                    mapiconl.place(x=1100,y=300)
                    result_labels.append(mapiconl)

                    mapcoordsl=tkinter.Button(root,text='Coords do mapa na vida real'
                                             ,font=('Arial',24,'bold')
                                             ,command=mapa
                                             ,bg=gray)
                    mapcoordsl.place(x=750,y=325)
                    result_labels.append(mapcoordsl)
                    

                    break

                else:
                    erro=True

                

            if erro:
                messagebox.showerror('ERROR',"Check if you're connected to wifi or if you entered a map name")


        else:
            messagebox.showerror('ERROR',"Check if you're connected to wifi or if you entered a map name")

                    
            
      