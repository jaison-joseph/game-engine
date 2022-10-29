'''
the box collision game! For instructions on how to play, look at the README
'''

from Sprite import Sprite
from Scene import Scene

'''
defines the box that moves around the screen, smashing onto other boxes on screen
'''
class MovingBox(Sprite):
    def __init__(self, scene, width, height, x = 0, y = 0, imgFileName=None, rgb=None) -> None:
        super().__init__(scene, width, height, x, y, imgFileName, rgb)

    '''
    handle WASD movement; signal to stop the game if it is the only sprite remaining in the scene's sprite group
    inherits from the Sprite class we defined
    '''
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

'''
defines the box that the MovingBox collides onto
inherits from the Sprite class we defined
'''
class TargetBox(Sprite):
    '''
    the constructor additionally accepts a reference to the MovingBox,
    which is the box that may collide with 'this' box
    '''
    def __init__(self, scene, width, height, movingBox: MovingBox, x=0, y=0, imgFileName=None, rgb=None) -> None:
        super().__init__(scene, width, height, x, y, imgFileName, rgb)
        self.movingBox = movingBox

    '''
    if we detect a collision with the MovingBox, remove 'self' from the list 
    of sprites that the Scene updates and draws using the self.kill() method
    '''
    def update(self):
        if self.collidesWith(self.movingBox):
            self.kill()

# instantiating the moving box @ (0, 0)
movingBox = MovingBox(None, 20, 20)

# instantiating the 4 target boxes @ (200, 200), (200, 300), (200, 400) & (200, 500)
targetBoxes = [
    TargetBox(None, 20, 20, movingBox, 200, 200, None, (0, 255, 0)),
    TargetBox(None, 20, 20, movingBox, 200, 300, None, (0, 255, 0)),
    TargetBox(None, 20, 20, movingBox, 200, 400, None, (0, 255, 0)),
    TargetBox(None, 20, 20, movingBox, 200, 500, None, (0, 255, 0)),
]

# just creating a set (hashable container) of the moving box and the 4 target boxes 
allSprites = set(targetBoxes)
allSprites.add(movingBox)

# instanting the scene object
scene = Scene((1080, 720), allSprites, 30, None, None)

# liftoff!
scene.start()