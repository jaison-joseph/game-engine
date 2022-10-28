from Sprite import Sprite
from Scene import Scene

class movingBox(Sprite):
    def __init__(self, scene, width, height, x = 0, y = 0, imgFileName=None, rgb=None) -> None:
        super().__init__(scene, width, height, x, y, imgFileName, rgb)

    def update(self):
        if self.scene.keyState_['s']:
            self.rect.y += 2
        elif self.scene.keyState_['d']:
            self.rect.x += 2
        elif self.scene.keyState_['w']:
            self.rect.y -= 2
        elif self.scene.keyState_['a']:
            self.rect.x -= 2        
        if (self.rect.x, self.rect.y) == (400,400):
            # self.walkieTalkie.addMessage("QUIT") 
            self.scene.keepGoing = False
        # print("called")

box = movingBox(None, 20, 20)
targetBox = Sprite(None, 20, 20, 400, 400, None, (0, 255, 0))
scene = Scene((1080, 720), (box, targetBox), 30, None, None)
# box.scene = scene
scene.start()

# print(os.getcwd())