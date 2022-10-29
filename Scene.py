'''
a Scene class that (ideally) contains sprite's 
it is essentially the pygame.Surface object on which the game's sprites get drawn onto
'''
import pygame
from pygame.locals import *
from WalkieTalkie import WalkieTalkie
import os

'''
initializing pygame's modules; required before pygame function calls
'''
pygame.init()

class Scene:
    '''
    size: size of the screen, a two number tuple
    sprites: a hashable container containing all the sprite objects for the scene
    frameRate: desired upper limit to the game's frame rate
    backgroundImgSrc: relative path to image for the background
    rgb: 3 number tuple with each number in the range [0, 255] to determine 
    '''
    def __init__(self, size, sprites, frameRate: int, backgroundImgSrc = None, rgb = None) -> None:
        self.size_ = size
        
        '''
        the walkieTalkie is a way for the sprites to communicate with the scene object
        the built in use of the walkieTalkie object is for the sprites to signal to the scene to stop the core game loop
        '''
        self.walkieTalkie = WalkieTalkie()
        
        '''
        each sprite needs a reference to the parent scene object for:
            keyboard input (the scene object has the keyboard input)
            scene dimensions for boundary checking
            sprite's draw method (the sprites draw on the scene) 
        '''
        for i in sprites:
            i.scene = self
            i.walkieTalkie = self.walkieTalkie
        
        '''
        a pygame sprite group is a collection of sprite objects that is convenient to manage
        for more: https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group 
        '''
        self.sprites_ = pygame.sprite.Group(sprites)

        '''
        the frame rate of the game
        '''
        self.frameRate_ = frameRate

        '''
        a dictionary of key value pairs that maintains the state of keys in the keyboarde
        the keys that are maintained are [a-z] and [0-9]
        '''
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
        
        '''
        initializing the window with the desired dimensions 
        '''
        self.screen = pygame.display.set_mode(self.size_)

        '''
        intializing a surface object
        in pygame, if any surface is being drawn on, it is a surface object
        so, the background is a pygame surface object
        '''
        self.background = pygame.Surface(self.size_)

        '''
        if neither the background image location nor the rgb tuple is supplied, the Scene defaults to a solid black fill
        '''
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

        '''
        the convert method changes the format of the surface object that
        makes it very quick to blit.

        https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert
        '''
        self.background = self.background.convert()

    '''
    the heart of the Scene class; the main loop that controls the screen 
    '''
    def start(self):
        # start the clock; used for maintaining frame rate
        clock = pygame.time.Clock()
        while True:
            # attempt to get a message from the walkie talkie; if we get a 'QUIT', stop the loop
            msg = self.walkieTalkie.getMessage()
            if msg is not None:
                if msg == 'QUIT':
                    self.end()
                    print("You win; wohoo")
                    return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end()
                    return
            
            # update the key states by getting the state of each of the keys in the keyState dictionary
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

            # update all the sprites, by calling their update methods
            self.sprites_.update()

            # draw the sprites onto the screen
            self.sprites_.draw(self.screen)

            # show the stuff on the screen object to the actual screen
            pygame.display.flip()

            # method that automatically adjusts tick (delay) to maintain desired frame rate
            clock.tick(self.frameRate_)

    '''
    method to call once the end loop ends / just before the main loop ends
    '''
    def end(self):
        # unitializes all the pygame modules
        pygame.quit()

    '''
    TODO
    '''
    def pause(self):
        pass

    def clear(self):
        # blit's the background onto the screen, effectively 'clearing' the screen
        self.screen.blit(self.background, (0, 0))

    '''
    hide the cursor of the machine
    '''
    def hideCursor(self):
        pygame.mouse.set_visible(False)

    '''
    un-hide/show the cursor of the machine
    '''
    def showCursor(self):
        pygame.mouse.set_visible(True)

    '''
    returns the (x, y) computer screen coordinates of the mouse
    '''
    def getMousePos(self):
        return pygame.mouse.get_pos()