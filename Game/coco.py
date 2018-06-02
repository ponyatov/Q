# tutorial here:
# https://www.youtube.com/playlist?list=PL1P11yPQAo7p_mEAk8Q8FNYVutIc58eXe

# install: $ sudo pip install cocos2d

import sys
import cocos
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite
import pyglet
from _bsddb import DB_GID_SIZE

class IntroLayer(Layer):
    def __init__(self):
		Layer.__init__(self)
		label = cocos.text.Label("Hell Cocos", font_size=H / 2 / 5,
			anchor_x='center', anchor_y='top')
		label.position = W / 2, H-5
		self.add(label)
        
class TetrisBG(Sprite):
    def __init__(self):
        Sprite.__init__(self,'img/tetris/bg.png',scale=.4)
        self.image_anchor_y = 0
        self.position = W/2,0
        
class Ani(Layer):
    def __init__(self):
        Layer.__init__(self)
        sheet = pyglet.image.load('img/tetris/walk.png')
        grid = pyglet.image.ImageGrid(sheet,2,8)[0:]
        grid = grid[8:] # reorder
        anim = pyglet.image.Animation.from_image_sequence(grid, .1, loop=True)
        spr = Sprite(anim) ; spr.position = W/2,H/2
        self.add(spr)

director.init(caption=str(sys.argv))
W, H = director.get_window_size()

intro_l = IntroLayer()

intro_s = Scene()
intro_s.add(TetrisBG(),0)
intro_s.add(intro_l)
intro_s.add(Ani(),9)

director.run(intro_s)
