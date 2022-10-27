import pygame, math

pygame.init()

constants = {
    'ninety': math.pi / 2,
    'degree2rad': math.pi / 180,
    'rad2degree': 180 / math.pi
}

class Sprite:
    def __init__(self, scene, width, height) -> None:

        '''
        this call is a call to the base class for all game objects (i.e. sprites)
        '''
        pygame.sprite.Sprite.__init__(self)
        self.size_ = (width, height)

        '''
        the Surface class is used to represent pygame images
        it has the nice blit() method which is used to draw the image onto
        the screen. 

        See: https://www.pygame.org/docs/ref/surface.html
        '''
        self.image_ = pygame.Surface(self.size_)

        '''
        the convert function converts a Surface object into 
        the format that is used for drawing onto the display;
        this is a relatively slow operation so it makes sense
        to just call it once during initialization

        See: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert
        '''
        self.image_ = self.image_.convert()

        '''
        the position of the center of the sprite
        '''
        self.position_ = [width//2, height//2]

        '''
        the angle at which the image is pointed/tilted
        '''
        self.imgAngle_ = 0

        '''
        the angle at which the object is moving; stored as 'regular' degrees
        '''
        self.moveAngle_ = 0

        '''
        defined as ((dx_**2) + (dy_**2))**0.5
        unit is pixels/frame
        '''
        self.speed_ = 0

        '''
        defined as ((ddx_**2) + (ddy_**2))**0.5
        unit is pixels**2/frame
        '''
        self.acceleration_ = 0

        '''
        change in x coordinate per frame
        '''
        self.dx_ = 0
        
        '''
        change in y coordinate per frame
        '''
        self.dy_ = 0

        '''
        change in dx_ per frame. 
        Note that this is NOT the same as chage in x coordinate per frame (dx_)
        '''
        self.ddx_ = 0

        '''
        change in dy_ per frame. 
        Note that this is NOT the same as chage in y coordinate per frame (dy_)
        '''
        self.ddy_ = 0

        '''
        A reference to the parent scene object that the sprite belongs to
        '''
        self.scene_ = scene 

        '''
        describes what the game engine should do to a sprite when it's at the boundary of a screen
        '''
        self.boundAction_ = None

        '''
        a flag used to determine whether to the sprite is within the screen/set to visible by the user
        '''
        self.isVisible_ = True


    def setImage(self, imgFileName = None, rgb = None):
        # if the imgFileName is None, the user wants to fill the sprite with a solid color
        if imgFileName is None:
            # if both the imgFileName and rgb are none, we have no fill information; use some default
            if rgb is None:
                print("Sprite has not been passed a color or imgFileName. Defaulting to red color fill")
                rgb = (255, 0, 0)
            # checking for invalid rgb values: the length of the rgb tuple
            if len(rgb) != 3:
                print("Sprite has not been passed a legitimate rgb tuple. Defaulting to red color fill")
                rgb = (255, 0, 0)
            # checking for invalid rgb values: bounds check for r,g and b
            for i in rgb:
                if i < 0 or i > 255:
                    print("Sprite has not been passed a legitimate rgb tuple. Defaulting to red color fill")
                    rgb = (255, 0, 0)
                    break
            # filling the image with the color
            self.image_.fill(rgb)
        else:
            '''
            we will first create a surface object by calling pygame.image.load
            then, we scale the surface object's size by calling the trasform.scale method
            we pass into the transform.scale method the following:
                the surface object we wish to scale
                the desired width and height after the transform
            '''
            self.image_ = pygame.transform.scale(
                pygame.image.load(imgFileName), #returns a surface object
                self.size_
            )

    '''
    uses the pygame.surface.blit method to draw the sprite's surface onto the scene surface
    Source: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    '''
    def draw(self):
        if self.isVisible_:
            upperLeft = (self.position_[0] - self.size_[0]//2, self.position_[1] - self.size_[1]//2)
            self.scene_.blit(self.image_, upperLeft)

    '''
    this method is to be extended by the child class inheriting from this class
    '''
    def update(self):
        pass

    def hide(self):
        self.isVisible_ = False

    def show(self):
        self.isVisible_ = True

    def setSpeed(self, magnitude):
        self.speed_ = magnitude
        self.dx_, self.dy_ = self.vectProject(magnitude, self.moveAngle_)

    def setImgAngle(self, imgAngle):
        self.imgAngle_ = imgAngle

    '''
    the angle argument should be in degrees
    Once the move angle changes,
        the dx_ and dy_ will change
        the ddx_ and ddy_ will change
    we update the 4 attributes by re-projecting the speed and acceleration vector along the new angle
    '''
    def setMoveAngle(self, angle):                   
        self.moveAngle_ = angle
        self.dx_, self.dy_ = self.vectProject(self.speed_, self.moveAngle_)
        self.ddx_, self.ddy_ = self.vectProject(self.acceleration_, self.moveAngle_)

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
    now since the move angle changed, we update the dx_ and dy_ attributes as well
    '''
    def addForce(self, magnitude, direction):
        cx, cy = self.project(magnitude, direction)
        self.ddx_ += cx
        self.ddy_ += cy
        self.acceleration_ = ((self.ddx_**2) + (self.ddy_**2))**0.5
        self.moveAngle_ = math.atan2(self.ddy_, self.ddx_)
        self.dx_, self.dy = self.vectProject(self.speed_, self.moveAngle_)
    
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
        if self.isVisible_ and s.isVisible:
            w, h = self.size_
            w = w/2
            h = h/2
            l, r = self.position_[0] - w, self.position_[0] + w
            u, d = self.position_[1] + h, self.position_[1] - h

            w_, h_ = self.size_
            w_ = w_/2
            h_ = h_/2
            l_, r_ = s.position_[0] - w_, s.position_[0] + w_
            u_, d_ = s.position_[1] + h_, s.position_[1] - h_

            return not(
                (d < u_) or (d_ < u) or (r < l_) or (r_ < l)
            )
        return False

    '''
    returns the distance between the centers of two sprites
    '''
    def distanceTo(self, s):
        return ((self.position_[0] - s.position[0])**2 + (self.position_[1] - s.position[1])**2)**0.5

    def angleTo(self):
        pass