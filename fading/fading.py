import pyxel
from fade import Fade

ZBUTTON = [
    pyxel.KEY_Z,
    pyxel.KEY_SPACE,
    pyxel.GAMEPAD1_BUTTON_A,
]

XBUTTON = [
    pyxel.KEY_X,
    pyxel.KEY_ALT,
    pyxel.GAMEPAD1_BUTTON_B,
]

PICO8 = [
    0x000000,
    0x1D2B53,
    0x7E2553,
    0x008751,
    0xAB5236,
    0x5F574F,
    0xC2C3C7,
    0xFFF1E8,
    0xFF004D,
    0xFFA300,
    0xFFEC27,
    0x00E436,
    0x29ADFF,
    0x83769C,
    0xFF77A8,
    0xFFCCAA,
]


class App:
    def __init__(self):
        self.fade = Fade()
        self.is_fadein = True
        self.is_finished = False
        self.message = ""
        pyxel.init(128, 128, fps=60)
        pyxel.colors.from_list(PICO8)
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.is_finished:
            for key in ZBUTTON:
                if pyxel.btnp(key):
                    self.is_fadein = True
                    self.is_finished = False
            for key in XBUTTON:
                if pyxel.btnp(key):
                    self.is_fadein = False
                    self.is_finished = False

    def draw(self):
        pyxel.cls(0)
        pyxel.text(2, 100, "Z: Fade In", 15)
        pyxel.text(2, 110, "X: Fade Out", 15)
        for c in range(16):
            pyxel.rect(c % 8 * 16, 20 + c // 8 * 16, 16, 16, c)

        if not self.is_finished:
            if self.is_fadein:
                self.is_finished = self.fade.fade_in()
            else:
                self.is_finished = self.fade.fade_out()


App()
