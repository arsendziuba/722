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

# Creating two Building objects
white_bricks = Building("Bricks", "White", 300)
brown_planks = Building("Planks", "Brown", 20)

# Printing the initial state
print(white_bricks)
print(brown_planks)

# Adding 50 bricks to the first object and removing 3 planks from the second object
white_bricks.plus(50)
brown_planks.minus(3)

# Printing the updated state
print(white_bricks)
print(brown_planks)
