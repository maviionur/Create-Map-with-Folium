import folium
import random

#Create map object
map = folium.Map(location=[41.123123, 28.343234], zoom_start=12)

#Locations
lc = [[41.123123, 28.343234],[40.123123, 27.343234],[42.123123, 29.343234],[39.123123, 32.343234]]

#Color Range
a ="0123456789abcdef"





#Circle Marker
for i in lc:
	color = '#'
	c = 1
	#Generate random color
	while c < 7:
		index = random.randint(0,16)
		color = color + a[index]
		c = c + 1
	folium.CircleMarker(
		location=i,
		radius=50,
		color=color,
		fill=True,
		fill_color=color
	).add_to(map)

#Generate map
map.save("map.html")
