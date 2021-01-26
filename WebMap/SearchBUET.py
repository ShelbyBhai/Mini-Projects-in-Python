import folium

f = folium.FeatureGroup("bd_BUET_Map")

f.add_child(folium.GeoJson(data=(open("bd.json", "r", encoding="utf-8-sig").read())))

f.add_child(folium.Marker(location=[23.7440, 90.3920], popup="BUET is here!!"))

mymap = folium.Map(location=[23.6850, 90.3563], zoom_start=5)

mymap.add_child(f)

mymap.save("hahavodox.html")

