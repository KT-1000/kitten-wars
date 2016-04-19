class City:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class Planet:

    def __init__(self, name, size, cities=[]):
        self.name = name
        self.size = size
        self.cities = cities

        self.grid = []

    def create_planet(self):

        for i in range(self.size):
            new_col = []

            for j in range(self.size):
                new_row = []

                new_col.append(new_row)

            self.grid.append(new_col)

    def show_planet(self):
        for grid_row in self.grid:
            print grid_row

    def place_city(self, city):
        self.grid[city.x][city.y].append(city)
