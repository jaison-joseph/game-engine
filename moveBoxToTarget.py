from Sprite import Sprite
from Scene import Scene
# import pygame

# class Box(Sprite, pygame.sprite.Sprite):
#     def __init__(self, scene, width, height, x = 0, y = 0, imgFileName=None, rgb=None) -> None:
#         pygame.sprite.Sprite.__init__(self)
#         Sprite.__init__(self, scene, width, height, x, y, imgFileName, rgb)
    
#     def update(self):
#         if self.scene.keyState_['s']:
#             self.rect.y += 2
#         elif self.scene.keyState_['d']:
#             self.rect.x += 2
#         elif self.scene.keyState_['w']:
#             self.rect.y -= 2
#         elif self.scene.keyState_['a']:
#             self.rect.x -= 2        
#         if (self.rect.x, self.rect.y) == (400,400):
#             self.walkieTalkie.addMessage("QUIT") 
#         print("called")

#     def setScene(self, scene):
#         self.scene = scene


# box = Box(None, 20, 20, 0, 0, None, (0, 0, 255))

target = Sprite(None, 20, 20, 400, 400, None, (0, 255, 0))

# boxUpdateFuncType = type(Sprite.update)

# box.update = boxUpdateFuncType(box_update, box, Sprite)

scene = Scene((1080, 720), (target,), 30, None, None)
# box.scene = scene
target.scene = scene
scene.start()