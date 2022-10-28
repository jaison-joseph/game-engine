from Sprite import Sprite
from Scene import Scene

class MovingBox(Sprite):
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
        if (len(self.scene.sprites_) == 1):
            self.walkieTalkie.addMessage('QUIT')

class TargetBox(Sprite):
    def __init__(self, scene, width, height, movingBox: MovingBox, x=0, y=0, imgFileName=None, rgb=None) -> None:
        super().__init__(scene, width, height, x, y, imgFileName, rgb)
        self.movingBox = movingBox

    def update(self):
        if self.collidesWith(self.movingBox):
            self.kill()

movingBox = MovingBox(None, 20, 20)
targetBoxes = [
    TargetBox(None, 20, 20, movingBox, 200, 200, None, (0, 255, 0)),
    TargetBox(None, 20, 20, movingBox, 200, 300, None, (0, 255, 0)),
    TargetBox(None, 20, 20, movingBox, 200, 400, None, (0, 255, 0)),
    TargetBox(None, 20, 20, movingBox, 200, 500, None, (0, 255, 0)),
]
allSprites = set(targetBoxes)
allSprites.add(movingBox)
scene = Scene((1080, 720), allSprites, 30, None, None)
scene.start()