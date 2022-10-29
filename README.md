# A game engine

## Dependencies

* [python](https://www.python.org/) 3.8.2 or greater
* [pygame](https://www.pygame.org/) 2.1.2 (SDL 2.0.18)

## How to play the starter game

* Clone the repo
* run the file `runner.py`

## Instructions to play game

* You are the red box, your objective is to collide with the green boxes as fast as possible!

## Quick overview of the engine

* The engine has 2 parts, a Sprite class, a Scene class.
* A WalkieTalkie class is also defined for communication between the sprites and the scene.
* To create a game:
    * To instantiate a sprite, you'll first need to create a child/derived class of the Sprite class and define an update() method. 
        * For a good example, refer to the classes defined in `runner.py`
    * Once you have defined that child class, instances of it can be used as Sprites.
    * Then you can instantiate a scene class object, pass into it's constructor a container with the sprites for that scene
    * Then you can call the `Scene.start()` method to start your game, again refer to `runner.py` to see how it's done!
* Refer to the UML in the repo for the overview of the classes
* All explanations for the engine's class attributes and methods are left as **detailed** comments.