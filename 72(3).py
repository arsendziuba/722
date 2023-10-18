class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self._number = number
        self.place = self.storage_place()

    def storage_place(self):
        if self._number < 0:
            return "out of stock"
        elif 0 < self._number < 100:
            return "warehouse"
        else:
            return "Remote warehouse"

    def plus(self, count):
        if count > 0:
            self._number += count
            self.place = self.storage_place()

    def minus(self, count):
        if count > 0:
            self._number -= count
            self.place = self.storage_place()

    def __str__(self):
        return f"{self.material} in {self.color}: {self._number} ({self.place})"

class Market(Building):
    def __init__(self, material, color, number=0):
        super().__init__(material, color, number)

    def plus(self, count):
        if count > 0:
            super().plus(count // 2)

    def minus(self, count):
        if count > 0:
            super().minus(count // 2)

# Creating two Market objects
white_bricks_market = Market("Bricks", "White", 300)
brown_planks_market = Market("Planks", "Brown", 20)

# Printing the initial state
print(white_bricks_market)
print(brown_planks_market)

# Adding 50 bricks to the first object
white_bricks_market.plus(50)

# Removing 3 planks from the second object
brown_planks_market.minus(3)

# Printing the updated state
print(white_bricks_market)
print(brown_planks_market)
