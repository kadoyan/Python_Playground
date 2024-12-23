import pyxel

class TileShift:
    def __init__(self, bank, speed_h, u, v, timing, width=8, height=8, delay=False):
        """
        Shift an image cell on an image bank

        Args:
            bank (int): The number of the image bank
            speed_h (int): Scrolling direction (+:left, -:right)
            u (int): X position of the target image on the image bank
            v (int): Y position of the target image on the image bank
            timing (int): Scroll timing (per frame)
            width (int): tile width(px)
            height (int): tile height(px)
            delay: delay shift per lines (Boolean)
        """
        self.screen_ptr = pyxel.images[bank].data_ptr()
        self.speed_h = speed_h
        self.u = u
        self.v = v
        self.timing = timing
        self.width = width
        self.height = height
        self.count = 0
        self.delay = delay
        
    def update(self):
        if self.timing == 0 :
            self.timing = 1
        self.count = (self.count + 1) % self.height
        
        if pyxel.frame_count % self.timing == 0:
            if self.delay:
                y = self.count
                self.shift_line(y)
            else:
                for y in range(0, self.height):
                    self.shift_line(y)

    def shift_line(self, y):
        cell = self.u + (self.v + y) * 256
        source = self.screen_ptr[cell:cell + self.width]
        shifted = self.rotate(source, self.speed_h)
        self.screen_ptr[cell:cell + self.width] = shifted
        
    def rotate(self, list, n):
        if not list: # empty list
            return list
        length = len(list)
        n = n % length
        # n<0: left / n>0: right
        return list[-n:] + list[:-n]
