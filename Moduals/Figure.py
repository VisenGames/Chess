from Moduals.Location import Location
from Moduals.Storage import Storage


class Figure:

    def __init__(self, location: Location, is_white: bool):
        self.location = location
        self.potential_positions = []
        self.is_white = is_white
        self.exists = True

    def remove(self):
        self.location.set_figure(None)
        self.exists = False
    
    def change_position(self, position):
        self.location = position
        for i in Storage.figures:
            i.update_potential_positions()
        if self.location.figure is not None:
            self.location.figure.remove()
        self.location.set_figure(self)

    def update_potential_positions(self):
        pass
