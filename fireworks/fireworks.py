import pyxel
from random import randint, uniform
from dataclasses import dataclass
from math import cos, sin, radians, floor

GRAVITY = 0.03
HORIZON = 220
SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256
COLOR_TABLE = [[7, 9, 10], [7, 14, 15], [7, 10, 15], [7, 15], [3, 7, 10], [13, 1]]


@dataclass
class Seed:
    x: float
    y: float
    speed: float


@dataclass
class Tail:
    x: float
    y: float
    life: int
    color: int


@dataclass
class Fire:
    x: float
    y: float
    max_radius: int
    delay: int
    radius: float
    speed: float
    gravity: float
    step: int
    color: int


@dataclass
class FireFlower:
    x: float
    y: float
    color: int


class Fireworks:
    def __init__(self):
        self.seeds: list[Seed] = []
        self.maxseed = 20
        self.tails: list[Tail] = []
        self.fires: list[Fire] = []
        self.particles: list[FireFlower] = []
        
    def move_fireworks(self):
        if PressKey.is_pressed(PressKey.KEY):
            new_seed = Seed(randint(40, 215), 255, randint(8, 10))
            self.seeds.append(new_seed)

        for i in range(len(self.seeds) - 1, -1, -1):
            seed = self.seeds[i]
            seed.y -= seed.speed
            seed.x += cos(pyxel.frame_count) * (seed.speed / 4)
            seed.speed *= 0.95
            new_tail = Tail(seed.x, seed.y, 10, 7)
            self.tails.append(new_tail)

            if seed.speed < 0.1:
                new_fire = Fire(
                    seed.x,
                    seed.y,
                    40 + randint(0, 30),
                    uniform(1, 3),
                    0,
                    1,
                    -0.5,
                    uniform(2, 4),
                    randint(7, 12),
                )
                self.fires.append(new_fire)
                del self.seeds[i]

        for i in range(len(self.tails) - 1, -1, -1):
            tail = self.tails[i]
            tail.life -= 1
            if tail.life < 0 or tail.y > HORIZON:
                del self.tails[i]

        self.particles = []
        for i in range(len(self.fires) - 1, -1, -1):
            fire = self.fires[i]
            fire.radius += fire.speed
            fire.speed -= 0.001
            fire.gravity += GRAVITY
            fire.y += fire.gravity

            # play sound
            if floor(fire.radius) == 10:
                pass

            if floor(fire.radius) % fire.delay:
                for n in range(0, 360, 6):
                    x = fire.x + cos(radians(n)) * fire.radius
                    y = fire.y + sin(radians(n)) * fire.radius
                    particle = FireFlower(x, y, fire.color)
                    self.particles.append(particle)
                    new_tail = Tail(x, y, randint(4, 20), fire.color)
                    self.tails.append(new_tail)

            if fire.radius > fire.max_radius:
                del self.fires[i]

    def draw_fireworks(self):
        for tail in self.tails:
            color = COLOR_TABLE[tail.color - 7][
                randint(0, len(COLOR_TABLE[tail.color - 7]) - 1)
            ]
            pyxel.pset(tail.x, tail.y, color)

        for seed in self.seeds:
            pyxel.pset(seed.x, seed.y, 13)

        for fire in self.fires:
            pyxel.pset(fire.x, fire.y, fire.color)

        for particle in self.particles:
            pyxel.pset(particle.x, particle.y, particle.color)

class PressKey:
    KEY = [pyxel.KEY_SPACE, pyxel.KEY_Z, pyxel.GAMEPAD1_BUTTON_A]

    @staticmethod
    def is_pressed(keys: list[int]) -> bool:
        for k in keys:
            if pyxel.btnp(k):
                return True
        return False


class CopyScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def copy_screen(self, horizon):
        screen_ptr = pyxel.screen.data_ptr()
        difference = 0
        for y in range(0, horizon - 1, self.height // (self.height - horizon)):
            screen_line = screen_ptr[y * self.width : y * self.width + self.width]
            copy_to = self.height - difference - 1
            screen_ptr[copy_to * self.width : copy_to * self.width + self.width] = (
                screen_line
            )
            difference += 1

class WaveScreen:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.counter = 0

    def wave_screen(self):
        shift_level = 1
        width = pyxel.width
        screen_ptr = pyxel.screen.data_ptr()
        self.counter += 0.1
        for y in range(self.start, self.end - 1):
            screen_line = screen_ptr[y * width : y * width + width]
            shift_x = int(cos(self.counter + y) * shift_level)
            screen_ptr[y * width + shift_x : y * width + width + shift_x] = screen_line
            shift_level += 0.1

class App:
    def __init__(self):
        self.fireworks = Fireworks()
        self.copy_screen = CopyScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.wave_screen = WaveScreen(HORIZON, SCREEN_HEIGHT)
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=60)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.fireworks.move_fireworks()

    def draw(self):
        pyxel.cls(0)
        self.fireworks.draw_fireworks()

        self.copy_screen.copy_screen(HORIZON)
        self.wave_screen.wave_screen()

if __name__ == "__main__":
    App()
