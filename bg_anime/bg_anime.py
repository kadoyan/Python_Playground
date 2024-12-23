import pyxel
from tile_shift import TileShift

class App:
    def __init__(self):
        pyxel.init(128, 112, fps=60, display_scale=3)
        pyxel.load("bg_anime.pyxres")
        self.tileshift = TileShift(0, 1, 40, 16, 1, 16, 16, True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.tileshift.update()
    
    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
App()
