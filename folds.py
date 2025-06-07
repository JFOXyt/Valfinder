import folium

# Create a Map instance
m = folium.Map(location=[80.25, 64.8],
                   zoom_start=10, control_scale=True)

outfp="C:\\Users\\Lenovo\\Desktop\\Valfinder\\base_map.html"
m.save(outfp)