import World as cw

p = cw.Planet("Yarnulon", 3)
p.create_planet()
c = cw.City("Pawston", 2, 0)
p.place_city(c)
p.show_planet()
