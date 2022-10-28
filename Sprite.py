import pygame, math

pygame.init()

constants = {
    'ninety': math.pi / 2,
    'degree2rad': math.pi / 180,
    'rad2degree': 180 / math.pi
}

class Sprite(pygame.sprite.Sprite):
    def __init__(self, scene, width, height, x = 0, y = 0, imgFileName = None, rgb = None) -> None:

        '''
        this call is a call to the base class for all game objects (i.e. sprites)
        '''
        super().__init__()
        self.size = (width, height)

        '''
        the Surface class is used to represent pygame images
        it has the nice blit() method which is used to draw the image onto
        the screen. 

        See: https://www.pygame.org/docs/ref/surface.html
        '''
        self.image = pygame.Surface(self.size)

        '''
        We are required to define the rect attribute; it is used
        by the sprites.Group.draw method
        '''
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        '''
        coloring the sprite
        '''
        if imgFileName is None:
            # if both the imgFileName and rgb are none, we have no fill information; use some default
            if rgb is None:
                print("Sprite has not been passed a color or imgFileName. Defaulting to red color fill")
                rgb = (255, 0, 0)
            self.image.fill(rgb)
        else:
            '''
            we will first create a surface object by calling pygame.image.load
            then, we scale the surface object's size by calling the trasform.scale method
            we pass into the transform.scale method the following:
                the surface object we wish to scale
                the desired width and height after the transform
            '''
            self.image = pygame.transform.scale(
                pygame.image.load(imgFileName), #returns a surface object
                self.size
            )
        
        '''
        the convert function converts a Surface object into 
        the format that is used for drawing onto the display;
        this is a relatively slow operation so it makes sense
        to just call it once during initialization

        See: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert
        '''
        # self.image = self.image.convert()

        '''
        the position of the center of the sprite
        '''
        self.position = [width//2, height//2]

        '''
        the angle at which the image is pointed/tilted
        '''
        self.imgAngle = 0

        '''
        the angle at which the object is moving; stored as 'regular' degrees
        '''
        self.moveAngle = 0

        '''
        defined as ((dx**2) + (dy**2))**0.5
        unit is pixels/frame
        '''
        self.speed = 0

        '''
        defined as ((ddx**2) + (ddy**2))**0.5
        unit is pixels**2/frame
        '''
        self.acceleration = 0

        '''
        change in x coordinate per frame
        '''
        self.dx = 0
        
        '''
        change in y coordinate per frame
        '''
        self.dy = 0

        '''
        change in dx per frame. 
        Note that this is NOT the same as chage in x coordinate per frame (dx)
        '''
        self.ddx = 0

        '''
        change in dy per frame. 
        Note that this is NOT the same as chage in y coordinate per frame (dy)
        '''
        self.ddy = 0

        '''
        A reference to the parent scene object that the sprite belongs to.
        We have a ref to the parent surface so that we can blit onto the surface
        in the sprite's draw method

        But if the sprite is part of a pygame.Sprite.group, we don't need to define a draw method
        If the sprite is part of a group, there is no use for the ref to the scene, since the group's draw method call
        will already contain a ref to the screen surface
        '''
        self.scene = scene 

        '''
        describes what the game engine should do to a sprite when it's at the boundary of a screen
        '''
        self.boundAction = None

        '''
        a flag used to determine whether to the sprite is within the screen/set to visible by the user
        '''
        self.isVisible = True


    '''
    filling in the color of the sprite; either pass in the relative location of 
    a picture or give a solid color
    '''
    def setImage(self, imgFileName = None, rgb = None):
        # if the imgFileName is None, the user wants to fill the sprite with a solid color
        if imgFileName is None:
            # if both the imgFileName and rgb are none, we have no fill information; use some default
            if rgb is None:
                print("Sprite has not been passed a color or imgFileName. Defaulting to red color fill")
                rgb = (255, 0, 0)
            self.image.fill(rgb)
        else:
            '''
            we will first create a surface object by calling pygame.image.load
            then, we scale the surface object's size by calling the trasform.scale method
            we pass into the transform.scale method the following:
                the surface object we wish to scale
                the desired width and height after the transform
            '''
            self.image = pygame.transform.scale(
                pygame.image.load(imgFileName), #returns a surface object
                self.size
            )
        self.image = self.image.convert()

    '''
    uses the pygame.surface.blit method to draw the sprite's surface onto the scene surface
    Source: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    '''
    def draw(self):
        if self.isVisible:
            upperLeft = (self.position[0] - self.size[0]//2, self.position[1] - self.size[1]//2)
            self.scene.blit(self.image, upperLeft)

    '''
    this method is to be extended by the child class inheriting from this class.
    Used by the sprite.group.update calls
    '''
    def update(self):
        pass

    def hide(self):
        self.isVisible = False

    def show(self):
        self.isVisible = True

    def setSpeed(self, magnitude):
        self.speed = magnitude
        self.dx, self.dy = self.vectProject(magnitude, self.moveAngle)

    def setImgAngle(self, imgAngle):
        self.imgAngle = imgAngle

    '''
    the angle argument should be in degrees
    Once the move angle changes,
        the dx and dy will change
        the ddx and ddy will change
    we update the 4 attributes by re-projecting the speed and acceleration vector along the new angle
    '''
    def setMoveAngle(self, angle):                   
        self.moveAngle = angle
        self.dx, self.dy = self.vectProject(self.speed, self.moveAngle)
        self.ddx, self.ddy = self.vectProject(self.acceleration, self.moveAngle)

    '''
    projetcs a  vector of magnitude 'val' along direction dir
    dir is in degrees,                                                                                                                                                                                                                                                                                            
    '''
    def vectProject(self, mag, dir):
        # t = radians(t-90);
        t = dir*constants['degree2rad'] - constants['ninety']
        return (mag * math.cos(t),mag * math.sin(t))

    '''
    does vector addition of sprites current force vector with the vector passed as arguments
    project new force vector
    add components to the existing sprite's components
    find new magnitude and direction and update acceleration and moveAngle attributes
    now since the move angle changed, we update the dx and dy attributes as well
    '''
    def addForce(self, magnitude, direction):
        cx, cy = self.project(magnitude, direction)
        self.ddx += cx
        self.ddy += cy
        self.acceleration = ((self.ddx**2) + (self.ddy**2))**0.5
        self.moveAngle = math.atan2(self.ddy, self.ddx)
        self.dx, self.dy = self.vectProject(self.speed, self.moveAngle)
    
    def setBoundAction(self):
        pass

    def checkBounds(self):
        pass    

    '''
    box-based collision detection
    - will return False if either of the sprites are not visible
    
    Collision algorithm:

        Let's see how we can check if the two boxes below, A and B will collide
        ------------------------------------------
        |                                        |
        |             u                          |
        |         _________                      |
        |         |       |                      |
        |      l  |   A   |  r                   |
        |         |       |                      |
        |         ‾‾‾‾‾‾‾‾‾                      |
        |             d         u_               |
        |                   _________            |
        |                   |       |            |
        |               l_  |   B   |  r_        |
        |                   |       |            |
        |                   ‾‾‾‾‾‾‾‾‾            |
        |                       d_               |
        |                                        |
        ------------------------------------------

        l is the x coordinate of the left edge of box A
        r is the x coordinate of the right edge of box A
        u is the y coordinate of the upper edge of box A
        d is the y coordinate of the bottom edge of box A
        l_, r_, u_, d_ are the analog for box B

        We know the boxes are not collidng if:
        1. right edge of self is to the left of the left edge of s
            - but this is true only under the assumption that A is to the left of B. 
                (If B and A were switched, right edge of B is NOT to the left of the left edge of A)
            - in our case, we don't know which sprite is to the left or right
            - we compensate for that by checking both cases (i.e either A or B is on the left)
            - this translates to (r < l_) or (r_ < l)

        2. bottom edge of A is above the top edge of B:
            - we can use a similar reasoning to (1.) which gives us:
                (d < u_) or (d_ < u)

        Thus, (r < l_) or (r_ < l) or (d < u_) or (d_ < u) reurns True if the sprites are NOT colliding

        Applying a not() to the result of the 4 cases will return True if the sprites do collide
    '''
    def collidesWith(self, s):
        if self.isVisible and s.isVisible:
            w, h = self.size
            w = w/2
            h = h/2
            l, r = self.position[0] - w, self.position[0] + w
            u, d = self.position[1] + h, self.position[1] - h

            w_, h_ = self.size
            w_ = w_/2
            h_ = h_/2
            l_, r_ = s.position[0] - w_, s.position[0] + w_
            u_, d_ = s.position[1] + h_, s.position[1] - h_

            return not(
                (d < u_) or (d_ < u) or (r < l_) or (r_ < l)
            )
        return False

    '''
    returns the distance between the centers of two sprites
    '''
    def distanceTo(self, s):
        return ((self.position[0] - s.position[0])**2 + (self.position[1] - s.position[1])**2)**0.5

    def angleTo(self):
        pass