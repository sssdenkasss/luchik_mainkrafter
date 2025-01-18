key_switch_camera = 'c'
key_switch_mode = 'z'
key_forward = 'w'
key_back = 's'
key_left = 'a'
key_right = 'd'
key_up = 'space'
key_down = 'shift'
key_turn_left = 'q'
key_turn_right = 'e'
step = 0.2
class hero():
    def __init__(self, pos, land):
        self.land = land
        self.mode =True
        self.hero = loader.loadModel('smiley')
        self.hero.setcolor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True
    def cameraUp(self):
        x,y,z = self.hero.getPos()
        base.mouseInterFaceNode.setPos(-x, -y, -z -3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn =False
    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)
    def turn_right(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

