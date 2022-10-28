import pygame
from pygame.locals import *
from WalkieTalkie import WalkieTalkie
import os
pygame.init()

class Scene:
    def __init__(self, size, sprites, frameRate: int, backgroundImgSrc = None, rgb = None) -> None:
        self.size_ = size
        self.walkieTalkie = WalkieTalkie()
        for i in sprites:
            i.scene = self
            i.walkieTalkie = self.walkieTalkie
        self.position_ = None
        self.sprites_ = pygame.sprite.Group(sprites)
        self.frameRate_ = frameRate
        self.keyState_ = {
            "a": False,
            "b": False,
            "c": False,
            "d": False,
            "e": False,
            "f": False,
            "g": False,
            "h": False,
            "i": False,
            "j": False,
            "k": False,
            "l": False,
            "m": False,
            "n": False,
            "o": False,
            "p": False,
            "q": False,
            "r": False,
            "s": False,
            "t": False,
            "u": False,
            "v": False,
            "w": False,
            "x": False,
            "y": False,
            "z": False,
            "0": False,
            "1": False,
            "2": False,
            "3": False,
            "4": False,
            "5": False,
            "6": False,
            "7": False,
            "8": False,
            "9": False
        }
        self.screen = pygame.display.set_mode(self.size_)
        self.mouseButton_ = []
        self.background = pygame.Surface(self.size_)
        if backgroundImgSrc is None:
            if rgb is None:
                print("Scene has not been passed a color or imgFileName. Defaulting to black background fill")
                rgb = (0, 0, 0)
            self.background.fill(rgb)
        else:
            backgroundImgSrc = os.getcwd() + backgroundImgSrc
            '''
            we will first create a surface object by calling pygame.image.load
            then, we scale the background image size by calling the trasform.scale method
            we pass into the transform.scale method the following:
                the surface object we wish to scale
                the desired width and height after the transform
            '''
            print("backgroundImgSrc: ", backgroundImgSrc)
            self.background = pygame.transform.scale(
                pygame.image.load(backgroundImgSrc), #returns a surface object
                self.size_
            )
        self.background = self.background.convert()

    def start(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.frameRate_)
            msg = self.walkieTalkie.getMessage()
            if msg is not None:
                if msg == 'QUIT':
                    print("You win; wohoo")
                    return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end()
                    return
            
            if True:
                self.keyState_["a"] = pygame.key.get_pressed()[K_a]
                self.keyState_["b"] = pygame.key.get_pressed()[K_b]
                self.keyState_["c"] = pygame.key.get_pressed()[K_c]
                self.keyState_["d"] = pygame.key.get_pressed()[K_d]
                self.keyState_["e"] = pygame.key.get_pressed()[K_e]
                self.keyState_["f"] = pygame.key.get_pressed()[K_f]
                self.keyState_["g"] = pygame.key.get_pressed()[K_g]
                self.keyState_["h"] = pygame.key.get_pressed()[K_h]
                self.keyState_["i"] = pygame.key.get_pressed()[K_i]
                self.keyState_["j"] = pygame.key.get_pressed()[K_j]
                self.keyState_["k"] = pygame.key.get_pressed()[K_k]
                self.keyState_["l"] = pygame.key.get_pressed()[K_l]
                self.keyState_["m"] = pygame.key.get_pressed()[K_m]
                self.keyState_["n"] = pygame.key.get_pressed()[K_n]
                self.keyState_["o"] = pygame.key.get_pressed()[K_o]
                self.keyState_["p"] = pygame.key.get_pressed()[K_p]
                self.keyState_["q"] = pygame.key.get_pressed()[K_q]
                self.keyState_["r"] = pygame.key.get_pressed()[K_r]
                self.keyState_["s"] = pygame.key.get_pressed()[K_s]
                self.keyState_["t"] = pygame.key.get_pressed()[K_t]
                self.keyState_["u"] = pygame.key.get_pressed()[K_u]
                self.keyState_["v"] = pygame.key.get_pressed()[K_v]
                self.keyState_["w"] = pygame.key.get_pressed()[K_w]
                self.keyState_["x"] = pygame.key.get_pressed()[K_x]
                self.keyState_["y"] = pygame.key.get_pressed()[K_y]
                self.keyState_["z"] = pygame.key.get_pressed()[K_z]
                self.keyState_["0"] = pygame.key.get_pressed()[K_0]
                self.keyState_["1"] = pygame.key.get_pressed()[K_1]
                self.keyState_["2"] = pygame.key.get_pressed()[K_2]
                self.keyState_["3"] = pygame.key.get_pressed()[K_3]
                self.keyState_["4"] = pygame.key.get_pressed()[K_4]
                self.keyState_["5"] = pygame.key.get_pressed()[K_5]
                self.keyState_["6"] = pygame.key.get_pressed()[K_6]
                self.keyState_["7"] = pygame.key.get_pressed()[K_7]
                self.keyState_["8"] = pygame.key.get_pressed()[K_8]
                self.keyState_["9"] = pygame.key.get_pressed()[K_9]

            self.screen.blit(self.background, (0, 0))

            # clear the sprites drawn in the previous frame by drawing the background over them
            self.sprites_.clear(self.screen, self.background)

            # update all the sprites
            self.sprites_.update()
            self.sprites_.draw(self.screen)

            pygame.display.flip()


    def end(self):
        pygame.quit()


    def pause(self):
        pass

    def clear(self):
        pass

    def hideCursor(self):
        pass

    def showCursor(self):
        pass

    def getMousePos(self):
        pass

    def hide(self):
        pass

    def show(self):
        pass