import pyxel
from key_input import KeyInput
from math import cos, sin

from dataclasses import dataclass

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

# Drawing chec
class DrawChecker:
    def __init__(self, width:int, height:int, x:int, y:int, scale:int):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.scale = scale
    
    def draw(self):
        color = 1
        for y in range(0, self.height, self.scale):
            for x in range(0, self.width, self.scale):
                color += 1
                paint_color = color % 15 +1
                pyxel.rect(x, y, x + self.scale, y + self.scale, paint_color)


from collections import deque
class WaveScreen:
    def __init__(self, width:int, height:int, x:int, y:int, wave_scale:int):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.shift_x = 0
        self.shift_y = 0
        self.wave_scale = wave_scale
        self.count = 0
        self.screen_ptr = pyxel.screen.data_ptr()
    
    def horizontal(self):
        self.count += 1
        # Horizontal
        if KeyInput.is_pressed(KeyInput.LEFT):
            self.shift_x -= 0.2
        if KeyInput.is_pressed(KeyInput.RIGHT):
            self.shift_x += 0.2
            
        for y in range(0, self.height, 1):
            start = y * self.width + self.x
            end = y * self.width + self.width + self.x
            source = self.screen_ptr[start:end]
            #Shift data
            shift_list = deque(source)
            shift_list.rotate(int(self.shift_x * cos((self.count + y)/self.wave_scale)))
            self.screen_ptr[start:end] = shift_list
    
    def vertical(self):        
        # Vertical
        if KeyInput.is_pressed(KeyInput.UP):
            self.shift_y -= 0.2
        if KeyInput.is_pressed(KeyInput.DOWN):
            self.shift_y += 0.2
            
        for x in range(0, self.width, 1):
            vertical_collection = []
            for y in range(0, self.height, 1):
                v_color = self.screen_ptr[self.x + x + y * self.width]
                vertical_collection.append(v_color)
            shift_list = deque(vertical_collection)
            shift_list.rotate(int(self.shift_y * sin((self.count + x)/self.wave_scale)))
            for y in range(0, self.height, 1):
                self.screen_ptr[self.x + x + y * self.width] = shift_list[y]
class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=60)
        self.checker = DrawChecker(SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 8)
        self.wave = WaveScreen(SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 8)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(0)
        self.checker.draw()
        self.wave.horizontal()
        self.wave.vertical()

if __name__ == "__main__":
    App()
