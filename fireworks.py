import pyxel
from random import randint, uniform
from dataclasses import dataclass
from math import cos, sin, radians, floor

GRAVITY = 0.03
HORIZON = 255
COLOR_TABLE = [
    [7, 9, 10],
    [7, 14, 15],
    [7, 10, 15],
    [7, 15],
    [3, 7, 10],
    [13, 1]
]

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
        self.flowers: list[FireFlower] = []

class PressKey:
    KEY = [
        pyxel.KEY_SPACE,
        pyxel.KEY_Z,
        pyxel.GAMEPAD1_BUTTON_A
    ]

    @staticmethod
    def is_pressed(keys: list[int]) -> bool:
        for k in keys:
            if pyxel.btnp(k):
                return True
        return False

class App:
    def __init__(self):
        self.fireworks = Fireworks()
        pyxel.init(256, 256, fps=60)
        pyxel.run(self.update, self.draw)

    def update(self):
        if PressKey.is_pressed(PressKey.KEY):
            new_seed = Seed(randint(40, 215), 255, randint(8, 10))
            self.fireworks.seeds.append(new_seed)

        for i in range(len(self.fireworks.seeds) - 1, -1, -1):
            seed = self.fireworks.seeds[i]
            seed.y -= seed.speed
            seed.x += cos(pyxel.frame_count) * (seed.speed / 4)
            seed.speed *= 0.95
            new_tail = Tail(seed.x, seed.y, 10, 7)
            self.fireworks.tails.append(new_tail)

            if seed.speed < 0.1:
                new_fire = Fire(seed.x, seed.y, 40 + randint(0, 30), uniform(1, 3), 0, 1, -0.5, uniform(2, 4), randint(7, 12))
                self.fireworks.fires.append(new_fire)
                del self.fireworks.seeds[i]

        for i in range(len(self.fireworks.tails) - 1, -1, -1):
            tail = self.fireworks.tails[i]
            tail.life -= 1
            if tail.life < 0 or tail.y > HORIZON:
                del self.fireworks.tails[i]

        self.fireworks.flowers = []
        for i in range(len(self.fireworks.fires) - 1, -1, -1):
            fire = self.fireworks.fires[i]
            fire.radius += fire.speed
            fire.speed -= 0.001
            fire.gravity += GRAVITY
            fire.y += fire.gravity

            # play sound
            if floor(fire.radius) == 10:
                pass

            if floor(fire.radius) % fire.delay:
                for n in range(60):
                    x = fire.x + cos(radians(n * 6)) * fire.radius
                    y = fire.y + sin(radians(n * 6)) * fire.radius
                    flower = FireFlower(x, y, fire.color)
                    self.fireworks.flowers.append(flower)
                    new_tail = Tail(x, y, randint(8, 14), fire.color)
                    self.fireworks.tails.append(new_tail)

            if fire.radius > fire.max_radius:
                del self.fireworks.fires[i]

    def draw(self):
        pyxel.cls(0)
        for tail in self.fireworks.tails:
            color = COLOR_TABLE[tail.color - 7][randint(0, len(COLOR_TABLE[tail.color - 7]) - 1)]
            pyxel.pset(tail.x, tail.y, color)

        for seed in self.fireworks.seeds:
            pyxel.pset(seed.x, seed.y, 13)

        for fire in self.fireworks.fires:
            pyxel.pset(fire.x, fire.y, fire.color)

        for flower in self.fireworks.flowers:
            pyxel.pset(flower.x, flower.y, flower.color)

if __name__ == "__main__":
    App()
