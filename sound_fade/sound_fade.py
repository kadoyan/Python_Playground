import pyxel

import json
def load_bgm(msc, filename, snd1, snd2, snd3, snd4):
    with open(filename, "rt") as file:
        bgm = json.loads(file.read())
        pyxel.sounds[snd1].set(*bgm[0])
        pyxel.sounds[snd2].set(*bgm[1])
        pyxel.sounds[snd3].set(*bgm[2])
        pyxel.sounds[snd4].set(*bgm[3])
        pyxel.musics[msc].set([snd1], [snd2], [snd3], [snd4])


class App:
    def __init__(self):
        # pyxel初期化
        pyxel.init(
            200, 200, fps=60, display_scale=2, title="Sound Test"
        )
        self.fade = False
        load_bgm(0, "assets/esperdream.json", 16, 17, 18, 19)

        print(pyxel.tones[0].gain)
        self.default_gain = []
        for tone in pyxel.tones:
            self.default_gain.append(tone.gain)

        pyxel.run(self.update, self.draw)

    def update(self):
        # BGM
        if pyxel.play_pos(0) is None:
            pyxel.playm(0, loop=True)

        # if pyxel.btnp(pyxel.KEY_UP):
        #     pyxel.play(1, 0, resume=True)
        # if pyxel.btnp(pyxel.KEY_DOWN):
        #     pyxel.play(1, 1, resume=True)
        # if pyxel.btnp(pyxel.KEY_LEFT):
        #     pyxel.play(3, 3, resume=True)
        # if pyxel.btnp(pyxel.KEY_RIGHT):
        #     pyxel.play(3, 5, resume=True)

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.fade = not self.fade

        if self.fade:
            for tone in pyxel.tones:
                if tone.gain > 0.001 and pyxel.frame_count % 5 == 0:
                    tone.gain *= 0.75
        else:
            for idx, tone in enumerate(pyxel.tones):
                incremental = self.default_gain[idx] * 0.1
                if tone.gain < self.default_gain[idx] and pyxel.frame_count % 5 == 0:
                    tone.gain += incremental

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, "SOUND TEST", 7)
        pyxel.text(10, 18, "PRESS SPACE to FADE IN / OUT", 7)
        for idx, tone in enumerate(pyxel.tones):
            pyxel.text(
                10,
                36 + 6 * idx,
                str(f"pyxel.tones[{idx}].gain = {tone.gain}"),
                10 + idx,
            )


if __name__ == "__main__":
    App()
