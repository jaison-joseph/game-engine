from Sprite import Sprite
from Scene import Scene
import os

box = Sprite(None, 20, 20)
scene = Scene((1080, 720), (box,), 30, None, None)
box.scene = scene
scene.start()

# print(os.getcwd())