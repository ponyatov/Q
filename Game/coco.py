# tutorial here:
# https://www.youtube.com/playlist?list=PL1P11yPQAo7p_mEAk8Q8FNYVutIc58eXe

# install: $ sudo pip install cocos2d

import sys
import cocos
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite

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

director.init(caption=str(sys.argv))
W, H = director.get_window_size()

# bg_l = TetrisBG()
intro_l = IntroLayer()

intro_s = Scene(TetrisBG()) ; intro_s.add(intro_l)

director.run(intro_s)
