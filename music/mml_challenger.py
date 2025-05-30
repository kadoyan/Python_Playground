import pyxel

class PreludeMusic:
    def __init__(self, p, m):
        self.done = False
        self.prelude = p
        self.melody = m
    
    def playing(self):
        if pyxel.play_pos(0) is None and not self.done:
            pyxel.playm(self.prelude, loop=False)
            self.done = True
        if pyxel.play_pos(0) is None and self.done:
            pyxel.playm(self.melody, loop=True)

class App:
    def __init__(self):
        pyxel.init(128, 128, display_scale=2)
        self.bgm = PreludeMusic(0,1)
        pyxel.run(self.update, self.draw)

    def update(self):
        prelude_ch1 = [
            "t140 v7 q7 @2 o2 x0:77656543 r2",
            "x0 l8fc16c16<b>cfc16c16<b>c",
            "fcfa->c2",
            "c2"
        ]
        melody_ch1 = [
            "t140 v7 q6 @2 o2 x0:7675432 x1:7654321 x2:765421",
            "x0 l8>c4<b-ag4agf4gac.d16c4",
            ">c4<b-a>d4c<ab->c16<b-16ab-16a16gl16<ab->cdef",
            "l8g16gg16fgab->c4<gab-4agf4",
            "g16gg16fgab->c4<b>cd.e16c4r4<",
            "x0 l8>c4<b-ag4agf4gac.d16c4",
            ">c4<b-a>d4c<ab->c16<b-16ab-16a16gl16<ab->cdef",
            "l8g16gg16fgab->c4<gab-4agf4",
            "g16gg16fgab->c4<b>cd.e16c4r4",
            "x2 l8 o2 fc16c16<b>cfc16c16<b>c>>q4aa4.q6l16<<fedcfedc",
            "x2 l8 o2 fc16c16<b>cfc16c16<b>c>>q4aa4.q6l16<<fedcfedc",
            "x2 l8 o2 fc16c16<b>cfc16c16<b>c>>q4aa4.q6l16<<fedcfedc",
            "x2 l8 o2 fc16c16<b>cfc16c16<b>c>>q4aa4.q6l16<<fedcfedc",
            "x0 l8 o2 fc16c16<b>caa4.a-e-16e-16de->cc4.",
            "<b-f16f16ef>dd4.d-<a->d-fa-4g4",
            "f2l16<f<b>caf<b>cag+ag+al8d#efl16<b>cfcfa"
        ]
        
        prelude_ch2 = [
            "t140 v7 q6 @2 o2 x0:646432 r2",
            "x0 c<a16a16g+a>c<a16a16g+a",
            ">d-<a->d-ff2",
            "e2"
        ]
        melody_ch2 = [
            "t140 v7 q6 @2 o2 x0:646432 x1:5454321",
            "af16f16ec<b-4>fec<a16b-16>c4<g.a16b-g",
            ">af16f16gfab-16a16f+df+ddc<b4rg16a16",
            "b-4>defga4e16c16f+e4fcc4",
            "<b-4>defga4l16gdafl8b.g16e4r4",
            "af16f16ec<b-4>fec<a16b-16>c4<g.a16b-g",
            ">af16f16gfab-16a16f+df+ddc<b4rg16a16",
            "b-4>defga4e16c16f+e4fcc4",
            "<b-4>defga4l16gdafl8b.g16e4r4",
            "l8 o2 c<a16a16ff>c<a16a16ff>>q4x1g+g+4.q6x0<<l16aaaaaaaa",
            "l8 o2 c<a16a16ff>c<a16a16ff>>q4x1g+g+4.q6x0<<l16aaaaaaaa",
            "l8 o2 c<a16a16ff>c<a16a16ff>>q4x1g+g+4.q6x0<<l16aaaaaaaa",
            "l8 o2 c<a16a16ff>c<a16a16ff>>q4x1g+g+4.q6x0<<l16aaaaaaaa",
            "l8 o2 c<a16a16ff>c.<a16>cde-c16c16<a-a->e-c16e-16a-e-",
            "fd16d16<b-b->f.d16fgfd-fa->d-4<b-4",
            "a2>c2<<l16b>c<b>c<l8ab-a4r4"
        ]
        
        prelude_ch3 = [
            "t140 q5 @0 o1 x0:665543 r2",
            "x0 f4rfe-4re-",
            "d-d->d-<d-c4r4",
            ">c16cc16de",
        ]
        melody_ch3 = [
            "t140 q5 @0 o1 x0:665543",
            "x0 f>a16a16gf<c>c16<b-16agf>f16f16efe.d16<ce",
            "f>a16a16fff+g16f+16d<d16f+16g>g16g16<d>f+16f+16<g4r4",
            "c16cc16>c4<ff>fal16cgd+eg8<g8f4>g+ag+a",
            "l8<c16cc16>c4<ff>fagd<g.b16>c<c16c16de",
            "x0 f>a16a16gf<c>c16<b-16agf>f16f16efe.d16<ce",
            "f>a16a16fff+g16f+16d<d16f+16g>g16g16<d>f+16f+16<g4r4",
            "c16cc16>c4<ff>fal16cgd+eg8<g8f4>g+ag+a",
            "l8<c16cc16>c4<ff>fagd<g.b16>c<c16c16de",
            "x0 l8 o0 f.>f16g+a<f.>f16l16gagaf>f<ffb8>c8<f>f<ffb>c<b>c",
            "x0 l8 o0 f.>f16g+a<f.>f16l16gagaf>f<ffb8>c8<f>f<ffb>c<b>c",
            "x0 l8 o0 f.>f16g+a<f.>f16l16gagaf>f<ffb8>c8<f>f<ffb>c<b>c",
            "x0 l8 o0 f.>f16g+a<f.>f16l16gagaf>f<ffb8>c8<f>f<ffb>c<b>c",
            "l8 o0 x0 f.>f16g+a<f>f16c16<fga-.>a-16b>c<<a->a-16c-16<a-a",
            "b-.>b-16>c+d<<b->b-16f16<b->cd-d-l16d-d-d->d-d-4<e-4",
            "l8 f>c16c16<b>cfc16c16<b>c<f.>f16c<cf4r4"
        ]
        
        prelude_ch4 = [
        ]
        melody_ch4 = [
            "t140 @3 o3 q2 x0:210",
            "x0 r1r1",
            "r1r1",
            "r1r1",
            "r1r1",
            "r1r1",
            "r1r1",
            "r1r1",
            "r1r1",
            "l16 r1b8b4.bbbbbbbb",
            "l16 r1b8b4.bbbbbbbb",
            "l16 r1b8b4.bbbbbbbb",
            "l16 r1b8b4.bbbbbbbb",
            "r1r1",
            "r1r1",
            "r1r1",
            
        ]

        pyxel.sounds[0].mml("".join(prelude_ch1))
        pyxel.sounds[1].mml("".join(prelude_ch2))
        pyxel.sounds[2].mml("".join(prelude_ch3))
        pyxel.sounds[3].mml("".join(prelude_ch4))
        pyxel.sounds[4].mml("".join(melody_ch1))
        pyxel.sounds[5].mml("".join(melody_ch2))
        pyxel.sounds[6].mml("".join(melody_ch3))
        pyxel.sounds[7].mml("".join(melody_ch4))
        pyxel.musics[0].set([0],[1],[2],[3])
        pyxel.musics[1].set([4],[5],[6],[7])
        self.bgm.playing()
    
    def draw(self):
        pyxel.cls(12)
        title = "Challenger Stage 1"
        for i,n in enumerate(title):
            pyxel.text(25+i*4, 60-i, n, 7)
        pyxel.text(1,1,str(pyxel.play_pos(0)[1]),2)
        # pyxel.text(25, 58, "play_pos:"+str(pyxel.play_pos(0)[1]), 5)
            
if __name__ == "__main__":
    App()
