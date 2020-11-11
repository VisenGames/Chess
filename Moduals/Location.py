from Moduals.Figure import Figure
from Moduals.Storage import Storage


class Location:

    def __init__(self, x: int, y: int, figure: Figure):
        self.x = x
        self.y = y
        self.figure = figure

    def set_figure(self, figure):
        self.figure = figure

    @staticmethod
    def get_location_at(x: int, y: int):
        for i in Storage.locations:
            if i.x is x and i.y is y:
                return i
        return None
