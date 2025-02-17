# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import folium

political_countries_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
)


m = folium.Map(location=(10, 30), zoom_start=3, tiles="Cartodb Positron")
folium.GeoJson(political_countries_url).add_to(m)
m.save("footprint.html")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
