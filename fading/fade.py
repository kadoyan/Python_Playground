import pyxel

class Fade:
    """
    Original idea from PICO-8(jelpi.p8)
    https://www.lexaloffle.com/bbs/?tid=1810
    
    """
    def __init__(self):
        self.step = 0
        self.palette_step = [0, 0, 1, 1, 2, 1, 13, 6, 4, 4, 9, 3, 13, 1, 13, 14]
        
    def fade_out(self):
        return self.fade_core(False)
            
    def fade_in(self):
        return self.fade_core(True)
    
    def fade_core(self, fadein:bool):
        self.step += 0.2
        for color in range(0,16):
            target_palette = color
            if fadein:
                for loop in range(5, int(self.step), -1):
                    target_palette = self.palette_step[target_palette]
            else:
                for loop in range(int(self.step)):
                    target_palette = self.palette_step[target_palette]
            pyxel.pal(color, target_palette)
        if self.step >= 10:
            self.step = 0
            return True
        return False
