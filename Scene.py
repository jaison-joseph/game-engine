import pygame, keyboard

pygame.init()

class Scene:
    def __init__(self, size, sprites, frameRate: int, backgroundImgSrc = None) -> None:
        self.size_ = size
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
        self.mouseButton_ = []
        self.background = pygame.Surface(self.size_)
        if backgroundImgSrc is not None:
            self.background = pygame.image.load(backgroundImgSrc)
        self.background = self.background.convert()

    def start(self):
        screen = pygame.display.set_mode(self.size)
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.frameRate_)
            for k in self.keyState_:
                self.keyState_[k] = keyboard.is_pressed(k)

            # quitting is the 'q' button
            if self.keyState_['q']:
                break

            # clear the sprites drawn in the previous frame by drawing the background over them
            self.sprites_.clear(screen, self.background)

            # update all the sprites
            self.sprites_.update()
            self.sprites_.draw(screen)

            pygame.display.flip()

    def end(self):
        pass

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