from garden import Potato, PotatoGarden

garden = PotatoGarden(5)
garden.are_all_ripe()
for j in range(3):
    garden.grow_garden()
    garden.are_all_ripe()
